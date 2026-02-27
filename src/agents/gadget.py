"""美容家電オタクエージェント"""

from src.agents.base import BaseAgent


class GadgetAgent(BaseAgent):
    """美容家電オタクエージェント。

    美容デバイス・家電の技術的分析を行い、スペック比較、
    技術原理、コスパ、実測データを提供する。
    """

    agent_name = "gadget"
    prompt_file = "gadget.md"
    uses_web_search = True

    def _build_search_query(self, query: str) -> str:
        """美容家電・デバイスに特化した検索クエリを構築する。

        Args:
            query: 元のクエリ

        Returns:
            美容デバイス向けに調整された検索クエリ
        """
        return f"美容家電 美容デバイス {query} スペック 比較"
