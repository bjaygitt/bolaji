"""Front cover: 'Lattice Witness'. Generates cover.html (inline SVG) for Chromium to render."""
import math, random, os
random.seed(1977)  # RSA's year, for a reproducible field

W, H = 504.0, 661.68          # 7in x 9.19in in points
PAPER, INK, GREY, BRASS = "#f3efe6", "#14213a", "#8f8a80", "#a8803a"
B1 = (9.0, 0.0)                # lattice basis vectors (slightly skewed)
B2 = (2.6, 8.4)
OX, OY = 48.0, 262.0           # lattice origin
X0, X1 = 96.0, 456.0           # tree field
LEFT = 48.0

def lp(i, j):
    return (OX + i * B1[0] + j * B2[0], OY + j * B2[1])

def row_points(j, xmin, xmax):
    pts = []
    for i in range(-20, 80):
        x, y = lp(i, j)
        if xmin <= x <= xmax:
            pts.append((i, x, y))
    return pts

svg = []
add = svg.append

# lattice field, fading toward the edges of the art area
for j in range(0, 37):
    for i, x, y in row_points(j, LEFT, W - LEFT):
        cx = (x - (X0 + X1) / 2) / ((W - 2 * LEFT) / 2)
        cy = (y - 420) / 170
        d = math.hypot(cx, cy)
        op = max(0.0, 0.55 - 0.42 * d)
        if op > 0.03:
            add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.42" fill="{GREY}" opacity="{op:.2f}"/>')

# tree levels: (lattice row, count)
levels = [(3, 1), (10, 3), (17, 12), (24, 36)]
nodes = []
for li, (j, n) in enumerate(levels):
    pts = row_points(j, X0, X1)
    span = (X1 - X0)
    targets = [X0 + span * (k + 0.5) / n for k in range(n)] if n > 1 else [(X0 + X1) / 2]
    used, lvl = set(), []
    for t in targets:
        best = min((p for p in pts if p[0] not in used), key=lambda p: abs(p[1] - t))
        used.add(best[0]); lvl.append((best[1], best[2]))
    nodes.append(lvl)

def parent(li, k):
    return k * len(nodes[li - 1]) // len(nodes[li])

# edges
for li in range(1, len(nodes)):
    for k, (x, y) in enumerate(nodes[li]):
        px, py = nodes[li - 1][parent(li, k)]
        my = (py + y) / 2
        w = [0, 0.7, 0.5, 0.35][li]
        add(f'<path d="M{px:.2f},{py:.2f} L{px + (my - py) * B2[0] / B2[1]:.2f},{my:.2f} '
            f'L{x - (y - my) * B2[0] / B2[1]:.2f},{my:.2f} L{x:.2f},{y:.2f}" fill="none" '
            f'stroke="{INK}" stroke-width="{w}" stroke-linejoin="round" opacity="0.85"/>')

# dust: the multitude below the leaves
dust = []
for dj in range(3, 13):
    j = levels[-1][0] + dj
    p = 0.95 - (dj - 3) * 0.085
    for i, x, y in row_points(j, X0, X1):
        if random.random() < p:
            s = 1.15 - (dj - 3) * 0.075
            op = 0.92 - (dj - 3) * 0.075
            dust.append((x, y, s, op))
for x, y, s, op in dust:
    add(f'<rect x="{x - s / 2:.2f}" y="{y - s / 2:.2f}" width="{s:.2f}" height="{s:.2f}" fill="{INK}" opacity="{op:.2f}"/>')

# the verified path: one far leaf, traced back to the root
leaves = nodes[-1]
lk = int(len(leaves) * 0.78)
lx, ly = leaves[lk]
cands = [d for d in dust if d[1] > ly + 7 * B2[1] and X0 <= d[0] <= X1 - 12]
vx, vy, vs, _ = min(cands, key=lambda d: abs(d[0] - (lx + (d[1] - ly) * B2[0] / B2[1])) + 0.02 * abs(d[1] - (ly + 8 * B2[1])))
path = [(vx, vy), leaves[lk]]
k = lk
for li in range(len(nodes) - 1, 0, -1):
    k = parent(li, k); path.append(nodes[li - 1][k])
d = f"M{path[0][0]:.2f},{path[0][1]:.2f}"
for (ax, ay), (bx, by) in zip(path, path[1:]):
    my = (ay + by) / 2
    d += f" L{ax - (ay - my) * B2[0] / B2[1]:.2f},{my:.2f} L{bx + (my - by) * B2[0] / B2[1]:.2f},{my:.2f} L{bx:.2f},{by:.2f}"
add(f'<path d="{d}" fill="none" stroke="{BRASS}" stroke-width="1.05" stroke-linejoin="round"/>')
add(f'<circle cx="{vx:.2f}" cy="{vy:.2f}" r="3.1" fill="none" stroke="{BRASS}" stroke-width="0.6"/>')
add(f'<rect x="{vx - 0.9:.2f}" y="{vy - 0.9:.2f}" width="1.8" height="1.8" fill="{BRASS}"/>')

# nodes drawn over edges
for li, lvl in enumerate(nodes):
    for (x, y) in lvl:
        if li == 0:
            for r, op in ((16, 0.22), (11.5, 0.38), (7.5, 0.6)):
                add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="none" stroke="{BRASS}" stroke-width="0.45" opacity="{op}"/>')
            add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3.4" fill="{BRASS}"/>')
        elif li == 1:
            add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.6" fill="{PAPER}" stroke="{INK}" stroke-width="0.8"/>')
        elif li == 2:
            add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.7" fill="{PAPER}" stroke="{INK}" stroke-width="0.6"/>')
        else:
            add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="1.05" fill="{INK}"/>')

# level scale in the left margin
mono = "font-family:'DM Mono';font-size:5.4px;letter-spacing:0.6px"
labels = ["n = 1", "n = 3", "n = 12", "n = 36"]
for (j, _), lab in zip(levels, labels):
    y = lp(0, j)[1]
    add(f'<line x1="{LEFT}" y1="{y:.2f}" x2="{LEFT + 6}" y2="{y:.2f}" stroke="{GREY}" stroke-width="0.4"/>')
    add(f'<text x="{LEFT + 9}" y="{y + 1.9:.2f}" fill="{GREY}" style="{mono}">{lab}</text>')
ytop, ybot = lp(0, levels[-1][0] + 3)[1], lp(0, levels[-1][0] + 12)[1]
add(f'<line x1="{LEFT + 3}" y1="{ytop:.2f}" x2="{LEFT + 3}" y2="{ybot:.2f}" stroke="{GREY}" stroke-width="0.4"/>')
for yy in (ytop, ybot):
    add(f'<line x1="{LEFT}" y1="{yy:.2f}" x2="{LEFT + 6}" y2="{yy:.2f}" stroke="{GREY}" stroke-width="0.4"/>')
add(f'<text x="{LEFT + 9}" y="{(ytop + ybot) / 2 + 1.9:.2f}" fill="{GREY}" style="{mono}">n &#8776; 10<tspan dy="-2" style="font-size:3.8px">9</tspan></text>')

# registration marks
for cx, cy in ((24, 24), (W - 24, 24), (24, H - 24), (W - 24, H - 24)):
    add(f'<g stroke="{GREY}" stroke-width="0.35" fill="none" opacity="0.8"><circle cx="{cx}" cy="{cy}" r="3.2"/>'
        f'<line x1="{cx - 6}" y1="{cy}" x2="{cx + 6}" y2="{cy}"/><line x1="{cx}" y1="{cy - 6}" x2="{cx}" y2="{cy + 6}"/></g>')

art = "\n".join(svg)

fonts = os.path.abspath(os.path.join(os.path.dirname(__file__), "fonts"))
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family:'Instrument Serif'; src:url('file://{fonts}/InstrumentSerif-Regular.ttf'); }}
@font-face {{ font-family:'Instrument Serif'; font-style:italic; src:url('file://{fonts}/InstrumentSerif-Italic.ttf'); }}
@font-face {{ font-family:'Jura'; font-weight:300; src:url('file://{fonts}/Jura-Light.ttf'); }}
@font-face {{ font-family:'Jura'; font-weight:500; src:url('file://{fonts}/Jura-Medium.ttf'); }}
@font-face {{ font-family:'DM Mono'; src:url('file://{fonts}/DMMono-Regular.ttf'); }}
@page {{ size: 7in 9.19in; margin: 0; }}
html,body {{ margin:0; padding:0; }}
.page {{ width:7in; height:9.19in; position:relative; background:{PAPER}; overflow:hidden; color:{INK}; }}
svg {{ position:absolute; inset:0; width:7in; height:9.19in; }}
.t {{ position:absolute; left:{LEFT}pt; right:{LEFT}pt; }}
.kicker {{ top:56pt; font:300 7.4pt 'Jura'; letter-spacing:3.4pt; text-transform:uppercase; color:{GREY}; }}
.sq {{ display:inline-block; width:4.2pt; height:4.2pt; background:{BRASS}; margin-right:12pt; vertical-align:0.6pt; }}
.t1 {{ top:92pt; font:italic 400 33pt/1 'Instrument Serif'; letter-spacing:0.2pt; }}
.t2 {{ top:124pt; font:400 66pt/1 'Instrument Serif'; letter-spacing:-0.6pt; }}
.rule {{ top:206pt; height:0; border-top:0.5pt solid {INK}; width:58pt; }}
.sub {{ top:216pt; font:300 9.2pt/1.5 'Jura'; letter-spacing:0.9pt; color:#3c4658; width:300pt; }}
.foot {{ bottom:46pt; display:flex; justify-content:space-between; align-items:baseline; }}
.plate {{ font:400 5.6pt 'DM Mono'; letter-spacing:1.2pt; color:{GREY}; text-transform:uppercase; }}
.author {{ font:500 10.5pt 'Jura'; letter-spacing:3.2pt; text-transform:uppercase; }}
</style></head><body><div class="page">
<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">{art}</svg>
<div class="t kicker"><i class="sq"></i>Applied cryptography for the enterprise</div>
<div class="t t1">Cryptographic</div>
<div class="t t2">Trust at Scale</div>
<div class="t rule"></div>
<div class="t sub">From first principles to the post-quantum era</div>
<div class="t foot"><span class="plate">Plate I &nbsp;/&nbsp; Second edition</span><span class="author">Bolaji Johnson A.</span></div>
</div></body></html>"""
open(os.path.join(os.path.dirname(__file__), "cover.html"), "w").write(html)
print("ok", len(dust), "dust marks")
