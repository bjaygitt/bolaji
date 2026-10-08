# Writing Guide: Cryptographic Trust at Scale (2nd edition)

Read this whole file before writing. Also read `book/OUTLINE-2e.md` for the chapter you are writing and its neighbours.

## The book

- **Title:** *Cryptographic Trust at Scale: Applied Cryptography for the Enterprise, from First Principles to the Post-Quantum Era*
- **Author:** Bolaji Johnson A.
- **Reader:** an engineer becoming an architect. They are comfortable with IT and security basics. They want to design, run and defend enterprise cryptography programmes, and to explain them to auditors and executives.
- **Promise:** by the end, the reader fully understands cryptography, PKI and key management, and sees how every piece fits into a real enterprise.

## Voice

- **Teach.** Explain from first principles, then connect each idea to the bigger enterprise picture.
  - Never assume the reader already has the context.
  - Define every term the first time it appears in the chapter, in **bold**.
  - Prefer concrete examples, numbers and analogies over abstractions.
- **Plain, confident sentences.** British spelling, as in the first edition: organisation, behaviour, favour.
  - Second person ("you") is fine.
  - No hype and no filler.
- **Hard rules:**
  - Never use em dashes (the character `—`). Use a comma, colon, parentheses or a new sentence instead.
  - Never use en dashes as punctuation. A hyphen in a range like "7-30 days" is fine.
- **Avoid AI-writing tics:**
  - "delve", "crucial", "landscape" as filler, "in today's world"
  - rule-of-three padding
  - "it's not X, it's Y" constructions
  - empty summaries

## Vendor and confidentiality rules (important)

- Name real products freely, but always **side by side**: whenever you describe how products do something, show at least two or three alternatives.
- Base product statements on **public documentation only**. Date them where they may change ("as of 2026").
- Prefer stable facts (architecture, protocols, integration methods) over version-specific UI details.
- **Never** present one combined vendor stack as "the" enterprise setup. **Never** describe any real company's internal environment.
- The running example company (below) uses **product categories, not vendor names** ("Meridian's CLM platform", "its cloud KMS"), so its architecture cannot be mistaken for any real employer's.
- Do not invent statistics, survey numbers, CVE numbers, RFC numbers, dates or quotations.
  - If you are not sure of a fact, use WebSearch or WebFetch to verify it if available, or leave the specific out.
  - Real incidents are welcome as failure stories when they are well documented, and must be cited.

## The running example: Meridian Financial Group (fictional)

Keep these facts consistent in every chapter:

- **Business:** a mid-sized financial group of about 18,000 employees, with headquarters in a fictional city. Three businesses:
  - retail and commercial banking
  - an insurance arm
  - **Meridian Pay**, a card-issuing and merchant-acquiring payments processor
- **Footprint:**
  - two owned data centres (DC-East and DC-West) linked by dark fibre
  - about 240 branches and offices on an SD-WAN
  - three public clouds (it uses all three hyperscalers for different workloads)
  - a CDN and WAF at the internet edge
  - a mobile banking app and a customer website
  - partner APIs (open banking)
  - a mainframe for core banking
  - Kubernetes platforms on-premises and in the cloud
- **Teams:**
  - Network Engineering
  - Platform Engineering
  - Identity and Access Management (IAM)
  - the **PKI and Cryptography Services** team (the reader's imagined home team)
  - Application teams
  - Payments Security
  - Governance, Risk and Compliance (GRC)
  - the Security Operations Centre (SOC)
- **Scale:** about 65,000 certificates (roughly 4,000 public, the rest private), a few thousand secrets in vaults, several HSM clusters (general-purpose and payment), and about 9,000 servers.
- **Regulation:** regulated as a bank and payments firm. Subject to PCI DSS, SOX, GLBA and regional privacy law. Operates in the EU too, so GDPR, NIS2 and DORA apply.

Use Meridian in an **"At Meridian"** callout at least once or twice per chapter, to show where the concept lives, who owns it and how it connects to other parts.

## File format (Markdown parsed by python-markdown with tables, fenced_code, sane_lists)

Each chapter is one file: `book/src2/chNN.md` (two-digit NN = new chapter number).

```
---
num: 17
title: Certificate Lifecycle Management: Foundations, Platforms and Protocols
part: 4
lead: Two to four sentences that tell the reader what the chapter is about and why it matters.
objectives: First objective | Second objective | Third objective | Fourth objective
---

## 17.1 First section title

Body text...
```

- **Headings:**
  - Sections are `## N.M Title`, numbered in order with no gaps.
  - Subsections are `### Title`, with no numbers.
  - Do not use `#` or `####`.
- **Callouts** are blockquotes whose first paragraph starts with one of these bold labels (exactly as written, including the full stop):
  - `> **In practice.** ...`
  - `> **Current development.** ...` (recent changes, with dates)
  - `> **Watch out.** ...`
  - `> **At Meridian.** ...`
  - `> **Compliance hook.** ...` (which controls in PCI DSS, NIST, ISO 27001 and others this satisfies)
- **Lists and nesting:**
  - Nested list items need **4 spaces** of indent.
  - Inside table cells, never use a literal `|`. Avoid shell redirection like `</dev/null` in tables.
- **Code blocks:** fenced with three backticks and a language name (bash, yaml, text, json, python, powershell, hcl). Keep lines under 78 characters.
- **Figures:** optional, and at most 2 per chapter. Use an inline `<figure class="fig">` containing a simple, clean `<svg viewBox=...>` with plain lines, boxes and text: black/grey strokes, font-family 'Fira Sans Condensed', font sizes 9 to 11. Follow it with `<figcaption><b>Figure N.M</b> Caption.</figcaption>`. Only add a figure if it really clarifies an architecture or flow, and make sure no text overlaps in it.
- **Required closing sections, in this order, numbered as the last sections:**
  - `## N.x Lab: <title>`: a hands-on exercise using free, local tools (OpenSSL, step-ca, EJBCA Community, Vault dev mode, SoftHSM, Docker, kind or k3d, Wireshark, strongSwan, NGINX, HAProxy). Give numbered steps with real commands, then an optional cloud extension with a cost warning.
  - `## N.x Failure story: <title>`: a real, documented incident (cited) explaining what failed and the lesson. If no suitable real incident exists, write a clearly labelled composite ("A composite scenario, based on common patterns:").
  - `## N.x Chapter summary`: 6 to 10 bullets.
  - `## N.x Review questions`: 6 to 10 numbered questions, mixing recall and design judgement.
- **Standard teaching pattern** (adapt freely):
  - why it matters
  - how it works
  - where it lives in the enterprise
  - how the major products do it
  - design decisions
  - operations and failure
  - compliance hooks

## Citations

- For every chapter, also write `book/src2/cites/chNN.json`: a JSON list of objects `{"cite": "...", "anchors": ["exact phrase from the chapter"]}`.
- Each anchor must be an exact substring of the chapter Markdown, copied from your own text. The build adds a superscript number after the first match.
- Cite standards (RFCs, NIST, FIPS, PCI, CA/B Forum ballots), incident reports, research papers and vendor documentation (for product facts).
- Aim for 6 to 20 citations per chapter.
- Formats:
  - RFC: `IETF. *RFC 8555, Automatic Certificate Management Environment (ACME).* 2019. https://www.rfc-editor.org/rfc/rfc8555`
  - Vendor docs: `F5. *BIG-IP SSL Administration* (product documentation). Accessed 2026. https://...` Only give a URL if you are confident it is real; otherwise give the title and publisher without a URL.
- When reusing material from the first edition, carry over the matching citations from `book/citations.py` (entries are keyed by old chapter number).

## Reusing the first edition

The first edition's chapters are in `book/src/chNN.md` (old numbering). When the outline says a chapter comes from an old chapter:

- Keep its best explanations, examples, labs and failure stories.
- Restructure them into the new chapter.
- Deepen them with enterprise context, product comparisons and Meridian.
- Renumber all sections, and update cross-references to the new chapter numbers in the outline.

## Length

Hit the target word count you are given (the body text, excluding code). Depth beats breadth. Explain how and why, not just what.

## Cross-references

Refer to other chapters as "Chapter N", using the NEW numbering in `OUTLINE-2e.md`. Only refer to sections that exist in your own chapter.
