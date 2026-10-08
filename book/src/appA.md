---
num: A
title: Glossary
part: 8
lead: Plain-language definitions of the terms used in this book, in alphabetical order. The chapter in brackets is where each term is explained in depth.
glossary: true
---

**ACME.** Automatic Certificate Management Environment (RFC 8555), the protocol that lets software obtain and renew certificates without human involvement. (19)

**AEAD.** Authenticated encryption with associated data: encryption that also detects any tampering, and can authenticate extra unencrypted data such as headers. AES-GCM and ChaCha20-Poly1305 are examples. (5)

**AES.** Advanced Encryption Standard, the world's standard block cipher, with 128, 192 or 256-bit keys. (4)

**Associated data.** Information authenticated, but not encrypted, by an AEAD, binding a ciphertext to its context. (5)

**Asymmetric cryptography.** Cryptography using a key pair: a public key that can be shared and a private key kept secret. Also called public-key cryptography. (1)

**Attestation.** Cryptographic evidence, usually signed by hardware, about the state or identity of a device or workload. (23)

**Birthday bound.** The rule that repeats among random values become likely after about the square root of the number of possibilities. (3)

**Block cipher.** An algorithm that encrypts fixed-size blocks of data under a key. (4)

**BYOK and HYOK.** Bring your own key: importing your key material into a provider's key service. Hold your own key: keeping the key outside the provider, which must ask you for each use. (21)

**CA (certificate authority).** An organisation or system that signs certificates. (15, 16)

**CAA record.** A DNS record listing which CAs may issue certificates for a domain. (16)

**CBOM.** Cryptographic bill of materials: a machine-readable list of the cryptographic algorithms, keys, certificates and protocols in a system. (27)

**Certificate.** A signed document binding a public key to a name and permitted uses. (15)

**Certificate Transparency (CT).** Public, append-only logs of all publicly trusted certificates, allowing anyone to detect mis-issuance. (16)

**Chain (certificate chain).** The sequence of certificates linking a leaf certificate to a trusted root. (15)

**Ciphertext.** Encrypted data. (1)

**CRL.** Certificate revocation list: a signed list of revoked certificate serial numbers. (17)

**CRQC.** Cryptographically relevant quantum computer: one large and reliable enough to break RSA and elliptic curve cryptography. (25)

**Crypto agility.** The ability to change algorithms, keys, certificates or providers quickly without redesigning systems. (24)

**Cryptoperiod.** The time a key is permitted to be used. (20)

**CSPRNG.** Cryptographically secure pseudo-random number generator, whose output cannot be predicted without its secret state. (3)

**CSR.** Certificate signing request: a file containing a public key and requested names, signed with the private key, sent to a CA. (15)

**DEK and KEK.** Data encryption key, which encrypts data; key encryption key, which encrypts (wraps) other keys. (20)

**Diffie-Hellman (DH, ECDH).** A method for two parties to agree on a shared secret over a public channel; ECDH is the elliptic curve form. (8)

**Digital signature.** A value created with a private key that anyone with the public key can verify, proving origin and integrity. (9)

**Discrete logarithm problem.** Given g and g^x in a group, find x. Believed hard classically; broken by quantum computers. (2)

**ECDSA and EdDSA.** Elliptic curve signature algorithms; Ed25519 is the most common EdDSA instance. (9)

**Elliptic curve.** A mathematical curve whose points form a group used for compact, efficient public-key cryptography. (2)

**Encrypted Client Hello (ECH).** A TLS extension that encrypts the server name and other sensitive handshake fields. (11)

**Entropy.** A measure of unpredictability, in bits. (3)

**Envelope encryption.** Encrypting data with a DEK and wrapping the DEK under a KEK held in a key management service. (20)

**FIPS 140-3.** The US and Canadian standard for validating cryptographic modules, with four security levels. (23)

**Forward secrecy.** The property that stealing a long-term key later does not expose past sessions, achieved with ephemeral key exchange. (8)

**Hash function.** A function producing a fixed-size fingerprint of any input, resistant to preimages and collisions. (6)

**HKDF.** HMAC-based key derivation function, used to derive multiple keys from one strong secret. (6)

**HMAC.** A message authentication code built from a hash function. (6)

**HSM.** Hardware security module: a tamper-resistant device that generates, stores and uses keys without exposing them. (23)

**Hybrid (key exchange or signature).** Combining a classical and a post-quantum algorithm so security holds if either survives. (26)

**IND-CCA2, IND-CPA.** Formal security definitions for encryption: indistinguishability under chosen-ciphertext or chosen-plaintext attack. (10)

**Intermediate CA.** A CA certificate signed by a root, used for day-to-day issuance. (15)

**JWT.** JSON Web Token: a signed (or encrypted) token carrying claims, used in OAuth and OpenID Connect. (14)

**KEM.** Key encapsulation mechanism: a public-key method where one party encapsulates a fresh shared key to another's public key. (8, 26)

**Key ceremony.** A scripted, witnessed and recorded procedure for generating or using high-value keys such as root CA keys. (18)

**KMIP.** Key Management Interoperability Protocol, a standard for clients such as storage arrays to manage keys in a key manager. (21)

**KMS.** Key management service: a system that stores keys and performs operations with them on request, under access policies and audit. (21)

**Lattice.** A regular grid of points in many dimensions; hard lattice problems underpin ML-KEM and ML-DSA. (2, 26)

**LMS and XMSS.** Stateful hash-based signature schemes used for firmware signing. (26)

**MAC.** Message authentication code: a keyed tag proving integrity and origin between parties sharing a key. (6)

**ML-DSA.** Module-Lattice-Based Digital Signature Algorithm, FIPS 204. (26)

**ML-KEM.** Module-Lattice-Based Key-Encapsulation Mechanism, FIPS 203. (26)

**Mode of operation.** A method for using a block cipher on data of any length, such as CBC, CTR or GCM. (5)

**mTLS.** Mutual TLS, where both client and server authenticate with certificates. (11)

**Nonce.** A number used once: a value that must never repeat under the same key. (3, 5)

**OCSP.** Online Certificate Status Protocol, for asking a CA whether one certificate is revoked; being retired on the public web. (17)

**Passkey.** A phishing-resistant login credential based on a per-site key pair stored on the user's devices. (14)

**PKCS#11.** The standard programming interface to HSMs and cryptographic tokens. (21, 23)

**PKI.** Public key infrastructure: the CAs, certificates, policies and processes that bind keys to identities. (15 to 19)

**Plaintext.** Unencrypted data. (1)

**Post-quantum cryptography (PQC).** Public-key algorithms believed secure against quantum computers, running on ordinary computers. (25, 26)

**Private key and public key.** The secret and shareable halves of an asymmetric key pair. (1)

**Revocation.** Declaring a certificate untrustworthy before its expiry date. (17)

**Root CA.** A self-signed CA certificate trusted because it is present in a trust store. (15)

**RSA.** A public-key algorithm based on the difficulty of factoring, used for signatures and encryption. (7)

**SAN.** Subject Alternative Name: the certificate extension listing the names a certificate is valid for. (15)

**Secret.** Any value granting access if disclosed: passwords, API keys, tokens, private keys. (22)

**Shor's and Grover's algorithms.** Quantum algorithms that respectively break RSA and elliptic curve cryptography, and modestly speed up brute-force search. (25)

**Side-channel attack.** An attack that learns secrets from timing, power use, cache behaviour or other physical effects of computation. (4, 9)

**SLH-DSA.** Stateless Hash-Based Digital Signature Algorithm, FIPS 205. (26)

**SPIFFE.** A standard for workload identity, issuing short-lived certificates or tokens to workloads after attestation. (22)

**Symmetric cryptography.** Cryptography where the same secret key is used by both parties. (1)

**Threat model.** A description of what is protected, from whom, with what capabilities, and for how long. (1, 24)

**TLS.** Transport Layer Security, the protocol that secures most internet connections. (11, 12)

**TPM.** Trusted Platform Module: a security chip in computers providing protected keys, measured boot and attestation. (23)

**Trust store.** The set of root certificates a client trusts. (15)

**X.509.** The standard format for public-key certificates. (15)

**X25519.** Diffie-Hellman key exchange on Curve25519, the default classical key exchange in modern protocols. (8)

**Zero-knowledge proof.** A proof that a statement is true which reveals nothing else. (28)
