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
- Anthropic Claude API (claude-sonnet-4-5-20250929)
- Tavily API（Web検索: evidence, gadget, supplement_pharma, global の4エージェントで使用）
- asyncio（6エージェント並列実行）

## ディレクトリ構成
- `src/prompts/` - 各エージェントのsystem promptをMarkdownで管理
- `src/agents/` - エージェント実装（base.pyで共通ロジック定義）
- `src/tools/` - Web検索ツール
- `src/utils/` - レポートフォーマッター等ユーティリティ
- `output/` - 生成レポートの出力先

## コード規約
- type hints必須
- docstring必須
- 日本語コメント推奨
- テスト: pytest（`pytest tests/`）

## 実行方法
```bash
# 依存インストール
pip install -e ".[dev]"

# 実行
python -m src.main
```

## レポート出力仕様
- Markdown形式で `output/` ディレクトリに保存
- ファイル名: `report_YYYYMMDD_HHMMSS.md`
- 必ず免責事項を末尾に含める

## 海外製品・医薬品の取り扱いポリシー
- 日本国内の選択肢に限定せず、海外製品・海外医薬品・海外治療法も積極的に候補に含める
- 入手方法・購入経路を必ず併記（iHerb、個人輸入代行、海外通販、渡航時購入等）
- 日本の薬機法上の分類と海外分類の違いを明記
- 法的リスク・安全性リスクがある場合は警告表示
