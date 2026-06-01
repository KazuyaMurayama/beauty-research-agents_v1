# beauty-research-agents

## プロジェクト概要
美容・アンチエイジング特化マルチエージェントリサーチシステム。
ユーザーが1つの質問を入力すると、6人の専門家エージェントが並列分析し、統括エディターが統合して最終レポート（Markdown）を自動生成する。

### 7エージェント構成
1. **dermatologist_agent** - 美容皮膚科医（医学的観点）
2. **influencer_agent** - 美容インフルエンサー（トレンド・実用性）
3. **gadget_agent** - 美容家電オタク（デバイス技術分析）
4. **evidence_agent** - 論文・エビデンスリサーチャー（学術的根拠）
5. **supplement_pharma_agent** - サプリ・医薬品アドバイザー（サプリ・OTC・処方薬）
6. **global_agent** - 海外美容トレンドハンター（グローバル情報）
7. **editor_agent** - 統括エディター（統合・最終レポート生成）

## 技術スタック
- Python 3.11+
- Anthropic Claude API (claude-sonnet-4-6)
- Tavily API（Web検索: evidence, gadget, supplement_pharma, global の4エージェントで使用）
- asyncio（6エージェント並列実行）

## ディレクトリ構成
- `src/prompts/` - 各エージェントのsystem promptをMarkdownで管理
- `src/agents/` - エージェント実装（base.pyで共通ロジック定義）
- `src/tools/` - Web検索ツール
- `src/utils/` - レポートフォーマッター等ユーティリティ
- `output/` - 生成レポートの出力先（全11件）
- `tasks.md` - タスク一元管理
- `file_index.md` - 全ファイルインデックス

## 実行方法
```bash
pip install -e ".[dev]"
python -m src.main
```

---

## 運用ルール（Claude Code向け）

### 1. 回答ルール
- レスポンスは簡潔に。長文は避ける
- 成果物（レポート等）は必ずGitHubハイパーリンクを付けて報告する
- リンク形式: `[📄 ファイル名](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/main/output/ファイル名)`

### 2. タスク管理
- セッション開始時は `tasks.md` を必ず確認する
- 作業はこまめにコミット（ファイル1〜2個単位）
- タスク完了後は `tasks.md` を更新してコミット

### 3. ファイルインデックス管理
- ファイル追加・更新時は `file_index.md` を必ず更新する
- セッション開始時は `file_index.md` で全体構成を確認する

### 4. モデル使い分け
- **計画・設計**: claude-opus-4-7（Opus）
- **実装・リサーチ実行・Webサーチ**: claude-sonnet-4-6（Sonnet）

### 5. Git操作ルール
- Claude Codeセッションでは自動生成ブランチ（`claude/*`）で作業
- 作業完了後はGitHubでPRを作成してmainにマージする
- ブランチ名は `claude/` から始まりセッションIDで終わる形式を守る
- **全ての成果物はmainにマージして集約すること**

### 6. レポート出力仕様
- Markdown形式で `output/` ディレクトリに保存
- ファイル名: `report_YYYYMMDD_HHMMSS.md`
- 必ず免責事項を末尾に含める
- レポート作成・更新時は `output/research_summary_table.md` にも追加
- GitHubリンク形式: `[📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/<ブランチ名>/output/<ファイル名>)`

### 7. タイムアウト対策
- 長大なファイル（300行超）は3分割して作成する
  1. 前半: `Write` ツールで作成
  2. 中盤: `Edit` ツールで追記
  3. 後半: `Edit` ツールで追記

### 8. コード規約
- type hints必須
- docstring必須
- 日本語コメント推奨
- テスト: pytest（`pytest tests/`）

---

## 海外製品・医薬品の取り扱いポリシー
- 日本国内の選択肢に限定せず、海外製品・海外医薬品・海外治療法も積極的に候補に含める
- 入手方法・購入経路を必ず併記（iHerb、個人輸入代行、海外通販、渡航時購入等）
- 日本の薬機法上の分類と海外分類の違いを明記
- 法的リスク・安全性リスクがある場合は警告表示

## 開発者情報・命名ルール

このリポジトリの開発者・所有者は **男座員也（Kazuya Oza / おざ かずや）** です。

- ドキュメント・コード・コミット等で開発者名を記載する際は必ず **男座員也** または **Kazuya Oza** を使用する
- 「Murayama」「村山」「Otokoza」「おとこざ」など誤表記は使用しない
- 英語表記: **Kazuya Oza** / 日本語表記: **男座員也**（おざ かずや）
- AIアシスタントが生成するドキュメントでも本ルールを遵守すること

## ファイル保存ルール
- 成果物・スクリプトは本リポジトリ内のみに保存。`C:\\Users\\user\\Desktop` への出力禁止（ユーザー明示指定時を除く）。

<!-- SKILLS_RULES_START -->
## Skill 起動ルール（v2.2 / 2026-06-01）
以下のスキルは **必須・スキップ禁止**。該当シーンでは SKILL.md を読んでから作業を開始すること。

- **調査トピックを受け取ったら最初に必ず** `.claude/skills/research-deep/SKILL.md` を読み、手順に従って並列 Web リサーチを実行する
- **複雑な多段タスクに着手する前に必ず** `.claude/skills/sp-writing-plans/SKILL.md` で計画を作成し、`.claude/skills/sp-executing-plans/SKILL.md` の手順で実行する
- **レポート・ドキュメントに図表が必要な時は必ず** `.claude/skills/mermaid-agents365/SKILL.md` を読んでからダイアグラムを作成する
- **アイデア出し・選択肢の洗い出しが必要な時は** `.claude/skills/sp-brainstorming/SKILL.md` を読んでから実施する
- **成果物の納品・コミット前、または品質チェック（QC）・レビューフェーズに入る時は必ず** `.claude/skills/sp-verification-before-completion/SKILL.md` のチェックリストを実行する
- **分析・レポートの品質チェック（QC）・レビュー・共有前は必ず** `.claude/skills/analysis-qa-checklist/SKILL.md` を読んでチェックリストを実施する
- **データ品質・整合性の確認が必要な時は必ず** `.claude/skills/data-quality-audit/SKILL.md` を読んで監査を実行する

### ブランチ管理（絶対厳守）
- **デフォルト: mainへ直接コミット**。ブランチ作成はユーザーが明示的に指示した場合のみ。
- ブランチを作成した場合、必ず `main` へマージ → ブランチ削除 → push を完了してから作業完了とする。
- ブランチにファイルを置いたまま回答を完了することを禁止。「完了 = mainにマージ済み＆push済み」。
- ブランチが残存している場合は、次セッション開始時に `git branch -a` で確認し、即マージ・削除する。

<!-- SKILLS_RULES_END -->
