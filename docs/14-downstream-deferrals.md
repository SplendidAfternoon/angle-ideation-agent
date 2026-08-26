# 14 — Downstream deferrals (explicit non-execution)

**Version:** 1.9.0  
**Methodology pin:** `angle-ideation-agent@1.9.0`  
**Purpose:** Record what this repo will **not** build next, so pipeline planning stays honest.

## 1. Pre-Lander agent — separate project

**Status:** Deferred (interface only).

- This repo freezes the **read contract** in [`docs/12-prelander-handoff-contract.md`](12-prelander-handoff-contract.md), `schemas/angle_pack.schema.json`, and the VSL beat map in [`docs/15-vsl-deployment-contract.md`](15-vsl-deployment-contract.md).
- A Pre-Lander / advertorial / VSL **generator** must live in a **separate** methodology or product repo.
- Consume only packs with Status `Ready for Pre-Lander Agent` **and** the full Ready predicate in `docs/12` §1.
- Do **not** expand Angle Ideation into page HTML, offer blocks, or Meta copy inside this repository.
- Do **not** mash eight pack currencies into one 15–30s cut (`docs/15` `D-MULTI-IDEA`).

**Unblock when:** A dedicated Pre-Lander owner/repo exists and agrees to `docs/12` + `docs/15` field mapping.

## 2. Cursor scheduled Automations — later wrapper

**Status:** Deferred until skills are stable **and** the repo is committed (done) **and** pushed to a remote Automations can check out.

- Interactive skills (`angle-ideation`, `angle-gate-critic`) are the source of truth.
- Scheduled Automations are a thin trigger wrapper only — they must not collapse Generator + Critic into one opaque prompt.
- Automations cannot reliably pin **untracked** files; baseline commit is a prerequisite (satisfied). Remote push is still required before org Automations.

**Unblock when:** Remote exists, branch pushed, and a human defines trigger (e.g. Slack/folder drop) without changing gate ownership.

## 3. Still out of scope here

- Automated research-agent ingestion pipelines / rich dossier feeds  
- Multi-tenant product app  
- Meta / Andromeda bidding or performance prediction  

See also README non-goals and [`docs/11`](11-stakeholder-handoff.md) §6.
