---
num: B
title: Standards, Further Reading and Practice
part: 8
lead: The primary sources behind this book, grouped by topic, plus the best books, courses and practice resources for going deeper. Standards change; check each body's website for the current version.
---

## B.1 Core standards by topic

| Topic | Key documents |
| --- | --- |
| Algorithms (symmetric) | FIPS 197 (AES); SP 800-38A to 38G (modes, including GCM in 38D); RFC 8439 (ChaCha20-Poly1305); RFC 8452 (AES-GCM-SIV) |
| Hashes, MACs, KDFs | FIPS 180-4 (SHA-2); FIPS 202 (SHA-3); FIPS 198-1 and RFC 2104 (HMAC); RFC 5869 (HKDF); RFC 9106 (Argon2); SP 800-132 (PBKDF2) |
| Public-key algorithms | FIPS 186-5 (signatures, including EdDSA); RFC 8017 (PKCS#1, RSA); RFC 7748 (X25519); RFC 8032 (Ed25519); RFC 6979 (deterministic ECDSA); SP 800-186 (elliptic curves); RFC 9180 (HPKE) |
| Random numbers | SP 800-90A, 90B, 90C |
| Key management | SP 800-57 Parts 1 to 3; SP 800-130 and 800-152 (key management systems); SP 800-131A (algorithm transitions) |
| TLS and protocols | RFC 8446 (TLS 1.3); RFC 8996 (deprecating TLS 1.0 and 1.1); RFC 9849 (Encrypted Client Hello); RFC 7296 (IKEv2); RFC 9420 (MLS) |
| Certificates and PKI | RFC 5280 (X.509 profile); RFC 6960 (OCSP); RFC 6962 (Certificate Transparency); RFC 8659 (CAA); RFC 3647 (CP/CPS framework); CA/Browser Forum Baseline Requirements |
| Automation | RFC 8555 (ACME); RFC 9773 (ACME Renewal Information); RFC 7030 (EST) |
| Identity | RFC 6749 (OAuth 2.0); RFC 7636 (PKCE); RFC 7519 (JWT); RFC 8725 (JWT best practices); RFC 9449 (DPoP); OpenID Connect Core; W3C WebAuthn |
| Hardware | FIPS 140-3 and ISO/IEC 19790; OASIS PKCS#11 v3; OASIS KMIP; TCG TPM 2.0 |
| Post-quantum | FIPS 203 (ML-KEM); FIPS 204 (ML-DSA); FIPS 205 (SLH-DSA); draft FIPS 206 (FN-DSA); SP 800-208 (LMS, XMSS); SP 800-227 (KEM guidance); NIST IR 8547 (transition, draft); NSA CNSA 2.0 |
| Inventories | CycloneDX 1.6 and later (CBOM) |

## B.2 Books

- **Serious Cryptography**, Jean-Philippe Aumasson (2nd edition, 2024). A practical, readable tour of modern cryptography and its pitfalls.
- **Real-World Cryptography**, David Wong (2021). Protocols and applied systems with clear diagrams.
- **A Graduate Course in Applied Cryptography**, Dan Boneh and Victor Shoup. Free online; the rigorous reference for definitions and proofs.
- **Introduction to Modern Cryptography**, Jonathan Katz and Yehuda Lindell. The standard university text on security definitions.
- **Cryptography Engineering**, Niels Ferguson, Bruce Schneier and Tadayoshi Kohno. How to build systems, and why they fail.
- **Bulletproof TLS and PKI**, Ivan Ristić (2nd edition). The practitioner's reference for deploying TLS and certificates.
- **Crypto 101**, Laurens Van Houtven. Free; a gentle introduction.

## B.3 Courses and practice

- **Cryptopals** challenges: eight sets of hands-on attacks, from repeated-key XOR to padding oracles and ECDSA nonce reuse.
- **CryptoHack**: browser-based challenges with a strong mathematics track.
- **Dan Boneh's Cryptography I** (online course): the classic introduction to the theory.
- **Real World Crypto** conference talks (free recordings): where industry and research meet each year.
- **Open Quantum Safe** project: libraries and demos for experimenting with post-quantum algorithms.

## B.4 Staying current

| Source | What it tells you |
| --- | --- |
| IACR ePrint archive | New research and attacks, often months before publication |
| NIST CSRC (Computer Security Resource Center) | Draft and final standards, comment periods, post-quantum updates |
| CA/Browser Forum ballots and minutes | Changes to public certificate rules |
| Root program announcements (Chrome, Mozilla, Apple, Microsoft) | Distrusts, new requirements, policy timelines |
| IETF working groups (TLS, LAMPS, ACME, CFRG, PQUIP) | Protocol and format standards in progress |
| National agencies (NCSC, BSI, ANSSI, CISA, NSA) | Guidance and migration deadlines |
| Let's Encrypt blog and community | Practical changes to the public PKI |
