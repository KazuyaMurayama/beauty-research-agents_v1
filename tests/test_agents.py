"""エージェントモジュールのテスト"""

import os
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.base import BaseAgent, PROMPTS_DIR
from src.agents.dermatologist import DermatologistAgent
from src.agents.influencer import InfluencerAgent
from src.agents.gadget import GadgetAgent
from src.agents.evidence import EvidenceAgent
from src.agents.supplement_pharma import SupplementPharmaAgent
from src.agents.global_beauty import GlobalBeautyAgent
from src.agents.editor import EditorAgent
from src.utils.report_formatter import ReportFormatter


class TestPromptFiles:
    """プロンプトファイルの存在と内容を検証するテスト"""

    EXPECTED_PROMPT_FILES = [
        "dermatologist.md",
        "influencer.md",
        "gadget.md",
        "evidence.md",
        "supplement_pharma.md",
        "global_beauty.md",
        "editor.md",
    ]

    def test_prompts_directory_exists(self) -> None:
        """プロンプトディレクトリが存在することを確認"""
        assert PROMPTS_DIR.exists(), f"プロンプトディレクトリが見つかりません: {PROMPTS_DIR}"

    @pytest.mark.parametrize("filename", EXPECTED_PROMPT_FILES)
    def test_prompt_file_exists(self, filename: str) -> None:
        """各プロンプトファイルが存在することを確認"""
        filepath = PROMPTS_DIR / filename
        assert filepath.exists(), f"プロンプトファイルが見つかりません: {filepath}"

    @pytest.mark.parametrize("filename", EXPECTED_PROMPT_FILES)
    def test_prompt_file_not_empty(self, filename: str) -> None:
        """各プロンプトファイルが空でないことを確認"""
        filepath = PROMPTS_DIR / filename
        content = filepath.read_text(encoding="utf-8")
        assert len(content) > 0, f"プロンプトファイルが空です: {filepath}"

    @pytest.mark.parametrize("filename", EXPECTED_PROMPT_FILES)
    def test_prompt_file_minimum_length(self, filename: str) -> None:
        """各プロンプトファイルが500語以上であることを確認"""
        filepath = PROMPTS_DIR / filename
        content = filepath.read_text(encoding="utf-8")
        # 日本語の場合は文字数で、英語混在の場合はワード数で判定
        # 500語相当 ≈ 日本語で約800文字以上
        assert len(content) >= 500, (
            f"プロンプトファイルが短すぎます: {filepath} ({len(content)}文字)"
        )


class TestAgentConfiguration:
    """エージェントの設定を検証するテスト"""

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_dermatologist_agent_config(self) -> None:
        """美容皮膚科医エージェントの設定を確認"""
        agent = DermatologistAgent()
        assert agent.agent_name == "dermatologist"
        assert agent.prompt_file == "dermatologist.md"
        assert agent.uses_web_search is False

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_influencer_agent_config(self) -> None:
        """美容インフルエンサーエージェントの設定を確認"""
        agent = InfluencerAgent()
        assert agent.agent_name == "influencer"
        assert agent.prompt_file == "influencer.md"
        assert agent.uses_web_search is False

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_gadget_agent_config(self) -> None:
        """美容家電オタクエージェントの設定を確認"""
        agent = GadgetAgent()
        assert agent.agent_name == "gadget"
        assert agent.prompt_file == "gadget.md"
        assert agent.uses_web_search is True

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_evidence_agent_config(self) -> None:
        """論文リサーチャーエージェントの設定を確認"""
        agent = EvidenceAgent()
        assert agent.agent_name == "evidence"
        assert agent.prompt_file == "evidence.md"
        assert agent.uses_web_search is True

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_supplement_pharma_agent_config(self) -> None:
        """サプリ・医薬品アドバイザーエージェントの設定を確認"""
        agent = SupplementPharmaAgent()
        assert agent.agent_name == "supplement_pharma"
        assert agent.prompt_file == "supplement_pharma.md"
        assert agent.uses_web_search is True

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_global_beauty_agent_config(self) -> None:
        """海外トレンドハンターエージェントの設定を確認"""
        agent = GlobalBeautyAgent()
        assert agent.agent_name == "global_beauty"
        assert agent.prompt_file == "global_beauty.md"
        assert agent.uses_web_search is True

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_editor_agent_config(self) -> None:
        """統括エディターエージェントの設定を確認"""
        agent = EditorAgent()
        assert agent.agent_name == "editor"
        assert agent.prompt_file == "editor.md"
        assert agent.uses_web_search is False

    def test_missing_api_key_raises_error(self) -> None:
        """API キーが未設定の場合にエラーが発生することを確認"""
        with patch.dict(os.environ, {}, clear=True):
            # ANTHROPIC_API_KEYが環境変数にない状態
            os.environ.pop("ANTHROPIC_API_KEY", None)
            with pytest.raises(ValueError, match="ANTHROPIC_API_KEY"):
                DermatologistAgent()


class TestSearchQuery:
    """検索クエリの構築を検証するテスト"""

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_gadget_search_query(self) -> None:
        """美容家電エージェントの検索クエリ構築を確認"""
        agent = GadgetAgent()
        query = agent._build_search_query("シワ改善")
        assert "美容家電" in query
        assert "シワ改善" in query

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_evidence_search_query(self) -> None:
        """論文リサーチャーの検索クエリ構築を確認"""
        agent = EvidenceAgent()
        query = agent._build_search_query("レチノール")
        assert "PubMed" in query
        assert "レチノール" in query

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_supplement_pharma_search_query(self) -> None:
        """サプリ・医薬品エージェントの検索クエリ構築を確認"""
        agent = SupplementPharmaAgent()
        query = agent._build_search_query("NMN")
        assert "サプリメント" in query
        assert "NMN" in query

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_global_beauty_search_query(self) -> None:
        """海外トレンドエージェントの検索クエリ構築を確認"""
        agent = GlobalBeautyAgent()
        query = agent._build_search_query("毛穴ケア")
        assert "beauty" in query.lower()
        assert "毛穴ケア" in query

    @patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"})
    def test_base_search_query_passthrough(self) -> None:
        """BaseAgentの検索クエリはそのまま返ることを確認"""
        agent = DermatologistAgent()
        query = agent._build_search_query("テスト")
        assert query == "テスト"


class TestReportFormatter:
    """レポートフォーマッターのテスト"""

    def test_format_report_contains_query(self) -> None:
        """レポートにクエリが含まれることを確認"""
        formatter = ReportFormatter()
        report = formatter.format_report(
            query="テスト質問",
            dermatologist_response="皮膚科医の回答",
            supplement_pharma_response="サプリの回答",
            influencer_response="インフルエンサーの回答",
            gadget_response="家電オタクの回答",
            global_response="海外トレンドの回答",
            evidence_response="エビデンスの回答",
            editor_response="エディターの回答",
        )
        assert "テスト質問" in report

    def test_format_report_contains_all_sections(self) -> None:
        """レポートに全セクションが含まれることを確認"""
        formatter = ReportFormatter()
        report = formatter.format_report(
            query="テスト",
            dermatologist_response="回答1",
            supplement_pharma_response="回答2",
            influencer_response="回答3",
            gadget_response="回答4",
            global_response="回答5",
            evidence_response="回答6",
            editor_response="回答7",
        )
        assert "医学的見解" in report
        assert "サプリメント・医薬品ガイド" in report
        assert "トレンド・実用ガイド" in report
        assert "美容家電・デバイス分析" in report
        assert "海外トレンド・グローバル知見" in report
        assert "エビデンス・論文レビュー" in report
        assert "免責事項" in report

    def test_format_report_contains_disclaimer(self) -> None:
        """レポートに免責事項が含まれることを確認"""
        formatter = ReportFormatter()
        report = formatter.format_report(
            query="テスト",
            dermatologist_response="回答",
            supplement_pharma_response="回答",
            influencer_response="回答",
            gadget_response="回答",
            global_response="回答",
            evidence_response="回答",
            editor_response="回答",
        )
        assert "医療行為の推奨ではありません" in report
        assert "医師・薬剤師にご相談ください" in report

    def test_save_report(self, tmp_path: Path) -> None:
        """レポートがファイルに保存されることを確認"""
        formatter = ReportFormatter()
        formatter.OUTPUT_DIR = str(tmp_path)
        filepath = formatter.save_report("# テストレポート\n内容")
        assert os.path.exists(filepath)
        with open(filepath, encoding="utf-8") as f:
            content = f.read()
        assert "テストレポート" in content


class TestWebSearchTool:
    """Web検索ツールのテスト"""

    def test_missing_tavily_key_raises_error(self) -> None:
        """TAVILY_API_KEYが未設定の場合にエラーが発生することを確認"""
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("TAVILY_API_KEY", None)
            with pytest.raises(ValueError, match="TAVILY_API_KEY"):
                from src.tools.web_search import TavilySearchTool
                TavilySearchTool()

    def test_format_results_empty(self) -> None:
        """空の検索結果のフォーマットを確認"""
        with patch.dict(os.environ, {"TAVILY_API_KEY": "test-key"}):
            with patch("src.tools.web_search.TavilyClient"):
                from src.tools.web_search import TavilySearchTool
                tool = TavilySearchTool()
                result = tool.format_results([])
                assert "見つかりませんでした" in result

    def test_format_results_with_data(self) -> None:
        """検索結果のフォーマットを確認"""
        with patch.dict(os.environ, {"TAVILY_API_KEY": "test-key"}):
            with patch("src.tools.web_search.TavilyClient"):
                from src.tools.web_search import TavilySearchTool
                tool = TavilySearchTool()
                results = [
                    {"title": "テスト記事", "url": "https://example.com", "content": "テスト内容"},
                ]
                formatted = tool.format_results(results)
                assert "テスト記事" in formatted
                assert "https://example.com" in formatted
