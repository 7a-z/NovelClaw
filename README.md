# 🦞 NovelClaw: Self-Evolving AI Novelist Skill for OpenClaw

> **NovelClaw** is a professional-grade AI writing plugin specifically designed for the **OpenClaw** ecosystem. It transforms your OpenClaw Agent into a "Master Novelist" capable of long-form storytelling, scene-specific style adaptation, and continuous self-improvement through a feedback-driven evolution loop.

[中文文档 (Chinese Documentation)](./README_CN.md)

---

## 🌟 Key Features

### 1. OpenClaw Native
Deeply integrated as a standard Skill. Trigger it naturally with commands like "Write a new novel" or "Create a new chapter".

### 2. Scene-Specific Stylist
Automatically switches between specialized style patches for different narrative contexts:
- ⚔️ **Combat**: Short sentences, fast-paced, high verb density.
- ❤️ **Emotion**: Micro-expression focus, environmental atmosphere, deep psychological detail.
- 🔍 **Suspense**: Limited perspective, strategic silence, psychological tension.

### 3. Self-Evolving Loop
Automatically detects "AI-typical" cliches and updates its local `style_constraints.json` to avoid them in future chapters. It learns from your feedback to mimic your unique writing style.

### 4. RAG-Based Consistency
Manages world-building and character lore to ensure narrative integrity across millions of words, preventing "plot holes" or character inconsistencies.

---

## 🚀 Quick Start

### 1. Prerequisites
- **Node.js**: v24+ (to run OpenClaw)
- **Python**: v3.10+ (to run NovelClaw core)
- **OpenClaw**: Ensure [OpenClaw](https://github.com/openclaw/openclaw) is installed and running.

### 2. Installation
#### Option 1: Quick Install (Recommended)
1. Download `novelclaw.skill` from this repository.
2. Place it into your OpenClaw skills directory: `~/.openclaw/skills/`.
3. Restart your OpenClaw Gateway.

#### Option 2: Manual Setup
1. Clone this repository.
2. Copy the contents of the `src/` directory into `~/.openclaw/skills/novelclaw/`.
3. Ensure all dependencies in `requirements.txt` are installed.

### 3. Usage
Once installed, simply talk to your OpenClaw Agent:
- "Create a new novel titled 'Sword of Destiny', genre Fantasy."
- "Write the first chapter."
- "Write a combat scene where the hero faces the dragon."
- "Check for AI cliches in the last chapter."

---

## 📂 Project Structure

```text
NovelClaw/
├── novelclaw.skill      # 📦 Ready-to-install Skill package
├── src/                 # 💻 Source code
│   ├── SKILL.md         # Core logic & workflow
│   ├── scripts/         # Execution scripts
│   ├── references/      # Style patches & AI Cliche handbook
│   └── app.py           # Optional Web Dashboard
├── README.md            # English Documentation
├── README_CN.md         # Chinese Documentation
└── requirements.txt     # Dependencies
```

---

## 🤝 Contributing
Contributions are welcome! If you have new style patches or better "AI-cliche" filters, please submit a PR.

---

## 📄 License
[MIT License](LICENSE)
