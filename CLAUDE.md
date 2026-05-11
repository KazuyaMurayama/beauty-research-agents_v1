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

### 開発者の作業環境
- **OS:** Windows 11（Macではない）。シェルは PowerShell 5.1 / Bash（WSL/Git Bash）。`brew` / `Cmd+` / Mac専用コマンドは使用不可。パッケージ管理は `winget` / `scoop`。
- **スマートフォン:** iPhone（iOS）。Android固有の手順・adb・Play Store等は不要。
- コマンド例はPowerShell構文（`;` 連結、`$env:VAR`）で提示。macOS専用ツールを回答に含めない。


## 🚀 自動実行ポリシー

### 確認不要で即実行する操作
- 全ファイル操作（作成・編集・削除）
- 全シェルコマンド（PowerShell, Bash, git, gh, npm, node, python）
- Git操作: add / commit / push（featureブランチ）/ pull / fetch / merge / branch -D / reset --hard
- GitHub操作: gh pr create / gh api 全般 / ブランチ削除
- パッケージ操作: npm install / pip install
- Web検索・フェッチ
- バックグラウンドプロセス起動

### 事前確認が必要な操作（例外のみ）
- `git push --force` を main / master ブランチに対して実行する場合
- `gh repo delete` 実行時

### 動作原則
- 計画提示（簡潔）→ 即実行 → 結果報告 のフロー厳守
- 事前確認文（「Should I run...?」等）を出力しない
- エラー時は即再試行 or 別アプローチで対応、判断が必要な場合のみ報告

## ドキュメント日付ルール

レポート・分析・調査系 .md ファイルを新規作成する際は、H1直下に必ず記載:

```
作成日: YYYY-MM-DD
最終更新日: YYYY-MM-DD
```

- 更新時は **最終更新日のみ** を当日付に書き換える（作成日は固定）
- 除外: README / CLAUDE.md / FILE_INDEX / tasks.md / CHANGELOG / LICENSE

## 作業品質ルール

### Git・ブランチ管理
- 作業前: `git branch --show-current` でブランチ確認 → main以外なら `git checkout main && git pull` してから開始。

### ファイル特定（編集前）
- ユーザー発話のキーワード全てをファイル名と照合してから編集。キーワード不完全一致・候補不確かなら必ず確認。

### 成果物報告
- ファイル作成・更新・push後は必ず3列表で報告: `| 成果物 | 説明 | リンク |`
- リンクは `/blob/<実ブランチ>/<パス>` 形式。報告前に `gh api repos/OWNER/REPO/contents/PATH?ref=BRANCH` で存在確認。push前はURL生成しない。

### ドキュメント品質
- UIパス・コマンド・設定名は公式ドキュメントで確認後に記載。確認不可なら「[要確認]」と明記。
- OS/環境制約（例: Windows専用）をタスク開始時に確認。完成後に `brew`/`Cmd`/`macOS` 等をgrepして除去。

<!-- GLOBAL_RULES_START -->
## Global Rules (synced from ~/.claude/CLAUDE.md)

### 成果物報告（最重要・毎回必須）
ファイルを1つでも作成・更新・pushしたら、**すべて**を3列表で報告する。例外なし。

| 成果物 | 説明 | リンク |
|---|---|---|
| ファイル名 | 1行説明 | [開く](https://github.com/OWNER/REPO/blob/BRANCH/PATH) |

厳守事項（違反＝再提出）:
1. Markdownリンク `[表示名](URL)` 形式必須。plain URL禁止。
2. `/blob/<実ブランチ名>/<実パス>` 形式。トップURL禁止。
3. 提示前に `gh api repos/OWNER/REPO/contents/PATH?ref=BRANCH` で存在確認。
4. ブランチ名は `git rev-parse --abbrev-ref HEAD` で取得。推測禁止。
5. push完了後のみURL生成。未pushはローカル絶対パス＋「（ローカル）」明記。
6. 404発生時は即訂正＋原因1行報告。

### ツール実行
- 確認不要・即実行。「Should I...?」等の事前確認文は出力しない。
- 例外（事前確認必須）: main/masterへの `git push --force`、`gh repo delete`。
- 長時間処理は `run_in_background: true` を積極使用。

### モデル・サブエージェント
- メイン Opus / 探索・検索・テスト系サブは Sonnet (`model: "sonnet"`)。
- サブ起動promptに必ず明記:「成果物は3列表報告・URL検証必須・Markdownリンク形式」

### 回答スタイル
- 回答末尾に「**Next Action:**」でユーザーの次アクションを具体推奨。
<!-- GLOBAL_RULES_END -->
