# 04 — MONARC

**Keywords:** MONARC · risk treatment · ISO 27005 · EBIOS · MOSP · MISP · CASES Luxembourg · asset modelling · risk register · SOA

MONARC is the tool I used to **treat** risk, not only describe it. Methodical Operational Risk Analysis — originally from CASES / NC3 Luxembourg, aligned with a qualitative operational-risk method (EBIOS-family) and usable as the engine behind an ISO 27005 process.

---

## Why a Security Officer uses a tool here

Art. 10 says: document preparation, execution and results, then adopt measures. A slide deck does not survive audit. MONARC gives:

- a **model of the organisation** (instances of assets, links, supporting assets)  
- **threats and vulnerabilities** tied to those assets  
- **risks** with CIA impact and likelihood  
- **recommendations / measures** and residual risk after treatment  
- an exportable **risk analysis** you can attach to the security plan and the annual report  

I also saw the training path: import preventive measures from **MISP** via **MOSP**, generate galaxies, map **ISO/IEC 27002:2022** controls. That is how you stop inventing a private control language.

---

## How I think in MONARC

1. **Context** — what is in scope (the Gestão platform, not “the whole company” on day one).  
2. **Assets** — primary (processes, information) vs supporting (netPA, Oracle, server, people, premises).  
3. **Impact** — C / I / A scores if this asset fails.  
4. **Threats × vulns** — operational scenarios, not CVE tourism.  
5. **Risk** — which scenarios actually move the needle.  
6. **Treatment** — select measures, owners, due dates; recompute residual.  
7. **Report** — something a non-specialist director can sign.

That is the same five-phase process as [module 3](../03-analise-risco/README.md), with a database behind it.

---

## What I would not do

- Run MONARC once, export PDF, never reopen it.  
- Model only IT gadgets and forget processes and suppliers.  
- Treat “we have antivirus” as a measure that drives residual risk to zero.  
- Confuse the **lab OVA** with a production deployment (GDPR of the risk register itself).

---

## Interview line

“I can run a qualitative operational risk analysis in MONARC, map treatments to ISO 27002, and leave an Art. 10 trail. The method matters more than the product — if the organisation uses another ISO 27005 tool, I transfer the same model.”

---

← [03 Risk analysis](../03-analise-risco/README.md) · [Index](../../README.md#modules) · [05 Technical & organisational measures](../05-medidas/README.md) →
