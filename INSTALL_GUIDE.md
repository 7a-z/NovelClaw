# NovelClaw Skill 安装指南

## 方式一：手动安装（推荐）

### 1. 找到 OpenClaw Skills 目录

```bash
# 全局 Skills 目录（所有 Agent 共享）
ls ~/.openclaw/skills/

# 或者 OpenClaw 自带的 Skills 目录
ls /usr/lib/node_modules/openclaw/skills/
```

### 2. 复制 Skill 文件

将 `novelclaw/` 整个文件夹复制到 Skills 目录：

```bash
cp -r novelclaw/ ~/.openclaw/skills/novelclaw/
```

### 3. 验证安装

```bash
# 确认文件结构正确
ls ~/.openclaw/skills/novelclaw/
# 应该看到：SKILL.md  scripts/  references/
```

### 4. 重启 Gateway 使 Skill 生效

```bash
openclaw gateway restart
```

重启后，当你对 Agent 说"写小说"、"新建小说"等关键词时，NovelClaw Skill 会自动触发。

---

## 方式二：通过 ClawHub 安装（如果已发布）

```bash
clawhub install novelclaw
```

---

## 文件结构说明

```
novelclaw/
├── SKILL.md                        # 核心指令文件（必需）
│   ├── YAML frontmatter            # name + description，决定何时触发
│   └── Markdown body               # 工作流、数据格式、关键原则
├── scripts/
│   └── init_project.py             # 项目初始化脚本
└── references/
    ├── style_combat.md             # 打斗场景文风规则
    ├── style_emotion.md            # 情感场景文风规则
    ├── style_suspense.md           # 悬疑场景文风规则
    ├── style_general.md            # 通用叙事规则
    └── ai_cliche.md                # AI味避雷手册
```

## 使用方法

安装完成后，直接对你的 OpenClaw Agent 说：

| 你说 | Agent 做什么 |
|------|-------------|
| "新建小说《xxx》，类型玄幻" | 初始化项目目录，引导设定世界观和人物 |
| "写第一章" | 加载上下文+文风规则，生成正文 |
| "写一段打斗场景" | 自动切换 combat 文风 |
| "加个人物：苏瑶" | 更新人物库 |
| "检查一下有没有AI味" | 自动扫描避雷词 |

## 注意事项

- Skill 依赖 OpenClaw 自身的 LLM 能力，不需要额外配置 API Key
- 项目数据存在用户工作区的 `novel/` 目录下
- 避雷词库会随使用自动增长（自进化）
- 首次使用建议先补充世界观和人物，再开始写
