#!/usr/bin/env python3
"""Builds assets/duty-map.svg: the Security Officer's legal duties in one dark diagram.

Layout: the upper band is the DL 65/2021 anatomy trained on (named functions,
risk cycle, incidents and authorities); the lower band is what DL 125/2025 +
Reg. 756/2026 add in 2026. Each box carries a tag with the module that details it.
No DL 125/2025 article numbers: only what the modules already state.

PNG: google-chrome --headless --screenshot=assets/duty-map.png \
       --window-size=1920,1140 --force-device-scale-factor=1.25 assets/duty-map.svg"""
from pathlib import Path

W, H = 1920, 1140
SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
MONO = "'DejaVu Sans Mono', 'Liberation Mono', monospace"

INK, MUTED, PAPER = "#e6edf3", "#8d99a8", "#0b1016"
RED, TEAL, DATA, VIOLET = "#ff6b5e", "#3fd18a", "#5cc8e0", "#b197fc"
BOX_FILL, BODY, NOTE_FILL, NOTE_TEXT = "#111821", "#c9d3df", "#161b22", "#b9c2cd"
RULE = "#3a4554"
ZONES = {  # band fill, border/label, box header
    "roles": ("#171309", "#f0a640", "#3a2a10"),
    "cycle": ("#0d1420", "#6ea8ff", "#15284a"),
    "incident": ("#170f12", "#ff7a6b", "#3a1b1e"),
    "authority": ("#130f1d", VIOLET, "#2a2142"),
    "now": ("#0c1712", "#4fd18b", "#113322"),
}
COLORS = {"duty": DATA, "report": RED, "cycle": TEAL, "sign": "#f0a640"}

out = []
add = out.append


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=15, weight="normal", fill=INK, anchor="start",
         style="normal", family=SANS, halo=False, spacing=0):
    extra = (f' paint-order="stroke" stroke="{PAPER}" stroke-width="5" '
             f'stroke-linejoin="round"') if halo else ""
    sp = f' letter-spacing="{spacing}"' if spacing else ""
    add(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" font-style="{style}" fill="{fill}" '
        f'text-anchor="{anchor}"{sp}{extra}>{esc(s)}</text>')


HDR, LINE, PAD = 54, 22, 14


def box_height(sections):
    return HDR + sum(PAD + LINE * len(sec) for sec in sections) + 6


def tag(x, y, w, label, color):
    pw = 14 + 7.5 * len(label)
    px = x + w - 8 - pw
    add(f'<rect x="{px}" y="{y + 8}" width="{pw}" height="20" rx="10" fill="{PAPER}" '
        f'stroke="{color}" stroke-width="1.2"/>')
    text(px + pw / 2, y + 22.5, label, 11.5, "bold", color, "middle", family=MONO)


def box(x, y, w, stereo, title, sections, key, module=None):
    """UML-style box: «stereotype» + name, then compartments. A line that
    starts with '#' is a bold compartment heading."""
    total = box_height(sections)
    edge = ZONES[key][1]
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{total}" rx="7" fill="{BOX_FILL}" '
        f'stroke="{edge}" stroke-width="1.6"/>')
    add(f'<path d="M{x},{y+HDR} L{x},{y+7} Q{x},{y} {x+7},{y} L{x+w-7},{y} '
        f'Q{x+w},{y} {x+w},{y+7} L{x+w},{y+HDR} Z" fill="{ZONES[key][2]}" '
        f'stroke="{edge}" stroke-width="1.6"/>')
    text(x + w / 2, y + 20, f"«{stereo}»", 13, "normal", MUTED, "middle", "italic")
    text(x + w / 2, y + 43, title, 18, "bold", edge, "middle")
    if module:
        tag(x, y, w, module, edge)
    cy = y + HDR
    for i, sec in enumerate(sections):
        if i:
            add(f'<line x1="{x}" y1="{cy}" x2="{x+w}" y2="{cy}" stroke="{edge}" stroke-width="1.2"/>')
        ly = cy + PAD + 12
        for ln in sec:
            if ln.startswith("#"):
                text(x + 16, ly, ln[1:], 15, "bold", INK)
            else:
                text(x + 16, ly, ln, 15, "normal", BODY)
            ly += LINE
        cy += PAD + LINE * len(sec)
    return total


def arrow(pts, kind="duty", dash=None):
    dasharray = dash if dash is not None else {"duty": "", "report": "8 6", "cycle": "9 6", "sign": ""}[kind]
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    da = f' stroke-dasharray="{dasharray}"' if dasharray else ""
    add(f'<path d="{d}" fill="none" stroke="{COLORS[kind]}" stroke-width="2.6"{da} '
        f'marker-end="url(#ah-{kind})"/>')


def label(x, y, s, kind, anchor="middle"):
    text(x, y, s, 13.5, "bold", COLORS[kind], anchor, halo=True)


def note(x, y, w, lines):
    fold, h = 16, 18 + 19 * len(lines)
    add(f'<path d="M{x},{y} L{x+w-fold},{y} L{x+w},{y+fold} L{x+w},{y+h} L{x},{y+h} Z" '
        f'fill="{NOTE_FILL}" stroke="{MUTED}" stroke-width="1.3"/>')
    add(f'<path d="M{x+w-fold},{y} L{x+w-fold},{y+fold} L{x+w},{y+fold}" fill="none" '
        f'stroke="{MUTED}" stroke-width="1.3"/>')
    ly = y + 23
    for ln in lines:
        text(x + 13, ly, ln, 14, "normal", NOTE_TEXT, style="italic")
        ly += 19


def band(x0, x1, y0, y1, key, title, dashed=True):
    fill, stroke, _ = ZONES[key]
    da = ' stroke-dasharray="8 6"' if dashed else ""
    add(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="18" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="1.8"{da}/>')
    text((x0 + x1) / 2, y0 + 32, title, 14, "bold", stroke, "middle", spacing=1.6)


# ------------------------------------------------------------------ canvas
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
add("<defs>")
for kind, color in COLORS.items():
    add(f'<marker id="ah-{kind}" viewBox="0 0 12 12" refX="10.5" refY="6" markerWidth="10" '
        f'markerHeight="10" orient="auto-start-reverse"><path d="M1,1 L11.5,6 L1,11 L4,6 Z" '
        f'fill="{color}"/></marker>')
add('<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse">'
    '<circle cx="2" cy="2" r="1.1" fill="#1c2633"/></pattern>')
add("</defs>")
add(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
add(f'<rect width="{W}" height="{H}" fill="url(#dots)"/>')

# title block
text(40, 62, "Security Officer Duty Map · Portugal", 38, "bold", DATA, family=MONO)
text(40, 94, "The DL 65/2021 anatomy I trained on   →   what DL 125/2025 (NIS2) + Regulamento 756/2026 "
     "add from April 2026", 17, "normal", MUTED)
text(1880, 60, "Gabriel Affonso", 19, "bold", INK, "end")
text(1880, 86, "CNCS training · Responsável de Cibersegurança · 2025", 15, "normal", MUTED, "end")
add(f'<line x1="40" y1="112" x2="1880" y2="112" stroke="{RULE}" stroke-width="1.4"/>')

# ------------------------------------------------------------------ upper band: trained model
TOP, BOT = 124, 780
band(40, 425, TOP, BOT, "roles", "NAMED FUNCTIONS")
band(440, 1420, TOP, BOT, "cycle", "RISK CYCLE · DL 65/2021")
band(1435, 1880, TOP, BOT, "incident", "INCIDENTS · AUTHORITIES")

# named functions
box(65, 200, 335, "function", "Ponto de Contacto Permanente",
    [["Operational channel with CNCS", "a function, not a person", "24/7 during activation"],
     ["#Notify CNCS", "≤ 20 working days after start", "immediately on any change"]],
    "roles", "Art.4")
SO_Y = 450
box(65, SO_Y, 335, "function", "Responsável de Segurança",
    [["CISO-shaped role", "reports to top management"],
     ["#Signs", "asset inventory", "security plan", "annual report"]],
    "roles", "Art.5")

# risk cycle: row 1 left → right, row 2 right → left
R1, R2, BW = 230, 500, 280
XS = (466, 791, 1116)
box(XS[0], R1, BW, "duty", "Asset inventory",
    [["internal CMDB for risk", "signed extract for CNCS", "owner = a name, not an alias"]],
    "cycle", "Art.6 · M07")
box(XS[1], R1, BW, "duty", "Risk analysis",
    [["threat · vuln · asset · control", "ISO 27005 · MONARC", "residual risk has an owner"]],
    "cycle", "Art.10 · M03")
box(XS[2], R1, BW, "duty", "Measures (TOMs)",
    [["from QNRCS / ISO 27002", "CIS v8 as first backlog", "defense in depth"]],
    "cycle", "Art.9 · M05")
box(XS[2], R2, BW, "duty", "Security plan",
    [["measures · owners · budget", "continuity: BCP / DR", "RTO / RPO"]],
    "cycle", "Art.7 · M10")
box(XS[1], R2, BW, "duty", "Annual report",
    [["what we said · what we did", "what broke · what is next", "sent to CNCS, on time"]],
    "cycle", "Art.8 · M11")
note(XS[0], 600, BW, ["Each artefact cites the", "previous one. The cycle is", "the compliance programme (M12)."])

MID1, MID2 = R1 + 70, R2 + 70
arrow([(XS[0] + BW, MID1), (XS[1] - 2, MID1)])
arrow([(XS[1] + BW, MID1), (XS[2] - 2, MID1)])
arrow([(XS[2] + BW / 2, R1 + 140), (XS[2] + BW / 2, R2 - 2)])
arrow([(XS[2], MID2), (XS[1] + BW + 2, MID2)])
arrow([(XS[1] + BW / 2, R2), (XS[1] + BW / 2, R1 + 142)], "cycle")
label(XS[1] + BW / 2 + 12, (R1 + 140 + R2) / 2 + 5, "next cycle", "cycle", "start")

# Security Officer signs the artefacts
SIGN_Y = 476
arrow([(400, SIGN_Y), (430, SIGN_Y), (430, MID1), (XS[0] - 2, MID1)], "sign")
arrow([(430, SIGN_Y), (760, SIGN_Y), (760, MID2), (XS[1] - 2, MID2)], "sign")
label(600, SIGN_Y - 10, "owns · signs", "sign")

# incidents and authorities
IX, IW = 1460, 395
box(IX, 215, IW, "authority", "CNCS · CSIRT Nacional",
    [["cyber incident notification", "supervision of the entity"]],
    "authority")
IR_Y = 390
box(IX, IR_Y, IW, "process", "Incident response",
    [["#Lifecycle", "prepare · detect · contain", "eradicate · recover · learn"],
     ["#Severity model", "lessons learned feed Art. 10"]],
    "incident", "Arts.11–17 · M08")
box(IX, 640, IW, "authority", "CNPD",
    [["personal-data breach", "RGPD Art. 33 · 72 h"]],
    "authority")
arrow([(IX + IW / 2, IR_Y), (IX + IW / 2, 335)], "report")
label(IX + IW / 2 + 12, 368, "notify", "report", "start")
arrow([(IX + IW / 2, IR_Y + 202), (IX + IW / 2, 638)], "report")
label(IX + IW / 2 + 14, 624, "if personal data", "report", "start")
# PCP is the channel to CNCS: routed along the top of the bands
arrow([(400, 240), (414, 240), (414, 188), (IX + 40, 188), (IX + 40, 213)], "report")
label(930, 208, "24/7 channel to CNCS", "report")

# ------------------------------------------------------------------ lower band: 2026
NY0, NY1 = 800, 1010
band(40, 1880, NY0, NY1, "now", "IN FORCE 2026 · DL 125/2025 (NIS2) + REGULAMENTO 756/2026", dashed=False)
NB, NW, NG = 850, 428, 26
nx = [40 + 25 + i * (NW + NG) for i in range(4)]
box(nx[0], NB, NW, "scope", "Wider scope",
    [["essential · important · relevant public", "thousands more organisations", "incl. medium enterprises in listed sectors"]],
    "now", "M01")
box(nx[1], NB, NW, "governance", "Management body accountable",
    [["liability is in force, not a talking point", "fines at GDPR scale", "same PCP + Security Officer, re-notified"]],
    "now", "M01")
box(nx[2], NB, NW, "measures", "Supply chain & more",
    [["supplier risk inside the measures", "cryptography · HR security", "business continuity"]],
    "now", "M05")
box(nx[3], NB, NW, "reporting", "MyCiber",
    [["CNCS platform: register / self-identify", "national incident-reporting channel", "early warning → notification → report"]],
    "now", "M08")

# ------------------------------------------------------------------ legend + footer
add(f'<line x1="40" y1="1030" x2="1880" y2="1030" stroke="{RULE}" stroke-width="1.4"/>')
ly = 1060
arrow([(40, ly), (90, ly)]); text(102, ly + 5, "duty flow", 15, "normal", MUTED)
arrow([(210, ly), (260, ly)], "sign"); text(272, ly + 5, "owns / signs", 15, "normal", MUTED)
arrow([(400, ly), (450, ly)], "report"); text(462, ly + 5, "report to an authority", 15, "normal", MUTED)
arrow([(650, ly), (700, ly)], "cycle"); text(712, ly + 5, "next cycle", 15, "normal", MUTED)
tag(820, ly - 18, 104, "Art.6 · M07", INK)
text(932, ly + 5, "DL 65/2021 article · repo module", 15, "normal", MUTED)


def chip(x, y, label_, w):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="15" fill="{BOX_FILL}" stroke="{MUTED}" stroke-width="1.3"/>')
    text(x + w / 2, y + 20.5, label_, 13.5, "bold", INK, "middle")


chip(40, 1088, "QNRCS · ISO/IEC 27001 / 27005 · NIST CSF 2.0 · CIS Controls v8 · MONARC", 600)
text(1880, 1109, "github.com/gabzaf/cybersecurity-officer", 17, "bold", INK, "end")

add("</svg>")

path = Path(__file__).with_name("duty-map.svg")
path.write_text("\n".join(out), encoding="utf-8")
print("wrote", path)
