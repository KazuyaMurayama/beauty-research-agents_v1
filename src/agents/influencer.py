"""美容インフルエンサーエージェント"""

from src.agents.base import BaseAgent


class InfluencerAgent(BaseAgent):
    """美容インフルエンサーエージェント。

    実体験ベースの回答で、トレンド商品、コスパ、使用感、
    SNSでの評判、ビフォーアフターを提供する。
    """

    agent_name = "influencer"
    prompt_file = "influencer.md"
    uses_web_search = False
