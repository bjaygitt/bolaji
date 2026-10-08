---
num: A
title: Glossary
part: 12
lead: Plain-language definitions of the terms used in this book, in alphabetical order. The chapter in brackets is where each term is explained in depth.
glossary: true
---

**3-D Secure (3DS).** An EMVCo protocol that lets a card issuer authenticate the cardholder during an online purchase, usually invisibly through risk data and sometimes with a challenge. Version 2 is current. (39)

**802.1X.** The IEEE standard for port-based network access control, in which a device must authenticate (often with EAP-TLS and a certificate) before a switch port or Wi-Fi network admits it. (22)

**ACME.** Automatic Certificate Management Environment (RFC 8555), the protocol that lets software obtain and renew certificates without human involvement. (17)

**ACME Renewal Information (ARI).** An ACME extension (RFC 9773) in which the CA tells clients when to renew, so it can spread load and trigger early renewal before a mass revocation. (17, 19)

**Acquirer.** The bank or processor that signs up merchants and sends their card transactions into the card networks. (37)

**AD CS.** Active Directory Certificate Services, the Microsoft Windows Server role that runs enterprise CAs, certificate templates and auto-enrolment. (15, 18)

**AEAD.** Authenticated encryption with associated data: encryption that also detects any tampering, and can authenticate extra unencrypted data such as headers. AES-GCM and ChaCha20-Poly1305 are examples. (6)

**AES.** Advanced Encryption Standard (FIPS 197), the world's standard block cipher, with 128, 192 or 256-bit keys. (5)

**AES-GCM.** AES in Galois/Counter Mode, the most widely used AEAD, which fails badly if a nonce is ever repeated under the same key. (6)

**Agent (CLM).** Software installed on a host that discovers certificates, generates keys locally and installs renewed certificates on behalf of a CLM platform. (17, 18)

**Agentless push.** A CLM delivery pattern in which the platform connects to a device's management API (for example a load balancer) to install certificates, with no software on the device. (18)

**Algorithm agility.** See crypto agility. (42)

**ANSI X9.24.** The US standard for retail financial services symmetric key management, covering key generation, distribution, DUKPT and dual control. (38)

**API gateway.** A proxy in front of APIs that terminates TLS, validates tokens or client certificates and applies rate limits and policy. (24)

**Application-layer encryption.** Encrypting data inside the application before it reaches a database or storage system, so infrastructure administrators see only ciphertext. (27)

**Approval workflow.** A step in a CLM platform where a request must be authorised by a named approver before issuance. (17)

**Approved algorithm list.** An organisation's published list of algorithms, key sizes and protocols permitted for use, with dates for deprecation. (42)

**Argon2.** A memory-hard password hashing function (RFC 9106), the recommended choice for new systems. (7)

**ARQC and ARPC.** Authorisation Request Cryptogram, a MAC an EMV chip card computes over transaction data, and the Authorisation Response Cryptogram the issuer returns to prove the response is genuine. (37)

**Associated data.** Information authenticated, but not encrypted, by an AEAD, binding a ciphertext to its context. (6)

**Asymmetric cryptography.** Cryptography using a key pair: a public key that can be shared and a private key kept secret. Also called public-key cryptography. (1)

**ATM.** Automated teller machine, which encrypts PINs with keys loaded manually or by remote key loading. (37)

**Attestation.** Cryptographic evidence, usually signed by hardware, about the state or identity of a device or workload. (30, 36)

**Audit evidence.** Records that prove a control operated as designed, such as key ceremony logs, certificate inventories, access reviews and rotation histories. (43)

**Authenticated encryption.** See AEAD. (6)

**Authenticated origin pull.** A CDN feature that presents a client certificate to the origin so the origin accepts only CDN traffic. (18, 23)

**Authenticode.** Microsoft's code-signing format for Windows executables, drivers and scripts. (36)

**Auto-enrolment.** A Windows feature in which domain members request and renew certificates from AD CS automatically, according to Group Policy and template permissions. (15, 18)

**Baseline Requirements.** The CA/Browser Forum rules every publicly trusted TLS CA must follow, including validation methods and maximum validity. (13)

**Bcrypt and scrypt.** Older but still acceptable password hashing functions; scrypt is memory-hard. (7)

**BDK (Base Derivation Key).** The master key in a DUKPT scheme, held in the acquirer's HSM, from which every terminal's initial key and every transaction key can be derived. (37, 38)

**BGP.** Border Gateway Protocol, which routes traffic between networks on the internet and has no built-in authentication of route announcements. (23)

**Birthday bound.** The rule that repeats among random values become likely after about the square root of the number of possibilities. (4)

**BitLocker.** Microsoft's full-volume encryption for Windows, usually with keys protected by a TPM. (26)

**Block cipher.** An algorithm that encrypts fixed-size blocks of data under a key. (5)

**Break-glass procedure.** A documented emergency method to access keys or systems when normal controls are unavailable, with extra logging and review. (43)

**Bring your own CA.** Using an organisation's own CA, rather than a provider's, to issue certificates for a cloud or SaaS service. (18)

**BYOK and HYOK.** Bring your own key: importing your key material into a provider's key service. Hold your own key: keeping the key outside the provider, which must ask you for each use. (28)

**CAA record.** A DNS record listing which CAs may issue certificates for a domain. (13)

**CA/Browser Forum.** The industry body of CAs and browser makers that writes the Baseline Requirements for publicly trusted TLS certificates. (13)

**CA (certificate authority).** An organisation or system that signs certificates. (12, 13)

**Card network.** A scheme such as Visa or Mastercard that routes transactions between acquirers and issuers and sets security rules for both. (37)

**Card-not-present (CNP).** A transaction in which the card is not physically presented, such as an online or telephone purchase. (37, 39)

**CBC mode.** Cipher block chaining, an older mode that encrypts but does not authenticate, and is prone to padding-oracle attacks if misused. (6)

**CBOM.** Cryptographic bill of materials: a machine-readable list of the cryptographic algorithms, keys, certificates and protocols in a system. CycloneDX defines a format. (43, 46)

**Certificate.** A signed document binding a public key to a name and permitted uses. (12)

**Certificate inventory.** The authoritative record of every certificate an organisation holds, with its key, endpoints, owner, issuer and expiry. (17)

**Certificate lifecycle management (CLM).** The discipline and platforms for discovering, issuing, deploying, monitoring, renewing and revoking certificates across an estate. (17 to 19)

**Certificate pinning.** Hard-coding an expected certificate or public key in a client, which blocks some attacks but breaks when the certificate legitimately changes. (19, 21)

**Certificate policy (CP).** A document stating the rules under which a CA issues certificates and the level of trust they carry. See also CPS. (15)

**Certificate Practice Statement (CPS).** A CA's description of how it actually implements its certificate policy. (15)

**Certificate profile.** The set of fields and extensions a certificate of a given type must contain. (12, 15)

**Certificate template.** A predefined profile (key type, validity, extensions, who may enrol) from which a CA or CLM platform issues certificates. (15, 17)

**Certificate Transparency (CT).** Public, append-only logs of publicly trusted certificates, allowing anyone to detect mis-issuance. (13)

**cert-manager.** An open-source Kubernetes controller that requests, stores and renews certificates as Kubernetes resources, using issuers such as ACME, Vault or cloud CAs. (18)

**ChaCha20-Poly1305.** An AEAD built from the ChaCha20 stream cipher and Poly1305 MAC, fast in software without AES hardware. (6)

**Chain (certificate chain).** The sequence of certificates linking a leaf certificate to a trusted root. (12)

**Chain of trust.** See chain (certificate chain). (12)

**Cipher policy.** A standard defining permitted TLS versions, cipher suites and key exchange groups. (21)

**Cipher suite.** The named combination of algorithms a TLS connection uses; in TLS 1.3, an AEAD and a hash. (20)

**Ciphertext.** Encrypted data. (1)

**Client certificate authentication.** Proving a user's or device's identity to a server with a certificate and private key, as in mTLS or smart-card logon. (16)

**Cloud HSM.** A dedicated, single-tenant HSM rented from a cloud provider and managed by the customer through standard HSM interfaces. (28, 33)

**CMDB.** Configuration management database, which records systems and owners and can be linked to the certificate inventory. (19)

**CMP.** Certificate Management Protocol (RFC 9810), a full-featured enrolment protocol used in telecoms and industrial PKI. (17)

**CMVP.** The Cryptographic Module Validation Program run by NIST and the Canadian Centre for Cyber Security, which validates modules against FIPS 140-3. (40)

**CNAME delegation (DCV).** Pointing an _acme-challenge or validation name to a zone controlled by a CA or CLM platform, so domain validation can be automated without broad DNS access. (17)

**CNG.** Cryptography API: Next Generation, the Windows cryptographic interface used by applications and key storage providers, including HSM providers. (33)

**CNSA 2.0.** The NSA's Commercial National Security Algorithm Suite 2.0, which sets post-quantum algorithms and transition dates for US national security systems. (41, 46)

**Code signing.** Signing software or firmware so that systems can verify who published it and that it has not been altered. (10, 36)

**Collision.** Two different inputs that produce the same hash value. (7)

**Common Criteria.** An international scheme (ISO/IEC 15408) for evaluating security products against a protection profile. (40)

**Compensating control.** An alternative control accepted when a stated requirement cannot be met, provided it reduces the same risk. (41, 43)

**Confidential computing.** Protecting data while it is being processed, using hardware-isolated environments whose state can be attested. (30)

**Confidential VM.** A virtual machine whose memory is encrypted by the processor and isolated from the hypervisor, with attestation. (30)

**Connector (CLM).** A component that integrates a CLM platform with a CA, device or cloud service, often deployed close to the systems it manages. (17, 18)

**Content Delivery Network (CDN).** A distributed network of edge servers that caches and serves content, terminating TLS close to users. (18, 23)

**CRL.** Certificate revocation list: a signed list of revoked certificate serial numbers. (14)

**Cross-certificate.** A certificate in which one CA certifies another CA's key, creating an alternative path between hierarchies. (14, 15)

**CRQC.** Cryptographically relevant quantum computer: one large and reliable enough to break RSA and elliptic curve cryptography. (44)

**Crypto agility.** The ability to change algorithms, keys, certificates or providers quickly without redesigning systems. (42)

**Crypto centre of excellence.** A small central team that sets cryptographic policy, reviews designs, runs shared services and coaches other teams. (42)

**Cryptogram.** A short value computed with a secret key to prove that a card, token or device is genuine, such as an ARQC. (37)

**Cryptographic inventory.** A list of where cryptography is used: algorithms, keys, certificates, libraries and protocols, by system and owner. (43, 46)

**Cryptographic module.** Hardware, software or firmware that implements approved cryptographic functions within a defined boundary, the unit validated under FIPS 140-3. (33, 40)

**Cryptoperiod.** The time a key is permitted to be used. (32)

**Crypto-shredding.** Making data permanently unreadable by destroying every copy of the key that encrypts it. (29)

**CSA CCM.** The Cloud Security Alliance Cloud Controls Matrix, whose CEK domain covers cryptography, encryption and key management. (41)

**CSPRNG.** Cryptographically secure pseudo-random number generator, whose output cannot be predicted without its secret state. (4)

**CSR.** Certificate signing request: a file containing a public key and requested names, signed with the private key, sent to a CA. (12)

**CTR mode.** Counter mode, which turns a block cipher into a stream cipher by encrypting successive counter values. (6)

**Customer-managed key (CMK).** A key in a cloud or SaaS key service that the customer creates and controls, as opposed to a provider-managed default key. (28)

**CVV and iCVV.** Card verification values: codes computed with an issuer key over card data, printed on the card (CVV2) or stored on the chip (iCVV) to detect counterfeits. (37)

**Data classification.** Labelling data by sensitivity, which drives which encryption and key controls apply. (29, 42)

**Data clean room.** An environment where several parties analyse combined data under privacy controls without exposing raw records. (31)

**Data encryption key (DEK).** See DEK and KEK. (32)

**Data in transit, at rest and in use.** The three states of data, each protected by different cryptographic controls: network encryption, storage encryption and confidential computing. (2)

**Data residency.** A requirement that data, and sometimes its keys, stay within a given country or region. (28)

**DCV (domain control validation).** The checks a CA performs to confirm that an applicant controls a domain, using HTTP, DNS or email methods. (13, 17)

**DEK and KEK.** Data encryption key, which encrypts data; key encryption key, which encrypts (wraps) other keys. (32)

**Differential privacy.** A mathematical guarantee, achieved by adding calibrated noise, that the result of an analysis reveals almost nothing about any one individual. (31)

**Diffie-Hellman (DH, ECDH).** A method for two parties to agree on a shared secret over a public channel; ECDH is the elliptic curve form. (9)

**Diffie-Hellman group.** The specific group or curve used for a key exchange, such as X25519 or P-256. (9, 20)

**Digital signature.** A value created with a private key that anyone with the public key can verify, proving origin and integrity. (10)

**Discovery (certificate).** Finding certificates and keys across networks, CT logs, CA accounts, clouds, Kubernetes clusters and hosts, to build an inventory. (17)

**Discrete logarithm problem.** Given g and g^x in a group, find x. Believed hard classically; broken by quantum computers. (3)

**Distrust (CA).** A root program's decision to stop trusting certificates from a CA, usually after compliance failures. (13, 19)

**DKIM.** DomainKeys Identified Mail, in which a sending domain signs email headers and body with a key published in DNS. (25)

**DNS-01 challenge.** An ACME validation method in which the client proves domain control by publishing a TXT record, and the only method that supports wildcard certificates. (17)

**DNS CAA account binding.** A CAA parameter (RFC 8657) restricting issuance to a specific ACME account or validation method. (13, 17)

**DNSSEC.** DNS Security Extensions, which sign DNS records so resolvers can verify they have not been forged. (23)

**Domain validation reuse.** The period during which a CA may rely on an earlier domain validation; being reduced to 10 days for public TLS. (13, 17)

**DORA.** The EU Digital Operational Resilience Act (Regulation 2022/2554), applying to financial entities from January 2025, with technical standards on encryption and key management. (41)

**Downgrade attack.** Tricking two parties into negotiating a weaker protocol version or algorithm than both support. (11, 20)

**DPoP.** Demonstrating Proof of Possession (RFC 9449), which binds OAuth tokens to a client key so a stolen token alone is useless. (16)

**Dual control.** A rule that two or more authorised people must act together to perform a sensitive operation, such as loading a key. (32, 38)

**DUKPT.** Derived Unique Key Per Transaction, a scheme in which each payment terminal derives a fresh key for every transaction from an initial key, so one stolen key exposes one transaction. (37)

**DV, OV and EV certificates.** Domain-validated, organisation-validated and extended-validation certificates, which differ in how much the CA checks about the applicant. (13, 17)

**EAP-TLS.** An 802.1X authentication method in which both the client and the RADIUS server authenticate with certificates. (22)

**ECDHE.** Ephemeral elliptic curve Diffie-Hellman, which provides forward secrecy in TLS. (9, 20)

**ECDSA and EdDSA.** Elliptic curve signature algorithms; Ed25519 is the most common EdDSA instance. (10)

**ECH (Encrypted Client Hello).** A TLS extension (RFC 9849) that encrypts the server name and other sensitive handshake fields. (20, 23)

**Edge certificate.** The certificate a CDN presents to visitors for a customer's domain. (18, 23)

**Edge HSM.** An HSM deployed at or near CDN edge locations to hold customer keys. (23)

**eIDAS 2.0.** The EU regulation (2024/1183) on electronic identification and trust services, covering qualified signatures, qualified certificates and the European Digital Identity Wallet. (41)

**Elliptic curve.** A mathematical curve whose points form a group used for compact, efficient public-key cryptography. (3)

**EMV.** The chip card specifications managed by EMVCo, which define how cards, terminals and issuers authenticate each other and transactions. (37)

**Encryption at rest.** Encrypting stored data on disks, arrays, databases, backups and cloud storage. (26)

**Encryption in transit.** Encrypting data as it crosses a network, with protocols such as TLS, IPsec, MACsec and SSH. (20 to 25)

**Endpoint (CLM).** A network location where a certificate is presented, such as a host and port, a load balancer virtual server or a CDN property. (17)

**Enterprise key manager (EKM).** A central system that creates, stores and serves keys to many products over KMIP or vendor APIs, often backed by an HSM. (34)

**Entropy.** A measure of unpredictability, in bits. (4)

**Envelope encryption.** Encrypting data with a DEK and wrapping the DEK under a KEK held in a key management service. (28, 32)

**EST.** Enrollment over Secure Transport (RFC 7030), a certificate enrolment protocol over HTTPS that supports re-enrolment with an existing certificate. (17)

**ETSI.** The European Telecommunications Standards Institute, which publishes standards for trust service providers and qualified certificates. (40)

**External Account Binding (EAB).** An ACME feature that links an ACME account to an existing customer account at a CA, so issuance can be authorised and billed. (17)

**External key manager (cloud EKM).** A cloud feature in which encryption keys stay in a customer-run key manager outside the provider, which is called for each use. (28, 34)

**FAPI.** The OpenID Foundation's Financial-grade API security profile, which hardens OAuth with mTLS or DPoP and signed requests for open banking. (39)

**FedRAMP.** The US programme that authorises cloud services for federal use, requiring FIPS-validated cryptography. (41)

**FF1.** A NIST-approved format-preserving encryption mode (SP 800-38G), which encrypts a value such as a card number into another value of the same format. (6, 27)

**FIDO2.** The FIDO Alliance and W3C standards (WebAuthn and CTAP) for phishing-resistant login with per-site key pairs held by authenticators. (16)

**Fingerprint.** A hash of a certificate or key used as a short, unique identifier. (12)

**FIPS 140-3.** The US and Canadian standard for validating cryptographic modules, with four security levels. (33, 40)

**FIPS mode.** A configuration in which a product uses only its validated module and approved algorithms. Running in FIPS mode is not the same as being validated. (33, 40)

**Firmware signing.** Signing device firmware so the device boots or installs only genuine images. (36)

**Format-preserving encryption (FPE).** Encryption whose output has the same format and length as the input, such as a 16-digit number. (6, 27)

**Forward secrecy.** The property that stealing a long-term key later does not expose past sessions, achieved with ephemeral key exchange. (9, 20)

**Fully homomorphic encryption (FHE).** Encryption that allows arbitrary computation on ciphertexts, producing an encrypted result. (31)

**GDPR.** The EU General Data Protection Regulation, which names encryption and pseudonymisation as appropriate security measures and relaxes breach notification for unintelligible data. (41)

**GLBA.** The US Gramm-Leach-Bliley Act, whose Safeguards Rule requires financial institutions to protect customer information, including by encryption. (41)

**HA pair.** Two devices, such as load balancers, configured for failover, which must hold the same certificate and key. (18, 19)

**Hardware root key.** A key fused into a chip at manufacture, used to derive device keys and verify firmware. (36)

**Harvest now, decrypt later.** Recording encrypted traffic today in order to decrypt it once a quantum computer exists. (44)

**Hash-based signature.** A signature scheme whose security rests only on a hash function, such as SLH-DSA, LMS or XMSS. (45)

**Hash function.** A function producing a fixed-size fingerprint of any input, resistant to preimages and collisions. (7)

**HIPAA.** The US Health Insurance Portability and Accountability Act, whose Security Rule treats encryption of electronic health information as an addressable safeguard. (41)

**HKDF.** HMAC-based key derivation function, used to derive multiple keys from one strong secret. (7)

**HMAC.** A message authentication code built from a hash function. (7)

**HPKE.** Hybrid Public Key Encryption (RFC 9180), a standard way to encrypt to a public key using a KEM, a KDF and an AEAD, used by ECH and MLS. (9, 20)

**HSM.** Hardware security module: a tamper-resistant device that generates, stores and uses keys without exposing them. (33)

**HSM partition.** A logically isolated slice of an HSM with its own keys, credentials and policies, used to separate tenants or applications. (33)

**HSTS.** HTTP Strict Transport Security, a header that tells browsers to use only HTTPS for a site. (21)

**Hybrid certificate.** A certificate that carries, or is paired with, both a classical and a post-quantum key or signature during migration. (19, 46)

**Hybrid (key exchange or signature).** Combining a classical and a post-quantum algorithm so security holds if either survives. (45, 46)

**Identity provider (IdP).** A service that authenticates users and issues signed assertions or tokens to applications, such as Entra ID, Okta or Ping. (16)

**IKEv2.** Internet Key Exchange version 2 (RFC 7296), the protocol that authenticates peers and negotiates keys for IPsec. (22)

**IND-CCA2, IND-CPA.** Formal security definitions for encryption: indistinguishability under chosen-ciphertext or chosen-plaintext attack. (11)

**Infrastructure as code (IaC).** Defining infrastructure, including certificates and key policies, in version-controlled files applied by tools such as Terraform or Ansible. (18)

**Ingress controller.** The Kubernetes component that terminates external HTTP and TLS traffic and routes it to services. (18, 24)

**Initialisation vector (IV).** A value that randomises encryption so that equal plaintexts produce different ciphertexts. (6)

**Intermediate CA.** A CA certificate signed by a root, used for day-to-day issuance. (12)

**IPsec.** A suite of protocols that encrypts and authenticates IP packets, used for site-to-site and remote-access VPNs. (22)

**ISO 27001.** The international standard for information security management systems; its Annex A control 8.24 covers the use of cryptography. (41)

**ISO 27002.** The guidance companion to ISO 27001 describing how to implement each Annex A control. (41)

**ISO 9564.** The international standard for PIN management and security, including the PIN block formats. (37)

**Issuer (card).** The bank that issues a card to a customer, holds the card keys and approves or declines transactions. (37)

**Issuing CA.** A CA, usually an intermediate, that signs end-entity certificates. (15)

**Java keystore and truststore.** Files (JKS or PKCS#12) holding a Java application's private keys and certificates, and the CA certificates it trusts. (18, 19)

**JWT.** JSON Web Token: a signed (or encrypted) token carrying claims, used in OAuth and OpenID Connect. (16)

**KEM.** Key encapsulation mechanism: a public-key method where one party encapsulates a fresh shared key to another's public key. (9, 45)

**Kerberos.** A ticket-based authentication protocol using symmetric keys and a trusted key distribution centre, central to Active Directory. (16)

**Kerckhoffs's principle.** The rule that a system should remain secure even if everything about it except the key is public. (1)

**Key backup.** A protected copy of a key, often wrapped under an HSM backup key, kept so keys survive device failure. (33)

**Key block.** A format that binds a key to its attributes (usage, algorithm, exportability) under a MAC, so the key cannot be misused, as in TR-31. (37, 38)

**Key ceremony.** A scripted, witnessed and recorded procedure for generating or using high-value keys such as root CA keys. (15, 38)

**Key check value (KCV).** A short value computed by encrypting zeros with a key, used to confirm that a key was entered or transferred correctly without revealing it. (38)

**Key component.** One of several values that are combined (often by XOR) to form a key, each held by a different custodian to enforce split knowledge. (38)

**Key compromise.** Any event in which a private or secret key may have been exposed to an unauthorised party. (32, 43)

**Key custodian.** A named person responsible for handling a key component or share under documented procedures. (38)

**Key derivation function (KDF).** A function that turns a secret into one or more keys of the right length, such as HKDF. (7)

**Key destruction.** Erasing every copy of a key so it can never be used again. (29, 32)

**Key escrow.** Keeping a copy of a key with a trusted party so data can be recovered. (32)

**Key hierarchy.** A tree of keys in which higher keys protect lower ones, from a master key down to data keys. (32, 37)

**Keyless SSL.** An arrangement in which a CDN terminates TLS while the private key stays on the customer's own server or HSM, which performs the signing on request. (23)

**Key rotation.** Replacing a key with a new one at the end of its cryptoperiod or after a suspected compromise. (32)

**Key share.** A piece of a key produced by a secret sharing scheme, where any threshold number of shares can rebuild the key. (32, 38)

**Key usage and extended key usage.** Certificate extensions that limit what a key may be used for, such as digital signature or server authentication. (12)

**Key wrap.** Encrypting a key under another key with a mode designed for keys, such as AES Key Wrap (RFC 3394 and 5649). (6)

**KMIP.** Key Management Interoperability Protocol, an OASIS standard for clients such as storage arrays to manage keys in a key manager. (34)

**KMS.** Key management service: a system that stores keys and performs operations with them on request, under access policies and audit. (28)

**KPI and KRI.** Key performance indicators (such as automation rate) and key risk indicators (such as certificates expiring without an owner) for a cryptography programme. (19, 43)

**Lattice.** A regular grid of points in many dimensions; hard lattice problems underpin ML-KEM and ML-DSA. (3, 45)

**Leaf certificate.** An end-entity certificate issued to a server, user, device or workload, which cannot sign other certificates. (12)

**LMS and XMSS.** Stateful hash-based signature schemes used for firmware signing. (45)

**Load balancer (ADC).** A device or service that distributes traffic across servers and often terminates and re-encrypts TLS; application delivery controller is the broader term. (18, 21)

**LUKS.** Linux Unified Key Setup, the standard disk encryption format on Linux. (26)

**MAC.** Message authentication code: a keyed tag proving integrity and origin between parties sharing a key. (7)

**MACsec.** IEEE 802.1AE, which encrypts Ethernet frames hop by hop between switches or across data-centre links. (22)

**Mass revocation.** The revocation of many certificates at once, for example after a CA error or a key compromise, requiring rapid replacement. (19, 43)

**MDM.** Mobile device management, which enrols devices and often provisions certificates through SCEP or PKCS connectors. (18, 36)

**Measured boot.** Recording a hash of each boot component in a TPM so that a remote verifier can check what software started. (36)

**Merchant.** A business that accepts card payments. (37)

**ML-DSA.** Module-Lattice-Based Digital Signature Algorithm, FIPS 204. (45)

**ML-KEM.** Module-Lattice-Based Key-Encapsulation Mechanism, FIPS 203. (45)

**Mode of operation.** A method for using a block cipher on data of any length, such as CBC, CTR or GCM. (6)

**MPC (multi-party computation).** Techniques that let several parties compute a joint result without revealing their inputs to each other. (31)

**MTA-STS.** Mail Transfer Agent Strict Transport Security (RFC 8461), which lets a domain require authenticated TLS for incoming mail. (25)

**mTLS.** Mutual TLS, where both client and server authenticate with certificates. (20, 24)

**Multi-tenant HSM service.** A cloud key service whose keys are protected by provider-run HSMs shared among customers, as in most cloud KMS offerings. (28)

**Name constraints.** A CA certificate extension that limits which names a subordinate CA may issue for. (14, 15)

**Network token.** A substitute card number issued by a card network for a specific merchant or device, with a cryptogram per transaction. (39)

**NIS2.** The EU Directive 2022/2555 on network and information security, which requires essential and important entities to adopt policies on cryptography and encryption. (41)

**NIST SP 800-131A.** NIST's guidance on transitioning away from weak algorithms and key lengths. (41, 42)

**NIST SP 800-53.** The NIST catalogue of security and privacy controls; its SC family covers cryptographic protection and key management. (41)

**NIST SP 800-57.** NIST's recommendation for key management, which defines key types, cryptoperiods and lifecycle states. (32)

**Nonce.** A number used once: a value that must never repeat under the same key. (4, 6)

**OAuth 2.0.** The authorisation framework that lets a client obtain access tokens to call APIs on a user's or its own behalf. (16)

**OCSP.** Online Certificate Status Protocol, for asking a CA whether one certificate is revoked; being retired on the public web. (14)

**OCSP stapling.** A server attaching a recent signed OCSP response to its TLS handshake, so clients need not contact the CA. (14, 21)

**Offline root.** A root CA whose key is kept in an HSM that is powered on only for ceremonies, never connected to a network. (15)

**OID (object identifier).** A dotted number that names an algorithm, extension or policy in certificates and other ASN.1 structures. (12, 15)

**Open banking.** Regulated sharing of account data and payment initiation with third parties through secured APIs. (39)

**OpenID Connect (OIDC).** An identity layer on OAuth 2.0 that issues signed ID tokens describing an authenticated user. (16)

**OpenSSL.** A widely used open-source cryptographic library and command-line tool, used for most labs in this book. (19)

**Origin certificate.** A certificate on the origin server behind a CDN, which may be issued by the CDN provider and trusted only by it. (18, 23)

**P2PE.** Point-to-point encryption, a PCI standard for solutions that encrypt card data in the terminal and decrypt it only in a secure environment. (39)

**Padding oracle.** A flaw in which error behaviour reveals whether decrypted padding is valid, letting an attacker decrypt CBC ciphertexts. (6, 11)

**PAN.** Primary account number, the long number on a payment card. (37, 39)

**Passkey.** A phishing-resistant login credential based on a per-site key pair stored on the user's devices. (16)

**Password hashing.** Storing passwords with a deliberately slow, salted function such as Argon2, scrypt, bcrypt or PBKDF2. (7)

**Path validation.** The algorithm a relying party runs to build a chain to a trusted root and check signatures, validity, names, constraints and revocation. (14)

**Payment HSM.** An HSM certified to PCI PTS HSM that implements payment functions such as PIN translation, cryptogram verification and key block handling. (38)

**PBKDF2.** Password-based key derivation function 2, an iterated HMAC construction still common in standards. (7)

**PCI DSS.** The Payment Card Industry Data Security Standard, whose version 4.0.1 sets requirements for protecting stored and transmitted card data and managing its keys. (39, 41)

**PCI PIN.** The PCI PIN Security Requirements, which govern how PINs and the keys that protect them are handled from terminal to issuer. (38, 39)

**PCI PTS HSM.** The PCI PIN Transaction Security standard for HSMs, against which payment HSMs are approved. (38)

**PIN block.** A formatted structure that combines a PIN with padding and often the card number before encryption; ISO 9564 defines the formats. (37)

**Pinning.** See certificate pinning. (21)

**PIN translation.** Decrypting a PIN block under one key and re-encrypting it under another inside an HSM, as it passes between parties. (37, 38)

**PKCS#11.** The standard programming interface to HSMs and cryptographic tokens. (33)

**PKCS#12.** A file format that bundles a private key with its certificate chain, protected by a password. (12)

**PKI.** Public key infrastructure: the CAs, certificates, policies and processes that bind keys to identities. (12 to 15)

**Plaintext.** Unencrypted data. (1)

**Policy as code.** Expressing cryptographic rules (allowed ciphers, key sizes, issuers) as machine-checked configuration. (21, 42)

**Post-quantum cryptography (PQC).** Public-key algorithms believed secure against quantum computers, running on ordinary computers. (44, 45)

**Private CA.** A CA trusted only within an organisation, used for internal servers, devices, users and workloads. (15)

**Private key and public key.** The secret and shareable halves of an asymmetric key pair. (1)

**Proof of possession.** Evidence that the requester holds the private key matching a public key, such as the signature on a CSR. (12, 17)

**Pseudonymisation.** Replacing identifying data with substitutes so it cannot be linked to a person without separately held information. (27, 41)

**Public CA.** A CA whose roots are included in browser and operating system trust stores, bound by the Baseline Requirements. (13)

**Quantum key distribution (QKD).** Exchanging keys using quantum physics over special links; not a replacement for PQC in most enterprise settings. (44)

**QUIC.** A UDP-based transport (RFC 9000) with TLS 1.3 built in, used by HTTP/3. (23)

**QWAC.** Qualified website authentication certificate, a certificate issued by an EU qualified trust service provider under eIDAS. (41)

**RADIUS.** A protocol that carries network access authentication, often wrapping EAP-TLS, between switches or Wi-Fi controllers and an authentication server. (22)

**Rate limit.** A limit a CA or device API places on requests, which mass renewals can hit. (17, 19)

**RBAC.** Role-based access control, granting permissions according to roles, used in CLM platforms, KMS and HSM administration. (17, 28)

**Re-encryption (TLS bridging).** Terminating TLS at a proxy or load balancer, inspecting or routing traffic, and opening a new TLS connection to the back end. (21)

**Registration authority (RA).** A function that verifies requests before a CA issues certificates. (15)

**Relying party.** Anyone who relies on a certificate or signature, such as a browser or API client. (12, 14)

**Remote attestation.** Verifying attestation evidence from another machine before trusting it or releasing keys to it. (30)

**Remote key loading (RKL).** Loading keys into payment terminals or ATMs over a network using public-key methods such as TR-34, instead of manual entry. (37, 38)

**Revocation.** Declaring a certificate untrustworthy before its expiry date. (14)

**Root CA.** A self-signed CA certificate trusted because it is present in a trust store. (12)

**Root of trust.** The component, usually hardware, whose integrity everything else depends on. (36)

**Root program.** A browser or operating system vendor's policy for which root CAs it trusts, such as those run by Chrome, Mozilla, Apple and Microsoft. (13)

**RPKI.** Resource Public Key Infrastructure, which lets address holders sign which networks may originate their routes, so routers can reject hijacks. (23)

**RSA.** A public-key algorithm based on the difficulty of factoring, used for signatures and encryption. (8)

**Runbook.** A step-by-step operational procedure for a known situation, such as emergency certificate replacement. (19, 43)

**SaaS customer-managed keys.** Features that let a customer control the keys a SaaS provider uses to encrypt its data. (28)

**Salt.** A random value added to each password before hashing, so identical passwords produce different hashes. (7)

**SAML.** Security Assertion Markup Language, an XML standard for federated single sign-on with signed assertions. (16)

**SAN.** Subject Alternative Name: the certificate extension listing the names a certificate is valid for. (12)

**SAN array and NAS encryption.** Encryption performed by storage arrays, usually with keys served from an external key manager over KMIP. (26, 34)

**SCEP.** Simple Certificate Enrollment Protocol (RFC 8894), an older enrolment protocol still widely used by MDM and network devices. (17, 36)

**SD-WAN.** Software-defined wide area network, which builds encrypted overlays (usually IPsec) between branches over any transport. (22)

**Secret.** Any value granting access if disclosed: passwords, API keys, tokens, private keys. (35)

**Secrets manager.** A service that stores, issues, rotates and audits secrets for applications, such as a vault or cloud secret store. (35)

**Secret sprawl.** Secrets copied into code, configuration files, tickets and chat, outside any managed store. (35)

**Secrets rotation.** Changing a secret on a schedule or after exposure, ideally automatically by the secrets manager. (35)

**Secure boot.** A boot process in which each stage verifies the signature of the next before running it. (36)

**Secure element.** A tamper-resistant chip in a phone, card or device that stores keys and runs sensitive code. (36, 39)

**Security level (FIPS).** One of four FIPS 140-3 levels, rising from basic software modules (Level 1) to tamper-responsive hardware for hostile environments (Level 4). (33, 40)

**Security policy (FIPS).** The public document accompanying a FIPS 140-3 validation that defines the module boundary, approved modes and rules for secure operation. (40)

**Self-encrypting drive (SED).** A disk that encrypts all data in hardware, unlocked by a key or password, typically managed under the TCG Opal specification. (26)

**Service CA (OpenShift).** An OpenShift component that issues certificates for in-cluster services automatically. (18, 24)

**Service mesh.** A layer of proxies beside each service that provides mTLS, identity and traffic policy, such as Istio, Linkerd or Consul. (24)

**Session key.** A short-lived symmetric key used for one connection or session. (20)

**Session resumption.** Reusing keys from an earlier TLS session to skip a full handshake, via tickets or pre-shared keys. (20)

**SHA-2 and SHA-3.** The current NIST hash families (FIPS 180-4 and FIPS 202). (7)

**Shor's and Grover's algorithms.** Quantum algorithms that respectively break RSA and elliptic curve cryptography, and modestly speed up brute-force search. (44)

**Short-lived certificate.** A certificate valid for hours or days, renewed automatically, which reduces dependence on revocation. (14, 19)

**Side-channel attack.** An attack that learns secrets from timing, power use, cache behaviour or other physical effects of computation. (5, 10)

**SIEM.** Security information and event management, which collects logs such as HSM, KMS and CA audit events for the SOC. (43)

**Signing service.** A central service that performs code, document or transaction signing with HSM-held keys on behalf of pipelines. (36)

**Sigstore.** An open-source project for signing software artefacts with short-lived certificates tied to an identity and recording signatures in a transparency log. (36)

**SLH-DSA.** Stateless Hash-Based Digital Signature Algorithm, FIPS 205. (45)

**Smart card (PIV, CAC).** A card holding a private key and certificate for logon and signing; PIV and CAC are US government profiles. (16)

**S/MIME.** A standard for signing and encrypting email with certificates. (25)

**SNI.** Server Name Indication, the TLS extension in which the client names the host it wants, sent in clear unless ECH is used. (20)

**SOC 2.** An AICPA attestation report on a service organisation's controls against the Trust Services Criteria, which include encryption and key protection. (41)

**SOX.** The US Sarbanes-Oxley Act, which requires controls over financial reporting, including IT general controls over the systems and keys that protect financial data. (41)

**SPIFFE.** A standard for workload identity, issuing short-lived certificates or tokens to workloads after attestation; SPIRE is its reference implementation. (24, 35)

**Split-horizon DNS.** Answering the same name differently for internal and external clients, which affects certificate names and validation. (18)

**Split knowledge.** A rule that no single person knows or holds a whole key, enforced with key components or shares. (32, 38)

**SSH certificate.** An OpenSSH key signed by an SSH CA, with principals and a validity period, avoiding per-host key distribution. (25)

**STARTTLS.** A command that upgrades a plaintext protocol connection, such as SMTP, to TLS. (25)

**Subordinate CA.** Any CA below the root in a hierarchy. (12, 15)

**Subscriber.** The person or organisation to whom a certificate is issued. (13)

**SWIFT CSP.** The SWIFT Customer Security Programme, whose controls framework sets mandatory security controls for SWIFT users. (39)

**Symmetric cryptography.** Cryptography where the same secret key is used by both parties. (1)

**TDE (transparent data encryption).** Database encryption of data files and logs, applied by the database engine without application changes. (27)

**Threat model.** A description of what is protected, from whom, with what capabilities, and for how long. (1, 42)

**Time-stamping authority (TSA).** A service that signs a time stamp over a hash, proving data existed at a given time (RFC 3161). (10, 36)

**TLS.** Transport Layer Security, the protocol that secures most internet connections. (20, 21)

**TLS inspection.** Decrypting traffic at a proxy or firewall, inspecting it and re-encrypting it, using a CA trusted by managed clients. (21)

**TLS passthrough.** Forwarding encrypted traffic without terminating it, so TLS ends at the back-end server. (21)

**TLS termination.** The point where a TLS connection ends and traffic is decrypted, such as a CDN, load balancer, ingress or application. (21)

**TMK and TPK.** Terminal master key, which protects keys loaded into a terminal, and terminal PIN key, which encrypts PIN blocks from that terminal. (37)

**Tokenisation.** Replacing sensitive data such as a card number with a random surrogate, while the real value is kept in a secure vault. (27, 39)

**TPM.** Trusted Platform Module: a security chip in computers providing protected keys, measured boot and attestation. (36)

**TR-31.** The ANSI X9 technical report that defines an interoperable key block format for exchanging symmetric keys with their attributes. (37, 38)

**TR-34.** The ANSI X9 technical report that defines how to distribute symmetric keys to devices using asymmetric cryptography, as in remote key loading. (37, 38)

**Transparency log.** An append-only, publicly verifiable log, used by Certificate Transparency and Sigstore. (13, 36)

**Truncation.** Showing or storing only part of a card number, such as the first six and last four digits. (39)

**Trust anchor.** A public key or certificate trusted directly, without a chain, as the start of path validation. (14)

**Trusted execution environment (TEE).** A hardware-isolated area of a processor in which code and data are protected from the rest of the system. (30)

**Trust service provider (TSP).** An organisation providing electronic trust services such as certificates, signatures or time stamps; under eIDAS, it may be qualified. (41)

**Trust store.** The set of root certificates a client trusts. (12)

**Validity period.** The time between a certificate's notBefore and notAfter dates. (12, 13)

**WebAuthn.** The W3C browser API for creating and using FIDO2 credentials. (16)

**Wildcard certificate.** A certificate valid for any single label in one position, such as `*.example.com`. (12, 13)

**WireGuard.** A modern, minimal VPN protocol with fixed algorithms and public-key peer authentication. (22)

**Workload identity.** A cryptographic identity issued to software (a pod, function or VM) rather than to a person, used instead of static secrets. (24, 35)

**WPA3-Enterprise.** The Wi-Fi security standard for organisations, using 802.1X authentication with a 192-bit mode for high-security networks. (22)

**Wrapping key.** A key used only to encrypt other keys for storage or transport. (6, 32)

**X25519.** Diffie-Hellman key exchange on Curve25519, the default classical key exchange in modern protocols. (9)

**X25519MLKEM768.** The hybrid TLS key exchange that combines X25519 with ML-KEM-768, widely deployed by browsers and CDNs. (20, 46)

**X.509.** The standard format for public-key certificates. (12)

**XTS mode.** A block cipher mode designed for disk sectors, providing confidentiality without integrity. (6, 26)

**Zero-knowledge proof.** A proof that a statement is true which reveals nothing else. (31)

**Zero-touch provisioning.** Enrolling devices with identities and certificates automatically when they first connect. (36)

**Zero trust.** An approach that grants access per request based on verified identity and device posture, rather than network location. (22)

**ZMK and ZPK.** Zone master key, shared between two payment parties to protect key exchange, and zone PIN key, which encrypts PIN blocks between them. (37, 38)

**ZTNA.** Zero trust network access, which connects users to specific applications through a broker after checking identity and device, replacing broad VPN access. (22)
