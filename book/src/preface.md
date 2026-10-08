Cryptography quietly holds the digital world together. It protects every login, card payment, software update, private message and backup. Yet most engineers learn it in fragments: a TLS setting here, a certificate renewal there, an audit question about key storage that nobody can quite answer. The fragments rarely connect, and the gaps between them are where outages and breaches happen.

This book connects the fragments. It is written for engineers, architects and security professionals who want to understand cryptography deeply enough to make good decisions, explain them clearly, and run cryptographic systems safely at scale.

## Who this book is for

You do not need a mathematics degree. You do need curiosity and a willingness to work through examples. If you can read a little code and use a command line, you can complete every lab. Readers who already work with certificates, keys or secrets will find the later parts immediately useful, and the early parts will fill gaps they may not know they have.

## How the book is organised

The book follows the order in which the ideas depend on each other.

- **Part I, Foundations,** explains what cryptography is for, the mathematics behind it, and the randomness it depends on.
- **Part II, Symmetric Cryptography,** covers block ciphers, authenticated encryption, hashing, MACs and key derivation.
- **Part III, Public-Key Cryptography,** covers RSA, Diffie-Hellman, elliptic curves, digital signatures and how security is proved.
- **Part IV, Protocols,** shows how these pieces become TLS, SSH, VPNs, secure messaging and identity systems.
- **Part V, Certificates and PKI,** explains certificates, the web's trust system, revocation, private CAs and lifecycle automation.
- **Part VI, Keys, Secrets and Hardware,** covers key management, key management services, secrets, HSMs and system architecture.
- **Part VII, The Post-Quantum Transition,** explains the quantum threat, the new standards, and how to migrate.
- **Part VIII, Frontiers and Reference,** surveys advanced techniques and provides a glossary and reading guide.

## How each chapter works

Every chapter opens with what you will be able to do by the end, and every term is defined in plain words where it first appears. Throughout the text you will find three kinds of highlighted box:

| Box | What it contains |
| --- | --- |
| **In practice** | How the idea shows up in real systems, and what to check in your own environment |
| **Current development** | Recent changes to standards, browser policies or regulations, current to October 2026 |
| **Watch out** | Common mistakes that cause outages or breaches |

Most chapters end with a hands-on lab using free tools, a failure story drawn from a real, publicly documented incident, a summary, and review questions. Do the labs. Cryptography becomes intuitive only when you have broken a toy system with your own hands.

## A note on currency

Cryptographic practice is changing faster now than at any time in the last twenty years. Public certificate lifetimes are shrinking toward 47 days. Browsers already use post-quantum key exchange for most connections. Governments have published deadlines for retiring RSA and elliptic-curve cryptography. Where this book cites a date, policy or statistic, it reflects the public record as of October 2026. Always check the primary source before relying on a date for a decision.

## Acknowledgements

This book stands on the work of the researchers, standards bodies and open-source maintainers whose publications, specifications and incident reports are cited throughout. Any errors are mine.

Bolaji Akinyele
