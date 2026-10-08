Cryptography holds the modern enterprise together, mostly out of sight. It protects every login, card payment, software update, database backup and API call between partners. Yet most engineers learn it in fragments: a TLS setting here, a certificate renewal there, an auditor's question about key custody that nobody in the room can quite answer. The fragments rarely connect, and the gaps between them are where outages and breaches happen.

*Cryptographic Trust at Scale* connects the fragments. The first edition explained the algorithms, protocols and infrastructure from first principles. This second edition keeps that foundation and adds what it lacked: where each piece lives inside a real organisation, who owns it, how the major products implement it, and how to defend your design in front of an auditor or an executive committee.

## Who this book is for

This book is written for an engineer who is becoming an architect. Today you may run firewalls, Kubernetes platforms, certificates or HSMs. Tomorrow you will be asked to design the programme rather than one corner of it: choose a certificate platform, set an algorithm policy, plan a post-quantum migration, or explain to a board why a key ceremony matters.

You do not need a mathematics degree. If you can read a little code and use a command line, you can complete every lab.

## How the book fits together

The book has 47 chapters in 12 parts, ordered so that each idea rests on the ones before it.

- **Part I, Foundations,** explains what cryptography is for, maps where it hides inside a typical enterprise, and covers the mathematics and randomness everything else depends on.
- **Part II, The Building Blocks,** covers block ciphers, modes and authenticated encryption, hashing and key derivation, RSA, elliptic curves, signatures, and how protocols fail.
- **Part III, Trust and Identity,** explains certificates, the Web PKI, revocation, enterprise PKI design and the identity protocols built on keys.
- **Part IV, Certificate Lifecycle Automation,** is a standalone guide to discovering, issuing, deploying and renewing certificates across a whole estate.
- **Part V, Data in Transit,** follows encryption across the network: TLS, IPsec and MACsec, the internet edge, service meshes, SSH and email.
- **Part VI, Data at Rest,** covers storage and database encryption, cloud key management and crypto-shredding.
- **Part VII, Data in Use,** covers confidential computing and privacy-enhancing technologies.
- **Part VIII, Key Management and Hardware,** covers key management fundamentals, HSMs, enterprise key managers, secrets and code signing.
- **Part IX, Payments Cryptography,** explains card payments, payment HSMs and payment security programmes.
- **Part X, Governance, Risk and Compliance,** covers standards and validation, regulation, governance and running a cryptography programme.
- **Part XI, The Post-Quantum Transition,** explains the quantum threat, the new algorithms and how an enterprise migrates.
- **Part XII, Bringing It Together,** traces one card payment end to end, and holds the appendices: a glossary, a reading guide, a command reference, a compliance crosswalk and a vendor capability matrix.

## The running example: Meridian Financial Group

Concepts stick when you can see where they live. Throughout the book you will follow **Meridian Financial Group**, a fictional bank, insurer and payments processor with about 18,000 employees. Meridian runs two data centres, about 240 branches, workloads in three public clouds, a CDN, a mobile app, open banking APIs and a mainframe. Its payments arm, Meridian Pay, issues cards and acquires merchants. It holds about 65,000 certificates and several HSM clusters, and it answers to PCI DSS, SOX, GLBA, GDPR, NIS2 and DORA.

Each part adds a layer to Meridian's architecture, and the final chapter traces one customer payment through all of it. Meridian is described in product categories ("its CLM platform", "its cloud KMS"), never vendor names, so that its design cannot be mistaken for any real organisation's.

## Part IV stands alone

Certificate lifecycle automation has become an urgent discipline. Public TLS certificate lifetimes are shrinking in steps towards 47 days, and an organisation that still renews by spreadsheet will not keep up. Part IV (Chapters 17 to 19) is written so that a certificate automation engineer can read it without the rest of the book. It covers the lifecycle and its protocols, integration with CDNs, load balancers, firewalls, Kubernetes, Windows and the clouds, and rollout, troubleshooting and runbooks.

## Conventions

Every chapter opens with a short lead and a list of objectives, and every term is defined in **bold** where it first appears. Five kinds of callout appear in the text.

| Callout | What it contains |
| --- | --- |
| **In practice** | How the idea shows up in real systems, and what to check in your own environment |
| **Current development** | Recent changes to standards, browser policies or regulations, with dates |
| **Watch out** | Common mistakes that cause outages or breaches |
| **At Meridian** | Where the concept lives in the running example, who owns it and what it connects to |
| **Compliance hook** | Which controls in PCI DSS, NIST, ISO 27001 and other frameworks the topic helps satisfy |

Each chapter closes the same way. A **lab** gives numbered steps using free tools on a laptop (OpenSSL, step-ca, EJBCA Community, Vault in dev mode, SoftHSM, Docker, kind, Wireshark, strongSwan), with an optional cloud extension and a cost warning. A **failure story** examines a real, publicly documented incident and draws the lesson from it; where no suitable incident exists, a clearly labelled composite is used instead. A summary, review questions and references follow. Do the labs: cryptography becomes intuitive only when you have broken a toy system yourself.

## How vendors are treated

Enterprise cryptography is delivered through products, so this book names them. It follows three rules. First, products appear side by side: when the text explains how a CLM platform, HSM or CDN does something, it shows two or three alternatives, including open-source options. Second, every product statement comes from public documentation, and statements that may change are dated "as of 2026". Third, no combination of products is presented as the right enterprise stack. Nothing in this book describes any real employer's environment, and no product mention is an endorsement. Appendix E gathers the comparisons into one matrix, with the same caveats.

## How to read this book

You can read from cover to cover, and the order is designed for that. Many readers will want a shorter path first.

| If you are | Start with | Then read |
| --- | --- | --- |
| A certificate or PKI engineer | Part IV, then Chapters 12 to 15 | Chapters 21, 33 and 46 |
| A network engineer | Chapters 2, 20 and 21 | Chapters 22 and 23, then Part IV |
| A platform or cloud engineer | Chapters 2, 24 and 28 | Chapters 35 and 18, then Part VI |
| A payments security specialist | Part IX | Chapters 32, 33 and 38, then Chapter 47 |
| A GRC or audit professional | Chapters 1, 2 and 41 | Chapters 42 and 43, then Appendix D |
| An aspiring security architect | Parts I and II | Everything else in order |

If a chapter uses an idea you have skipped, the text names the chapter that explains it, and Appendix A defines every key term with a chapter reference.

## A note on currency

Cryptographic practice is changing faster now than at any time in the last twenty years: certificate lifetimes are falling, post-quantum key exchange is already common, and regulators have published dates for retiring RSA and elliptic-curve cryptography. Where this book cites a date, policy or product capability, it reflects the public record as of 2026. Always check the primary source before relying on a date for a decision.

## Sources and originality

The text is original writing. Where a chapter relies on a specific fact, date, incident, standard or research result, a superscript number points to the References list at the end of that chapter. All diagrams were drawn for this book.

## Acknowledgements

This book stands on the work of the researchers, standards bodies, open-source maintainers and incident responders whose publications are cited throughout, and on the many practitioners who share what they learn from failure. Any errors are mine.

Bolaji Johnson A.
