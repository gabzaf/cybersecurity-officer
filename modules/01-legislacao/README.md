# 01 — Legislation applicable to cybersecurity

**Keywords:** RJC · DL 125/2025 · Regulamento 756/2026 · MyCiber · RJSC · Lei 46/2018 · DL 65/2021 · Regulamento 183/2022 · NIS · NIS2 · SRI2 · CNCS · Responsável de Segurança · Ponto de Contacto Permanente · entidades essenciais · entidades importantes · RGPD · DORA · CER

This is the spine. Every later module is one of the duties created here.

The training (May 2025) was taught on **Lei 46/2018 + DL 65/2021**. Those texts are how I first learned the operating model. They are no longer the whole story.

---

## Current law

| Date | Instrument | Meaning |
| --- | --- | --- |
| 4 Dec 2025 | **Decreto-Lei 125/2025** | Transposes **NIS2**. New **Regime Jurídico da Cibersegurança (RJC)**. |
| 3 Apr 2026 | DL 125/2025 **in force** | Replaces the NIS1-era RJSC as the main national regime. |
| 4 May 2026 | First clock | Essential and important entities to notify CNCS of the **Responsável pela cibersegurança** and the **Ponto de Contacto Permanente**. |
| Jun 2026 | **Regulamento 756/2026** | CNCS implementing rules: **MyCiber** platform, operationalisation of QNRCS against the new RJC. |
| +60 days after MyCiber is available | Self-identification | Entities register / self-identify on the CNCS platform. |

**What changed in the job, not just the gazette**

- Scope jumps: NIS1-style operators → **essential**, **important**, and **relevant public** entities (thousands more organisations, including medium enterprises in listed sectors).
- Same two named functions, now under the new diploma: Security Officer + 24/7-capable PCP.
- **Management liability** is no longer a “NIS2 will bring this” talking point — it is in force.
- QNRCS is explicitly the national control reference next to NIST CSF 2.0, ISO 27001/27002, CIS Controls.
- Fines at NIS2 / GDPR scale (up to the order of €10M or a percentage of worldwide turnover, plus possible disqualification of directors in serious cases).

I still walk through DL 65/2021 Arts. 4–17 below because that is the **anatomy** I trained on (inventory, plan, annual report, incident clocks). In production I would re-cite the equivalent duties in **DL 125/2025 + Reg. 756/2026**, not pretend the 2021 article numbers are still the ones on the form.

---

## Timeline I keep in my head (how we got here)

| Year | Instrument | What it does |
| --- | --- | --- |
| 2016 | Directive (EU) 2016/1148 — **NIS / SRI** | Common EU level of network and information security. National strategy, CSIRT network, security + incident duties for OES and DSP. |
| 2018 | Commission Implementing Reg. 2018/151 | How to execute NIS. |
| 2018 | **Lei 46/2018 — RJSC** | Transposes NIS into Portuguese law. Creates the cyberspace security structure (Conselho Superior, **CNCS**, national CSIRT). Material scope: public administration, critical infrastructure operators, operators of essential services, digital service providers, other entities using networks and information systems. **Out of scope:** EMGFA C2 networks; classified information systems. |
| 2021 | **Decreto-Lei 65/2021** | Operationalises RJSC: security requirements and incident notification rules. This is the text a Security Officer lives in. |
| 2022 | **Regulamento 183/2022 (GNS)** | Technical instruction for how entities talk to CNCS (forms, structure of inventory, annual report, contacts). |
| 2022 | Directive (EU) 2022/2555 — **NIS2 / SRI2** | Replaces the OES/DSP split with **essential** vs **important** entities. Harder supervision, GDPR-scale fines, supply-chain security, **management liability** (Art. 20). Companion files: CER/REC (critical entities) and **DORA** (financial digital operational resilience). |

Directive vs regulation vs law (question I wrote down in class): a **directive** must be transposed; a **regulation** applies directly; **RJSC + DL 65/2021** were how Portugal made NIS1 operational. **DL 125/2025** is the NIS2 transposition — I do not quote 2018/2021 as if they were still the live regime.

---

## The two named functions (DL 65/2021)

### Ponto de Contacto Permanente — Art. 4

Operational/technical channel with CNCS. It is a **function**, not a person: one or more people or a department, **24/7 during activation**. Notify CNCS within 20 working days of starting activity, and immediately on any change. Must be able to route authority requests inside the organisation.

### Responsável de Segurança — Art. 5

The Security Officer / CISO-shaped role this training is named after. Manages security requirements and incident notification. **Signs** the asset inventory, the security plan and the annual report. Should report to top management, know both business and tech, turn entity objectives into information-security requirements and keep the PCP actually usable.

Responsibilities I list in interviews:

1. Information security strategy
2. Conformity with **RJC** (formerly RJSC) and **RGPD**
3. Good practice — **QNRCS**, **ISO/IEC 27001**
4. Define requirements and measures
5. Policies, processes, procedures
6. Legal literacy 
7. Risk management
8. Change and incident management
9. Follow audits
10. Application-system strategy
11. Cyber awareness

---

## Obligations the later modules unpack

| Duty | Article | Module |
| --- | --- | --- |
| Permanent contact point | Art. 4 | this one |
| Security Officer | Art. 5 | this one |
| Asset inventory | Art. 6 | [07](../07-inventario-ativos/README.md) |
| Security plan | Art. 7 | [10](../10-plano-seguranca/README.md) |
| Annual report | Art. 8 | [11](../11-relatorio-anual/README.md) |
| Technical and organisational measures | Art. 9 | [05](../05-medidas/README.md) |
| Risk analysis of all relevant assets | Art. 10 | [03](../03-analise-risco/README.md) |
| Incident notification | Arts. 11–17 | [08](../08-gestao-incidentes/README.md) |

Original RJSC rollout dates I memorised: PCP + Security Officer + security plan + incident duty from Dec 2021; annual report + inventory from Jan 2022; risk analysis and measures from Aug 2022. Those clocks mattered for first-wave entities. DL 125/2025 has since reset the map (see **Current law** above).

Micro and small digital service providers were carved out of some NIS-era duties (micro: <10 people / <€2M; small: <50 / <€10M). NIS2 **narrows** those carve-outs — I do not quote 2018 thresholds as if they were still the whole story.

---

## NIS2 / RJC

- Drop OES vs DSP. Use **essential** vs **important** (plus Portugal’s **relevant public entities**). Same core duties, different supervisory intensity.
- **Governance:** management bodies can be held to account for non-compliance. Security is no longer a side-of-desk IT topic.  
- Risk-management measures include supply chain, cryptography, HR security, incident handling, business continuity.  
- Incident reporting with an early warning and follow-up (plus MyCiber as the national channel).  
- Fines designed to hurt at **GDPR scale**.  
- Overlap with **RGPD Art. 33/34** if personal data is involved — one incident, two clocks, two authorities (CNCS and CNPD).

---

## RGPD (short, because it always walks into the room)

Processing must satisfy the six principles (lawfulness, fairness, transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality) plus accountability.

**Consent ≠ terms and conditions.** That was a note I wrote on day one. If the legal basis is consent, it has to be specific, informed, unambiguous and withdrawable. Stuffing it into T&Cs is how you fail a CNPD conversation.

Cyber incident with personal data: technical and organisational measures (GDPR Art. 32) and breach notification sit next to RJSC notification, not instead of it.

---

[Index](../../README.md#modules) · [02 Frameworks](../02-frameworks/README.md) →
