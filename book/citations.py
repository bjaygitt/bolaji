"""Per-chapter references. Each entry: (citation text, [exact anchor phrases in the chapter text]).
The build inserts a numbered marker after the first occurrence of each anchor and appends a
References section to the chapter."""

NIST_57 = "NIST. *SP 800-57 Part 1 Rev. 5, Recommendation for Key Management: Part 1, General.* May 2020. https://doi.org/10.6028/NIST.SP.800-57pt1r5"
NIST_8547 = "NIST. *IR 8547 (Initial Public Draft), Transition to Post-Quantum Cryptography Standards.* November 2024. https://doi.org/10.6028/NIST.IR.8547.ipd"
CNSA2 = "National Security Agency. *Announcing the Commercial National Security Algorithm Suite 2.0* (with FAQ updates). September 2022. https://media.defense.gov/"
SC081 = "CA/Browser Forum. *Ballot SC-081v3: Introduce Schedule of Reducing Validity and Data Reuse Periods.* April 2025. https://cabforum.org/"
BR = "CA/Browser Forum. *Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates.* Current version. https://cabforum.org/working-groups/server/baseline-requirements/"
FIPS203 = "NIST. *FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard.* August 2024. https://doi.org/10.6028/NIST.FIPS.203"
FIPS204 = "NIST. *FIPS 204, Module-Lattice-Based Digital Signature Standard.* August 2024. https://doi.org/10.6028/NIST.FIPS.204"
FIPS205 = "NIST. *FIPS 205, Stateless Hash-Based Digital Signature Standard.* August 2024. https://doi.org/10.6028/NIST.FIPS.205"
RFC = lambda n, t, y: f"IETF. *RFC {n}, {t}.* {y}. https://www.rfc-editor.org/rfc/rfc{n}"
SHATTERED = "Stevens, M., Bursztein, E., Karpman, P., Albertini, A., Markov, Y. \"The First Collision for Full SHA-1.\" CRYPTO 2017. https://shattered.io/"
SWEET32 = "Bhargavan, K., Leurent, G. \"On the Practical (In-)Security of 64-bit Block Ciphers: Collision Attacks on HTTP over TLS and OpenVPN.\" ACM CCS 2016. https://sweet32.info/"
STORM_MS = "Microsoft Security Response Center. \"Results of Major Technical Investigations for Storm-0558 Key Acquisition.\" September 2023. https://msrc.microsoft.com/blog/"
CSRB = "Cyber Safety Review Board. *Review of the Summer 2023 Microsoft Exchange Online Intrusion.* US Department of Homeland Security, March 2024. https://www.cisa.gov/resources-tools/resources/CSRB-report-microsoft-exchange-online-intrusion"
EQUIFAX = "US House of Representatives Committee on Oversight and Government Reform. *The Equifax Data Breach* (Majority Staff Report). December 2018."
GIDNEY25 = "Gidney, C. \"How to Factor 2048 Bit RSA Integers with Less than a Million Noisy Qubits.\" arXiv:2505.15917, May 2025."
GIDNEY19 = "Gidney, C., Ekerå, M. \"How to Factor 2048 Bit RSA Integers in 8 Hours Using 20 Million Noisy Qubits.\" *Quantum* 5, 433 (2021); arXiv:1905.09749."
CHROME_PQ = "Google Chrome team. Post-quantum key exchange (X25519MLKEM768) enabled by default in Chrome 131. Chromium Blog and Google Security Blog, 2024. https://security.googleblog.com/"
LOGJAM = "Adrian, D., Bhargavan, K., Durumeric, Z., et al. \"Imperfect Forward Secrecy: How Diffie-Hellman Fails in Practice.\" ACM CCS 2015. https://weakdh.org/"
ROCA = "Nemec, M., Sys, M., Svenda, P., Klinec, D., Matyas, V. \"The Return of Coppersmith's Attack: Practical Factorization of Widely Used RSA Moduli.\" ACM CCS 2017. https://crocs.fi.muni.cz/public/papers/rsa_ccs17"
LUCKY13 = "AlFardan, N. J., Paterson, K. G. \"Lucky Thirteen: Breaking the TLS and DTLS Record Protocols.\" IEEE Symposium on Security and Privacy 2013."
DANGEROUS = "Georgiev, M., Iyengar, S., Jana, S., Anubhai, R., Boneh, D., Shmatikov, V. \"The Most Dangerous Code in the World: Validating SSL Certificates in Non-Browser Software.\" ACM CCS 2012."
FOX_IT = "Fox-IT. *Black Tulip: Report of the Investigation into the DigiNotar Certificate Authority Breach.* Commissioned by the Dutch Ministry of the Interior, August 2012."
PS3 = "fail0verflow (bushing, marcan, sven). \"Console Hacking 2010: PS3 Epic Fail.\" 27th Chaos Communication Congress (27C3), December 2010."
ROGUE_CA = "Sotirov, A., Stevens, M., Appelbaum, J., Lenstra, A., Molnar, D., Osvik, D. A., de Weger, B. \"MD5 Considered Harmful Today: Creating a Rogue CA Certificate.\" 25th Chaos Communication Congress, December 2008. https://www.win.tue.nl/hashclash/rogue-ca/"
LE_OCSP = "Let's Encrypt. \"Ending OCSP Support in 2025.\" December 2024 (OCSP service ended August 2025). https://letsencrypt.org/2024/12/05/ending-ocsp/"
FIPS1403 = "NIST. *FIPS 140-3, Security Requirements for Cryptographic Modules.* March 2019; and NIST CMVP, FIPS 140-2 sunset and Historical list notices. https://csrc.nist.gov/projects/cryptographic-module-validation-program"
CF_PQ = "Cloudflare. Post-quantum encryption adoption statistics, Cloudflare Radar and Cloudflare Blog, 2025 to 2026. https://radar.cloudflare.com/adoption-and-usage"
NCSC = "UK National Cyber Security Centre. \"Timelines for Migration to Post-Quantum Cryptography.\" March 2025. https://www.ncsc.gov.uk/"
EU_PQ = "European Commission and NIS Cooperation Group. *A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography.* June 2025."

C = {
"01": [
 ("Kerckhoffs, A. \"La cryptographie militaire.\" *Journal des sciences militaires*, vol. IX, 1883. The principle is paraphrased here.", ["by the Dutch cryptographer Auguste Kerckhoffs in 1883"]),
 (NIST_57, ["The values follow NIST guidance (SP 800-57)"]),
 (NIST_8547, ["NIST's draft transition plan (IR 8547, published for comment in November 2024)"]),
 ("Debian Security Advisory DSA-1571-1, \"openssl: predictable random number generator\" (CVE-2008-0166). May 2008. https://www.debian.org/security/2008/dsa-1571", ["When the flaw was found in May 2008"]),
],
"02": [
 ("Shor, P. W. \"Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer.\" *SIAM Journal on Computing* 26(5), 1997 (conference version 1994).", ["**Shor's algorithm**"]),
 ("Rabin, M. O. \"Probabilistic Algorithm for Testing Primality.\" *Journal of Number Theory* 12(1), 1980; Miller, G. L. \"Riemann's Hypothesis and Tests for Primality.\" 1976.", ["such as Miller-Rabin"]),
 (RFC(7748, "Elliptic Curves for Security", 2016), ["| Curve25519 / X25519 |"]),
 ("NIST. *SP 800-186, Recommendations for Discrete Logarithm-Based Cryptography: Elliptic Curve Domain Parameters.* February 2023.", ["| P-256 (secp256r1) |"]),
 ("Regev, O. \"On Lattices, Learning with Errors, Random Linear Codes, and Cryptography.\" STOC 2005.", ["**Learning With Errors (LWE)**"]),
],
"03": [
 ("Linux kernel documentation and man page for getrandom(2); Mueller, S. and others on the Linux random number generator design.", ["The `getrandom()` call handles the one genuinely risky moment"]),
 ("NIST. *SP 800-38D, Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC.* November 2007, section 8.3.", ["NIST limits random-nonce use to 2^32 messages per key"]),
 (SWEET32, ["old 64-bit block ciphers fell to attacks like Sweet32"]),
 (SHATTERED, ["SHA-1 collisions were found with about 2^63"]),
 ("Python Software Foundation. Documentation of the `random` module (warning that it must not be used for security) and of the `secrets` module.", ["Python's `random` module uses the Mersenne Twister"]),
 (PS3, ["a group of researchers presented a complete break of the code-signing system protecting the PlayStation 3"]),
 (RFC(6979, "Deterministic Usage of the Digital Signature Algorithm (DSA) and Elliptic Curve Digital Signature Algorithm (ECDSA)", 2013), ["(RFC 6979, and the design of EdDSA)"]),
],
"04": [
 ("Electronic Frontier Foundation. *Cracking DES: Secrets of Encryption Research, Wiretap Politics and Chip Design.* O'Reilly, 1998.", ["a purpose-built machine costing about 250,000 US dollars found a DES key in days"]),
 (SWEET32, ["the **Sweet32** attack recovered secret cookies"]),
 ("NIST. *SP 800-131A Rev. 2, Transitioning the Use of Cryptographic Algorithms and Key Lengths.* March 2019.", ["NIST has since disallowed 3DES for encryption after 2023"]),
 ("NIST. *FIPS 197, Advanced Encryption Standard (AES).* November 2001 (updated 2023); Daemen, J., Rijmen, V. *The Design of Rijndael.* Springer, 2002.", ["published in 2001 as the **Advanced Encryption Standard (AES)**, FIPS 197"]),
 ("Shannon, C. E. \"Communication Theory of Secrecy Systems.\" *Bell System Technical Journal* 28(4), 1949.", ["a term introduced by Claude Shannon in 1949"]),
 ("Biryukov, A., Khovratovich, D. \"Related-Key Cryptanalysis of the Full AES-192 and AES-256.\" ASIACRYPT 2009.", ["related-key attacks exploit it for AES-256"]),
 (CNSA2, ["The US NSA's CNSA 2.0 suite, for example, requires AES-256"]),
 ("Bernstein, D. J. \"Cache-Timing Attacks on AES.\" 2005; Osvik, D. A., Shamir, A., Tromer, E. \"Cache Attacks and Countermeasures: the Case of AES.\" CT-RSA 2006.", ["In 2005, researchers recovered full AES keys from a server over the network"]),
 ("Krebs, B. Reporting on the 2013 password database breach at a large software company and the analysis of its 3DES-ECB encrypted passwords. *Krebs on Security*, October and November 2013.", ["a breach at a large software company exposed about 150 million user records"]),
],
"05": [
 ("Vaudenay, S. \"Security Flaws Induced by CBC Padding: Applications to SSL, IPSEC, WTLS...\" EUROCRYPT 2002.", ["In 2002, Serge Vaudenay showed"]),
 ("Duong, T., Rizzo, J. \"Here Come the XOR Ninjas\" (BEAST). Ekoparty 2011.", ["enabled the BEAST attack on TLS 1.0 in 2011"]),
 (LUCKY13, ["the Lucky Thirteen attack in 2013"]),
 ("Möller, B., Duong, T., Kotowicz, K. \"This POODLE Bites: Exploiting the SSL 3.0 Fallback.\" Google Security Advisory, 2014.", ["POODLE in 2014 broke SSL 3.0"]),
 ("Bellare, M., Namprempre, C. \"Authenticated Encryption: Relations among Notions and Analysis of the Generic Composition Paradigm.\" ASIACRYPT 2000.", ["**Encrypt-then-MAC** is safe"]),
 ("NIST. *SP 800-38D* (GCM). 2007.", ["**Galois/Counter Mode (GCM)**"]),
 ("Böck, H., Zauner, A., Devlin, S., Somorovsky, J., Jovanovic, P. \"Nonce-Disrespecting Adversaries: Practical Forgery Attacks on GCM in TLS.\" USENIX WOOT 2016.", ["A 2016 internet-wide study found 184 HTTPS servers repeating GCM nonces"]),
 (RFC(8439, "ChaCha20 and Poly1305 for IETF Protocols", 2018), ["standardised in RFC 8439"]),
 (RFC(8452, "AES-GCM-SIV: Nonce Misuse-Resistant Authenticated Encryption", 2019), ["**AES-GCM-SIV** (RFC 8452)"]),
 ("Tervoort, T. \"Zerologon: Unauthenticated Domain Controller Compromise by Subverting Netlogon Cryptography (CVE-2020-1472).\" Secura whitepaper, September 2020.", ["Researchers named it **Zerologon**"]),
],
"06": [
 ("Wang, X., Yu, H. \"How to Break MD5 and Other Hash Functions.\" EUROCRYPT 2005.", ["**2004:** researchers found practical MD5 collisions"]),
 (ROGUE_CA, ["**2008:** a team used MD5 collisions to create a rogue certificate authority certificate", "In December 2008, at the Chaos Communication Congress"]),
 ("Microsoft. Security Advisory 2718704, \"Unauthorized Digital Certificates Could Allow Spoofing.\" June 2012 (Flame).", ["**2012:** the Flame malware used an MD5 collision"]),
 (SHATTERED, ["announced **SHAttered**"]),
 ("Leurent, G., Peyrin, T. \"SHA-1 is a Shambles: First Chosen-Prefix Collision on SHA-1 and Application to the PGP Web of Trust.\" USENIX Security 2020.", ["the **Shambles** attack"]),
 ("NIST. \"NIST Retires SHA-1 Cryptographic Algorithm.\" News release, December 2022.", ["NIST plans to withdraw SHA-1 entirely by 2030"]),
 ("NIST. *FIPS 180-4, Secure Hash Standard*, 2015; *FIPS 202, SHA-3 Standard*, 2015.", ["standardised in 2015 (FIPS 202)"]),
 (RFC(2104, "HMAC: Keyed-Hashing for Message Authentication", 1997), ["**HMAC** (RFC 2104, FIPS 198-1)"]),
 (RFC(5869, "HMAC-based Extract-and-Expand Key Derivation Function (HKDF)", 2010), ["The standard is **HKDF** (RFC 5869)"]),
 (RFC(9106, "Argon2 Memory-Hard Function for Password Hashing and Proof-of-Work Applications", 2021), ["Winner of the 2015 Password Hashing Competition; RFC 9106"]),
 ("OWASP Foundation. *Password Storage Cheat Sheet.* Current version. https://cheatsheetseries.owasp.org/", ["(OWASP suggests 600,000)"]),
 (BR + " Section 7.1 (serial number entropy).", ["at least 64 bits of randomness in its serial number"]),
],
"07": [
 ("Rivest, R. L., Shamir, A., Adleman, L. \"A Method for Obtaining Digital Signatures and Public-Key Cryptosystems.\" *Communications of the ACM* 21(2), 1978.", ["In 1977, Ron Rivest, Adi Shamir and Leonard Adleman published"]),
 ("Bleichenbacher, D. \"Chosen Ciphertext Attacks Against Protocols Based on the RSA Encryption Standard PKCS #1.\" CRYPTO 1998.", ["discovered by Daniel Bleichenbacher in 1998"]),
 ("Böck, H., Somorovsky, J., Young, C. \"Return Of Bleichenbacher's Oracle Threat (ROBOT).\" USENIX Security 2018. https://robotattack.org/", ["in 2017 as **ROBOT**"]),
 ("Kario, H. \"Everlasting ROBOT: the Marvin Attack.\" ESORICS 2023. https://people.redhat.com/~hkario/marvin/", ["in 2023 as the **Marvin** attack"]),
 (RFC(8017, "PKCS #1: RSA Cryptography Specifications Version 2.2", 2016), ["standardised in PKCS#1 v2"]),
 ("Finney, H. \"Bleichenbacher's RSA signature forgery based on implementation error.\" Report of D. Bleichenbacher's CRYPTO 2006 rump session talk, 2006.", ["in 2006, Bleichenbacher showed"]),
 ("Boudot, F., Gaudry, P., Guillevic, A., Heninger, N., Thomé, E., Zimmermann, P. \"Factorization of RSA-250.\" Announcement, February 2020.", ["(RSA-250, in 2020)"]),
 (GIDNEY25, ["a 2025 analysis by Google researchers estimated"]),
 (NIST_8547, ["NIST's draft transition plan proposes that 2048-bit RSA be deprecated after 2030"]),
 ("Heninger, N., Durumeric, Z., Wustrow, E., Halderman, J. A. \"Mining Your Ps and Qs: Detection of Widespread Weak Keys in Network Devices.\" USENIX Security 2012; Lenstra, A. K., et al. \"Ron was wrong, Whit is right.\" 2012.", ["In 2012, two research teams scanned the internet's public keys"]),
 (ROCA, ["The **ROCA** vulnerability (2017)", "In October 2017, researchers from Masaryk University"]),
 ("Estonian Information System Authority (RIA). Public statements on the suspension and renewal of ID card certificates following ROCA, November 2017.", ["Estonia had to replace the keys on 760,000 national ID cards", "Estonia suspended the certificates of 760,000 ID cards"]),
],
"08": [
 ("Diffie, W., Hellman, M. E. \"New Directions in Cryptography.\" *IEEE Transactions on Information Theory* 22(6), 1976.", ["Whitfield Diffie and Martin Hellman published"]),
 ("Ellis, J. H. \"The History of Non-Secret Encryption.\" CESG, 1987, released by GCHQ in 1997.", ["researchers at the UK's GCHQ had discovered the same idea secretly"]),
 (RFC(7748, "Elliptic Curves for Security", 2016) + "; Bernstein, D. J. \"Curve25519: New Diffie-Hellman Speed Records.\" PKC 2006.", ["**X25519**, defined in RFC 7748"]),
 ("NIST. *SP 800-186*, 2023 (approves Curve25519 for use in key agreement under NIST guidance).", ["(now allowed under SP 800-186)"]),
 (LOGJAM, ["In 2015, the **Logjam** research", "In May 2015, a team of 14 researchers published"]),
 (RFC(7919, "Negotiated Finite Field Diffie-Hellman Ephemeral Parameters for TLS", 2016), ["(RFC 7919 for finite fields)"]),
 ("Jager, T., Schwenk, J., Somorovsky, J. \"Practical Invalid Curve Attacks on TLS-ECDH.\" ESORICS 2015.", ["In 2015, researchers demonstrated invalid-curve attacks"]),
 (RFC(9180, "Hybrid Public Key Encryption", 2022), ["(Hybrid Public Key Encryption, RFC 9180)"]),
 (CHROME_PQ, ["Since late 2024, Chrome, Edge and Firefox negotiate"]),
],
"09": [
 (RFC(6979, "Deterministic Usage of DSA and ECDSA", 2013), ["**RFC 6979** removes the dependence on randomness"]),
 (PS3, ["This is how the PlayStation 3 master key was recovered"]),
 ("Jancar, J., Sedlacek, V., Svenda, P., Sys, M. \"Minerva: The Curse of ECDSA Nonces.\" *IACR TCHES* 2020(4); Moghimi, D., Sunar, B., Eisenbarth, T., Heninger, N. \"TPM-FAIL: TPM meets Timing and Lattice Attacks.\" USENIX Security 2020.", ["The 2019 **Minerva** and **TPM-Fail** attacks"]),
 (RFC(8032, "Edwards-Curve Digital Signature Algorithm (EdDSA)", 2017), ["**Ed25519** (RFC 8032)"]),
 ("NIST. *FIPS 186-5, Digital Signature Standard (DSS).* February 2023.", ["was added to FIPS 186-5 in 2023"]),
 ("US Cybersecurity and Infrastructure Security Agency. Emergency Directive 21-01 and Alert AA20-352A on the 2020 software supply-chain compromise, December 2020; vendor SEC filing reporting up to about 18,000 affected customers.", ["delivered to about 18,000 customers"]),
 ("Newman, Z., Meyers, J. S., Torres-Arias, S. \"Sigstore: Software Signing for Everybody.\" ACM CCS 2022. https://www.sigstore.dev/", ["**Sigstore**, an open-source project launched in 2021"]),
 (STORM_MS, ["In July 2023, Microsoft disclosed", "Microsoft's investigation suggested it ended up in a crash dump"]),
 (CSRB, ["The US Cyber Safety Review Board's 2024 report"]),
],
"10": [
 ("Goldwasser, S., Micali, S. \"Probabilistic Encryption.\" *Journal of Computer and System Sciences* 28(2), 1984.", ["**IND-CPA secure**"]),
 ("Rackoff, C., Simon, D. R. \"Non-Interactive Zero-Knowledge Proof of Knowledge and Chosen Ciphertext Attack.\" CRYPTO 1991.", ["**IND-CCA2** (often just \"IND-CCA\")"]),
 ("Bellare, M., Namprempre, C. \"Authenticated Encryption: Relations among Notions...\" ASIACRYPT 2000.", ["A scheme that is IND-CPA and INT-CTXT secure is automatically IND-CCA secure"]),
 ("Goldwasser, S., Micali, S., Rivest, R. L. \"A Digital Signature Scheme Secure Against Adaptive Chosen-Message Attacks.\" *SIAM Journal on Computing* 17(2), 1988.", ["**EUF-CMA** (existential unforgeability under chosen-message attack)"]),
 ("Bellare, M., Rogaway, P. \"Random Oracles are Practical: A Paradigm for Designing Efficient Protocols.\" ACM CCS 1993.", ["proven secure in the **random oracle model (ROM)**"]),
 ("Canetti, R., Goldreich, O., Halevi, S. \"The Random Oracle Methodology, Revisited.\" STOC 1998.", ["in 1998 researchers constructed (artificial) schemes"]),
 ("Boneh, D., Dagdelen, Ö., Fischlin, M., Lehmann, A., Schaffner, C., Zhandry, M. \"Random Oracles in a Quantum World.\" ASIACRYPT 2011.", ["**quantum random oracle model (QROM)**"]),
 (LUCKY13, ["In 2013, Nadhem AlFardan and Kenny Paterson published **Lucky Thirteen**"]),
],
"11": [
 (RFC(8446, "The Transport Layer Security (TLS) Protocol Version 1.3", 2018), ["| TLS 1.3 | 2018 (RFC 8446) |"]),
 (RFC(8996, "Deprecating TLS 1.0 and TLS 1.1", 2021), ["Deprecated by RFC 8996 in 2021"]),
 ("Cremers, C., Horvat, M., Hoyland, J., Scott, S., van der Merwe, T. \"A Comprehensive Symbolic Analysis of TLS 1.3.\" ACM CCS 2017.", ["designed alongside machine-checked security proofs"]),
 (RFC(9849, "TLS Encrypted Client Hello", 2026), ["ECH was published as RFC 9849 in March 2026"]),
 (CHROME_PQ + " Mozilla Firefox 132 release notes, October 2024.", ["X25519MLKEM768 has been the default key exchange in Chrome and Edge since version 131"]),
 ("Apple. Platform security documentation and WWDC 2025 session on quantum-secure cryptography in iOS 26 and macOS 26.", ["Apple added it across iOS 26 and macOS in 2025"]),
 (CF_PQ, ["major CDNs reported that around two-thirds of human web traffic"]),
 ("Aviram, N., Schinzel, S., Somorovsky, J., et al. \"DROWN: Breaking TLS using SSLv2.\" USENIX Security 2016. https://drownattack.com/", ["In 2016, researchers published **DROWN**"]),
],
"12": [
 ("Mozilla. *Server Side TLS* guidelines and SSL Configuration Generator. https://wiki.mozilla.org/Security/Server_Side_TLS. The configuration in section 12.2 is adapted from the intermediate profile.", ["The Mozilla Server Side TLS guidelines are the most widely used"]),
 (RFC(6797, "HTTP Strict Transport Security (HSTS)", 2012), ["**HTTP Strict Transport Security (HSTS).**"]),
 ("Marlinspike, M. \"New Tricks for Defeating SSL in Practice\" (sslstrip). Black Hat DC 2009.", ["| 2009 | SSL stripping |"]),
 ("Rizzo, J., Duong, T. \"The CRIME Attack.\" Ekoparty 2012; Gluck, Y., Harris, N., Prado, A. \"BREACH.\" Black Hat USA 2013.", ["| 2012 | CRIME, later BREACH |"]),
 ("Durumeric, Z., Li, F., Kasten, J., et al. \"The Matter of Heartbleed.\" ACM IMC 2014; CVE-2014-0160.", ["In April 2014, a flaw named **Heartbleed**"]),
 ("Qualys SSL Labs. *SSL Server Rating Guide.* https://github.com/ssllabs/research/wiki/SSL-Server-Rating-Guide", ["Qualys SSL Labs Server Test"]),
 ("Linux Foundation. Announcement of the Core Infrastructure Initiative, April 2014; Open Source Security Foundation (2020).", ["The response led to the Core Infrastructure Initiative"]),
],
"13": [
 ("OpenSSH project. Release notes for OpenSSH 9.0 (April 2022) and OpenSSH 10.0 (April 2025). https://www.openssh.com/releasenotes.html", ["version 10.0 in April 2025 made **mlkem768x25519-sha256** the default"]),
 (RFC(7296, "Internet Key Exchange Protocol Version 2 (IKEv2)", 2014), ["**IKEv2** (Internet Key Exchange, RFC 7296)"]),
 (RFC(9370, "Multiple Key Exchanges in IKEv2", 2023), ["RFC 9370 defines how IKEv2 adds post-quantum KEMs"]),
 ("Donenfeld, J. A. \"WireGuard: Next Generation Kernel Network Tunnel.\" NDSS 2017. https://www.wireguard.com/papers/wireguard.pdf", ["**WireGuard**, created by Jason Donenfeld"]),
 ("Perrin, T. *The Noise Protocol Framework.* 2018. https://noiseprotocol.org/", ["The Noise protocol framework (Noise_IK)"]),
 ("Marlinspike, M., Perrin, T. *The X3DH Key Agreement Protocol* and *The Double Ratchet Algorithm.* Signal specifications, 2016. https://signal.org/docs/", ["This is **X3DH** (Extended Triple Diffie-Hellman)"]),
 ("Kret, E., Schmidt, R. *The PQXDH Key Agreement Protocol.* Signal specification, 2023.", ["In 2023, Signal upgraded this to **PQXDH**"]),
 ("Signal. Announcement of the Sparse Post-Quantum Ratchet (SPQR) and triple ratchet design, October 2025. https://signal.org/blog/", ["In October 2025, Signal announced a \"triple ratchet\" design"]),
 ("Apple Security Engineering and Architecture. \"iMessage with PQ3: The new state of the art in quantum-secure messaging at scale.\" February 2024.", ["Apple's iMessage moved to a comparable post-quantum design, PQ3, in 2024"]),
 (RFC(9420, "The Messaging Layer Security (MLS) Protocol", 2023), ["standardised as RFC 9420 in 2023"]),
 ("Ylönen, T., Turner, P., Scarfone, K., Souppaya, M. *NIST IR 7966, Security of Interactive and Automated Access Management Using Secure Shell (SSH).* NIST, 2015.", ["Beginning around 2013, the inventor of SSH, Tatu Ylönen"]),
],
"14": [
 (RFC(6749, "The OAuth 2.0 Authorization Framework", 2012), ["**OAuth 2.0** (RFC 6749)"]),
 (RFC(7636, "Proof Key for Code Exchange by OAuth Public Clients", 2015), ["**PKCE** (Proof Key for Code Exchange, RFC 7636)"]),
 ("IETF OAuth Working Group. *The OAuth 2.1 Authorization Framework* (Internet-Draft); RFC 9700, *Best Current Practice for OAuth 2.0 Security*, 2025.", ["OAuth 2.1 consolidation of best practices"]),
 (RFC(9449, "OAuth 2.0 Demonstrating Proof of Possession (DPoP)", 2023) + "; RFC 8705, OAuth 2.0 Mutual-TLS Client Authentication, 2020.", ["**DPoP** (RFC 9449)"]),
 ("OpenID Foundation. *OpenID Connect Core 1.0.* https://openid.net/specs/openid-connect-core-1_0.html", ["**OpenID Connect (OIDC)** adds an **ID token**"]),
 (RFC(7519, "JSON Web Token (JWT)", 2015), ["**JSON Web Tokens (JWT)**, RFC 7519"]),
 (RFC(8725, "JSON Web Token Best Current Practices", 2020), ["the JWT best-practice RFC 8725 was published in 2020"]),
 ("McLean, T. \"Critical Vulnerabilities in JSON Web Token Libraries.\" March 2015.", ["In 2015, security researcher Tim McLean reviewed popular JWT libraries"]),
 ("US Cybersecurity and Infrastructure Security Agency. Alert AA21-008A, \"Detecting Post-Compromise Threat Activity in Microsoft Cloud Environments.\" January 2021.", ["a technique researchers named **Golden SAML**"]),
 ("W3C. *Web Authentication: An API for Accessing Public Key Credentials, Level 2.* 2021; FIDO Alliance, FIDO2 and passkey specifications. https://fidoalliance.org/", ["**FIDO2** and its web API, **WebAuthn**"]),
 ("US Office of Management and Budget. Memorandum M-22-09, *Moving the U.S. Government Toward Zero Trust Cybersecurity Principles.* January 2022.", ["US federal guidance has required phishing-resistant multi-factor authentication for agency staff since 2022"]),
],
"15": [
 (RFC(5280, "Internet X.509 Public Key Infrastructure Certificate and CRL Profile", 2008), ["profiled for the internet in **RFC 5280**"]),
 (BR, ["Must include at least 64 random bits for public certificates"]),
 ("CA/Browser Forum. Ballot SC47v2, \"Sunset of subject:organizationalUnitName.\" 2022.", ["Public CAs stopped including `OU` in TLS certificates in 2022"]),
 ("Marlinspike, M. \"Internet Explorer SSL Vulnerability.\" Bugtraq, August 2002.", ["such as a 2002 flaw in Internet Explorer"]),
 ("Let's Encrypt. \"DST Root CA X3 Expiration (September 2021).\" https://letsencrypt.org/docs/dst-root-ca-x3-expiration-september-2021/", ["the expiry of that cross-signature in September 2021"]),
 ("CA/Browser Forum. *Baseline Requirements for the Issuance and Management of Publicly-Trusted Code Signing Certificates* (hardware key protection effective June 2023); *S/MIME Baseline Requirements* (effective September 2023).", ["keys must be in hardware since 2023"]),
 ("Ayer, A. \"Fixing the Breakage from the AddTrust External CA Root Expiration.\" SSLMate blog, May 2020.", ["On 30 May 2020, a widely used root certificate"]),
],
"16": [
 (BR, ["writes the **Baseline Requirements**"]),
 (FOX_IT, ["| 2011 | DigiNotar |", "In the summer of 2011, attackers broke into DigiNotar"]),
 ("Mozilla. \"WoSign and StartCom\" investigation report, 2016; Google Chrome Security. \"Distrust of WoSign and StartCom Certificates.\" 2016.", ["| 2015 to 2016 | CNNIC, WoSign and StartCom |"]),
 ("Google Chrome Security. \"Chrome's Plan to Distrust Symantec Certificates.\" Google Security Blog, September 2017.", ["| 2017 to 2018 | Symantec (and its brands) |"]),
 ("Google Chrome Root Program. \"Sustaining Digital Certificate Security: Entrust Certificate Distrust.\" Google Security Blog, June 2024.", ["| 2024 | Entrust |"]),
 ("Google Chrome Root Program. \"Sustaining Digital Certificate Security: Upcoming Changes to the Chrome Root Store\" (Chunghwa Telecom and Netlock), May 2025.", ["| 2025 | Chunghwa Telecom and Netlock |"]),
 ("CA/Browser Forum. Ballot SC-067, \"Require Multi-Perspective Issuance Corroboration.\" 2024; Birge-Lee, H., Sun, Y., Edmundson, A., Rexford, J., Mittal, P. \"Bamboozling Certificate Authorities with BGP.\" USENIX Security 2018.", ["Multi-Perspective Issuance Corroboration, adopted in Ballot SC-067"]),
 (SC081, ["the CA/Browser Forum approved **Ballot SC-081**"]),
 ("Let's Encrypt. \"Announcing Six Day and IP Address Certificate Options in 2025.\" January 2025. https://letsencrypt.org/2025/01/16/6-day-and-ip-certs/", ["Let's Encrypt began offering optional **six-day certificates** in 2025"]),
 (RFC(6962, "Certificate Transparency", 2013), ["specified in RFC 6962"]),
 ("Valsorda, F. *Sunlight* CT log implementation and the static-ct-api specification, 2024. https://sunlight.dev/", ["(the \"Sunlight\" architecture and the static-ct-api specification)"]),
 (RFC(8659, "DNS Certification Authority Authorization (CAA) Resource Record", 2019), ["A **CAA** (Certification Authority Authorization) record"]),
 ("Google Chrome. Removal of EV certificate indicators in Chrome 77, 2019; Thompson, C., Shelton, M., Stark, E., et al. \"The Web's Identity Crisis: Understanding the Effectiveness of Website Identity Indicators.\" USENIX Security 2019.", ["Browsers removed the special EV indicator around 2019"]),
],
"17": [
 (RFC(5280, "Internet X.509 PKI Certificate and CRL Profile", 2008), ["the algorithm in RFC 5280, section 6"]),
 (DANGEROUS, ["A 2012 study titled \"The Most Dangerous Code in the World\"", "In 2012, researchers from Stanford and the University of Texas published"]),
 (RFC(6960, "X.509 Internet PKI Online Certificate Status Protocol (OCSP)", 2013), ["The **Online Certificate Status Protocol** (RFC 6960)"]),
 ("Langley, A. \"No, Don't Enable Revocation Checking.\" *ImperialViolet* blog, April 2014. The seat belt comparison is paraphrased.", ["Security researcher Adam Langley summarised it in 2014"]),
 ("Larisch, J., Choffnes, D., Levin, D., Maggs, B. M., Mislove, A., Wilson, C. \"CRLite: A Scalable System for Pushing All TLS Revocations to All Browsers.\" IEEE Symposium on Security and Privacy 2017.", ["**CRLite (Firefox)**"]),
 ("CA/Browser Forum. Ballot SC-063, \"Make OCSP Optional, Require CRLs, and Incentivize Automation.\" 2023.", ["(Ballot SC-063)"]),
 (LE_OCSP, ["Let's Encrypt, the largest CA, ended its OCSP service in August 2025"]),
],
"18": [
 (RFC(3647, "Internet X.509 PKI Certificate Policy and Certification Practices Framework", 2003), ["in a standard RFC 3647 structure"]),
 (NIST_57, ["10 to 20 years"]),
 ("Schroeder, W., Christensen, L. *Certified Pre-Owned: Abusing Active Directory Certificate Services.* SpecterOps whitepaper, June 2021.", ["Researchers showed in 2021 (\"Certified Pre-Owned\")"]),
 ("Smallstep. *step-ca* documentation. https://smallstep.com/docs/step-ca/", ["Install **step-ca**, initialise a CA"]),
],
"19": [
 (RFC(8555, "Automatic Certificate Management Environment (ACME)", 2019), ["The **Automatic Certificate Management Environment (ACME)**, RFC 8555"]),
 ("Aas, J., Barnes, R., Case, B., et al. \"Let's Encrypt: An Automated Certificate Authority to Encrypt the Entire Web.\" ACM CCS 2019.", ["which launched in 2015 and now issues certificates for hundreds of millions of websites"]),
 (RFC(9773, "ACME Renewal Information (ARI) Extension", 2025), ["standardised in 2025 as RFC 9773"]),
 (SC081, ["| 47 days (from March 2029) | 31 days | 11,800 |"]),
 ("Ericsson. Press statement on software certificate expiry affecting mobile networks, December 2018; BBC News, \"O2 data outage,\" 6 December 2018.", ["a mobile network outage affecting millions of users in 2018"]),
 ("Reporting on the February 2020 Microsoft Teams outage caused by an expired authentication certificate, e.g., *The Verge*, 3 February 2020.", ["a global collaboration-tool outage in 2020"]),
 ("Public CA incident report on the mass revocation of certificates issued with flawed CNAME-based domain control validation, Mozilla Bugzilla CA Certificate Compliance component, July 2024; see also trade-press coverage of the revocation, July 2024.", ["one large CA had to revoke over 80,000 in 2024 within days"]),
 (EQUIFAX + " See also US GAO, *Data Protection: Actions Taken by Equifax and Federal Agencies in Response to the 2017 Breach*, GAO-18-559, August 2018.", ["In 2017, attackers stole personal data on about 147 million people from Equifax", "A US House of Representatives committee report later found"]),
],
"20": [
 (NIST_57, ["NIST's **SP 800-57** (Recommendation for Key Management)"]),
 ("CircleCI. \"CircleCI Incident Report for January 4, 2023 Security Incident.\" January 2023. https://circleci.com/blog/", ["In January 2023, a widely used continuous integration service disclosed"]),
 ("PCI Security Standards Council. *PCI DSS v4.0.1*, Requirement 3.6 and 3.7 (key management, dual control, split knowledge). June 2024.", ["is a requirement in standards such as PCI DSS for payment keys"]),
],
"21": [
 ("OASIS. *Key Management Interoperability Protocol (KMIP) Specification* Version 2.1. 2020.", ["**Key Management Interoperability Protocol (KMIP)**, an OASIS standard"]),
 ("OASIS. *PKCS #11 Specification* Version 3.1. 2023.", ["| **PKCS#11** (Cryptoki) |"]),
 ("US Department of Justice. Criminal complaint in *United States v. Paige A. Thompson* (W.D. Wash.), July 2019; and the bank's public statement on the cloud data breach, July 2019.", ["In the 2019 breach of a large US bank's cloud environment"]),
],
"22": [
 ("GitGuardian. *The State of Secrets Sprawl 2025.* March 2025 (reporting about 23.8 million new hardcoded secrets detected on public GitHub in 2024). https://www.gitguardian.com/state-of-secrets-sprawl-report-2025", ["Industry studies by secret-scanning vendors have counted tens of millions of secrets leaked"]),
 ("SPIFFE project. *SPIFFE Standards* and SPIRE documentation. Cloud Native Computing Foundation. https://spiffe.io/", ["**SPIFFE** (Secure Production Identity Framework for Everyone)"]),
 ("Uber. \"Security Update\" (incident disclosure), September 2022.", ["In 2022, a ride-sharing company suffered a breach"]),
],
"23": [
 (FIPS1403, ["**FIPS 140-3** is the US and Canadian standard", "on 21 September 2026, all remaining FIPS 140-2 validation certificates moved"]),
 ("Common Criteria Recognition Arrangement. *Common Criteria for Information Technology Security Evaluation* (ISO/IEC 15408). https://www.commoncriteriaportal.org/", ["**Common Criteria** (ISO/IEC 15408)"]),
 ("PCI Security Standards Council. *PIN Transaction Security (PTS) Hardware Security Module (HSM) Modular Security Requirements.* Current version.", ["certified under **PCI PTS HSM**"]),
 ("OASIS. *PKCS #11 Cryptographic Token Interface Base Specification* Version 3.1, 2023 (key attributes CKA_SENSITIVE, CKA_EXTRACTABLE).", ["`CKA_SENSITIVE = true`"]),
 ("Trusted Computing Group. *TPM 2.0 Library Specification.* https://trustedcomputinggroup.org/", ["**Trusted Platform Module (TPM)**"]),
 ("Moghimi, D., Sunar, B., Eisenbarth, T., Heninger, N. \"TPM-FAIL: TPM meets Timing and Lattice Attacks.\" USENIX Security 2020.", ["TPM-Fail (2019) extracted ECDSA keys through timing"]),
 ("Intel. *Intel Trust Domain Extensions (TDX)* whitepaper; AMD. *AMD SEV-SNP: Strengthening VM Isolation with Integrity Protection and More.* 2020; Arm. *Arm Confidential Compute Architecture.*", ["| Intel TDX | Whole virtual machines from the hypervisor |"]),
 (STORM_MS + " " + CSRB, ["The Storm-0558 incident (Chapter 9) is, at its heart, an HSM story"]),
],
"24": [
 ("Kohnfelder, L., Garg, P. \"The Threats to Our Products.\" Microsoft internal paper, 1999 (origin of STRIDE); Shostack, A. *Threat Modeling: Designing for Security.* Wiley, 2014.", ["STRIDE (spoofing, tampering, repudiation"]),
 ("PCI Security Standards Council. *PCI DSS v4.0.1.* June 2024 (Requirement 12.3.3: inventory of cryptographic cipher suites and protocols).", ["| **PCI DSS v4.0.1** |"]),
 ("ISO/IEC 27001:2022, *Information security, cybersecurity and privacy protection: Information security management systems: Requirements*, Annex A control 8.24.", ["Control 8.24 \"Use of cryptography\""]),
 ("Regulation (EU) 2022/2554 (Digital Operational Resilience Act, DORA) and Directive (EU) 2022/2555 (NIS2).", ["DORA applies since January 2025"]),
 ("Regulation (EU) 2024/1183 amending Regulation (EU) No 910/2014 (eIDAS 2.0).", ["| **eIDAS 2.0** |"]),
 (CNSA2, ["| **CNSA 2.0** | US national security systems |"]),
 ("Greenberg, A. \"The Untold Story of NotPetya, the Most Devastating Cyberattack in History.\" *Wired*, August 2018 (citing the White House estimate of 10 billion US dollars in damage).", ["In June 2017, a destructive malware outbreak known as NotPetya"]),
],
"25": [
 ("Shor, P. W. \"Algorithms for Quantum Computation: Discrete Logarithms and Factoring.\" FOCS 1994; *SIAM Journal on Computing* 26(5), 1997.", ["In 1994, Peter Shor showed"]),
 ("Grover, L. K. \"A Fast Quantum Mechanical Algorithm for Database Search.\" STOC 1996.", ["**Grover's algorithm** (1996)"]),
 ("Google Quantum AI. \"Quantum Error Correction Below the Surface Code Threshold.\" *Nature* 638, 2025 (published online December 2024).", ["In December 2024, Google demonstrated error correction"]),
 (GIDNEY19, ["In 2019, the best estimate for factoring 2048-bit RSA"]),
 (GIDNEY25, ["In 2025, a revised analysis by Craig Gidney at Google"]),
 ("Mosca, M., Piani, M. *Quantum Threat Timeline Report.* Global Risk Institute, annual editions 2019 to 2024.", ["such as those published annually by the Global Risk Institute"]),
 ("Mosca, M. \"Cybersecurity in an Era with Quantum Computers: Will We Be Ready?\" *IEEE Security & Privacy* 16(5), 2018.", ["Michele Mosca proposed a simple way"]),
 (NIST_8547, ["| **US NIST (IR 8547, draft, 2024)** |"]),
 (CNSA2, ["| **US NSA (CNSA 2.0)** |"]),
 ("The White House. National Security Memorandum 10 (NSM-10), May 2022; *Quantum Computing Cybersecurity Preparedness Act*, Public Law 117-260, December 2022.", ["National Security Memorandum 10 (2022)"]),
 (NCSC, ["| **UK NCSC (2025)** |"]),
 (EU_PQ, ["| **European Union (coordinated roadmap, 2025)** |"]),
 ("Australian Signals Directorate. *Information Security Manual* and guidance on planning for post-quantum cryptography, 2024 to 2025.", ["Australia's guidance targets ceasing traditional asymmetric cryptography by 2030"]),
 ("National Security Agency. \"Quantum Key Distribution (QKD) and Quantum Cryptography (QC).\" Position statement; with similar positions from the UK NCSC, France's ANSSI and Germany's BSI.", ["is not recommended by the NSA, NCSC, ANSSI or BSI"]),
 (SHATTERED, ["the same year the first real collision was produced"]),
],
"26": [
 ("NIST. *NIST IR 8413, Status Report on the Third Round of the NIST Post-Quantum Cryptography Standardization Process.* July 2022.", ["In 2016, NIST launched an open competition"]),
 ("Castryck, W., Decru, T. \"An Efficient Key Recovery Attack on SIDH.\" EUROCRYPT 2023 (preprint July 2022).", ["one finalist, SIKE, which fell in 2022", "In July 2022, Wouter Castryck and Thomas Decru published an attack"]),
 (FIPS203, ["| **FIPS 203** |", "| ML-KEM-512 | 1 (about AES-128) |"]),
 (FIPS204, ["| **FIPS 204** |", "| ML-DSA-44 | 2 |"]),
 (FIPS205, ["| **FIPS 205** |", "| SLH-DSA-128s (\"small\") |"]),
 ("NIST. FN-DSA (FIPS 206) draft status updates, 2025; Fouque, P.-A., et al. *Falcon: Fast-Fourier Lattice-based Compact Signatures over NTRU.* Specification v1.2.", ["**FN-DSA** (Falcon), a compact lattice signature, as FIPS 206"]),
 ("NIST. \"NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption.\" March 2025; *NIST IR 8545*, Status Report on the Fourth Round. https://www.nist.gov/news-events/news/2025/03/", ["**HQC**, a code-based KEM selected in March 2025"]),
 ("NIST. *SP 800-208, Recommendation for Stateful Hash-Based Signature Schemes.* October 2020; RFC 8554 (LMS), 2019; RFC 8391 (XMSS), 2018.", ["approved by NIST in SP 800-208 in 2020"]),
 ("IETF LAMPS Working Group. *Composite ML-DSA for use in X.509 Public Key Infrastructure* (Internet-Draft) and RFC for ML-DSA in X.509.", ["The IETF LAMPS working group has specified composite ML-DSA formats"]),
 ("Bernstein, D. J., Bhargavan, K., Bhasin, S., et al. \"KyberSlash: Exploiting Secret-Dependent Division Timings in Kyber Implementations.\" 2024.", ["researchers found **KyberSlash**"]),
 ("OpenSSL Project. *OpenSSL 3.5* release notes, April 2025. https://www.openssl.org/", ["(3.5 and later include ML-KEM, ML-DSA and SLH-DSA)"]),
],
"27": [
 ("OWASP CycloneDX. *CycloneDX Specification v1.6* (Cryptography Bill of Materials). April 2024. https://cyclonedx.org/", ["The CycloneDX standard (version 1.6 onward)"]),
 (RFC(9370, "Multiple Key Exchanges in IKEv2", 2023), ["post-quantum KEMs (RFC 9370)"]),
 ("Benjamin, D., O'Brien, D., Westerbaan, B., et al. *Merkle Tree Certificates* (IETF Internet-Draft), 2023 to 2026.", ["**Merkle Tree Certificates**"]),
 (CNSA2, ["why CNSA 2.0 sets early dates for firmware signing"]),
],
"28": [
 ("Goldwasser, S., Micali, S., Rackoff, C. \"The Knowledge Complexity of Interactive Proof Systems.\" *SIAM Journal on Computing* 18(1), 1989 (STOC 1985).", ["A **zero-knowledge proof (ZKP)**"]),
 ("Google. Open-source release of zero-knowledge age assurance libraries (Longfellow ZK), 2025.", ["such as Google's open-sourced ZK age verification in 2025"]),
 (RFC(9591, "The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures", 2024), ["(standardised as RFC 9591 in 2024)"]),
 ("NIST. Multi-Party Threshold Cryptography project and *NIST IR 8214C* (First Call for Multi-Party Threshold Schemes). https://csrc.nist.gov/projects/threshold-cryptography", ["NIST is running a project on multi-party threshold cryptography"]),
 ("Gentry, C. \"Fully Homomorphic Encryption Using Ideal Lattices.\" STOC 2009.", ["first shown possible by Craig Gentry in 2009"]),
 ("Jarecki, S., Krawczyk, H., Xu, J. \"OPAQUE: An Asymmetric PAKE Protocol Secure Against Pre-Computation Attacks.\" EUROCRYPT 2018; IRTF Crypto Forum Research Group OPAQUE specification; IETF RFCs 9576 to 9578 (Privacy Pass), 2024.", ["OPAQUE, specified by the IRTF Crypto Forum Research Group"]),
 ("Coalition for Content Provenance and Authenticity (C2PA). *C2PA Technical Specification.* https://c2pa.org/", ["**Content provenance (C2PA)**"]),
 ("Regulation (EU) 2024/1183 (eIDAS 2.0) establishing the European Digital Identity Wallet.", ["The EU's digital identity wallet framework under eIDAS 2.0"]),
],
"A": [],
"B": [],
"C": [],
}
