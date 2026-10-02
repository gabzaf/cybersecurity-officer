# 09 — Information Security Policy (PSI)

**Keywords:** PSI · information security policy · SGSI · ISO 27001 clause 5 · acceptable use · least privilege · Zero Trust · management commitment · CISO · DPO · policy hierarchy

The PSI is the **parent document**. Everything else (AUP, password standard, IRP, supplier policy) hangs under it. Without a signed PSI, “we have security” is folklore.

ISO 27001 expects leadership to establish a policy aligned with the organisation’s purpose. In Portugal, the PSI is also how you show Art. 9 “organisational measures” and feed the [security plan](../10-plano-seguranca/README.md).

---

## What I put in a PSI (structure I would defend)

1. **Purpose and scope** — who, which systems (on-prem, cloud, endpoints, partners), full information lifecycle.  
2. **Strategic alignment** — SGSI (ISO 27001), functions (NIST CSF / QNRCS), measurable objectives.  
3. **Principles** — least privilege, defense in depth, security by design, Zero Trust where it is honest (verify explicitly, never assume LAN = trusted).  
4. **Governance** — board approves; Security Officer / CISO implements and reports; DPO for personal data; business owners for their assets.  
5. **Policy family** — list of child documents (access, email, remote access, cryptography, logging, IR, suppliers, disposal…).  
6. **People** — awareness, acceptable use, disciplinary path.  
7. **Review cycle** — on incident, on legal change (NIS2), at least annually.  
8. **Management commitment** — a one-page “compromisso” leadership actually signs, not only the 40-page annex.

---

## Child policies I expect to exist

Acceptable use · access control / IAM · password and authenticator · email · remote access · server / workstation hardening · logging · cryptography and key handling · supplier / acquisition · incident response (identification, containment, recovery, chain of custody) · data disposal.

I studied a large set of templates so I can **draft**, not so I paste SANS PDFs into a Portuguese public body.

---

## Training exercise (what I practised)

I structured a PSI for a fictional company (TechSolutions): ISO 27001:2022 SGSI, NIST CSF functions, GDPR privacy-by-design, phishing reduction with DMARC/SPF/DKIM, 99.9% availability target for critical systems, SIEM monitoring, pentest against OWASP Top 10, CISO reporting to CEO, DPO as authority contact. The point of the exercise was **traceability**: every objective has an owner and a control, not a slogan.

---

## Interview line

“A PSI is leadership’s security contract with the organisation. I write it short enough to be read, hang child standards under it, and I will not call it ‘implemented’ until joiner/leaver and incident processes match the text.”

---

← [08 Incident management](../08-gestao-incidentes/README.md) · [Index](../../README.md#modules) · [10 Security plan](../10-plano-seguranca/README.md) →
