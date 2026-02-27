"""論文・エビデンスリサーチャーエージェント"""

from src.agents.base import BaseAgent


class EvidenceAgent(BaseAgent):
    """論文・エビデンスリサーチャーエージェント。

    学術論文・臨床試験ベースの回答を行い、PubMed等の論文引用、
    エビデンスレベル評価を提供する。
    """

    agent_name = "evidence"
    prompt_file = "evidence.md"
    uses_web_search = True

    def _build_search_query(self, query: str) -> str:
        """学術論文に特化した検索クエリを構築する。

        Args:
            query: 元のクエリ

        Returns:
            論文検索向けに調整された検索クエリ
        """
        return f"PubMed clinical trial {query} skincare dermatology evidence"
