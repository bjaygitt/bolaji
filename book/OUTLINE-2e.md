# Trust at Scale, Second Edition: Proposed Outline

**Applied Cryptography for the Enterprise, from First Principles to the Post-Quantum Era**
Bolaji Akinyele

## At a glance

| Item | Plan |
|---|---|
| Length | About 650 pages: 47 chapters in 12 parts, plus 5 appendices |
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
16. **Enterprise Identity and Authentication Protocols** *(ch14, expanded)*: Kerberos and Active Directory, SAML, OAuth 2.0 and OIDC, JWT, FIDO2 passkeys, smart cards (PIV/CAC), client-certificate auth, and how identity providers (Entra ID, Okta, Ping) use keys.

## Part IV. Certificate Lifecycle Automation (standalone)

This Part is written to stand alone: a certificate automation engineer can read these three chapters without the rest of the book. Each one covers both private enterprise networks and the public internet. Integrations are explained from public vendor documentation, with alternatives shown side by side.

17. **Certificate Lifecycle Management: Foundations, Platforms and Protocols** *(new, absorbs 1st ed. ch19)*:
    - **Why automate now:** the 200/100/47-day schedule, 10-day validation reuse, CA distrust events and outage economics
    - **The lifecycle:** discovery, inventory, ownership, request, approval, issuance, installation, validation, monitoring, renewal, revocation, retirement
    - **Discovery:** network scanning across private ranges and DMZs, CT-log monitoring for public names, CA account imports, cloud and Kubernetes API discovery, agents on hosts
    - **The inventory data model:** certificate, key, endpoint, application, owner, environment, policy
    - **Policy:** templates, approved CAs, key types and sizes, SAN rules, validity, and who may request what
    - **Issuing CAs:**
      - public CAs (DigiCert, Sectigo, GlobalSign, Entrust, Let's Encrypt and others), and how DV, OV and EV validation is automated, including DNS-01, CNAME delegation and DCV for many domains
      - private CAs (AD CS, EJBCA, Vault PKI, step-ca, AWS Private CA, Google CAS, Azure options)
    - **Enrolment protocols in depth:** ACME with External Account Binding and ARI, EST, SCEP, CMP, and CA REST APIs, with when to use each
    - **Platform architecture:** central service, connectors, agents and agentless push, satellite or proxy components for segmented networks, RBAC, workflow and approvals, HSM-backed keys, high availability
    - **Platforms compared:** CyberArk Certificate Manager (formerly Venafi), Keyfactor Command, AppViewX, DigiCert Trust Lifecycle Manager, Sectigo Certificate Manager and GlobalSign, against open-source options (cert-manager, certbot, acme.sh, Smallstep)
    - **Where keys are generated:** on the device, centrally or in an HSM, and the security trade-offs of each
18. **Integrating Certificate Automation Across the Enterprise Technology Stack** *(new)*:
    - **Delivery patterns:**
      - API push from the platform
      - agent pull
      - native ACME clients
      - secret-store sync
      - infrastructure as code (Ansible, Terraform)
      - each with its trust and network-path implications
    - **Public edge and CDN:** Akamai (CPS and Property Manager), Cloudflare (edge, custom and origin certificates), AWS CloudFront with ACM, Fastly; edge-issued versus customer-managed certificates; origin certificates and mTLS to origin
    - **Load balancers and ADCs:** F5 BIG-IP (iControl REST, SSL profiles, HA pairs, keys in a FIPS module or network HSM), Citrix NetScaler, NGINX and HAProxy, AWS ALB/NLB, Azure Application Gateway and Front Door, Google Cloud load balancers
    - **Network and security devices:** Palo Alto firewalls and Panorama (inbound and forward-proxy decryption certificates, GlobalProtect), Fortinet, Cisco ASA/FTD and ISE, Check Point, Zscaler; VPN gateway certificates; 802.1X, RADIUS and Wi-Fi server certificates
    - **Platforms and containers:**
      - Kubernetes with cert-manager (Issuers, ClusterIssuers, ACME, Vault, venafi and cloud issuers)
      - OpenShift routes, the ingress controller, and its service CA
      - Istio and SPIFFE workload certificates
      - HashiCorp Vault PKI
      - CI/CD pipelines
    - **Windows and endpoints:** AD CS templates and auto-enrolment, Intune SCEP and PKCS connectors, Jamf, IIS and Exchange, RDP, macOS and mobile device certificates
    - **Applications and middleware:** Java keystores and truststores (Tomcat, WebLogic, Kafka), IBM MQ, databases, mainframe
    - **Cloud certificate services:** AWS ACM and Private CA, Azure Key Vault certificates and App Service, Google Certificate Manager and CAS, and how to integrate them with a central CLM platform
    - **Private versus public networks:**
      - split-horizon DNS
      - reaching devices behind firewalls and in DMZs
      - outbound-only connectors
      - air-gapped and OT segments
      - multi-cloud and on-premises hybrid designs
19. **Operating Certificate Automation: Rollout, Troubleshooting and the Short-Lived Era** *(new)*:
    - **The rollout programme:** phases, onboarding application owners, change management, CMDB integration
    - **Post-installation validation:** chain, SAN, key match, OCSP and CRL reachability, cipher policy
    - **Monitoring, alerting and KPIs:** coverage, automation rate, time-to-renew, expiry incidents
    - **Failure modes and fixes:**
      - missing intermediates
      - old roots in Java and appliance truststores
      - pinned certificates
      - HA pairs updated on one node only
      - CDN propagation delays
      - HSM-backed keys that cannot be exported
      - device API rate limits
      - DCV failures
    - **The troubleshooting toolkit:** openssl, curl, keytool, certutil, kubectl, and reading platform logs
    - **Runbooks:** mass revocation and CA distrust, key compromise, emergency replacement at scale
    - **Getting ready for 47-day certificates and ARI**
    - **Audit evidence and compliance mapping:** PCI DSS 4.0.1 inventory requirement, NIST, ISO
    - **PQC and hybrid certificates in CLM:** what to ask vendors now
    - **Skills and career path** for a certificate automation engineer
    - **Labs:** ACME with step-ca and DNS-01, cert-manager on a local Kubernetes cluster, and pushing a certificate to NGINX and HAProxy through an API


## Part V. Data in Transit

20. **Building a Secure Channel with TLS 1.3** *(ch11)*
21. **Deploying TLS in the Enterprise** *(ch12, expanded)*:
    - where TLS terminates (CDN, WAF, load balancer, ingress, sidecar, app)
    - re-encryption versus passthrough
    - TLS inspection (Palo Alto, Zscaler, Netskope, F5 SSL Orchestrator) and its legal and privacy limits
    - cipher policy as code
    - mTLS
22. **Private Networks: IPsec, MACsec, VPNs and Zero Trust** *(new, partly ch13)*:
    - IKEv2/IPsec site-to-site
    - MPLS and SD-WAN encryption
    - MACsec on data-centre links and inter-DC fibre
    - remote access VPN versus ZTNA (Zscaler, Palo Alto Prisma, Cloudflare One)
    - WireGuard
    - enterprise Wi-Fi (WPA3-Enterprise, 802.1X, EAP-TLS) and NAC
23. **The Public Internet and the Edge** *(new)*:
    - CDN and WAF key custody (Akamai, Cloudflare, Fastly, CloudFront)
    - keyless SSL and edge HSMs
    - DNSSEC
    - BGP security and RPKI
    - DDoS and TLS
    - ECH and QUIC
24. **Service-to-Service and Platform Encryption** *(new)*:
    - Kubernetes and OpenShift
    - service meshes (Istio, Linkerd, Consul)
    - SPIFFE/SPIRE
    - API gateways
    - Kafka and message queues
    - database connections
    - mainframe and legacy protocols
25. **SSH, Email and Secure Messaging** *(ch13, expanded)*: SSH certificates at scale; email (STARTTLS, MTA-STS, DANE, DKIM, S/MIME); Signal-style messaging.

## Part VI. Data at Rest

26. **Storage Encryption** *(new)*:
    - disks and laptops (BitLocker, FileVault, LUKS)
    - self-encrypting drives (OPAL)
    - SAN and NAS arrays (NetApp, Dell, Pure)
    - VMware and Hyper-V VM encryption
    - backup and tape (LTO)
    - cloud volume and object encryption options
27. **Database and Application-Layer Encryption** *(new)*:
    - TDE in Oracle, SQL Server, PostgreSQL and MySQL
    - column- and field-level encryption
    - SQL Server Always Encrypted, MongoDB Queryable Encryption
    - client-side and envelope encryption done right
    - tokenisation versus FPE
    - searchable encryption trade-offs
28. **Cloud Key Management: KMS, BYOK, HYOK and EKM** *(ch21, expanded)*:
    - AWS KMS, Azure Key Vault and Managed HSM, Google Cloud KMS and EKM
    - Oracle and IBM options
    - multi-cloud key strategy
    - sovereignty and data residency
    - SaaS customer-managed keys (Microsoft 365, Salesforce Shield, ServiceNow)
29. **Data-Centric Protection and Crypto-Shredding** *(new)*: file and document encryption, Microsoft Purview labels and rights management, email encryption, data lifecycle, retention, crypto-shredding and proving deletion.

## Part VII. Data in Use

30. **Confidential Computing** *(ch23 part, expanded)*:
    - Intel SGX and TDX, AMD SEV-SNP, Arm CCA
    - AWS Nitro Enclaves, Azure and GCP confidential VMs
    - attestation flows and key release
    - what it does and does not protect
31. **Privacy-Enhancing Technologies** *(ch28, expanded)*: MPC, FHE, zero knowledge, differential privacy, data clean rooms, and where each is deployed in industry today.

## Part VIII. Key Management and Hardware

32. **Key Management Fundamentals** *(ch20)*: NIST SP 800-57, lifecycles, crypto-periods and key hierarchies.
33. **HSMs in the Enterprise** *(ch23, expanded)*:
    - general-purpose HSMs (Thales Luna, Entrust nShield, Utimaco, Securosys, Marvell LiquidSecurity)
    - cloud HSMs
    - PKCS#11, JCE, CNG and KMIP
    - partitions, HA clusters, backup, firmware and FIPS mode
    - sizing and performance
34. **Enterprise Key Managers and Integration** *(new)*: centralised key managers (Thales CipherTrust, Fortanix DSM, Entrust KeyControl, IBM GKLM), KMIP for storage and VMware, external key managers for cloud, and key brokering.
35. **Secrets Management and Workload Identity** *(ch22)*: Vault, CyberArk Conjur and Secrets Hub, the cloud secret stores, and the PAM relationship.
36. **Endpoints, Devices and Code Signing** *(new)*:
    - TPM and secure/measured boot
    - code and firmware signing pipelines (Sigstore, Authenticode, HSM-backed signing)
    - mobile secure elements
    - IoT and OT device identity
    - MDM and SCEP

## Part IX. Payments Cryptography

37. **How Card Payments Work, Cryptographically** *(new)*:
    - the four-party model
    - EMV chip cryptograms (ARQC/ARPC)
    - PIN blocks and PIN translation
    - the key hierarchy (ZMK, ZPK, TMK, BDK)
    - DUKPT, TR-31 key blocks, TR-34 remote key loading
38. **Payment HSMs and Payment Key Management** *(new)*: payment HSMs (Thales payShield, Futurex, Utimaco Atalla), cloud payment cryptography (AWS Payment Cryptography and others), key ceremonies, dual control and split knowledge, ANSI X9.24.
39. **Payment Security Programmes** *(new)*:
    - PCI DSS v4.0.1 cryptographic requirements
    - PCI PIN, P2PE and PTS HSM
    - tokenisation and network tokens
    - 3-D Secure 2
    - Apple Pay and Google Pay
    - SWIFT CSP
    - real-time payments
    - open banking (FAPI, mTLS, signed requests)

## Part X. Governance, Risk and Compliance

40. **Standards and Validation** *(new, partly appendix B)*: how NIST, ISO/IEC, IETF, ETSI and ANSI X9 make standards; FIPS 140-3 and CMVP; Common Criteria; how to read a security policy and a certificate; what "FIPS compliant" really means.
41. **Regulations and Frameworks Mapped to Cryptographic Controls** *(new)*:
    - US: NIST SP 800-53, SP 800-131A, FedRAMP, CNSA 2.0, HIPAA, SOX, GLBA
    - international: ISO 27001 (A.8.24), SOC 2, CSA CCM
    - EU: GDPR, NIS2, DORA, eIDAS 2.0
    - UK NCSC
    - one crosswalk table for all of them
42. **Cryptographic Architecture, Agility and Governance** *(ch24)*: policy, standards, approved-algorithm lists, the crypto centre of excellence, RACI, exceptions and threat modelling.
43. **Running a Cryptography Programme** *(new)*:
    - inventory and CBOM
    - metrics and KRIs
    - audit evidence
    - vendor and third-party risk
    - incident playbooks (CA compromise, key leak, mass revocation, algorithm break)
    - budgeting and executive reporting

## Part XI. The Post-Quantum Transition

44. **The Quantum Threat** *(ch25)*
45. **The New Algorithms: ML-KEM, ML-DSA, SLH-DSA and Beyond** *(ch26)*
46. **Enterprise Post-Quantum Migration** *(ch27, expanded)*:
    - vendor readiness by category (browsers, CDNs, load balancers, HSMs, KMS, CAs, VPNs)
    - payments and PQC
    - regulatory deadlines
    - a worked Meridian migration plan

## Part XII. Bringing It Together

47. **One Transaction, End to End** *(new capstone)*: follow a Meridian customer's card payment from phone to CDN, WAF, load balancer, mesh, application, database, KMS, payment HSM, card network and back. Every key, certificate and protocol on the path, who owns it, how it is rotated, what auditors ask about it, and what breaks first.

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
