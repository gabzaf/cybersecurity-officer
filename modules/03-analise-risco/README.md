# 03 — Risk analysis and management

**Keywords:** risk assessment · risk treatment · ISO 27005 · ISO 27000 · CIA · threat · vulnerability · asset · impact · likelihood · risk matrix · risk acceptance · residual risk · DL 65/2021 Art. 10 · MONARC

This is the module that turns the Security Officer from a policy writer into someone who can **justify spend**.

---

## Vocabulary I use precisely

| Term | Meaning I will defend |
| --- | --- |
| **Asset** | Anything of value to the entity. Under DL 65/2021, the in-scope set is networks, information systems, equipment and other essential physical and logical resources that support services, directly or indirectly. |
| **Threat** | Potential cause of an unwanted incident. Threat **agents** want to harm assets. |
| **Vulnerability** | Weakness that a threat can exploit. |
| **Control / measure** | Technical or organisational means to reduce risk. Controls can themselves be vulnerable. |
| **Event / incident** | Event = something happened. Incident = impact on CIA of information or services. |
| **Risk** | Combination of **likelihood** and **impact** of a threat exploiting a vulnerability against an asset. |
| **CIA / CID** | Confidentiality, integrity, availability. |

Stakeholders want to protect **assets**, impose **controls**, and still live with **residual risk**. Attackers hunt **vulnerabilities**. That loop is the whole job.

---

## Why the law forces this (DL 65/2021)

- **Art. 9** — public administration, critical infrastructure operators and operators of essential services must implement technical and organisational measures **adequate to the risk**, based on a risk analysis.  
- **Art. 10** — analyse risk of **all** relevant assets; **document** preparation, execution and results; after each analysis, adopt adequate measures.

Risk analysis is not a workshop you do once for ISO. It is a **documented, repeating legal duty**.

---

## Process I follow (ISO 27005-shaped)

1. **Establish context** — scope, criteria, risk appetite, roles.  
2. **Risk identification** — assets, threats, existing controls, vulnerabilities.  
3. **Risk analysis** — likelihood × impact.  
4. **Risk evaluation** — compare against criteria / matrix; what is acceptable.  
5. **Risk treatment** — mitigate, avoid, transfer, accept. This is where I used **[MONARC](../04-monarc/README.md)**.  
6. **Communication and consultation** — business owners, board, PCP.  
7. **Monitor and review** — new assets, new threats, control failures, incidents.

If it is not documented, it did not happen for Art. 10.

---

## Worked exercise (training)

**Entity:** C-Academy. **Role:** Joana Silva, Security Officer.  
**Trigger:** vulnerabilities on the Gestão platform — need an Art. 10 analysis.

**System:** internet-facing web app. Auth = username + password (already a finding). Components: application **netPA**, **Oracle** database, **physical server**.

The entity already had: asset criticality, threat ID, vulnerability ID, analysis, risk matrix, acceptance criteria.

What I would do next, in order:

1. Scope the asset and its data (CIA needs, users, internet exposure).  
2. Identify threats: credential stuffing, SQLi, ransomware on the host, insider, supply chain on netPA.  
3. Identify vulns: single-factor auth, patch level, backup, network exposure.  
4. Score inherent risk; apply existing controls; score residual.  
5. Treat: MFA, WAF, hardening, backup restore test, vendor SLA — record in MONARC / the register.  
6. Feed residual risk into the **security plan** and the **PSI** so this is not a spreadsheet orphan.

---

## Interview line

“Risk is not a colour on a heatmap. It is Art. 10 evidence: scoped assets, named threats, documented treatment, residual risk accepted by someone who is allowed to accept it.”
