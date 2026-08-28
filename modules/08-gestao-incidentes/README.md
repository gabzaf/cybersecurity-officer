# 08 — Cybersecurity incident management

**Keywords:** incident response · CSIRT · SOC · IRP · NIST SP 800-61 · Lei 46/2018 · DL 65/2021 Arts. 11–17 · notification · CNCS · personal data breach · GDPR Arts. 33–34 · containment · eradication · lessons learned

Incident management is procedures and responsibilities aligned to the **lifecycle of an incident**. Frameworks disagree on stage names; they agree you must have a named cycle **before** the ransomware.

---

## Legal frame (Portugal)

**Lei 46/2018 (RJSC)** — duty to notify incidents that affect network and information security, according to the legal regime.

**DL 65/2021 Arts. 11–17** — how notification works in practice (what, when, to whom, follow-up). **Regulamento 183/2022** — the channel and forms toward CNCS.

The **Ponto de Contacto Permanente** is the operational pipe. The **Responsável de Segurança** owns the process quality and the post-incident paper.

If personal data is involved: **CNPD + GDPR Arts. 33/34** in parallel. One incident, two authorities, two clocks. I never let “we told CNCS” substitute for a personal-data breach assessment.

---

## Lifecycle I can run

I am fluent in both common vocabularies:

**NIST SP 800-61-style:** preparation → detection & analysis → containment → eradication → recovery → post-incident activity.

**PICERL-style:** Preparation, Identification, Containment, Eradication, Recovery, Lessons learned.

Preparation is the only stage you can still do on a quiet day: IRP, contact lists, evidence handling, logging, tabletop, retainers.

---

## What must exist on a normal Tuesday

- Incident **classification** (severity / impact on essential service, data, reputation)  
- On-call / PCP activation  
- **Register** of incidents (tickets are not a register if nobody can report from them)  
- Decision tree: notify CNCS? notify CNPD? notify customers? law enforcement?  
- Containment patterns that do not destroy forensic value when you still need it  
- Comms: internal, CNCS, regulators, media — pre-approved stubs  
- After-action that **changes** the risk register and the security plan  

---

## Interview line

“Incident response is a legal duty with a clock, not a hero moment. I care about preparation, a severity model, dual CNCS/CNPD notification when data is in play, and a lessons-learned loop back into Art. 10.”
