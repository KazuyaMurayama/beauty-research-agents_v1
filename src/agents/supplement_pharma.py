"""サプリ・医薬品アドバイザーエージェント"""

from src.agents.base import BaseAgent


class SupplementPharmaAgent(BaseAgent):
    """サプリ・医薬品アドバイザーエージェント。

    サプリメント・OTC医薬品・処方薬・機能性食品に関する
    専門的分析を提供する。
    """

    agent_name = "supplement_pharma"
    prompt_file = "supplement_pharma.md"
    uses_web_search = True

    def _build_search_query(self, query: str) -> str:
        """サプリ・医薬品に特化した検索クエリを構築する。

        Args:
            query: 元のクエリ

        Returns:
            サプリ・医薬品向けに調整された検索クエリ
        """
        return f"サプリメント 医薬品 {query} 成分 効果 用量"
