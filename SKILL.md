---
name: novelclaw
description: AI 长篇小说写作助手。用于：网文/小说创作、章节生成、人物管理、世界观设定、文风切换（打斗/情感/悬疑）、自进化避雷。触发词：写小说、写章节、小说助手、novelclaw、网文创作、人物设定、世界观。
---

# NovelClaw — 自进化 AI 写作助手

## 前置条件

项目目录结构（用户工作区内）：

```
novel/
├── config.json          # 项目配置（标题、类型、默认文风）
├── characters.json      # 人物志
├── world.json           # 世界观设定
├── style_constraints.json  # 自进化避雷词库
├── chapters/            # 已写章节
│   ├── 001.md
│   └── ...
└── outlines/            # 大纲
    └── outline.md
```

## 工作流

### 1. 初始化项目

用户说"新建小说"或"初始化项目"时：

1. 询问小说标题和类型（玄幻/都市/科幻/言情等）
2. 运行 `python3 <skill_dir>/scripts/init_project.py <项目目录> --title <标题> --genre <类型>`
3. 引导用户补充世界观和核心人物
4. 将信息写入 `characters.json` 和 `world.json`

### 2. 写章节

用户要求写章节时，按以下顺序：

#### 2a. 加载上下文

读取以下文件（不存在则跳过）：
- `characters.json` — 人物性格、关系
- `world.json` — 世界观规则
- `style_constraints.json` — 避雷词和文风偏好
- 最近 2-3 章正文（`chapters/` 目录最新的 .md 文件）
- `outlines/outline.md` — 大纲（如有）

#### 2b. 识别场景类型

根据内容自动判断或由用户指定：
- `combat` — 打斗/战斗场景
- `emotion` — 情感/互动场景
- `suspense` — 悬疑/推理场景
- `general` — 通用叙事

读取对应的文风规则：`<skill_dir>/references/style_{scene}.md`

#### 2c. 生成正文

生成时必须遵守：
1. 加载 `style_constraints.json` 中的避雷词，严格禁止使用
2. 遵守场景文风规则
3. 保持人物性格一致
4. 保持剧情连贯（参考前文摘要）

输出格式：直接输出正文内容，不要加章节标题以外的装饰。

#### 2d. 自进化反思（生成后）

写完一章后自动执行：
1. 检查正文中是否含有避雷词库中的词汇
2. 检查是否有明显的"AI味"表达（参考 references/ai_cliche.md）
3. 如发现新的避雷词，追加到 `style_constraints.json`
4. 将章节摘要（2-3 句话）追加到 `outlines/summary_log.md`

### 3. 人物管理

- **添加人物**：更新 `characters.json`，格式见下方
- **查询人物**：读取 `characters.json` 并展示
- **修改人物**：直接编辑对应条目

### 4. 世界观管理

- **添加设定**：更新 `world.json`
- **查询设定**：读取并展示
- **一致性检查**：写新章节前，检查是否与已有设定冲突

## 数据格式

### characters.json

```json
{
  "林风": {
    "description": "主角，性格坚韧，天赋平庸但努力过人",
    "traits": ["坚韧", "隐忍", "重情义"],
    "relationships": {"苏瑶": "师妹", "萧长老": "师父"},
    "first_appearance": 1
  }
}
```

### world.json

```json
{
  "genre": "玄幻",
  "setting": "高武大陆，灵气复苏",
  "power_system": "练气→筑基→金丹→元婴→化神→渡劫→大乘",
  "factions": ["天剑宗", "魔道联盟", "散修联盟"],
  "rules": ["灵气浓度决定修炼速度", "金丹以下无法飞行"]
}
```

### style_constraints.json

```json
{
  "banned_phrases": ["不仅如此", "总之", "仿佛在说", "显然", "毫无疑问"],
  "preferred_style": {
    "sentence_length": "短句为主",
    "description_density": "高动词密度",
    "dialogue_style": "简洁有力"
  },
  "evolution_log": [
    {"date": "2026-05-02", "lesson": "用户偏好短句叙事，减少形容词堆砌"}
  ]
}
```

## 关键原则

1. **不要当"AI写手"，要当"代笔作家"** — 写出来的东西要像人写的，不是AI生成的
2. **上下文是命脉** — 写之前必须读前文，不读不写
3. **避雷词零容忍** — style_constraints.json 里的词，一个都不能出现
4. **进化是核心** — 每次写完都要反思，把教训记下来
5. **人物一致性** — 写对话前先查人物性格，别让温柔的人突然暴躁
