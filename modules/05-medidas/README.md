# 05 — Technical and organisational measures

**Keywords:** TOMs · technical and organisational measures · Art. 9 DL 65/2021 · GDPR Art. 32 · CNPD · defense in depth · MFA · encryption · backup · firewall · awareness · QNRCS · CIA

Measures are how residual risk becomes a number leadership can live with. The law’s word is **adequate and proportional** to the risk of the networks and information systems you operate — not “best in class everywhere”.

---

## What the measures must cover

I keep this checklist (NIS-era, still the right conversation):

- Security of systems and facilities  
- Incident handling  
- Business continuity  
- Monitoring, audit and testing  
- Compliance with standards  

Organisational risk flavours: **operational, regulatory, financial, reputational**.

Adequacy depends on volume of data, scale of processing, and nature of the data (GDPR Art. 32 logic walks in even when the hat is “cyber”).

---

## Organisational (people, process, paper)

From the CNPD-style list I studied — this is also how I brief HR and legal:

- Incident response and disaster recovery **plan** (not a poster)  
- Information classification by confidentiality  
- **Documented security policies** (PSI and children)  
- Traffic-monitoring procedures  
- Password policy and **user lifecycle** (joiner/mover/leaver, least privilege)  
- Alerting on abuse / failed access  
- Privacy by design, pseudonymisation / anonymisation where it earns its keep  
- IT security audits and vulnerability assessments  
- Re-verify controls when circumstances change  
- Document and fix vulns  
- Personal-data breach playbook  
- Privacy / security culture and confidentiality duty  
- Periodic review of TOMs  

---

## Technical

| Layer | Examples I can specify |
| --- | --- |
| Authentication | Long unique passwords, MFA, privileged access management |
| Infrastructure | Patched OS and firmware, **segmentation**, hardened workstations and servers |
| Email | DLP-minded rules, encryption, delayed send, anti-phishing / anti-spam, DMARC |
| Malware | EDR, backup that restores, encryption at rest |
| Off-site / mobile | VPN, lockout, MFA, disk encryption, remote wipe, automatic backups, acceptable-use rules |
| Data in transit | Encryption |

Defense in depth: no single control is the control.

---

## Map onto QNRCS / NIST CSF

| Function | Examples |
| --- | --- |
| **Identify** | Asset mgmt, context, governance, risk, supply chain |
| **Protect** | IAM, awareness, data security, protective processes, maintenance, protective tech |
| **Detect** | Anomalies, continuous monitoring, detection processes |
| **Respond** | Planning, communications, analysis, mitigation, improvements |
| **Recover** | Recovery plan, improvements, communications |

Legal hooks: RJSC Lei 46/2018 (duties and incident regime) + DL 65/2021 Art. 9.

---

## Interview line

“Measures are the output of Art. 10, not a shopping list. I pick TOMs from QNRCS / ISO 27002 against residual risk, then I can show a CNPD or CNCS auditor *why this control exists*.”

---

← [04 MONARC](../04-monarc/README.md) · [Index](../../README.md#modules) · [06 Audit & monitoring](../06-auditoria/README.md) →
