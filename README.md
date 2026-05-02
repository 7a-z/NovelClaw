# 🦞 NovelClaw — Self-Evolving AI Novelist Skill for OpenClaw

NovelClaw is a long-form novel writing Skill based on OpenClaw. It's not just an "AI that writes for you," but a **writing partner that learns your style, self-corrects, and adapts its tone based on the scene.**

---

## Core Features

### 1. Scene-Specific Stylist

Automatically switches to short, fast-paced sentences for combat, or micro-expressions and environmental atmosphere for emotional scenes. Four styles are automatically matched based on the context:

| Scene | Triggers | Style Characteristics |
|------|--------|----------|
| ⚔️ Combat | Battle, Duel, Swordplay | Short sentences, +30% verb density, sensory explosion |
| ❤️ Emotion | Dialogue, Intimacy, Parting | Micro-expressions, atmosphere, subtext |
| 🔍 Suspense | Exploration, Discovery, Shadows | Limited perspective, psychological tension, mystery |
| 📖 General | Default | Concise, vivid imagery, high information density |

### 2. Self-Evolving Anti-Cliche System

Automatically scans every chapter after writing to detect AI-typical phrases and cliches:

```
📝 Self-Check Report: 002.md
==================================================
🚫 Banned Phrases (1):
   [In short] appeared 1 time → Auto-fixed to [Ultimately]

📏 Word Count: 1653 Chinese characters
==================================================
```

- Scans for 20+ built-in banned phrases.
- Detects AI-typical patterns (emotional labeling, generic metaphors, invalid dialogue, etc.).
- Automatically adds new banned phrases to the library, becoming stricter over time.
- High-frequency word warnings (e.g., "Suddenly" appearing more than 3 times).

### 3. Outline-Driven Writing

Instead of writing aimlessly, NovelClaw follows a structured plan:

```
Step 1: Define World-building and Characters
Step 2: List 5-10 Chapter Outlines
Step 3: Start writing only after confirmation
```

Automatically records summaries for each chapter to ensure plot consistency and prevent "plot holes."

### 4. Segmented Writing + Human Feedback

Instead of outputting a massive block of text at once, it pauses for feedback:

```
Write 500-word Intro → "Is the direction right? Continue?"
Write to 1500 words → "Is the pace and style okay?"
Complete Chapter → Self-check + Word count confirmation
```

You can say "Write it all at once" to skip interruptions.

### 5. Seamless Continuation

When writing the next chapter, it automatically reads the end of the previous chapter and the summary log to ensure a smooth transition without repetitive openings.

### 6. Character Consistency Management

Automatically checks character settings before writing dialogue. It won't let a taciturn character suddenly become talkative or a fiery character suddenly become gentle.

---

## Quick Start

### Installation

```bash
# Extract to Skills directory
tar -xzf novelclaw-v2.skill -C ~/.openclaw/skills/

# Restart OpenClaw
openclaw gateway restart
```

### Create a New Novel

Tell the Agent:

> "Create a new novel titled 'Sword of Destiny', genre Fantasy. The setting is a world of sword cultivators where the protagonist cannot hold a sword. The protagonist is named Lin Feng..."

The Agent will:
1. Initialize the project directory.
2. Write world-building and character data.
3. Guide you through creating an outline.
4. Start writing the first chapter after confirmation.

### Writing Chapters

> "Write the first chapter."
> "Write a combat scene."
> "Continue to the next chapter."

---

## Project Structure

```text
novel/                          # Your novel project (Auto-created)
├── config.json                 # Project config (Title, Genre, Word count target)
├── characters.json             # Character lore (Traits, Relationships, Combat style)
├── world.json                  # World-building (Setting, Power system, Factions)
├── style_constraints.json      # Banned phrases library (Self-evolving)
├── chapters/                   # Written chapters
│   ├── 001.md
│   └── 002.md
└── outlines/
    ├── outline.md              # Master outline
    └── summary_log.md          # Chapter summaries (Auto-recorded)
```

### Skill File Structure

```text
~/.openclaw/skills/novelclaw/
├── SKILL.md                    # Core instructions (Workflow, Style rules, Cliche handbook)
├── scripts/
│   ├── init_project.py         # Project initialization script
│   └── self_check.py           # Self-evolving check script
└── references/                 # Reference files (Backup)
    ├── style_combat.md
    ├── style_emotion.md
    ├── style_suspense.md
    ├── style_general.md
    └── ai_cliche.md
```

---

## Self-Check Script Usage

Run self-check manually (usually called automatically by the Agent):

```bash
# Check a chapter
python3 ~/.openclaw/skills/novelclaw/scripts/self_check.py \
  novel/chapters/001.md \
  novel/style_constraints.json

# Check without fixing
python3 ~/.openclaw/skills/novelclaw/scripts/self_check.py \
  novel/chapters/001.md \
  novel/style_constraints.json --no-fix
```

---

## Changelog

### v2 (2026-05-02)
- ✅ Style rules inlined into SKILL.md.
- ✅ New self-check script `self_check.py` (Auto-scan + Auto-fix + Auto-update library).
- ✅ New word count control (Default 2500 words/chapter).
- ✅ New outline-driven workflow.
- ✅ New segmented writing mechanism (500w → 1500w → Finish).
- ✅ New continuation mode (Seamless transition).

### v1 (2026-05-02)
- Initial release: Basic writing workflow, 4 style rules, banned phrases library.
