"""ベースエージェントモジュール。全エージェントの共通ロジックを定義する。"""

import os
from pathlib import Path

import anthropic


# プロンプトファイルのディレクトリ
PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

# リトライ設定
MAX_RETRIES = 3

# 使用モデル
MODEL_NAME = "claude-sonnet-4-5-20250929"


class BaseAgent:
    """全エージェントの基底クラス。

    各専門家エージェントはこのクラスを継承し、
    prompt_fileとagent_nameを指定する。
    """

    # サブクラスでオーバーライドする
    agent_name: str = "base"
    prompt_file: str = ""
    uses_web_search: bool = False

    def __init__(self) -> None:
        """BaseAgentを初期化する。"""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY が設定されていません。.envファイルを確認してください。")
        self._client = anthropic.AsyncAnthropic(api_key=api_key)
        self._system_prompt = self._load_system_prompt()

    def _load_system_prompt(self) -> str:
        """プロンプトファイルからsystem promptを読み込む。

        Returns:
            system prompt文字列
        """
        if not self.prompt_file:
            return ""
        prompt_path = PROMPTS_DIR / self.prompt_file
        if not prompt_path.exists():
            raise FileNotFoundError(f"プロンプトファイルが見つかりません: {prompt_path}")
        return prompt_path.read_text(encoding="utf-8")

    async def run(self, query: str) -> str:
        """エージェントを実行してクエリに回答する。

        API呼び出しに失敗した場合は最大MAX_RETRIES回リトライする。

        Args:
            query: ユーザーからの質問

        Returns:
            エージェントの回答文字列
        """
        # Web検索対応エージェントは検索結果をコンテキストに追加
        search_context = ""
        if self.uses_web_search:
            search_context = await self._perform_web_search(query)

        user_message = self._build_user_message(query, search_context)

        for attempt in range(MAX_RETRIES):
            try:
                response = await self._client.messages.create(
                    model=MODEL_NAME,
                    max_tokens=4096,
                    system=self._system_prompt,
                    messages=[{"role": "user", "content": user_message}],
                )
                # テキストブロックから回答を抽出
                text_parts: list[str] = []
                for block in response.content:
                    if block.type == "text":
                        text_parts.append(block.text)
                return "\n".join(text_parts)
            except Exception as e:
                print(f"[{self.agent_name}] API呼び出し失敗 (試行 {attempt + 1}/{MAX_RETRIES}): {e}")
                if attempt == MAX_RETRIES - 1:
                    return f"⚠ {self.agent_name}の回答取得に失敗しました。エラー: {e}"
        # ここには到達しないが型チェッカーのために記述
        return f"⚠ {self.agent_name}の回答取得に失敗しました。"

    async def _perform_web_search(self, query: str) -> str:
        """Web検索を実行してコンテキスト情報を取得する。

        Args:
            query: 検索クエリ

        Returns:
            フォーマットされた検索結果文字列
        """
        try:
            from src.tools.web_search import TavilySearchTool

            search_tool = TavilySearchTool()
            # エージェントの専門性に合わせた検索クエリを生成
            search_query = self._build_search_query(query)
            results = search_tool.search(search_query)
            return search_tool.format_results(results)
        except Exception as e:
            print(f"[{self.agent_name}] Web検索エラー: {e}")
            return ""

    def _build_search_query(self, query: str) -> str:
        """エージェントの専門性に合わせた検索クエリを構築する。

        サブクラスでオーバーライド可能。

        Args:
            query: 元のクエリ

        Returns:
            検索用に調整されたクエリ文字列
        """
        return query

    def _build_user_message(self, query: str, search_context: str) -> str:
        """ユーザーメッセージを構築する。

        Args:
            query: ユーザーの質問
            search_context: Web検索結果のコンテキスト

        Returns:
            構築されたメッセージ文字列
        """
        message = f"以下の質問について、あなたの専門分野の観点から詳しく回答してください。\n\n質問: {query}"
        if search_context:
            message += f"\n\n以下は参考情報として取得したWeb検索結果です。必要に応じて活用してください:\n\n{search_context}"
        return message
