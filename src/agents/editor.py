"""統括エディターエージェント"""

from src.agents.base import BaseAgent


class EditorAgent(BaseAgent):
    """統括エディターエージェント。

    6人の専門家エージェントの回答を統合し、矛盾点の指摘、
    総合評価、実行可能なアクションプランを含む最終レポートを生成する。
    """

    agent_name = "editor"
    prompt_file = "editor.md"
    uses_web_search = False
    max_tokens = 8192  # 統合分析は長くなるため大きめ

    def __init__(self) -> None:
        """EditorAgentを初期化する。"""
        super().__init__()
        self._agent_responses: dict[str, str] = {}

    async def run_with_agent_responses(
        self,
        query: str,
        agent_responses: dict[str, str],
    ) -> str:
        """各エージェントの回答を統合して最終分析を行う。

        内部で_build_user_messageをオーバーライドし、BaseAgent.runを再利用する。

        Args:
            query: ユーザーの元の質問
            agent_responses: 各エージェント名をキー、回答を値とするdict

        Returns:
            統括エディターによる統合分析・アクションプラン
        """
        self._agent_responses = agent_responses
        return await self.run(query)

    def _build_user_message(self, query: str, search_context: str) -> str:
        """エディター専用のユーザーメッセージを構築する。

        6人の専門家の回答を含む統合分析リクエストを生成する。

        Args:
            query: ユーザーの質問
            search_context: Web検索結果（エディターでは未使用）

        Returns:
            構築されたメッセージ文字列
        """
        # 通常のrun()呼び出し（agent_responsesが空）の場合はベースクラスの動作
        if not self._agent_responses:
            return super()._build_user_message(query, search_context)

        # 各エージェントの回答をまとめたコンテキストを作成
        agent_labels = {
            "dermatologist": "美容皮膚科医",
            "influencer": "美容インフルエンサー",
            "gadget": "美容家電オタク",
            "evidence": "論文・エビデンスリサーチャー",
            "supplement_pharma": "サプリ・医薬品アドバイザー",
            "global_beauty": "海外美容トレンドハンター",
        }

        context_parts: list[str] = []
        for agent_name, agent_response in self._agent_responses.items():
            label = agent_labels.get(agent_name, agent_name)
            context_parts.append(f"### {label}の回答:\n{agent_response}")

        all_responses = "\n\n---\n\n".join(context_parts)

        return (
            f"以下のユーザーの質問に対して、6人の専門家が回答しました。\n"
            f"これらを統合し、あなたの役割に基づいて以下の構成で回答を作成してください。\n"
            f"Markdownの見出しをそのまま使って構造化してください：\n\n"
            f"最初に、最も重要な発見TOP5を箇条書きで簡潔にまとめてください。\n\n"
            f"次に以下のセクションを作成してください：\n\n"
            f"### 7. 総合評価と推奨アクションプラン\n\n"
            f"#### ⚠ 安全性・法的リスク警告\n"
            f"（該当する場合のみ。未承認薬、個人輸入の注意点など）\n\n"
            f"#### 矛盾点・専門家間で意見が分かれた点\n\n"
            f"#### 総合ランキング\n"
            f"| 順位 | 対策 | コスパ | 効果 | 入手しやすさ | 総合スコア |\n\n"
            f"#### 予算別おすすめアクション\n"
            f"- 月5,000円以下:\n- 月5,000〜20,000円:\n"
            f"- 月20,000〜50,000円:\n- 月50,000円以上（本気モード）:\n\n"
            f"#### 入手難易度別アクション\n"
            f"- ★1（Amazon.co.jp/ドラッグストアで即購入）:\n"
            f"- ★2（iHerb/楽天で購入可能）:\n"
            f"- ★3（海外通販/個人輸入）:\n"
            f"- ★4（医師の処方が必要）:\n"
            f"- ★5（海外渡航or特殊ルート）:\n\n"
            f"#### 優先度順アクションリスト（すぐやるべき→じっくり取り組む）\n\n"
            f"---\n\n"
            f"ユーザーの質問: {query}\n\n"
            f"---\n\n"
            f"各専門家の回答:\n\n{all_responses}"
        )
