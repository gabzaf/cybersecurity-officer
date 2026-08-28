# 02 — Frameworks: CIS, COBIT, ISO/IEC, NIST, QNRCS

**Keywords:** CIS Controls v8 · COBIT 2019 · EGIT · ISO/IEC 27001 · ISMS / SGSI · ISO 27002 · ISO 27005 · NIST CSF · NIST 800-53 · QNRCS · CiberCheckup · GRC · control mapping

A Security Officer who only knows the law cannot implement. A Security Officer who only knows a framework cannot defend it to CNCS. I treat frameworks as **implementation languages** for DL 65/2021 and NIS2.

---

## How I choose

| Framework | I reach for it when… | Weakness I admit |
| --- | --- | --- |
| **CIS Controls v8** | I need a **prioritised, actionable** list that ops can execute this quarter. Easier to implement than COBIT. | Does not, by itself, give you an ISMS or a Portuguese legal mapping. |
| **COBIT 2019** | The conversation is **governance vs management**, board reporting, value from IT. More flexible, heavier. | Easy to drown in the Core Model if you have no design factors. |
| **ISO/IEC 27001:2022** | The organisation wants a **certifiable SGSI**, sales/trust, or a SoA. Most popular in companies. | Certificate ≠ security. Annex A without risk is cargo cult. |
| **NIST CSF** | I need a **common language** (Identify / Protect / Detect / Respond / Recover / Govern) that maps onto ISO, CIS, QNRCS. | US origin; in PT I still hang legal duties on DL 65/2021. |
| **QNRCS** | I am in **Portugal**, talking to CNCS, public sector, OES-shaped entities, or a certification scheme. | National reference — complement it with ISO/CIS for technical depth. |

My class note: *“É mais fácil implementar o CIS que o COBIT. Mas o COBIT é mais flexível. A ISO 27001 é a mais popular entre empresas.”*

---

## CIS Critical Security Controls v8 — 18 controls

CSC v8 is a set of **safeguards** against prevalent attacks. It does not grant immunity. v8 organises by **activity**, not by who owns the device.

| CSC | Control | Why a Security Officer cares |
| --- | --- | --- |
| 1 | Inventory and Control of Enterprise Assets | You cannot protect what you cannot list. RMM / discovery. Maps to DL Art. 6. |
| 2 | Inventory and Control of Software Assets | Allow-list authorised software; no shadow binaries. |
| 3 | Data Protection | Classify, retain, dispose. Data is the asset attackers actually want. |
| 4 | Secure Configuration | Defaults, open ports, default admin passwords. Hardening baselines. |
| 5 | Account Management | Lifecycle of accounts; MFA; no orphan accounts. |
| 6 | Access Control Management | Least privilege, RBAC/ABAC. Limits blast radius after compromise. |
| 7 | Continuous Vulnerability Management | Scan, prioritise, patch. SIEM / MDR sits next to this. |
| 8 | Audit Log Management | Logs that a SIEM can actually use. |
| 9 | Email and Web Browser Protections | DMARC/SPF/DKIM, DNS filtering, browser restriction. |
| 10 | Malware Defenses | AV, EDR, XDR, IDS, MDR. |
| 11 | Data Recovery | Tested backups, RTO/RPO. Ransomware reality. |
| 12 | Network Infrastructure Management | Know the network you claim to defend. |
| 13 | Network Monitoring and Defense | Detect east-west and north-south abuse. |
| 14 | Security Awareness and Skills Training | Humans as control, not just as liability. |
| 15 | Service Provider Management | Third-party / supply-chain — NIS2 Art. 21 territory. |
| 16 | Application Software Security | SSDLC, SAST/DAST. |
| 17 | Incident Response Management | IRP, roles, comms. Maps to DL Arts. 11–17. |
| 18 | Penetration Testing | White / grey / black box. Evidence for audit, not a trophy. |

Implementation IG1 / IG2 / IG3 (Implementation Groups) is how I would phase this in a small vs essential entity.

---

## COBIT 2019 — governance of information and technology

ISACA’s COBIT is **EGIT**: enterprise governance of information and technology. Expected outcomes: **benefits realisation, risk optimisation, resource optimisation**.

**Governance system principles:** provide stakeholder value; holistic approach; dynamic system; **governance distinct from management**; tailored to the enterprise; end-to-end.

**Governance ≠ management**

- Governance: evaluate stakeholder needs, set direction, monitor performance and compliance. Domain **EDM** (Evaluate, Direct, Monitor).  
- Management: plan, build, run, monitor. Domains **APO, BAI, DSS, MEA**.

I use this split when a board asks “who owns cyber?” The Security Officer **manages**; the board **governs**. NIS2 Art. 20 is the legal version of that sentence.

---

## ISO/IEC 27001 — SGSI / ISMS

27001 is the requirements standard to **establish, implement, maintain and improve** an information security management system. The family I actually cite:

| Standard | Role |
| --- | --- |
| 27001 | Requirements (certifiable) |
| 27002 | Control catalogue / code of practice |
| 27003 | Implementation guidance |
| 27004 | Measurement |
| 27005 | **Information security risk management** (pairs with [module 3](../03-analise-risco/README.md) and [MONARC](../04-monarc/README.md)) |
| 27006 / 27007 | Certification bodies and auditors |

Why organisations pick it: size-agnostic, short, certifiable, huge ecosystem. Why I push back: a certificate without Art. 10 risk analysis is a sticker.

---

## NIST Cybersecurity Framework

Functions (CSF 2.0 adds **Govern**):

**Govern · Identify · Protect · Detect · Respond · Recover**

Same backbone as **QNRCS** security objectives. I use CSF as the slide that non-specialists understand, then hang Portuguese articles and ISO controls under each function.

Mapped widely to ISO 27001, COBIT, CIS. Tiers (Partial → Risk Informed → Repeatable → Adaptive) are useful when leadership asks “how mature are we?” without buying a full CMMI programme.

---

## QNRCS (national)

The **Quadro Nacional de Referência para a Cibersegurança** is Portugal’s reference model. Objectives match CSF: Identify (assets, context, governance, risk, supply chain), Protect, Detect, Respond, Recover.

CNCS **CiberCheckup** (https://cibercheckup.cncs.gov.pt/) is the questionnaire I used in the exercise to baseline posture and then argue **financial impact** of raising maturity: reduced annualised loss expectancy, fewer downtime hours, insurance and fine avoidance, enablement of contracts in regulated sectors. Cyber as value driver, not only cost centre.

---

## Interview line

“I do not implement a framework for its logo. I map **DL 65/2021 duties** to **QNRCS functions**, pick **CIS** for the first control backlog, keep an **ISO 27001** ISMS if the organisation needs a SoA or a certificate, and use **COBIT** when I am talking to the board about governance versus management.”
