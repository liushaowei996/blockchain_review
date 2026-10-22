"""Reproduce the revision's illustrative policy replay and byte accounting.

Requires Python >=3.10 and cryptography. No Fabric node, consensus protocol,
network emulator or physical vehicle is run. Times are scenario inputs, not
measured latency. Fixed public example keys MUST NOT be used in deployments.
Run from any directory; results are written beside this script.
"""
from __future__ import annotations
import csv
import hashlib
import itertools
import json
from pathlib import Path
import struct
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

OUT = Path(__file__).resolve().parent
BODY = struct.Struct('>BB16s16sIqqI32s32s32s')
H = lambda b: hashlib.sha256(b).digest()
KEYS = {name:Ed25519PrivateKey.from_private_bytes(H(('public demonstration key: '+name).encode()))
        for name in ['uuv-01','usv-01','A','B','C','D']}
DOMAIN = b'OAL-REPLAY-v1:'

def pack(seq: int, lo: int, hi: int, kind: int = 1, payload: bytes | None = None, producer='uuv-01',parent=None) -> bytes:
    return BODY.pack(1, kind, b'mission-01'.ljust(16, b'\0'), producer.encode().ljust(16, b'\0'),
                     seq, lo, hi, 1, H(b'policy-v1'), payload or H(f'data-{seq}'.encode()), parent or H(b'parent'))

def signed(body: bytes, signer='uuv-01') -> bytes:
    return body + KEYS[signer].sign(DOMAIN + body)

def verify(record: bytes, signer='uuv-01') -> bool:
    try:
        KEYS[signer].public_key().verify(record[-64:], DOMAIN + record[:-64])
        return True
    except InvalidSignature:
        return False

def merkle(records: list[bytes]):
    # Domain-separated leaf/node hashes, repeated final leaf to power of two.
    leaves = [H(b'\x00' + r) for r in records]
    while len(leaves) & (len(leaves)-1): leaves.append(leaves[-1])
    levels = [leaves]
    while len(levels[-1]) > 1:
        a = levels[-1]
        levels.append([H(b'\x01' + a[i] + a[i+1]) for i in range(0, len(a), 2)])
    return levels

def proof(levels, index):
    result=[]
    for level in levels[:-1]:
        result.append(level[index ^ 1]); index //= 2
    return result

def verify_proof(record, index, branch, root, count):
    # The checkpoint's original count excludes repeated padding leaves.
    if count < 1 or not 0 <= index < count:
        return False
    if len(branch) != (count - 1).bit_length() or len(root) != 32:
        return False
    if any(len(sibling) != 32 for sibling in branch):
        return False
    h=H(b'\x00'+record)
    for sibling in branch:
        h=H(b'\x01'+(sibling+h if index & 1 else h+sibling)); index //= 2
    return h==root

def authority(lo, hi, effective=240):
    # Interval is closed; revocation applies from effective time onward.
    if hi < effective: return 'eligible historical record'
    if lo >= effective: return 'revoked at event time'
    return 'quarantine: time interval overlaps revocation'

def joint_policy(signers):
    return {'A','B'}.issubset(signers) and bool({'C','D'} & signers)

def local_authority(now, expiry=480):
    return 'restricted delegated use' if now < expiry else 'deny: delegation expired'

def write_csv(name, rows):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def main():
    records=[signed(pack(i,114+60*i,126+60*i)) for i in range(10)]
    levels=merkle(records)
    assert all(verify(r) and verify_proof(r,i,proof(levels,i),levels[-1][0],len(records)) for i,r in enumerate(records))
    tampered=bytes([records[0][0]^1])+records[0][1:]
    assert not verify(tampered)
    assert not verify_proof(tampered,0,proof(levels,0),levels[-1][0],10)
    assert not verify_proof(records[0],1,proof(levels,0),levels[-1][0],10)
    assert not verify_proof(records[-1],10,proof(levels,10),levels[-1][0],10)
    assert not verify_proof(records[0],-1,proof(levels,0),levels[-1][0],10)
    assert not verify_proof(records[0],0,proof(levels,0)[:-1],levels[-1][0],10)
    checkpoint=pack(1,114,666,kind=2,payload=levels[-1][0],producer='usv-01',parent=H(b'previous-batch'))+struct.pack('>H',10)
    compact=signed(checkpoint,'usv-01')
    assert verify(compact,'usv-01') and not verify(compact,'uuv-01')
    receipts={name:KEYS[name].sign(DOMAIN+checkpoint) for name in 'ABC'}
    for name,sig in receipts.items():KEYS[name].public_key().verify(sig,DOMAIN+checkpoint)
    assert joint_policy(set(receipts))
    # Demonstration receipt signature verification only: no Fabric commit is asserted.
    assert len(records[0])+sum(map(len,proof(levels,0)))+2+len(checkpoint)+1+sum(map(len,receipts.values()))==697
    application={
        'version':1,'kind':'batch','mission': 'mission-01','gateway':'usv-01',
        'sequence':1,'event_from':114,'event_to':666,'epoch':1,
        'policy_hash':H(b'policy-v1').hex(),'root':levels[-1][0].hex(),
        'previous_root':H(b'previous-batch').hex(),'count':10,
        'gateway_signature':compact[-64:].hex()}
    payload=json.dumps(application,sort_keys=True,separators=(',',':')).encode()
    (OUT/'example-batch.json').write_bytes(payload+b'\n')
    trace=[]
    for label,lo,hi,auth_feature in [('before',114,126,1),('overlap',234,246,.5),('after',294,306,0)]:
        features=[1,.95,1,1,auth_feature]  # signature, quality, lineage, cached epoch, temporal authority
        mean=sum(features)/len(features)
        status=authority(lo,hi)
        veto=('eligible historical record' if auth_feature==1 else
              'revoked at event time' if auth_feature==0 else 'quarantine: time interval overlaps revocation')
        assert veto==status
        trace.append(dict(event=label,event_lo_s=lo,event_hi_s=hi,ledger=status,
                          validating_witnessed_log=status,mean_score=round(mean,2),
                          mean_threshold_075='accept' if mean>=.75 else 'restrict',veto_scalar=veto))
    # Every permutation produces the same historical decisions; duplicate IDs
    # are idempotent and rejected signatures do not enter the accepted set.
    canonical={r['event']:r['ledger'] for r in trace}
    for order in itertools.permutations(trace):
        state={}
        for event in [*order,order[0]]: state.setdefault(event['event'],authority(event['event_lo_s'],event['event_hi_s']))
        assert state==canonical
    updates=[]
    for bits in itertools.product([False,True],repeat=4):
        signers={name for name,b in zip('ABCD',bits) if b}
        accepted=joint_policy(signers)
        # The log baseline uses the identical policy and membership epoch.
        assert accepted==('A' in signers and 'B' in signers and ('C' in signers or 'D' in signers))
        updates.append(dict(signers=''.join(sorted(signers)) or 'none',ledger_accepts=accepted,
                            validating_log_accepts=accepted,consistency_only_log='records proposal; authorization requires application check'))
    availability=[]
    for n in (4,7,10):
        f=(n-1)//3; q=2*f+1
        for reachable in (q-1,q,n):
            for duration in (0,10,30,58,59,60,120):
                # Same independent membership and responsive quorum for both.
                ledger_delay=duration+2 if reachable>=q else None
                log_delay=duration+1 if reachable>=q else None
                availability.append(dict(validators=n,quorum=q,reachable_responsive=reachable,partition_s=duration,
                    assumed_ledger_completion_s=ledger_delay,assumed_log_completion_s=log_delay,
                    ledger_meets_60s=ledger_delay is not None and ledger_delay<=60,
                    log_meets_60s=log_delay is not None and log_delay<=60))
    budget=[]
    for scheme,sig in [('Ed25519',64),('ML-DSA-44',2420)]:
        sizes={'individual record':BODY.size+sig,'batch of 10 compact commitment':len(checkpoint)+sig,
               '10 complete records':10*(BODY.size+sig),
               'one record proof and three-signature application receipt':BODY.size+sig+128+2+len(checkpoint)+1+3*sig}
        for message,size in sizes.items():
            for rate in (100,1000,5000):
                budget.append(dict(signature=scheme,message=message,bytes=size,net_payload_bit_s=rate,
                                   serialization_s=round(size*8/rate,5)))
    summary=dict(record_body_bytes=BODY.size,ed25519_record_bytes=len(records[0]),
        checkpoint_body_bytes=len(checkpoint),ed25519_checkpoint_bytes=len(compact),
        canonical_json_application_bytes=len(payload),merkle_branch_bytes=128,
        trace_records=len(trace),arrival_permutations=6,signer_subsets=len(updates),quorum_sensitivity_rows=len(availability),
        local_authority_expiry_s=480,local_action_at_420_s=local_authority(420),local_action_at_540_s=local_authority(540),
        consensus_execution=False,fabric_execution=False,latencies='assumed sensitivity inputs, not measurements')
    assert local_authority(420)=='restricted delegated use'
    assert local_authority(480)==local_authority(540)=='deny: delegation expired'
    for name,rows in [('trace-results.csv',trace),('endorsement-results.csv',updates),('partition-sensitivity.csv',availability),('communication-budget.csv',budget)]:write_csv(name,rows)
    (OUT/'replay-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
