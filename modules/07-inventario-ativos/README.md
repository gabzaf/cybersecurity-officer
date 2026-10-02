# 07 — Asset inventory

**Keywords:** asset inventory · critical asset · CMDB · DL 65/2021 Art. 6 · Regulamento 183/2022 · QNRCS ID.GA · ID.AO · asset owner · classification · internet-facing assets

An **asset** is anything of value to the organisation. A **critical asset** is one that supports at least one essential service.

People, organisational processes, information and facilities are assets in the ISO sense. They are **not** all in the DL 65/2021 inventory scope — the legal inventory is about networks, systems, equipment and essential physical/logical resources that support services.

---

## QNRCS Identify (asset management)

| ID | Expectation |
| --- | --- |
| ID.GA-1 | Inventory physical, network and information-system devices; classify by relevance |
| ID.GA-2 | Applications and software platforms that support critical services |
| ID.GA-3 | Communication networks and data-flow mapping |
| ID.GA-4 | Networks and systems **outside** the organisation’s premises (cloud, colo, home, suppliers) |
| ID.GA-5 | Assets needed to deliver goods and services |
| ID.AO-4 | Critical assets identified and recorded |

---

## Two inventories, one signature

This distinction is the one I got wrong until module 11, then wrote down:

1. **Internal inventory** — everything you need to operate and to run Art. 10 risk analysis (including supporting assets that are not on the public internet).  
2. **CNCS-facing inventory (Art. 6 + Reg. 183/2022)** — not “every laptop”. The list of assets **directly reachable from the public internet**, structured as the instruction requires, **signed by the Responsável de Segurança**.

Confusing the two either over-discloses junk or under-reports the attack surface CNCS actually cares about.

Each asset needs an **owner** (accountable), classification, location, dependencies, and a reason it is in or out of the CNCS file.

---

## Interview line

“I keep a living internal CMDB-quality inventory for risk, and a signed Art. 6 extract for CNCS that is only the internet-facing set. Asset owner is a name, not a team alias.”

---

← [06 Audit & monitoring](../06-auditoria/README.md) · [Index](../../README.md#modules) · [08 Incident management](../08-gestao-incidentes/README.md) →
