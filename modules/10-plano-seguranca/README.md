# 10 — Security plan (Plano de Segurança)

**Keywords:** plano de segurança · DL 65/2021 Art. 7 · BCP · DR · RTO · RPO · CSIRT · SOC · vulnerability SLA · awareness · IAM · security roadmap

Art. 7 is the document the Security Officer **signs**. It is not the PSI. The PSI says *what we believe*. The plan says *what we are doing this period, who owns it, and how we survive an incident*.

---

## What Art. 7 is for

Implement the policy: organisational measures, people (training), technical controls, incident handling, continuity — calibrated to the Art. 10 risk analysis. Regulamento 183/2022 tells you how this talks to CNCS when required.

If the risk register says “MFA on the internet-facing app, Q3, owner X” and the plan does not, the plan is fiction.

---

## Skeleton I use

1. **Normative frame** — PSI version, DL 65/2021 Art. 7, ISO 27001 controls, any sector overlay.  
2. **Organisational measures** — IRP, CSIRT/SOC model, vulnerability SLAs (e.g. critical / high / medium clocks), notification to CNCS, BCP/DR with **RTO/RPO**, HR joiner-leaver, disciplinary path.  
3. **Awareness and specialist training** — phishing programme with a metric, funded certs for the people who actually operate controls.  
4. **Named roles** — Security Officer, PCP, system owners, DPO. Contacts that work at 02:00.  
5. **Technical programme** — the backlog for this cycle (hardening, backup immutability, segmentation, MFA, logging).  
6. **Tests** — restore tests, tabletop, failover — dated.  
7. **Review** — after incidents, after audit, annually.

---

## Numbers I insist on being real

- **RTO / RPO** per critical service, not a single corporate fantasy.  
- Vulnerability remediation SLAs that match staffing.  
- Notification targets that match the legal clock, not “as soon as possible”.  
- Backup: tested restore beats “we have backups” every time.

---

## Training exercise

I practised a plan that tied IR to NIST 800-61, SOC 24/7, dual-cloud failover thinking, IAM offboarding, and a named CISO + PCP. The useful lesson: a plan without **owners and dates** is a brochure.

---

## Interview line

“The security plan is the yearly (or cycle) contract between residual risk and budget. I write it so Art. 7, the risk register, and next year’s annual report tell the same story.”
