"""Build the full textbook HTML from book/src/*.md.

Usage: python3 build_book.py <out_dir> [pagemap.json]
"""
import glob, html, json, os, re, sys
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
PAGEMAP = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}

TITLE = "Trust at Scale"
SUBTITLE = "Applied Cryptography from First Principles to the Post-Quantum Era"
AUTHOR = "Bolaji Akinyele"
EDITION = "First Edition · 2026"

PARTS = {
    1: ("I", "Foundations", "The ideas every later chapter depends on: what cryptography is for, the mathematics behind it, and the randomness and hardness that make it work."),
    2: ("II", "Symmetric Cryptography", "The fast workhorses: block ciphers, modes of operation, authenticated encryption, hashing, MACs and key derivation."),
    3: ("III", "Public-Key Cryptography", "How strangers agree on secrets and prove who they are: RSA, Diffie-Hellman, elliptic curves, signatures and the proofs behind them."),
    4: ("IV", "Protocols", "How primitives are assembled into the secure channels and identity systems the world runs on, and how those designs fail."),
    5: ("V", "Certificates and PKI", "Certificates, the trust hierarchies behind them, revocation, private certificate authorities and lifecycle automation at scale."),
    6: ("VI", "Keys, Secrets and Hardware", "Managing keys and secrets across their whole life, the hardware that protects them, and the architecture and governance around it all."),
    7: ("VII", "The Post-Quantum Transition", "Why quantum computers threaten today's public-key cryptography, the new standards that replace it, and how to migrate."),
    8: ("VIII", "Frontiers and Reference", "Where cryptography is heading next, plus a glossary and a guide to further study."),
}

def parse(path):
    src = open(path).read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", src, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    meta["body"] = m.group(2)
    meta["part"] = int(meta["part"])
    meta["objectives"] = [o.strip() for o in meta.get("objectives", "").split("|") if o.strip()]
    return meta

chapters = [parse(p) for p in sorted(glob.glob(f"{ROOT}/src/ch*.md"))]
appendices = [parse(p) for p in sorted(glob.glob(f"{ROOT}/src/app*.md"))]

SPECIAL = [
    ("Lab", "HANDS-ON LAB", "k-lab"), ("At work", "TOOLKIT", "k-work"), ("Failure story", "CASE STUDY", "k-case"),
    ("Chapter summary", "KEY TAKEAWAYS", "k-sum"), ("Review questions", "CHECK YOURSELF", "k-rev"),
    ("Further reading", "GO DEEPER", "k-src"), ("Sources", "REFERENCES", "k-src"), ("References", "REFERENCES", "k-src"),
]

import citations
MISSING = []

def add_citations(md, key):
    refs = citations.C.get(key, [])
    if not refs:
        return md
    for i, (text, anchors) in enumerate(refs, start=1):
        for a in anchors:
            idx = -1
            start = 0
            while True:
                j = md.find(a, start)
                if j < 0:
                    break
                if md[:j].count("```") % 2 == 0 and md.rfind("<svg", 0, j) <= md.rfind("</svg>", 0, j):
                    idx = j
                    break
                start = j + 1
            if idx < 0:
                MISSING.append((key, i, a))
                continue
            end = idx + len(a)
            md = md[:end] + f'<sup class="cite">[{i}]</sup>' + md[end:]
    md = md.rstrip() + "\n\n## References\n\n" + "\n".join(f"{i}. {t}" for i, (t, _) in enumerate(refs, start=1)) + "\n"
    return md

def render_body(ch, label):
    md = add_citations(ch["body"], ch["num"].zfill(2) if ch["num"].isdigit() else ch["num"])
    md = re.sub(r"^(\s*)- \[ \] ", r"\1- ☐ ", md, flags=re.M)
    out = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists"])
    secs = []
    def h2(m):
        title = html.unescape(re.sub("<[^>]+>", "", m.group(1)))
        num = re.match(r"(\d+\.\d+|[A-Z]\.\d+)\s+(.*)", title)
        if num:
            secs.append((num.group(1), num.group(2)))
            return (f'<h2 class="sec"><span class="num">{num.group(1)}</span>'
                    f'<span class="ttl">{html.escape(num.group(2))}</span></h2>')
        for key, kick, cls in SPECIAL:
            if title.startswith(key):
                return (f'<h2 class="sec special {cls}"><span class="kicker">{kick}</span>'
                        f'<span class="ttl">{html.escape(title)}</span></h2>')
        return f'<h2 class="sec"><span class="ttl">{html.escape(title)}</span></h2>'
    out = re.sub(r"<h2>(.*?)</h2>", h2, out)
    def bq(m):
        inner = m.group(1)
        for key, cls, label_txt in [("In practice", "practice", "IN PRACTICE"),
                                    ("Current development", "current", "CURRENT DEVELOPMENT"),
                                    ("Watch out", "warn", "WATCH OUT")]:
            pat = re.compile(r"<p><strong>" + key + r"\.?</strong>\.?\s*")
            if pat.search(inner):
                inner = pat.sub(f'<p><span class="co-label">{label_txt}</span> ', inner, count=1)
                inner = inner.replace('<p><span class="co-label">' + label_txt + '</span> </p>',
                                      f'<p class="co-label-only"><span class="co-label">{label_txt}</span></p>')
                return f'<blockquote class="co {cls}">{inner}</blockquote>'
        return f'<blockquote class="co def">{inner}</blockquote>'
    out = re.sub(r"<blockquote>(.*?)</blockquote>", bq, out, flags=re.S)
    out = re.sub(r"<p><strong>([^<]{2,90}\.)</strong>", r'<p class="term"><strong>\1</strong>', out) if ch.get("glossary") else out
    out = re.sub(r"<li>☐ ", '<li class="chk">', out)
    out = out.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    return out, secs

def pg(key):
    p = PAGEMAP.get(key)
    return f'<span class="pgn">{p}</span>' if p else '<span class="pgn"></span>'

# ---------- per-chapter page rules ----------
page_css = []
def page_rule(name, right, left):
    right = right.replace('"', "'")
    left = left.replace('"', "'")
    page_css.append(f'@page {name} {{ @top-right {{ content: "{right}"; }} @bottom-left {{ content: "{left}"; }} }}')

# ---------- content ----------
parts_html = []
toc_rows = []
for pnum, (roman, ptitle, pdesc) in PARTS.items():
    chs = [c for c in chapters if c["part"] == pnum]
    apps = [a for a in appendices if a["part"] == pnum]
    if not chs and not apps:
        continue
    pkey = f"P{pnum}"
    toc_rows.append(f'<div class="toc-part"><span>Part {roman} · {html.escape(ptitle)}</span>{pg(pkey)}</div>')
    items = "".join(f'<li><span class="n">{c["num"]}</span>{html.escape(c["title"])}</li>' for c in chs)
    items += "".join(f'<li><span class="n">{a["num"]}</span>{html.escape(a["title"])}</li>' for a in apps)
    parts_html.append(f'''
<div class="partpage"><span class="marker">@@{pkey}@@</span>
  <div class="pp-num">PART {roman}</div>
  <h1 class="pp-title">{html.escape(ptitle)}</h1>
  <p class="pp-desc">{html.escape(pdesc)}</p>
  <div class="pp-in">In this part</div>
  <ol class="pp-list">{items}</ol>
</div>''')
    for c in chs + apps:
        is_app = not c["num"].isdigit()
        key = f"C{c['num']}"
        body, secs = render_body(c, c["num"])
        pname = f"ch{c['num']}"
        short = c["title"].split(":")[0]
        if len(short) > 34: short = short[:34].rsplit(" ", 1)[0].rstrip(",") + "…"
        right = (f"APPENDIX {c['num']}" if is_app else f"CHAPTER {c['num']}") + "  ·  " + short.upper()
        page_rule(pname, right, f"Part {roman} · {ptitle}")
        toc_rows.append(f'<div class="toc-ch"><span class="n">{c["num"]}</span><span class="t">{html.escape(c["title"])}</span>{pg(key)}</div>')
        objectives = "".join(f"<li>{html.escape(o)}</li>" for o in c["objectives"])
        sec_list = "".join(f'<li><span class="n">{n}</span>{html.escape(t)}</li>' for n, t in secs)
        obj_box = (f'<div class="op-box"><div class="op-box-h">After this chapter you will be able to</div><ul>{objectives}</ul></div>'
                   if objectives else "")
        parts_html.append(f'''
<div class="opener"><span class="marker">@@{key}@@</span>
  <div class="op-side">
    <div class="op-part">PART {roman}</div>
    <div class="op-part-t">{html.escape(ptitle)}</div>
    <div class="op-label">{"APPENDIX" if is_app else "CHAPTER"}</div>
    <div class="op-num{' small' if len(c['num'])>1 else ''}">{c["num"]}</div>
    <svg class="op-art" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><g fill="#ff5a6a">{''.join(f'<circle cx="{20+x*40+(y%2)*20}" cy="{20+y*40}" r="{3 if (x+y)%3 else 5}" opacity="{0.35 if (x+y)%3 else 0.9}"/>' for x in range(4) for y in range(5))}</g></svg>
  </div>
  <div class="op-main">
    <h1 class="op-title">{html.escape(c["title"])}</h1>
    <p class="op-lead">{html.escape(c.get("lead", ""))}</p>
    {obj_box}
    {'<div class="op-box-h plain">In this chapter</div><ol class="op-toc">' + sec_list + '</ol>' if sec_list else ''}
  </div>
</div>
<main class="body" style="page: {pname}">{body}</main>''')

FONT_FACES = "".join(
    f"@font-face {{ font-family: '{fam}'; src: url('file://{ROOT}/fonts/{fn}'); font-weight: {w}; font-style: {st}; }}\n"
    for fam, fn, w, st in [
        ("Crimson Pro", "CrimsonPro.ttf", "200 900", "normal"), ("Crimson Pro", "CrimsonPro-Italic.ttf", "200 900", "italic"),
        ("Source Sans 3", "SourceSans3.ttf", "200 900", "normal"), ("Source Sans 3", "SourceSans3-Italic.ttf", "200 900", "italic"),
        ("Ubuntu Mono", "UbuntuMono-Regular.ttf", "400", "normal"), ("Ubuntu Mono", "UbuntuMono-Bold.ttf", "700", "normal")])
css = FONT_FACES + open(f"{ROOT}/book.css").read() + "\n" + "\n".join(page_css)

lattice = "".join(
    f'<circle cx="{40 + x*56 + (y*18) % 56}" cy="{30 + y*48}" r="{4 if (x*7+y*3) % 5 else 7}" fill="{"#ff5a6a" if (x*7+y*3) % 5 == 0 else "#9fb4d4"}" opacity="{0.95 if (x*7+y*3) % 5 == 0 else 0.45}"/>'
    for x in range(11) for y in range(7))

doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title><style>{css}</style></head><body>

<div class="cover">
  <svg class="cover-lattice" viewBox="0 0 640 330" xmlns="http://www.w3.org/2000/svg">
    <g stroke="#2c4a73" stroke-width="1" opacity="0.6">{''.join(f'<line x1="{40 + (y*18)%56}" y1="{30+y*48}" x2="{40+10*56+(y*18)%56}" y2="{30+y*48}"/>' for y in range(7))}</g>
    <polyline points="58,30 152,78 226,126 338,174 410,222 522,270" fill="none" stroke="#ff5a6a" stroke-width="2.5" stroke-dasharray="7 6"/>
    {lattice}
  </svg>
  <div class="cover-top">
    <div class="series">A PRACTITIONER'S TEXTBOOK</div>
    <h1 class="book">{TITLE}</h1>
    <p class="cover-sub">{SUBTITLE}</p>
    <div class="cover-tags"><span>Cryptography</span><span>PKI</span><span>Key management</span><span>Secrets</span><span>HSMs</span><span>Post-quantum</span></div>
  </div>
  <div class="cover-author">{AUTHOR}</div>
  <div class="cover-foot"><span>{EDITION}</span><span>Keys · Certificates · Secrets · Post-Quantum</span></div>
</div>

<div class="titlepage">
  <div class="tp-title">{TITLE}</div>
  <div class="tp-sub">{SUBTITLE}</div>
  <div class="tp-rule"></div>
  <div class="tp-author">{AUTHOR}</div>
  <div class="tp-ed">{EDITION}</div>
</div>

<div class="copyright">
  <p><b>{TITLE}</b><br>{SUBTITLE}</p>
  <p>Copyright © 2026 {AUTHOR}. All rights reserved.</p>
  <p>The text and diagrams in this book are original. Facts, data and research drawn from other works are attributed in the References section of each chapter. This book describes general industry practice and publicly documented standards, incidents and research. It does not describe the systems, configuration or practices of any specific organisation. Product and company names mentioned for illustration belong to their respective owners, and their mention does not imply endorsement.</p>
  <p>Standards, browser policies and regulatory timelines change frequently. Facts are current to October 2026; always confirm dates and requirements against the primary source before relying on them.</p>
  <p>{EDITION}</p>
</div>

<div class="front prose">
  <h1 class="fm-h">Preface</h1>
  {markdown.markdown(open(f"{ROOT}/src/preface.md").read(), extensions=["tables"])}
</div>

<div class="front toc-page">
  <div class="kicker-lg">CONTENTS</div>
  <h1 class="toc-h">Contents</h1>
  {''.join(toc_rows)}
</div>

{''.join(parts_html)}

<div class="backcover">
  <div class="bc-title">{TITLE}</div>
  <p>Cryptography protects every login, payment, software update and private message, yet most engineers learn it in fragments. This book connects the fragments. It starts from the mathematics, builds through symmetric and public-key cryptography and real protocols, and arrives at the work that keeps organisations running: certificates and PKI, key and secret management, hardware security modules, and the migration to post-quantum cryptography already under way.</p>
  <p>Every term is defined in plain words. Every chapter ends with labs, real failure stories and review questions, so you can turn understanding into practice.</p>
  <div class="bc-author">{AUTHOR}</div>
</div>
</body></html>"""

os.makedirs(OUT, exist_ok=True)
open(f"{OUT}/book.html", "w").write(doc)
print(f"chapters={len(chapters)} appendices={len(appendices)}")
for m in MISSING: print("MISSING ANCHOR", m)
