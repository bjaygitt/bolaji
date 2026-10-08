---
num: C
title: Command Reference
part: 8
lead: The commands used most often in this book's labs and in daily practice, grouped by task. Commands use OpenSSL 3.5 or later unless stated. Replace file names and hosts with your own.
---

## C.1 Inspecting certificates and connections

| Task | Command |
| --- | --- |
| Show a server's certificate chain | `openssl s_client -connect host:443 -servername host -showcerts` (press Ctrl+D to close) |
| Read a certificate | `openssl x509 -in cert.pem -noout -text` |
| Show expiry dates | `openssl x509 -in cert.pem -noout -dates` |
| Show names (SAN) | `openssl x509 -in cert.pem -noout -ext subjectAltName` |
| Fingerprint | `openssl x509 -in cert.pem -noout -fingerprint -sha256` |
| Verify a chain | `openssl verify -CAfile root.pem -untrusted intermediate.pem leaf.pem` |
| Check key and certificate match | Compare `openssl x509 -in cert.pem -noout -pubkey` with `openssl pkey -in key.pem -pubout`; they must be identical |
| Test a specific TLS version | `openssl s_client -connect host:443 -tls1_2` or `-tls1_3` |
| Request post-quantum key exchange | `openssl s_client -connect host:443 -groups X25519MLKEM768` |
| Scan a server | `testssl.sh https://host` |

## C.2 Keys and requests

| Task | Command |
| --- | --- |
| EC P-256 key | `openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out key.pem` |
| Ed25519 key | `openssl genpkey -algorithm ED25519 -out key.pem` |
| RSA 3072 key | `openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out key.pem` |
| ML-DSA-65 key | `openssl genpkey -algorithm ML-DSA-65 -out key.pem` |
| ML-KEM-768 key | `openssl genpkey -algorithm ML-KEM-768 -out key.pem` |
| Public key from private | `openssl pkey -in key.pem -pubout -out pub.pem` |
| CSR with SANs | `openssl req -new -key key.pem -out req.csr -subj "/CN=host" -addext "subjectAltName=DNS:host"` |
| Read a CSR | `openssl req -in req.csr -noout -text -verify` |
| Self-signed certificate | `openssl req -x509 -new -key key.pem -days 30 -subj "/CN=test" -out cert.pem` |

## C.3 Formats

| Task | Command |
| --- | --- |
| PEM to DER | `openssl x509 -in cert.pem -outform DER -out cert.der` |
| DER to PEM | `openssl x509 -in cert.der -inform DER -out cert.pem` |
| Create PKCS#12 | `openssl pkcs12 -export -inkey key.pem -in cert.pem -certfile chain.pem -out bundle.p12` |
| Extract from PKCS#12 | `openssl pkcs12 -in bundle.p12 -nodes -out all.pem` |
| Read a CRL | `openssl crl -in ca.crl -inform DER -noout -text` |

## C.4 Encryption, hashing and signing

| Task | Command |
| --- | --- |
| SHA-256 of a file | `openssl dgst -sha256 file` |
| HMAC-SHA256 | `openssl dgst -sha256 -hmac "secret" file` |
| Random bytes | `openssl rand -hex 32` |
| Sign (Ed25519 or ML-DSA) | `openssl pkeyutl -sign -inkey key.pem -rawin -in file -out file.sig` |
| Verify | `openssl pkeyutl -verify -inkey pub.pem -pubin -rawin -in file -sigfile file.sig` |
| Sign with RSA-PSS | `openssl dgst -sha256 -sigopt rsa_padding_mode:pss -sign key.pem -out sig file` |
| Benchmark | `openssl speed -evp aes-256-gcm` |

## C.5 SSH

| Task | Command |
| --- | --- |
| Ed25519 user key | `ssh-keygen -t ed25519 -f id_ed25519` |
| Create a CA | `ssh-keygen -t ed25519 -f user_ca` |
| Sign a user certificate for 8 hours | `ssh-keygen -s user_ca -I alice -n alice -V +8h id_ed25519.pub` |
| Inspect a certificate | `ssh-keygen -L -f id_ed25519-cert.pub` |
| See negotiated key exchange | `ssh -v host`, then look for the line starting "kex: algorithm" |

## C.6 DNS and the web PKI

| Task | Command |
| --- | --- |
| CAA records | `dig +short CAA example.com` |
| HTTPS record (ECH config) | `dig +short HTTPS example.com` |
| Certificates for a domain in CT | Search `https://crt.sh/?q=example.com` |
| HSTS header | `curl -sI https://example.com`, then look for Strict-Transport-Security |
