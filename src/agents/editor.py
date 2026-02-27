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

    async def run_with_agent_responses(
        self,
        query: str,
        agent_responses: dict[str, str],
    ) -> str:
        """各エージェントの回答を統合して最終分析を行う。

        Args:
            query: ユーザーの元の質問
            agent_responses: 各エージェント名をキー、回答を値とするdict

        Returns:
            統括エディターによる統合分析・アクションプラン
        """
        # 各エージェントの回答をまとめたコンテキストを作成
        context_parts: list[str] = []
        agent_labels = {
            "dermatologist": "美容皮膚科医",
            "influencer": "美容インフルエンサー",
            "gadget": "美容家電オタク",
            "evidence": "論文・エビデンスリサーチャー",
            "supplement_pharma": "サプリ・医薬品アドバイザー",
            "global_beauty": "海外美容トレンドハンター",
        }

        for agent_name, response in agent_responses.items():
            label = agent_labels.get(agent_name, agent_name)
            context_parts.append(f"### {label}の回答:\n{response}")

        all_responses = "\n\n---\n\n".join(context_parts)

        user_message = (
            f"以下のユーザーの質問に対して、6人の専門家が回答しました。\n"
            f"これらを統合し、あなたの役割に基づいて以下を作成してください：\n\n"
            f"1. エグゼクティブサマリー（最も重要な発見TOP5）\n"
            f"2. 矛盾点・専門家間で意見が分かれた点\n"
            f"3. 総合ランキング（コスパ/効果/入手しやすさ/総合スコア）\n"
            f"4. 予算別おすすめアクション（4段階）\n"
            f"5. 入手難易度別アクション（5段階: ★1〜★5）\n"
            f"6. 優先度順アクションリスト\n"
            f"7. 安全性・法的リスク警告（該当する場合）\n\n"
            f"---\n\n"
            f"ユーザーの質問: {query}\n\n"
            f"---\n\n"
            f"各専門家の回答:\n\n{all_responses}"
        )

        for attempt in range(self._max_retries):
            try:
                response = await self._client.messages.create(
                    model=self._model_name,
                    max_tokens=8192,
                    system=self._system_prompt,
                    messages=[{"role": "user", "content": user_message}],
                )
                text_parts: list[str] = []
                for block in response.content:
                    if block.type == "text":
                        text_parts.append(block.text)
                return "\n".join(text_parts)
            except Exception as e:
                print(f"[{self.agent_name}] API呼び出し失敗 (試行 {attempt + 1}/{self._max_retries}): {e}")
                if attempt == self._max_retries - 1:
                    return f"⚠ 統括エディターの統合分析に失敗しました。エラー: {e}"
        return "⚠ 統括エディターの統合分析に失敗しました。"

    @property
    def _max_retries(self) -> int:
        """リトライ回数を返す。"""
        from src.agents.base import MAX_RETRIES
        return MAX_RETRIES

    @property
    def _model_name(self) -> str:
        """モデル名を返す。"""
        from src.agents.base import MODEL_NAME
        return MODEL_NAME
