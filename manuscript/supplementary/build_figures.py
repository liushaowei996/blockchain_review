"""Build all publication figures as reproducible vector PDFs (ReportLab).

No photographic, stock, generated-image, or external graphical assets are used.
The OAL heatmap is aggregated from the supplementary claim-level CSV.
"""
from pathlib import Path
import csv,json,collections,math
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER,TA_LEFT

ROOT=Path(__file__).resolve().parents[1]
MANUSCRIPT=ROOT/'manuscript' if (ROOT/'manuscript/main.tex').exists() else ROOT
OUT=MANUSCRIPT/'figures'; DATA=MANUSCRIPT/'supplementary'
FONT='Helvetica'; BOLD='Helvetica-Bold'
for folder,regular,bold in [(Path('C:/Windows/Fonts'),'arial.ttf','arialbd.ttf'),
                            (Path('/usr/share/fonts/truetype/dejavu'),'DejaVuSans.ttf','DejaVuSans-Bold.ttf')]:
    if (folder/regular).exists():
        pdfmetrics.registerFont(TTFont('Figure',str(folder/regular)))
        pdfmetrics.registerFont(TTFont('FigureBold',str(folder/bold)))
        FONT,BOLD='Figure','FigureBold';break
INK=colors.HexColor('#172D3A'); TEAL=colors.HexColor('#006F77'); LIGHT=colors.HexColor('#EEF5F5')
GRAY=colors.HexColor('#667580'); LINE=colors.HexColor('#9AAEB6')

def start(name,h):
    c=canvas.Canvas(str(OUT/name),pagesize=(500,h),invariant=1,pageCompression=1)
    c.setTitle(name);c.setAuthor('Anonymous authors');return c

def text(c,x,y,s,size=12,bold=False,color=INK):
    c.setFillColor(color);c.setFont(BOLD if bold else FONT,size);c.drawString(x,y,s)

def para(c,x,y,w,h,s,size=12,align=TA_CENTER):
    p=Paragraph(s,ParagraphStyle('diagram',fontName=FONT,fontSize=size,leading=size*1.3,textColor=INK,alignment=align))
    pw,ph=p.wrap(w,h)
    if ph>h+0.1:raise ValueError((s,ph,h))
    p.drawOn(c,x,y+(h-ph)/2)

def box(c,x,y,w,h,s,size=12,fill=LIGHT):
    c.setStrokeColor(LINE);c.setFillColor(fill);c.setLineWidth(.8)
    c.roundRect(x,y,w,h,5,fill=1,stroke=1);para(c,x+7,y+5,w-14,h-10,s,size)

def arrow(c,x1,y1,x2,y2,color=TEAL,dash=False):
    c.setStrokeColor(color);c.setFillColor(color);c.setLineWidth(1.4)
    if dash:c.setDash(4,3)
    c.line(x1,y1,x2,y2);c.setDash()
    ang=math.atan2(y2-y1,x2-x1);a=6
    p=c.beginPath();p.moveTo(x2,y2)
    p.lineTo(x2-a*math.cos(ang-.45),y2-a*math.sin(ang-.45))
    p.lineTo(x2-a*math.cos(ang+.45),y2-a*math.sin(ang+.45));p.close();c.drawPath(p,stroke=0,fill=1)

def finish(c):c.showPage();c.save()

def architecture():
    c=start('figure-01-reference-architecture.pdf',330)
    text(c,12,309,'Coalition governance and shore services',14,True)
    for i,s in enumerate(['A: authority','B: research','C: communications','D: data service']):
        box(c,12+i*122,244,110,48,s+'<br/>peer + orderer',11)
    box(c,80,179,340,43,'Joint policy, membership, commitments and audit',12)
    for i in range(4):arrow(c,67+i*122,244,67+i*122,231);arrow(c,67+i*122,231,250,222)
    box(c,12,84,142,56,'UAV<br/>source evidence / radio',12)
    box(c,179,84,142,56,'USV gateway<br/>cache and forwarding',12)
    box(c,346,84,142,56,'UUV<br/>signed local records',12)
    arrow(c,154,112,179,112);arrow(c,346,112,321,112)
    text(c,328,148,'acoustic / optical',10.5)
    arrow(c,238,140,238,179);arrow(c,263,179,263,140,dash=True)
    text(c,274,156,'radio / shore contact',10.5)
    box(c,12,10,476,46,'All vehicles: local appraisal, bounded delegation and safety fallback<br/>A gateway partition delays global state; shore consensus is not sent acoustically.',11.5,colors.white)
    finish(c)

def assurance():
    c=start('figure-02-assurance-chain.pdf',294)
    rows=[('O  Observation validity','Physical bounds, calibration, diagnostics and corroboration'),
          ('C  Commitment / provenance','Signatures, content IDs, event times and derivation'),
          ('G  Shared governance','Membership, joint authorization, ordered valid state'),
          ('M  Mission-use suitability','Purpose, authority, freshness, uncertainty and consequence')]
    for i,(a,b) in enumerate(rows):
        y=226-i*69
        box(c,12,y,476,52,f'<b>{a}</b><br/>{b}',12)
        if i<3:arrow(c,250,y,250,y-17)
    finish(c)

def heatmap():
    claims=list(csv.DictReader((DATA/'oal-study-mapping.csv').open(encoding='utf-8')))
    cells=collections.defaultdict(set); levels=collections.defaultdict(set)
    for r in claims:
        for stage in r['lifecycle_stages'].split(';'):cells[(r['object'],r['assurance'],stage)].add(r['study_id'])
        for level in r['evidence_levels'].split(';'):levels[level].add(r['study_id'])
    rows=[]
    c=start('figure-03-oal-framework.pdf',500)
    text(c,12,481,'Coverage by object, assurance claim and lifecycle',14,True)
    stages=['A','S','T','F','D','R']; mx=max(map(len,cells.values()))
    for j,label in enumerate(['Admission','Sensing','Relay','Fusion','Decision','Recovery']):
        para(c,142+j*56,446,56,22,label,10.5)
    for i,(o,a) in enumerate((o,a) for o in 'EPLD' for a in 'OCGM'):
        y=425-i*18
        if i%4==0:text(c,12,y+4,{'E':'Entity','P':'Platform','L':'Link/path','D':'Data product'}[o],11.5,True)
        text(c,118,y+4,a,11.5,True)
        for j,s in enumerate(stages):
            n=len(cells[(o,a,s)]);t=n/mx
            c.setFillColor(colors.Color(.95-.7*t,.97-.5*t,.97-.49*t))
            c.setStrokeColor(colors.white);c.rect(142+j*56,y,55,18,fill=1,stroke=1)
            c.setFillColor(colors.white if t>.6 else INK);c.setFont(BOLD if n else FONT,11)
            c.drawCentredString(169+j*56,y+4,str(n))
            rows.append(dict(object=o,assurance=a,stage=s,study_count=n,study_ids=';'.join(sorted(cells[(o,a,s)]))))
    para(c,12,117,476,27,'O: observation  ·  C: commitment/provenance  ·  G: governance  ·  M: mission use',10.5)
    text(c,12,96,'Reported evidence forms (study profiles overlap)',12,True)
    for i,l in enumerate(['L0','L1','L2','L3','L4','L5']):
        box(c,12+i*80,39,72,42,f'<b>{l}: {len(levels[l])}</b>',12)
    para(c,12,7,476,26,'23 studies; 49 claim records. Zero means no coded claim in this sample.',11)
    finish(c)
    with (DATA/'oal-cell-counts.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    summary={'studies':len({r['study_id'] for r in claims}),'claim_records':len(claims),
             'nonempty_cells':sum(r['study_count']>0 for r in rows),'evidence_profiles':{l:len(levels[l]) for l in sorted(levels)}}
    (DATA/'mapping-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8');print(summary)

def dependencies():
    c=start('figure-04-dependency-threat.pdf',304)
    box(c,12,230,140,55,'Entity / authority<br/>credential and delegation',11.5)
    box(c,180,230,140,55,'Platform / device<br/>measured state',11.5)
    box(c,348,230,140,55,'Observation product<br/>time and quality',11.5)
    arrow(c,152,256,180,256);arrow(c,320,256,348,256)
    text(c,151,290,'controls',10);text(c,318,290,'produces',10)
    box(c,12,130,140,55,'Shared record<br/>joint commitment',11.5)
    box(c,180,130,140,55,'Derived product<br/>inputs + transformation',11.5)
    box(c,348,130,140,55,'Link / path<br/>custody and delay',11.5)
    arrow(c,418,185,418,230);arrow(c,305,185,362,230);arrow(c,152,157,180,157)
    text(c,429,205,'transmits',10);text(c,269,212,'depends on',10);text(c,125,194,'commits to',10)
    box(c,12,12,228,77,'<b>Causal hypotheses</b><br/>Adversarial intervention<br/>Benign degradation<br/>Both may coexist',11.5,colors.white)
    box(c,260,12,228,77,'<b>Epistemic outcomes</b><br/>Supported / contradicted / unknown<br/>Reassess descendants using<br/>an explicit inference rule',11.5,colors.white)
    finish(c)

def ctg():
    c=start('figure-05-ctg-reasoning-loop.pdf',272)
    for x,y,s in [(12,196,'1  Collect evidence'),(180,196,'2  Verify bindings'),(348,196,'3  Appraise claims'),
                  (348,34,'4  Review dependencies'),(180,34,'5  Apply relying policy'),(12,34,'6  Record and revisit')]:box(c,x,y,140,48,s,12)
    arrow(c,152,220,180,220);arrow(c,320,220,348,220);arrow(c,418,196,418,82)
    arrow(c,348,58,320,58);arrow(c,180,58,152,58);arrow(c,82,82,82,196)
    box(c,116,111,268,52,'<b>Shared knowledge</b><br/>Context · event/receipt time · graph · policy',11.5,colors.white)
    para(c,12,0,476,26,'Changes in evidence, authority or context trigger a new appraisal.',11)
    finish(c)

def boundary():
    c=start('figure-06-blockchain-boundary.pdf',320)
    box(c,12,257,476,48,'Which parties must approve state changes, and which faults must be tolerated?',12)
    arrow(c,143,257,143,224);arrow(c,357,257,357,224)
    box(c,12,164,226,60,'<b>One accountable administrator</b><br/>Authenticated database / signed log<br/>Crash replication if required',11.5)
    box(c,262,164,226,60,'<b>Independent joint control</b><br/>Shared authorization + fault model<br/>Reachable quorum required',11.5)
    arrow(c,375,164,375,137)
    box(c,12,70,226,67,'<b>Validating witnessed log</b><br/>Consistency proofs + independent<br/>policy-validating cosigners',11.5,colors.white)
    box(c,262,70,226,67,'<b>Permissioned ledger</b><br/>Ordering + application validation<br/>+ jointly governed configuration',11.5,colors.white)
    arrow(c,238,102,262,102)
    para(c,12,7,476,49,'Compare equal guarantees, latency, bytes, recovery and governance cost.<br/>Physical validity, evidence availability and local safety need their own controls.',11.5)
    finish(c)

def maturity():
    c=start('figure-07-evidence-maturity.pdf',296)
    data=[('L0  Concept','Use case, architecture, argument'),('L1  Analysis','Formal, mathematical or security reasoning'),
          ('L2  Simulation / data','Configured models or recorded observations'),('L3  Prototype / testbed','Implemented component and stated workload'),
          ('L4  Field trial','Physical operating conditions and scope'),('L5  Sustained operation','Duration, multiple parties and recovery history')]
    for i,(a,b) in enumerate(data):
        x=12+(i%2)*244;y=208-(i//2)*88
        box(c,x,y,232,70,f'<b>{a}</b><br/>{b}',12)
    para(c,12,0,476,28,'Evidence forms are complementary. Rigor and claim scope are assessed separately.',11)
    finish(c)

if __name__=='__main__':
    architecture();assurance();heatmap();dependencies();ctg();boundary();maturity()
    print('Built seven vector publication figures.')
