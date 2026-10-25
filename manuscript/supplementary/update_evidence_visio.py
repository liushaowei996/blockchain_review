"""Build Figure 7 as six native text-and-box diagrams in the existing Visio file.

Only the Figure-07 page content and its page dimensions change. The other
figure pages, original uploaded drawing and existing figure PDFs are preserved.
Export this page with export_visio_figures.ps1 -FigureNumbers 7.
"""
from pathlib import Path
from zipfile import ZipFile
from xml.dom import minidom
import argparse
import math
import os
import tempfile

NS = 'http://schemas.microsoft.com/office/visio/2012/main'
DATA = Path(__file__).resolve().parent


def children(node, name):
    return [n for n in node.childNodes
            if n.nodeType == n.ELEMENT_NODE and n.localName == name]


def element(doc, parent, name, **attributes):
    node = doc.createElement(name)
    for key, value in attributes.items():
        node.setAttribute(key, str(value))
    parent.appendChild(node)
    return node


def cell(doc, parent, name, value, formula=None):
    attrs = {'N': name, 'V': str(value)}
    if formula is not None:
        attrs['F'] = formula
    return element(doc, parent, 'Cell', **attrs)


def update(source):
    with ZipFile(source) as archive:
        infos = archive.infolist()
        parts = {info.filename: archive.read(info) for info in infos}
    pages = minidom.parseString(parts['visio/pages/pages.xml'])
    target = next(p for p in children(pages.documentElement, 'Page')
                  if p.getAttribute('Name') == 'Figure-07')
    relationship = children(target, 'Rel')[0].getAttribute('r:id')
    rels = minidom.parseString(parts['visio/pages/_rels/pages.xml.rels'])
    page_name = next(r.getAttribute('Target') for r in children(rels.documentElement, 'Relationship')
                     if r.getAttribute('Id') == relationship)
    page_part = 'visio/pages/' + page_name
    sheet = children(target, 'PageSheet')[0]
    for name, value in [('PageWidth', 12), ('PageHeight', 7.2), ('DrawingResizeType', 0)]:
        entries = [c for c in children(sheet, 'Cell') if c.getAttribute('N') == name]
        c = entries[0] if entries else element(pages, sheet, 'Cell', N=name)
        c.setAttribute('V', str(value))
        if name != 'DrawingResizeType':
            c.setAttribute('U', 'IN')
        if c.hasAttribute('F'):
            c.removeAttribute('F')

    doc = minidom.Document()
    root = element(doc, doc, 'PageContents', xmlns=NS,
                   **{'xmlns:r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'})
    shapes = element(doc, root, 'Shapes')
    next_id = 0

    def shape():
        nonlocal next_id
        next_id += 1
        return element(doc, shapes, 'Shape', ID=next_id, Type='Shape',
                       LineStyle=3, FillStyle=3, TextStyle=3)

    def rectangle(x, y, width, height, text='', fill='#FFFFFF', line='#CBD3DC',
                  color='#203864', font=15.5, bold=False, rounding=.06):
        sh = shape()
        values = {'PinX': x+width/2, 'PinY': y+height/2, 'Width': width, 'Height': height,
                  'LocPinX': width/2, 'LocPinY': height/2, 'Angle': 0,
                  'FillForegnd': fill, 'FillPattern': 1, 'LineColor': line,
                  'LinePattern': 1, 'LineWeight': .011, 'Rounding': rounding,
                  'ShdwPattern': 0, 'GlowSize': 0, 'SoftEdgesSize': 0,
                  'VerticalAlign': 1, 'LeftMargin': .055, 'RightMargin': .055,
                  'TopMargin': .015, 'BottomMargin': .015}
        for key, value in values.items():
            cell(doc, sh, key, value)
        character = element(doc, sh, 'Section', N='Character')
        row = element(doc, character, 'Row', IX=0)
        for key, value in [('Color', color), ('Style', 1 if bold else 0), ('Size', font/72)]:
            cell(doc, row, key, value)
        paragraph = element(doc, sh, 'Section', N='Paragraph')
        row = element(doc, paragraph, 'Row', IX=0)
        cell(doc, row, 'HorzAlign', 1)
        geometry = element(doc, sh, 'Section', N='Geometry', IX=0)
        cell(doc, geometry, 'NoFill', 0)
        cell(doc, geometry, 'NoLine', 0)
        for i, (xx, yy) in enumerate([(0,0),(width,0),(width,height),(0,height),(0,0)], 1):
            row = element(doc, geometry, 'Row', T='MoveTo' if i==1 else 'LineTo', IX=i)
            cell(doc, row, 'X', xx)
            cell(doc, row, 'Y', yy)
        if text:
            node = element(doc, sh, 'Text')
            element(doc, node, 'cp', IX=0)
            node.appendChild(doc.createTextNode(text+'\n'))
        return sh

    def arrow(x, y_top, y_bottom, color):
        sh = shape()
        length = y_top-y_bottom
        values = {'PinX': x, 'PinY': (y_top+y_bottom)/2, 'Width': length, 'Height': 0,
                  'LocPinX': length/2, 'LocPinY': 0, 'Angle': -math.pi/2,
                  'BeginX': x, 'BeginY': y_top, 'EndX': x, 'EndY': y_bottom,
                  'LineColor': color, 'LineWeight': .014, 'LinePattern': 1,
                  'BeginArrow': 0, 'EndArrow': 4, 'EndArrowSize': 1,
                  'ShdwPattern': 0, 'GlowSize': 0, 'SoftEdgesSize': 0}
        for key, value in values.items():
            cell(doc, sh, key, value)
        geometry = element(doc, sh, 'Section', N='Geometry', IX=0)
        cell(doc, geometry, 'NoFill', 1)
        for i, xx in enumerate([0,length], 1):
            row=element(doc, geometry, 'Row', T='MoveTo' if i==1 else 'LineTo', IX=i)
            cell(doc,row,'X',xx)
            cell(doc,row,'Y',0)

    cards = [
        ('Conceptual\nargument', '#547730', '#EBF4E4',
         ['Mission need', 'Proposed mechanism', 'Claim and rationale']),
        ('Analytical/security\nreasoning', '#1D5D86', '#EAF2F9',
         ['Assumptions and model', 'Derivation or security analysis', 'Property under assumptions']),
        ('Simulation or\nrecorded data', '#946F00', '#FFF6D9',
         ['Simulation or recorded data', 'Evaluation protocol', 'Measured outcomes']),
        ('Prototype or\ntestbed', '#585F6A', '#F0F2F5',
         ['Implemented system', 'Controlled workload', 'Observed behavior']),
        ('Physical\noperating trial', '#A95D26', '#FFF0E4',
         ['Platform and environment', 'Test in operating conditions', 'Observed outcomes']),
        ('Sustained multi-party\noperation', '#6849A0', '#F2EDF9',
         ['Multi-party operation', 'Failures and recovery', 'Longitudinal evidence']),
    ]
    card_width = (12-.44-.44)/3
    for i, (title, color, tint, boxes) in enumerate(cards):
        x=.22+(i%3)*(card_width+.22)
        top=6.98-(i//3)*2.92
        rectangle(x,top-2.72,card_width,2.72,fill='#FFFFFF',line='#BCC6D1',rounding=.10)
        rectangle(x+.02,top-.76,card_width-.04,.74,fill=tint,line=tint,rounding=.08)
        rectangle(x+.14,top-.61,.5,.46,f'L{i}',fill=color,line=color,
                  color='#FFFFFF',font=19,bold=True)
        rectangle(x+.75,top-.70,card_width-.88,.62,title,fill=tint,line=tint,
                  font=17.5,bold=True)
        for j, label in enumerate(boxes):
            center_y=top-1.06-j*.61
            rectangle(x+.25,center_y-.22,card_width-.50,.44,label,
                      fill=tint if j==2 else '#FFFFFF',line=color,
                      color='#203864',font=15.5,bold=(j==2))
            if j<2:
                arrow(x+card_width/2,center_y-.235,center_y-.375,color)
    rectangle(.22,.22,11.56,.92,fill='#F5F7FA',line='#BCC6D1',rounding=.08)
    rectangle(.40,.72,11.20,.28,'Assess each supported claim',fill='#F5F7FA',line='#F5F7FA',font=16.5,bold=True)
    for i,label in enumerate(['Rigor and uncertainty','Environmental fit','Scope and duration']):
        rectangle(.44+i*3.77,.34,3.57,.31,label,fill='#FFFFFF',line='#D5DDE7',font=15.5)

    parts[page_part] = doc.toxml(encoding='utf-8')
    parts['visio/pages/pages.xml'] = pages.toxml(encoding='utf-8')
    handle, temporary = tempfile.mkstemp(suffix='.vsdx', dir=source.parent)
    os.close(handle)
    try:
        with ZipFile(temporary,'w') as archive:
            for info in infos:
                archive.writestr(info,parts[info.filename])
        with ZipFile(temporary) as archive:
            assert archive.testzip() is None
        os.replace(temporary,source)
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)
    print(f'Built six text-and-box panels ({next_id} native shapes) in {page_part}.')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',nargs='?',type=Path,default=DATA.parent/'figures/Figures-revised.vsdx')
    update(parser.parse_args().source.resolve())
