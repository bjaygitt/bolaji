"""Build the second edition (Cryptographic Trust at Scale) from book/src2/*.md.

Usage: python3 build_book.py <out_dir> [pagemap.json]
"""
import glob, html, json, os, re, sys
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
PAGEMAP = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}

TITLE = "Cryptographic Trust at Scale"
SUBTITLE = "Applied Cryptography for the Enterprise, from First Principles to the Post-Quantum Era"
AUTHOR = "Bolaji Johnson A."
EDITION = "Second Edition · 2026"

PARTS = {
    1: ("I", "Foundations: Cryptography in the Enterprise", "What cryptography is for, where it lives across a modern enterprise, and the mathematics, randomness and hardness everything else rests on."),
    2: ("II", "The Building Blocks", "Block ciphers, modes and authenticated encryption, hashing and key derivation, RSA, Diffie-Hellman, elliptic curves and signatures, and how protocols fail."),
    3: ("III", "Trust and Identity: PKI", "Certificates, the public and private trust hierarchies behind them, revocation, enterprise PKI architecture and the identity protocols built on keys."),
    4: ("IV", "Certificate Lifecycle Automation", "A standalone guide for certificate automation engineers: platforms, protocols, integrations across every technology stack, and operations in the short-lived era."),
    5: ("V", "Data in Transit", "TLS from handshake to enterprise deployment, private networks and zero trust, the public internet and the edge, service-to-service encryption, SSH and email."),
    6: ("VI", "Data at Rest", "Storage, database and application-layer encryption, cloud key management, data-centric protection and crypto-shredding."),
    7: ("VII", "Data in Use", "Confidential computing and the privacy-enhancing technologies that compute on data without exposing it."),
    8: ("VIII", "Key Management and Hardware", "Key management fundamentals, HSMs, enterprise key managers, secrets and workload identity, endpoints and code signing."),
    9: ("IX", "Payments Cryptography", "How card payments are protected end to end, the payment HSMs and key hierarchies behind them, and the programmes that govern them."),
    10: ("X", "Governance, Risk and Compliance", "Standards and validation, the regulations mapped to cryptographic controls, architecture and agility, and running a cryptography programme."),
    11: ("XI", "The Post-Quantum Transition", "The quantum threat, the new standardised algorithms, and how an enterprise plans and executes its migration."),
    12: ("XII", "Bringing It Together", "One transaction traced end to end across every key, certificate and protocol in the book, followed by the reference appendices."),
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

chapters = [parse(p) for p in sorted(glob.glob(f"{ROOT}/src2/ch*.md"))]
appendices = [parse(p) for p in sorted(glob.glob(f"{ROOT}/src2/app*.md"))]

SPECIAL = [
    ("Lab", "HANDS-ON LAB", "k-lab"), ("Where to go next", "NEXT", "k-sum"), ("At work", "TOOLKIT", "k-work"), ("Failure story", "CASE STUDY", "k-case"),
    ("Chapter summary", "KEY TAKEAWAYS", "k-sum"), ("Review questions", "CHECK YOURSELF", "k-rev"),
    ("Further reading", "GO DEEPER", "k-src"), ("Sources", "REFERENCES", "k-src"), ("References", "REFERENCES", "k-src"),
]

class _C: pass
citations = _C()
citations.C = {}
for _p in glob.glob(f"{ROOT}/src2/cites/*.json"):
    _k = os.path.basename(_p)[:-5]
    _k = _k[2:] if _k.startswith("ch") else _k[3:]
    citations.C[_k] = [(e["cite"], e["anchors"]) for e in json.load(open(_p))]
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
            end = idx + len(a.rstrip(' |')) if a.endswith('|') else idx + len(a)
            md = md[:end] + f'<sup class="cite">[{i}]</sup>' + md[end:]
    md = md.rstrip() + "\n\n## References\n\n" + "\n".join(f"{i}. {t}" for i, (t, _) in enumerate(refs, start=1)) + "\n"
    return md

def render_body(ch, key):
    md = add_citations(ch["body"], ch["num"].zfill(2) if ch["num"].isdigit() else ch["num"])
    md = re.sub(r"^(\s*)- \[ \] ", r"\1- ☐ ", md, flags=re.M)
    out = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists"])
    # demote headings: chapter title is h2 (part is h1), sections h3, subsections h4
    out = re.sub(r"<(/?)h3>", r"<\1h4>", out)
    secs = []
    def h2(m):
        title = html.unescape(re.sub("<[^>]+>", "", m.group(1)))
        sid = f"{key}-s{len(secs) + 1}"
        mk = f'<span class="marker">@@{sid.upper().replace("-", "")}@@</span>'
        num = re.match(r"(\d+\.\d+|[A-Z]\.\d+)\s+(.*)", title)
        label = num.group(2) if num else title
        secs.append((sid, label))
        numhtml = f'<span class="num">{num.group(1)}</span>' if num else ""
        cls = "sec"
        for k2, _, c2 in SPECIAL:
            if title.startswith(k2):
                cls += " special " + c2
        return f'<h3 class="{cls}" id="{sid}">{mk}{numhtml}{html.escape(label)}</h3>'
    out = re.sub(r"<h2>(.*?)</h2>", h2, out)
    def bq(m):
        inner = m.group(1)
        for k2, cls, lab in [("In practice", "practice", "In Practice"),
                             ("Current development", "current", "Current Development"),
                             ("Watch out", "warn", "Warning"),
                             ("At Meridian", "meridian", "At Meridian"),
                             ("Compliance hook", "comp", "Compliance Hook")]:
            pat = re.compile(r"<p><strong>" + k2 + r"\.?</strong>\.?\s*")
            if pat.search(inner):
                inner = pat.sub("<p>", inner, count=1).replace("<p></p>", "")
                return f'<aside class="co {cls}"><div class="co-label">{lab}</div>{inner}</aside>'
        return f'<blockquote class="def">{inner}</blockquote>'
    out = re.sub(r"<blockquote>(.*?)</blockquote>", bq, out, flags=re.S)
    if ch.get("glossary"):
        out = re.sub(r"<p><strong>([^<]{2,90}\.)</strong>", r'<p class="term"><strong>\1</strong>', out)
    out = re.sub(r"<li>☐ ", '<li class="chk">', out)
    return out, secs

def pg(key):
    p = PAGEMAP.get(key.upper().replace("-", ""))
    return str(p) if p else ""

def esc_css(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

page_css = ['@page front:left { @bottom-left { content: counter(page) "   |   Cryptographic Trust at Scale"; } }\n@page front:right { @bottom-right { content: "Cryptographic Trust at Scale   |   " counter(page); } }']
def page_rule(name, left_text, right_text):
    page_css.append(
        f'@page {name}:left {{ @bottom-left {{ content: counter(page) "   |   {esc_css(left_text)}"; }} }}\n'
        f'@page {name}:right {{ @bottom-right {{ content: "{esc_css(right_text)}   |   " counter(page); }} }}')

parts_html, toc = [], []
toc.append(f'<div class="toc-ch top"><a href="#preface"><span class="t">Preface</span><span class="dots"></span><span class="p">{pg("PREFACE")}</span></a></div>')
for pnum, (roman, ptitle, pdesc) in PARTS.items():
    chs = [c for c in chapters if c["part"] == pnum] + [a for a in appendices if a["part"] == pnum]
    if not chs:
        continue
    pid = f"part{pnum}"
    toc.append(f'<div class="toc-part"><a href="#{pid}"><span class="pn">Part {roman}.</span><span class="t">{html.escape(ptitle)}</span><span class="p">{pg(pid)}</span></a></div>')
    items = "".join(f'<li><a href="#ch{c["num"]}"><span class="n">{"Appendix " if not c["num"].isdigit() else ""}{c["num"]}</span>{html.escape(c["title"])}</a></li>' for c in chs)
    parts_html.append(f"""
<section class="partpage" id="{pid}"><span class="marker">@@{pid.upper()}@@</span>
  <div class="pp-label">Part {roman}</div>
  <h1 class="pp-title">{html.escape(ptitle)}</h1>
  <p class="pp-desc">{html.escape(pdesc)}</p>
  <ol class="pp-list">{items}</ol>
</section>""")
    for c in chs:
        is_app = not c["num"].isdigit()
        cid = f"ch{c['num']}"
        body, secs = render_body(c, cid)
        pname = f"pg{c['num']}"
        label = (f"Appendix {c['num']}" if is_app else f"Chapter {c['num']}")
        short = c["title"].split(":")[0]
        if len(short) > 66: short = short[:66].rsplit(" ", 1)[0].rstrip(",") + "…"
        page_rule(pname, f"{label}: {short}", short)
        toc.append(f'<div class="toc-ch"><a href="#{cid}"><span class="n">{"" if is_app else c["num"] + "."}</span>'
                   f'<span class="t">{"Appendix " + c["num"] + ": " if is_app else ""}{html.escape(c["title"])}</span><span class="dots"></span><span class="p">{pg(cid)}</span></a></div>')
        toc.append('<ul class="toc-secs">' + "".join(
            f'<li><a href="#{sid}"><span class="t">{html.escape(t)}</span><span class="p">{pg(sid)}</span></a></li>' for sid, t in secs) + "</ul>")
        objectives = "".join(f"<li>{html.escape(o)}</li>" for o in c["objectives"])
        obj = (f'<div class="objectives"><p class="obj-h">By the end of this chapter, you will be able to:</p><ul>{objectives}</ul></div>'
               if objectives else "")
        parts_html.append(f"""
<article class="chapter" id="{cid}" style="page: {pname}"><span class="marker">@@{cid.upper()}@@</span>
  <header class="ch-head">
    <div class="ch-label">{label}</div>
    <h2 class="ch-title">{html.escape(c["title"])}</h2>
  </header>
  <p class="ch-lead">{html.escape(c.get("lead", ""))}</p>
  {obj}
  {body}
</article>""")

FONTS = [("Source Serif 4", "SourceSerif4.ttf", "200 900", "normal"), ("Source Serif 4", "SourceSerif4-Italic.ttf", "200 900", "italic"),
         ("Fira Sans Condensed", "FiraSansCondensed-Regular.ttf", "400", "normal"), ("Fira Sans Condensed", "FiraSansCondensed-Medium.ttf", "500", "normal"),
         ("Fira Sans Condensed", "FiraSansCondensed-SemiBold.ttf", "600", "normal"), ("Fira Sans Condensed", "FiraSansCondensed-Bold.ttf", "700", "normal"),
         ("Outfit", "Outfit.ttf", "100 900", "normal"),
         ("Ubuntu Mono", "UbuntuMono-Regular.ttf", "400", "normal"), ("Ubuntu Mono", "UbuntuMono-Bold.ttf", "700", "normal")]
FONT_FACES = "".join(f"@font-face {{ font-family: '{f}'; src: url('file://{ROOT}/fonts/{fn}'); font-weight: {w}; font-style: {s}; }}\n" for f, fn, w, s in FONTS)
css = FONT_FACES + open(f"{ROOT}/book.css").read() + "\n" + "\n".join(page_css)

preface_html = markdown.markdown(open(f"{ROOT}/src2/preface.md").read(), extensions=["tables"])
preface_html = re.sub(r"<(/?)h2>", r"<\1h3>", preface_html)
COVER = open(f"{ROOT}/cover/cover_frag.html").read()

doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title><style>{css}</style></head><body>

{COVER}

<div class="titlepage">
  <div class="tp-title">{TITLE}</div>
  <div class="tp-sub">{SUBTITLE}</div>
  <div class="tp-author">{AUTHOR}</div>
</div>

<div class="copyright">
  <p><b>{TITLE}</b><br>{SUBTITLE}<br>by {AUTHOR}</p>
  <p>Copyright © 2026 {AUTHOR}. All rights reserved.</p>
  <p>The text and diagrams in this book are original. Facts, data and research drawn from other works are attributed in the References section of each chapter. This book describes general industry practice and publicly documented standards, incidents and research. It does not describe the systems, configuration or practices of any specific organisation. Product and company names mentioned for illustration belong to their respective owners, and their mention does not imply endorsement.</p>
  <p>Standards, browser policies and regulatory timelines change frequently. Facts and product descriptions are current to October 2026 and are based on public documentation; always confirm dates and requirements against the primary source before relying on them.</p>
  <p>Typeset in Source Serif 4, Fira Sans Condensed and Ubuntu Mono. Cover set in Instrument Serif, Jura and DM Mono.</p>
  <p>{EDITION}</p>
</div>

<section class="front toc-page">
  <h1 class="fm-h">Table of Contents</h1>
  {''.join(toc)}
</section>

<section class="front prose" id="preface"><span class="marker">@@PREFACE@@</span>
  <h1 class="fm-h">Preface</h1>
  {preface_html}
</section>

{''.join(parts_html)}

<div class="backcover">
  <div class="bc-title">{TITLE}</div>
  <div class="bc-cols">
    <div class="bc-main">
      <p>Cryptography protects every login, payment, API call, backup and software update in a modern enterprise, yet most engineers meet it in fragments: a TLS setting here, a certificate renewal there, an audit question about key custody that nobody can quite answer. This book connects the fragments into one picture.</p>
      <p>It builds from first principles to the systems that run real organisations: PKI and certificate lifecycle automation across edge, network, platform and cloud; data in transit, at rest and in use; HSMs, cloud KMS and secrets; payments cryptography; governance and compliance; and the migration to post-quantum cryptography now under way. A fictional financial group, Meridian, shows where every concept lives and who owns it.</p>
      <ul>
        <li>Design enterprise PKI and automate certificates at scale</li>
        <li>Protect data in transit, at rest and in use</li>
        <li>Choose and operate HSMs, cloud KMS and key managers</li>
        <li>Understand payments cryptography from PIN to token</li>
        <li>Map cryptographic controls to PCI DSS, NIST, ISO, DORA and more</li>
        <li>Plan and lead a post-quantum migration</li>
      </ul>
    </div>
    <div class="bc-side">
      <div class="bc-box"><b>{AUTHOR}</b> is a security practitioner focused on applied cryptography, public key infrastructure, certificate automation and key management.</div>
    </div>
  </div>
  <div class="bc-foot"><span>SECURITY / CRYPTOGRAPHY</span></div>
</div>
</body></html>"""

os.makedirs(OUT, exist_ok=True)
open(f"{OUT}/book.html", "w").write(doc)
print(f"chapters={len(chapters)} appendices={len(appendices)}")
for m in MISSING: print("MISSING ANCHOR", m)
