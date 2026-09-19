# AI Landing Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a canonical, bilingual AI Landing markdown guide (`AGENTS.md`) and harness connectors (`CLAUDE.md`, `GEMINI.md`, `00-START-HERE.md`) so that Claude, Codex, and Gemini understand the full topology ("دهاليز"), truth hierarchy, and operating playbooks of the Code Square vault.

**Architecture:** A single universal Source-of-Truth (`AGENTS.md`) in repo root; lightweight runner configurations in `CLAUDE.md` and `GEMINI.md` pointing to it; integration link in `00-START-HERE.md`.

**Tech Stack:** Markdown (CommonMark + Obsidian Flavored Markdown `[[Wikilinks]]`), YAML frontmatter, Git.

## Global Constraints

- Never fabricate: only 4 documented real projects (M Tech Square Website, Techno Square Platform, El Shoush Travel System, Osama Sakr Manning Agency).
- Maintain truth hierarchy: `00-Source/` is immutable; `Foundation Brief.md` is canonical.
- Founder is a pharmacist: communication must be consequence-first, zero marketing/tech fluff, plain language.
- Banned phrases must be explicitly stated: أقوى فريق · أفضل شركة · حلول متكاملة · أحدث التقنيات · "Awwwards-tier" · "99.9% uptime" · "worldwide".
- Commit and push to git as requested by user.

---

### Task 1: Create Canonical `AGENTS.md`

**Files:**
- Create: `d:/vault/code-square/AGENTS.md`

**Interfaces:**
- Consumes: `00-Source/Foundation Brief.md`, `_CLAUDE.md`, `00-START-HERE.md`.
- Produces: `AGENTS.md` containing full operational, structural, and dispatch knowledge for AI models.

- [ ] **Step 1: Write `AGENTS.md` content**
Write the comprehensive guide including:
1. Executive Quick Start (30-second context for LLMs).
2. Persona & Founder Profile (Pharmacist in Port Said, B2B software, communication rules).
3. The Truth Hierarchy & Guardrails (00-Source immutable, Foundation Brief canonical, anti-fabrication, 4 real projects, confidence labels, banned phrases).
4. Detailed Vault Map ("دهاليز الفولت"): Folders 00 to 10, Conversations, Logs, visual assets, docs.
5. Task Dispatch Matrix (Marketing, Technical Audit/Remediation, Sales/Offers, Case Studies, Operations).
6. Agent Execution Standards (Read before edit, file creation constraints, multi-agent worktrees).

- [ ] **Step 2: Verify `AGENTS.md` file integrity and links**
Check that all internal folder and file paths match existing files in `d:/vault/code-square`.

- [ ] **Step 3: Commit Task 1**
```bash
git add AGENTS.md
git commit -m "feat(ai): create canonical AGENTS.md landing guide"
```

---

### Task 2: Configure `CLAUDE.md` and `GEMINI.md`

**Files:**
- Modify: `d:/vault/code-square/CLAUDE.md`
- Create: `d:/vault/code-square/GEMINI.md`

**Interfaces:**
- Consumes: `AGENTS.md`.
- Produces: Streamlined runner configs that ensure Claude Code and Gemini read `AGENTS.md` on session start.

- [ ] **Step 1: Update `CLAUDE.md`**
Replace generic Ruflo template with a clean, high-signal config that immediately instructs Claude Code to read `AGENTS.md` and keep file/session rules.

- [ ] **Step 2: Create `GEMINI.md`**
Write `GEMINI.md` instructing Gemini / Antigravity to ingest `AGENTS.md` and apply planning/execution guidelines.

- [ ] **Step 3: Commit Task 2**
```bash
git add CLAUDE.md GEMINI.md
git commit -m "feat(ai): wire CLAUDE.md and GEMINI.md to canonical AGENTS.md"
```

---

### Task 3: Update `00-START-HERE.md` Dashboard

**Files:**
- Modify: `d:/vault/code-square/00-START-HERE.md`

**Interfaces:**
- Consumes: `AGENTS.md`.
- Produces: Updated Obsidian home note with prominent `[[AGENTS]]` link.

- [ ] **Step 1: Update `00-START-HERE.md`**
Add an AI agents section linking directly to `[[AGENTS]]` and explaining its purpose.

- [ ] **Step 2: Verify Obsidian links**
Ensure `[[AGENTS]]` resolves cleanly.

- [ ] **Step 3: Commit Task 3**
```bash
git add 00-START-HERE.md
git commit -m "docs(vault): link AGENTS.md in 00-START-HERE.md dashboard"
```

---

### Task 4: Final Validation & Push to Remote

**Files:**
- All modified and new files.

- [ ] **Step 1: Run git status and diff check**
Verify all changes are committed and working tree is clean.

- [ ] **Step 2: Push commits to remote origin**
Run `git push origin master` (or `main`) as requested by the user.

- [ ] **Step 3: Verify push status**
Ensure remote is up to date.
