# Trust at Scale, Second Edition: Proposed Outline

**Applied Cryptography for the Enterprise, from First Principles to the Post-Quantum Era**
Bolaji Akinyele

## At a glance

| Item | Plan |
|---|---|
| Length | About 600 pages: 45 chapters in 11 parts, plus 5 appendices |
| Reader | An engineer becoming an architect who will design, run and defend enterprise cryptography programmes, and explain them to auditors and executives |
| Spine | Every concept is explained from first principles, then connected to where it lives in a real enterprise, then shown in several real products |
| Products | Many vendors shown side by side, based only on public documentation, dated "as of 2026". No single vendor stack is followed end to end |
| Running example | **Meridian Financial Group**, a fictional bank, insurer and payments processor with offices, data centres, three clouds, a CDN, mobile apps and a card business. Each part adds a layer to Meridian's architecture, and the final chapter traces one transaction through all of it |
| Labs | Free tools on a laptop first (OpenSSL, step-ca, EJBCA Community, Vault dev mode, SoftHSM, Docker, Wireshark, strongSwan). Optional cloud extensions with cost warnings |
| Kept from the first edition | All 28 chapters are kept, reorganised and deepened; the best explanations, failure stories, labs and citations carry over |

## The standard chapter pattern

1. **Why it matters**: the business problem, in one page
2. **How it works**: the concept from first principles, with diagrams
3. **Where it lives in the enterprise**: the teams, systems and trust boundaries involved, shown on the Meridian map
4. **How the major products do it**: a comparison of several vendors and open-source tools, with their trade-offs
5. **Design decisions**: the choices an architect makes and how to defend them
6. **Operations and failure**: what breaks, how you detect it, a real failure story
7. **Compliance hooks**: which controls in PCI DSS, NIST, ISO and others this chapter satisfies
8. **Lab**, **Chapter summary**, **Review questions**, **References**

---

## Part I. Foundations: Cryptography in the Enterprise

1. **How to Think About Cryptography** *(1st ed. ch1, expanded)*: the goals, the threat models, Kerckhoffs, and why crypto fails in operations rather than in maths.
2. **The Enterprise Cryptographic Landscape** *(new)*: data at rest, in transit and in use; private networks versus the public internet; where crypto hides in a typical enterprise (more than 40 places); who owns each piece (network, platform, IAM, PKI, app, payments, GRC); Meridian introduced.
3. **The Mathematics You Actually Need** *(ch2)*
4. **Randomness, Probability and Hardness** *(ch3)*: adds enterprise entropy sources, VMs and containers, and HSM RNGs.

## Part II. The Building Blocks

5. **Block Ciphers and AES** *(ch4)*
6. **Modes of Operation and Authenticated Encryption** *(ch5)*: adds XTS for disks, key wrap (RFC 3394/5649), and format-preserving encryption (FF1).
7. **Hash Functions, MACs, Key Derivation and Password Storage** *(ch6)*
8. **RSA** *(ch7)*
9. **Diffie-Hellman and Elliptic Curves** *(ch8)*
10. **Digital Signatures** *(ch9)*: adds code-, document- and transaction-signing uses.
11. **Security Definitions and How Protocols Fail** *(ch10)*

## Part III. Trust and Identity: PKI

12. **X.509 Certificates Explained** *(ch15)*
13. **The Web PKI: CAs, Root Programs and Transparency** *(ch16)*: adds the 47-day timeline and what it means for enterprise operations.
14. **Path Validation and Revocation** *(ch17)*
15. **Enterprise PKI Architecture** *(ch18, greatly expanded)*:
    - hierarchy design, policy OIDs and CP/CPS
    - Microsoft AD CS in depth, including ESC attacks and hardening
    - EJBCA, Vault PKI and step-ca
    - cloud private CAs (AWS Private CA, Google CAS, Azure options)
    - public CA enterprise accounts (DigiCert, Sectigo, GlobalSign, Entrust)
    - key ceremonies
16. **Certificate Lifecycle Management at Scale** *(ch19, greatly expanded)*:
    - discovery, inventory and ownership
    - CLM platforms compared (CyberArk/Venafi, Keyfactor, AppViewX, DigiCert Trust Lifecycle, Sectigo CM)
    - ACME, EST, SCEP and CMP
    - integration patterns for load balancers, CDNs, firewalls, Kubernetes (cert-manager), Windows auto-enrolment and MDM
17. **Enterprise Identity and Authentication Protocols** *(ch14, expanded)*: Kerberos and Active Directory, SAML, OAuth 2.0 and OIDC, JWT, FIDO2 passkeys, smart cards (PIV/CAC), client-certificate auth, and how identity providers (Entra ID, Okta, Ping) use keys.

## Part IV. Data in Transit

18. **Building a Secure Channel with TLS 1.3** *(ch11)*
19. **Deploying TLS in the Enterprise** *(ch12, expanded)*:
    - where TLS terminates (CDN, WAF, load balancer, ingress, sidecar, app)
    - re-encryption versus passthrough
    - TLS inspection (Palo Alto, Zscaler, Netskope, F5 SSL Orchestrator) and its legal and privacy limits
    - cipher policy as code
    - mTLS
20. **Private Networks: IPsec, MACsec, VPNs and Zero Trust** *(new, partly ch13)*:
    - IKEv2/IPsec site-to-site
    - MPLS and SD-WAN encryption
    - MACsec on data-centre links and inter-DC fibre
    - remote access VPN versus ZTNA (Zscaler, Palo Alto Prisma, Cloudflare One)
    - WireGuard
    - enterprise Wi-Fi (WPA3-Enterprise, 802.1X, EAP-TLS) and NAC
21. **The Public Internet and the Edge** *(new)*:
    - CDN and WAF key custody (Akamai, Cloudflare, Fastly, CloudFront)
    - keyless SSL and edge HSMs
    - DNSSEC
    - BGP security and RPKI
    - DDoS and TLS
    - ECH and QUIC
22. **Service-to-Service and Platform Encryption** *(new)*:
    - Kubernetes and OpenShift
    - service meshes (Istio, Linkerd, Consul)
    - SPIFFE/SPIRE
    - API gateways
    - Kafka and message queues
    - database connections
    - mainframe and legacy protocols
23. **SSH, Email and Secure Messaging** *(ch13, expanded)*: SSH certificates at scale; email (STARTTLS, MTA-STS, DANE, DKIM, S/MIME); Signal-style messaging.

## Part V. Data at Rest

24. **Storage Encryption** *(new)*:
    - disks and laptops (BitLocker, FileVault, LUKS)
    - self-encrypting drives (OPAL)
    - SAN and NAS arrays (NetApp, Dell, Pure)
    - VMware and Hyper-V VM encryption
    - backup and tape (LTO)
    - cloud volume and object encryption options
25. **Database and Application-Layer Encryption** *(new)*:
    - TDE in Oracle, SQL Server, PostgreSQL and MySQL
    - column- and field-level encryption
    - SQL Server Always Encrypted, MongoDB Queryable Encryption
    - client-side and envelope encryption done right
    - tokenisation versus FPE
    - searchable encryption trade-offs
26. **Cloud Key Management: KMS, BYOK, HYOK and EKM** *(ch21, expanded)*:
    - AWS KMS, Azure Key Vault and Managed HSM, Google Cloud KMS and EKM
    - Oracle and IBM options
    - multi-cloud key strategy
    - sovereignty and data residency
    - SaaS customer-managed keys (Microsoft 365, Salesforce Shield, ServiceNow)
27. **Data-Centric Protection and Crypto-Shredding** *(new)*: file and document encryption, Microsoft Purview labels and rights management, email encryption, data lifecycle, retention, crypto-shredding and proving deletion.

## Part VI. Data in Use

28. **Confidential Computing** *(ch23 part, expanded)*:
    - Intel SGX and TDX, AMD SEV-SNP, Arm CCA
    - AWS Nitro Enclaves, Azure and GCP confidential VMs
    - attestation flows and key release
    - what it does and does not protect
29. **Privacy-Enhancing Technologies** *(ch28, expanded)*: MPC, FHE, zero knowledge, differential privacy, data clean rooms, and where each is deployed in industry today.

## Part VII. Key Management and Hardware

30. **Key Management Fundamentals** *(ch20)*: NIST SP 800-57, lifecycles, crypto-periods and key hierarchies.
31. **HSMs in the Enterprise** *(ch23, expanded)*:
    - general-purpose HSMs (Thales Luna, Entrust nShield, Utimaco, Securosys, Marvell LiquidSecurity)
    - cloud HSMs
    - PKCS#11, JCE, CNG and KMIP
    - partitions, HA clusters, backup, firmware and FIPS mode
    - sizing and performance
32. **Enterprise Key Managers and Integration** *(new)*: centralised key managers (Thales CipherTrust, Fortanix DSM, Entrust KeyControl, IBM GKLM), KMIP for storage and VMware, external key managers for cloud, and key brokering.
33. **Secrets Management and Workload Identity** *(ch22)*: Vault, CyberArk Conjur and Secrets Hub, the cloud secret stores, and the PAM relationship.
34. **Endpoints, Devices and Code Signing** *(new)*:
    - TPM and secure/measured boot
    - code and firmware signing pipelines (Sigstore, Authenticode, HSM-backed signing)
    - mobile secure elements
    - IoT and OT device identity
    - MDM and SCEP

## Part VIII. Payments Cryptography

35. **How Card Payments Work, Cryptographically** *(new)*:
    - the four-party model
    - EMV chip cryptograms (ARQC/ARPC)
    - PIN blocks and PIN translation
    - the key hierarchy (ZMK, ZPK, TMK, BDK)
    - DUKPT, TR-31 key blocks, TR-34 remote key loading
36. **Payment HSMs and Payment Key Management** *(new)*: payment HSMs (Thales payShield, Futurex, Utimaco Atalla), cloud payment cryptography (AWS Payment Cryptography and others), key ceremonies, dual control and split knowledge, ANSI X9.24.
37. **Payment Security Programmes** *(new)*:
    - PCI DSS v4.0.1 cryptographic requirements
    - PCI PIN, P2PE and PTS HSM
    - tokenisation and network tokens
    - 3-D Secure 2
    - Apple Pay and Google Pay
    - SWIFT CSP
    - real-time payments
    - open banking (FAPI, mTLS, signed requests)

## Part IX. Governance, Risk and Compliance

38. **Standards and Validation** *(new, partly appendix B)*: how NIST, ISO/IEC, IETF, ETSI and ANSI X9 make standards; FIPS 140-3 and CMVP; Common Criteria; how to read a security policy and a certificate; what "FIPS compliant" really means.
39. **Regulations and Frameworks Mapped to Cryptographic Controls** *(new)*:
    - US: NIST SP 800-53, SP 800-131A, FedRAMP, CNSA 2.0, HIPAA, SOX, GLBA
    - international: ISO 27001 (A.8.24), SOC 2, CSA CCM
    - EU: GDPR, NIS2, DORA, eIDAS 2.0
    - UK NCSC
    - one crosswalk table for all of them
40. **Cryptographic Architecture, Agility and Governance** *(ch24)*: policy, standards, approved-algorithm lists, the crypto centre of excellence, RACI, exceptions and threat modelling.
41. **Running a Cryptography Programme** *(new)*:
    - inventory and CBOM
    - metrics and KRIs
    - audit evidence
    - vendor and third-party risk
    - incident playbooks (CA compromise, key leak, mass revocation, algorithm break)
    - budgeting and executive reporting

## Part X. The Post-Quantum Transition

42. **The Quantum Threat** *(ch25)*
43. **The New Algorithms: ML-KEM, ML-DSA, SLH-DSA and Beyond** *(ch26)*
44. **Enterprise Post-Quantum Migration** *(ch27, expanded)*:
    - vendor readiness by category (browsers, CDNs, load balancers, HSMs, KMS, CAs, VPNs)
    - payments and PQC
    - regulatory deadlines
    - a worked Meridian migration plan

## Part XI. Bringing It Together

45. **One Transaction, End to End** *(new capstone)*: follow a Meridian customer's card payment from phone to CDN, WAF, load balancer, mesh, application, database, KMS, payment HSM, card network and back. Every key, certificate and protocol on the path, who owns it, how it is rotated, what auditors ask about it, and what breaks first.

## Appendices

- **A. Glossary** *(expanded)*
- **B. Standards, Further Reading and Practice** *(updated)*
- **C. Command Reference** *(expanded)*
- **D. Compliance Crosswalk** *(new)*: each framework's crypto requirements against the chapter that teaches them.
- **E. Vendor Capability Matrix** *(new)*: product categories against capabilities (FIPS level, PQC status, APIs), dated and drawn from public documentation.

## Ground rules carried over

- Vendor-neutral judgement. Products are compared on public documentation only, and no part of the book describes any real employer's environment.
- Every factual claim that needs one has a citation, and there is a full reference list per chapter.
- Same O'Reilly-style design, clickable contents, PDF plus an editable Canva version.
- No em dashes.
