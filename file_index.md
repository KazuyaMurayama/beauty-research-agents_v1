# ファイルインデックス

最終更新: 2026-04-18  
ブランチ: `claude/organize-research-table-VlDjI`

---

## 管理ファイル

| ファイル | 説明 |
|---------|------|
| `CLAUDE.md` | Claude Code向け運用ルール・プロジェクト概要 |
| `tasks.md` | タスク一元管理（本ファイル） |
| `file_index.md` | 全ファイルインデックス（本ファイル） |
| `README.md` | プロジェクト説明 |
| `.env.example` | 環境変数サンプル（ANTHROPIC_API_KEY, TAVILY_API_KEY） |
| `pyproject.toml` | Pythonパッケージ設定・依存関係 |

---

## ソースコード（`src/`）

| ファイル | 説明 |
|---------|------|
| `src/main.py` | エントリーポイント |
| `src/orchestrator.py` | 6エージェント並列実行オーケストレーター |
| `src/__init__.py` | パッケージ初期化 |

### エージェント（`src/agents/`）

| ファイル | 説明 |
|---------|------|
| `src/agents/base.py` | エージェント共通基底クラス |
| `src/agents/dermatologist.py` | 美容皮膚科医エージェント |
| `src/agents/influencer.py` | 美容インフルエンサーエージェント |
| `src/agents/gadget.py` | 美容家電オタクエージェント |
| `src/agents/evidence.py` | 論文・エビデンスリサーチャーエージェント |
| `src/agents/supplement_pharma.py` | サプリ・医薬品アドバイザーエージェント |
| `src/agents/global_beauty.py` | 海外美容トレンドハンターエージェント |
| `src/agents/editor.py` | 統括エディターエージェント |
| `src/agents/__init__.py` | パッケージ初期化 |

### プロンプト（`src/prompts/`）

| ファイル | 説明 |
|---------|------|
| `src/prompts/dermatologist.md` | 皮膚科医エージェントのシステムプロンプト |
| `src/prompts/influencer.md` | インフルエンサーエージェントのシステムプロンプト |
| `src/prompts/gadget.md` | 家電エージェントのシステムプロンプト |
| `src/prompts/evidence.md` | エビデンスエージェントのシステムプロンプト |
| `src/prompts/supplement_pharma.md` | サプリエージェントのシステムプロンプト |
| `src/prompts/global_beauty.md` | グローバルエージェントのシステムプロンプト |
| `src/prompts/editor.md` | エディターエージェントのシステムプロンプト |

### ツール・ユーティリティ

| ファイル | 説明 |
|---------|------|
| `src/tools/web_search.py` | Tavily API Web検索ツール |
| `src/tools/__init__.py` | パッケージ初期化 |
| `src/utils/report_formatter.py` | レポートMarkdownフォーマッター |
| `src/utils/__init__.py` | パッケージ初期化 |

### テスト（`tests/`）

| ファイル | 説明 |
|---------|------|
| `tests/test_agents.py` | エージェントユニットテスト |
| `tests/__init__.py` | パッケージ初期化 |

---

## 生成レポート（`output/`）

| # | ファイル | テーマ | 作成日 | GitHubリンク |
|---|---------|--------|--------|-------------|
| - | `research_summary_table.md` | 全レポートサマリーテーブル | 随時更新 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/research_summary_table.md) |
| 1 | `report_20260228_100613.md` | リフトアップ・フェイスライン（美容医療/家電/サプリ統合） | 2026-02-28 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260228_100613.md) |
| 2 | `report_20260228_214142.md` | IPLマシン比較（サロン/家庭用） | 2026-02-28 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260228_214142.md) |
| 3 | `report_20260301_110614.md` | 身長最大化プロトコル | 2026-03-01 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260301_110614.md) |
| 4 | `report_20260302_011255.md` | 白髪・薄毛対策完全ガイド | 2026-03-02 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260302_011255.md) |
| 5 | `report_20260303_005413.md` | 総合アンチエイジング戦略 | 2026-03-03 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260303_005413.md) |
| 6 | `report_20260303_014509.md` | 美容医療7施術比較（IPL/ルビー/CO2/ピコフラクショナル/ダーマペン4/シルファームX/HIFU） | 2026-03-03 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260303_014509.md) |
| 7 | `report_20260303_093406.md` | 美容医療施術比較拡張版 | 2026-03-03 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260303_093406.md) |
| 8 | `report_skin_texture_pore_analysis.md` | キメの細かさ・毛穴徹底分析（40代男性向け） | 2026-03-05 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_skin_texture_pore_analysis.md) |
| 9 | `report_20260309_062633.md` | 美容医療7施術14軸スコア比較 | 2026-03-09 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260309_062633.md) |
| 10 | `report_20260328_120000.md` | 内臓脂肪を減らす完全ガイド | 2026-03-28 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260328_120000.md) |
| 11 | `report_20260331_120000.md` | 花小金井駅前スキンクリニック全20施術比較 | 2026-03-31 | [📄 開く](https://github.com/KazuyaMurayama/beauty-research-agents_v1/blob/claude/organize-research-table-VlDjI/output/report_20260331_120000.md) |

---

## ブランチ履歴

| ブランチ | 内容 | 状態 |
|---------|------|------|
| `claude/organize-research-table-VlDjI` | 全レポート・運用ルール整備（現在の最新） | **現在のブランチ** |
| `claude/beauty-research-agents-DG80s` | 初期セットアップ | remote HEAD |
| `claude/custom-toner-formula-kdeNf` | カスタムトナー関連 | remote |
| `claude/laser-treatment-skincare-guide-YUssY` | レーザー治療ガイド | remote |
