#!/usr/bin/env python3
"""NovelClaw 项目初始化脚本"""
import argparse
import json
import os
import sys


def main():
    parser = argparse.ArgumentParser(description="初始化 NovelClaw 小说项目")
    parser.add_argument("project_dir", help="项目目录路径")
    parser.add_argument("--title", required=True, help="小说标题")
    parser.add_argument("--genre", default="玄幻", help="小说类型")
    args = parser.parse_args()

    project_dir = os.path.abspath(args.project_dir)

    # 创建目录结构
    os.makedirs(os.path.join(project_dir, "chapters"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "outlines"), exist_ok=True)

    # config.json
    config = {
        "title": args.title,
        "genre": args.genre,
        "default_scene": "general",
        "created_at": __import__("datetime").datetime.now().isoformat()
    }
    _write_json(os.path.join(project_dir, "config.json"), config)

    # characters.json
    if not os.path.exists(os.path.join(project_dir, "characters.json")):
        _write_json(os.path.join(project_dir, "characters.json"), {})

    # world.json
    if not os.path.exists(os.path.join(project_dir, "world.json")):
        world = {
            "genre": args.genre,
            "setting": "",
            "power_system": "",
            "factions": [],
            "rules": []
        }
        _write_json(os.path.join(project_dir, "world.json"), world)

    # style_constraints.json
    if not os.path.exists(os.path.join(project_dir, "style_constraints.json")):
        constraints = {
            "banned_phrases": [
                "不仅如此", "总之", "仿佛在说", "显然", "毫无疑问",
                "值得一提的是", "不言而喻", "众所周知", "事实上",
                "与此同时", "换言之", "可以说", "某种程度上"
            ],
            "preferred_style": {
                "sentence_length": "短句为主，长短交替",
                "description_density": "高动词密度，少形容词堆砌",
                "dialogue_style": "简洁有力，符合人物性格"
            },
            "evolution_log": []
        }
        _write_json(os.path.join(project_dir, "style_constraints.json"), constraints)

    # outline
    outline_path = os.path.join(project_dir, "outlines", "outline.md")
    if not os.path.exists(outline_path):
        with open(outline_path, "w", encoding="utf-8") as f:
            f.write(f"# {args.title} 大纲\n\n> 类型：{args.genre}\n\n<!-- 在这里编写故事大纲 -->\n")

    # summary log
    summary_path = os.path.join(project_dir, "outlines", "summary_log.md")
    if not os.path.exists(summary_path):
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(f"# {args.title} 章节摘要\n\n")

    print(f"✅ 项目 [{args.title}] 初始化完成")
    print(f"   目录: {project_dir}")
    print(f"   类型: {args.genre}")
    print(f"\n下一步:")
    print(f"  1. 编辑 {project_dir}/world.json 补充世界观")
    print(f"  2. 编辑 {project_dir}/characters.json 添加核心人物")
    print(f"  3. 编辑 {project_dir}/outlines/outline.md 写大纲")
    print(f"  4. 然后就可以开始写第一章了")


def _write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  创建: {path}")


if __name__ == "__main__":
    main()
