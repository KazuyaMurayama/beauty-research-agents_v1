# FILE_INDEX — beauty-research-agents_v1

> ⚠️ このファイルは自動生成です。手動編集は次回更新で上書きされます。

| 項目 | 値 |
|---|---|
| リポジトリ | KazuyaMurayama/beauty-research-agents_v1 |
| ブランチ | main |
| 総ファイル数 | 49 |
| 最終更新 | 2026-05-02 |
| 管理者 | 男座員也（Kazuya Oza） |

---

## カテゴリ別サマリー

| カテゴリ | ファイル数 |
|---|---|
| Documentation | 27 |
| Code | 18 |
| Config | 3 |
| Other | 1 |

---

## ディレクトリ構成

```
.
├── output/
│   ├── .gitkeep
│   ├── report_20260228_100613.md
│   ├── report_20260228_214142.md
│   ├── report_20260301_110614.md
│   ├── report_20260302_011255.md
│   ├── report_20260303_005413.md
│   ├── report_20260303_014509.md
│   ├── report_20260303_093406.md
│   ├── report_20260309_062633.md
│   ├── report_20260328_120000.md
│   ├── report_20260331_120000.md
│   ├── report_20260427_120000.md
│   ├── report_20260427_140000.md
│   ├── report_20260427_160000.md
│   ├── report_skin_texture_pore_analysis.md
│   └── research_summary_table.md
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dermatologist.py
│   │   ├── editor.py
│   │   ├── evidence.py
│   │   ├── gadget.py
│   │   ├── global_beauty.py
│   │   ├── influencer.py
│   │   └── supplement_pharma.py
│   ├── prompts/
│   │   ├── dermatologist.md
│   │   ├── editor.md
│   │   ├── evidence.md
│   │   ├── gadget.md
│   │   ├── global_beauty.md
│   │   ├── influencer.md
│   │   └── supplement_pharma.md
│   ├── tools/
│   │   ├── __init__.py
│   │   └── web_search.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── report_formatter.py
│   ├── __init__.py
│   ├── main.py
│   └── orchestrator.py
├── tests/
│   ├── __init__.py
│   └── test_agents.py
├── .env.example
├── .gitignore
├── CLAUDE.md
├── file_index.md
├── pyproject.toml
├── README.md
├── tasks.md
└── Timeout_Prevention.md
```

---

## ファイル詳細

### Documentation (27件)

| ファイル | サイズ | 説明 |
|---|---|---|
| `CLAUDE.md` | 4.7 KB | Claude Code プロジェクト設定・命名ルール |
| `file_index.md` | 5.9 KB | Markdown ドキュメント |
| `output/report_20260228_100613.md` | 78.6 KB | Markdown ドキュメント |
| `output/report_20260228_214142.md` | 72.7 KB | Markdown ドキュメント |
| `output/report_20260301_110614.md` | 53.4 KB | Markdown ドキュメント |
| `output/report_20260302_011255.md` | 74.8 KB | Markdown ドキュメント |
| `output/report_20260303_005413.md` | 78.6 KB | Markdown ドキュメント |
| `output/report_20260303_014509.md` | 89.0 KB | Markdown ドキュメント |
| `output/report_20260303_093406.md` | 71.8 KB | Markdown ドキュメント |
| `output/report_20260309_062633.md` | 22.3 KB | Markdown ドキュメント |
| `output/report_20260328_120000.md` | 22.8 KB | Markdown ドキュメント |
| `output/report_20260331_120000.md` | 24.8 KB | Markdown ドキュメント |
| `output/report_20260427_120000.md` | 18.1 KB | Markdown ドキュメント |
| `output/report_20260427_140000.md` | 21.0 KB | Markdown ドキュメント |
| `output/report_20260427_160000.md` | 34.0 KB | Markdown ドキュメント |
| `output/report_skin_texture_pore_analysis.md` | 22.5 KB | Markdown ドキュメント |
| `output/research_summary_table.md` | 19.0 KB | Markdown ドキュメント |
| `README.md` | 1.3 KB | リポジトリ概要・セットアップ手順 |
| `src/prompts/dermatologist.md` | 3.4 KB | Markdown ドキュメント |
| `src/prompts/editor.md` | 4.0 KB | Markdown ドキュメント |
| `src/prompts/evidence.md` | 4.0 KB | Markdown ドキュメント |
| `src/prompts/gadget.md` | 3.7 KB | Markdown ドキュメント |
| `src/prompts/global_beauty.md` | 4.3 KB | Markdown ドキュメント |
| `src/prompts/influencer.md` | 3.7 KB | Markdown ドキュメント |
| `src/prompts/supplement_pharma.md` | 4.7 KB | Markdown ドキュメント |
| `tasks.md` | 5.9 KB | タスク管理・セッション履歴 |
| `Timeout_Prevention.md` | 4.9 KB | タイムアウト対策ガイド |

### Code (18件)

| ファイル | サイズ | 説明 |
|---|---|---|
| `src/__init__.py` | 97 B | Python スクリプト |
| `src/agents/__init__.py` | 627 B | Python スクリプト |
| `src/agents/base.py` | 5.3 KB | Python スクリプト |
| `src/agents/dermatologist.py` | 445 B | Python スクリプト |
| `src/agents/editor.py` | 4.5 KB | Python スクリプト |
| `src/agents/evidence.py` | 799 B | Python スクリプト |
| `src/agents/gadget.py` | 778 B | Python スクリプト |
| `src/agents/global_beauty.py` | 791 B | Python スクリプト |
| `src/agents/influencer.py` | 439 B | Python スクリプト |
| `src/agents/supplement_pharma.py` | 811 B | Python スクリプト |
| `src/main.py` | 1.6 KB | Python スクリプト |
| `src/orchestrator.py` | 4.3 KB | Python スクリプト |
| `src/tools/__init__.py` | 114 B | Python スクリプト |
| `src/tools/web_search.py` | 2.3 KB | Python スクリプト |
| `src/utils/__init__.py` | 130 B | Python スクリプト |
| `src/utils/report_formatter.py` | 6.4 KB | Python スクリプト |
| `tests/__init__.py` | - | Python スクリプト |
| `tests/test_agents.py` | 11.9 KB | Python スクリプト |

### Config (3件)

| ファイル | サイズ | 説明 |
|---|---|---|
| `.env.example` | 103 B | 環境変数テンプレート |
| `.gitignore` | 240 B | Git 除外設定 |
| `pyproject.toml` | 661 B | Python プロジェクト設定 |

### Other (1件)

| ファイル | サイズ | 説明 |
|---|---|---|
| `output/.gitkeep` | - | ファイル |

---

_自動生成: 2026-05-02 | 管理者: 男座員也（Kazuya Oza）_
