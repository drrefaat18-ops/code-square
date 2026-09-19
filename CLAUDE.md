# Code Square — Claude Code Configuration & Onboarding

> **MANDATORY FIRST STEP:** Read `AGENTS.md` immediately upon session start.
> `AGENTS.md` is the canonical operational guide, truth hierarchy, and vault map for **Code Square (CS)**. All rules and boundaries defined in `AGENTS.md` apply to this session.

---

## 1. Vault Operating Rules

- **First Action:** Read `AGENTS.md` to understand the company, founder persona (pharmacist), truth hierarchy, and "دهاليز" of the vault.
- **The Golden Rule:** **NEVER FABRICATE.** Only 4 real projects exist (M Tech Square Website, Techno Square Platform, El Shoush Travel System, Osama Sakr Manning Agency). Never invent clients, numbers, awards, or pricing ($19/$49/$99 is mockup art).
- **Scope Discipline:** Do what has been asked; nothing more, nothing less.
- **File Cleanliness:**
  - NEVER create loose files or scratch notes in the vault root directory.
  - New strategy specs go to `docs/superpowers/specs/`.
  - New implementation plans go to `docs/superpowers/plans/`.
  - ALWAYS read a file before editing it.
- **Git Attribution:** NEVER add a `Co-Authored-By` trailer to user commits. The tool is a facilitator, not a co-author.
- **Communication Style:** The founder is a pharmacist. Explain technical or business concepts directly through real-world consequences, avoiding corporate or developer jargon. Prefer checklists and tables over long prose.

---

## 2. Multi-Agent & Tool Coordination (If Ruflo / Swarm Active)

- **Isolated Scopes:** When spawning subagents, assign each an exclusive folder or explicit file list.
- **Single Source of Truth:** Only the coordinating session updates shared files (`AGENTS.md`, `00-START-HERE.md`, `Foundation Brief.md`, `Open Questions and Decisions Needed.md`).
- **Memory & Logging:** Append notable session decisions to the current day's log in `Logs/YYYY-MM-DD.md`.
