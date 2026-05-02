#!/usr/bin/env python3
"""NovelClaw 自进化自检脚本
扫描章节正文中的避雷词和AI味表达，自动追加新发现的避雷词。
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime


# 内置AI味高频词（即使 style_constraints.json 没列也要检查）
BUILTIN_BANNED = [
    "不仅如此", "总之", "仿佛在说", "显然", "毫无疑问",
    "值得一提的是", "不言而喻", "众所周知", "事实上",
    "与此同时", "换言之", "可以说", "某种程度上",
    "综上所述", "简而言之", "众所周知", "从某种意义上来说",
    "令人印象深刻", "令人叹为观止", "举世闻名", "举足轻重",
    "在这个充满挑战的时代", "面对如此严峻的形势",
    "这无疑是一个", "他的实力不容小觑",
]

# AI味句式模式
PATTERN_CHECKS = [
    (r"他感到.{2,10}(涌上|袭来|充斥)", "情绪标签化：用动作/环境代替"),
    (r"她感到.{2,10}(涌上|袭来|充斥)", "情绪标签化：用动作/环境代替"),
    (r"一阵.{2,6}(涌上心头|袭来|充斥)", "套路表达：改用具体描写"),
    (r"仿佛.{4,20}一般", "万能比喻：减少'仿佛...一般'频率"),
    (r"异常.{1,4}(激烈|强大|恐怖)", "空洞修饰：改用具体细节"),
    (r"不由自主地", "AI味副词：删除或改写"),
    (r"下意识地(?!.*侧身|.*后退|.*闪避)", "检查是否必要，能删就删"),
]


def load_banned_phrases(constraints_path):
    """从 style_constraints.json 加载避雷词"""
    phrases = list(BUILTIN_BANNED)
    if os.path.exists(constraints_path):
        with open(constraints_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for p in data.get("banned_phrases", []):
                if p not in phrases:
                    phrases.append(p)
    return phrases


def scan_chapter(chapter_path, banned_phrases):
    """扫描章节正文"""
    with open(chapter_path, "r", encoding="utf-8") as f:
        text = f.read()

    issues = []
    new_discoveries = []

    # 1. 扫描避雷词
    for phrase in banned_phrases:
        count = text.count(phrase)
        if count > 0:
            issues.append({
                "type": "banned_phrase",
                "word": phrase,
                "count": count,
                "action": "删除或改写"
            })

    # 2. 扫描AI味句式
    for pattern, desc in PATTERN_CHECKS:
        matches = re.findall(pattern, text)
        if matches:
            issues.append({
                "type": "ai_pattern",
                "pattern": pattern,
                "count": len(matches),
                "desc": desc,
                "action": "改写"
            })

    # 3. 检查高频词（出现超过3次的可疑词）
    suspicious_words = ["突然", "忽然", "一阵", "不禁", "竟然"]
    for word in suspicious_words:
        count = text.count(word)
        if count > 3:
            issues.append({
                "type": "overuse",
                "word": word,
                "count": count,
                "action": f"出现{count}次，建议减少到2次以内"
            })

    return issues


def auto_fix(chapter_path, issues):
    """自动修正：替换避雷词（仅限明确可替换的）"""
    with open(chapter_path, "r", encoding="utf-8") as f:
        text = f.read()

    fixed = 0
    # 只自动替换明确的避雷词，不替换句式
    auto_replace = {
        "不仅如此": "更甚者",
        "总之": "说到底",
        "与此同时": "就在这时",
        "换言之": "换句话说",
        "事实上": "说白了",
        "显然": "明摆着",
        "毫无疑问": "",
        "可以说": "",
        "某种程度上": "",
    }

    for issue in issues:
        if issue["type"] == "banned_phrase":
            word = issue["word"]
            if word in auto_replace:
                replacement = auto_replace[word]
                if replacement:
                    text = text.replace(word, replacement)
                else:
                    # 删除词和多余的逗号
                    text = text.replace(word + "，", "")
                    text = text.replace(word + "、", "")
                    text = text.replace(word, "")
                fixed += 1

    if fixed > 0:
        with open(chapter_path, "w", encoding="utf-8") as f:
            f.write(text)

    return fixed


def update_constraints(constraints_path, new_words):
    """将新发现的避雷词追加到 style_constraints.json"""
    if not new_words:
        return

    data = {"banned_phrases": [], "preferred_style": {}, "evolution_log": []}
    if os.path.exists(constraints_path):
        with open(constraints_path, "r", encoding="utf-8") as f:
            data = json.load(f)

    added = 0
    for word in new_words:
        if word not in data["banned_phrases"]:
            data["banned_phrases"].append(word)
            added += 1

    if added > 0:
        data["evolution_log"].append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "action": f"自检发现 {added} 个新避雷词",
            "words": new_words
        })

        with open(constraints_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description="NovelClaw 章节自检")
    parser.add_argument("chapter", help="章节文件路径")
    parser.add_argument("constraints", help="style_constraints.json 路径")
    parser.add_argument("--fix", action="store_true", default=True, help="自动修正避雷词")
    parser.add_argument("--no-fix", action="store_true", help="只检查不修正")
    args = parser.parse_args()

    if not os.path.exists(args.chapter):
        print(f"❌ 章节文件不存在: {args.chapter}")
        sys.exit(1)

    # 加载避雷词
    banned = load_banned_phrases(args.constraints)

    # 扫描
    issues = scan_chapter(args.chapter, banned)

    # 输出报告
    print(f"\n📝 自检报告: {os.path.basename(args.chapter)}")
    print("=" * 50)

    if not issues:
        print("✅ 全部通过！无避雷词，无AI味表达。")
    else:
        banned_issues = [i for i in issues if i["type"] == "banned_phrase"]
        pattern_issues = [i for i in issues if i["type"] == "ai_pattern"]
        overuse_issues = [i for i in issues if i["type"] == "overuse"]

        if banned_issues:
            print(f"\n🚫 避雷词 ({len(banned_issues)} 个):")
            for i in banned_issues:
                print(f"   [{i['word']}] 出现 {i['count']} 次 → {i['action']}")

        if pattern_issues:
            print(f"\n⚠️  AI味句式 ({len(pattern_issues)} 个):")
            for i in pattern_issues:
                print(f"   {i['desc']} (匹配 {i['count']} 次)")

        if overuse_issues:
            print(f"\n📊 高频词 ({len(overuse_issues)} 个):")
            for i in overuse_issues:
                print(f"   [{i['word']}] {i['action']}")

    # 自动修正
    if not args.no_fix and issues:
        fixed = auto_fix(args.chapter, [i for i in issues if i["type"] == "banned_phrase"])
        if fixed > 0:
            print(f"\n🔧 已自动修正 {fixed} 个避雷词")

    # 更新避雷词库
    new_words = [i["word"] for i in issues if i["type"] == "banned_phrase"
                 and i["word"] not in BUILTIN_BANNED]
    if new_words:
        update_constraints(args.constraints, new_words)
        print(f"📚 已将 {len(new_words)} 个新词追加到避雷词库")

    # 字数统计
    with open(args.chapter, "r", encoding="utf-8") as f:
        text = f.read()
    # 只统计中文字符
    cn_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    total_chars = len(text)
    print(f"\n📏 字数: {cn_chars} 中文字 / {total_chars} 总字符")

    print("=" * 50)
    return len(issues)


if __name__ == "__main__":
    main()
