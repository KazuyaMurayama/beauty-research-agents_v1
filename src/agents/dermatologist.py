"""美容皮膚科医エージェント"""

from src.agents.base import BaseAgent


class DermatologistAgent(BaseAgent):
    """美容皮膚科医エージェント。

    医学的観点から回答し、成分の安全性、治療法の有効性、
    副作用リスク、推奨される医療グレードの対策を提供する。
    """

    agent_name = "dermatologist"
    prompt_file = "dermatologist.md"
    uses_web_search = False
