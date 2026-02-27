"""海外美容トレンドハンターエージェント"""

from src.agents.base import BaseAgent


class GlobalBeautyAgent(BaseAgent):
    """海外美容トレンドハンターエージェント。

    日本未上陸・海外先行の美容トレンド、製品、治療法、
    成分の情報を提供する。
    """

    agent_name = "global_beauty"
    prompt_file = "global_beauty.md"
    uses_web_search = True

    def _build_search_query(self, query: str) -> str:
        """海外美容トレンドに特化した検索クエリを構築する。

        Args:
            query: 元のクエリ

        Returns:
            海外トレンド向けに調整された検索クエリ
        """
        return f"beauty trend global {query} K-beauty skincare 2024 2025"
