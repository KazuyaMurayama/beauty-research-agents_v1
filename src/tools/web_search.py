"""Tavily APIを使用したWeb検索ツール"""

import os
from typing import Any

from tavily import TavilyClient


class TavilySearchTool:
    """Tavily APIを使用してWeb検索を行うツール。

    evidence_agent、gadget_agent、supplement_pharma_agent、global_agentの
    4体のエージェントで使用される。
    """

    def __init__(self) -> None:
        """TavilySearchToolを初期化する。"""
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            raise ValueError("TAVILY_API_KEY が設定されていません。.envファイルを確認してください。")
        self._client = TavilyClient(api_key=api_key)

    def search(self, query: str, max_results: int = 5) -> list[dict[str, Any]]:
        """Web検索を実行し、結果を返す。

        Args:
            query: 検索クエリ
            max_results: 最大検索結果数

        Returns:
            検索結果のリスト。各結果はtitle, url, contentを含むdict。
        """
        try:
            response = self._client.search(
                query=query,
                max_results=max_results,
                search_depth="advanced",
            )
            results: list[dict[str, Any]] = []
            for result in response.get("results", []):
                results.append({
                    "title": result.get("title", ""),
                    "url": result.get("url", ""),
                    "content": result.get("content", ""),
                })
            return results
        except Exception as e:
            print(f"[Web検索エラー] {e}")
            return []

    def format_results(self, results: list[dict[str, Any]]) -> str:
        """検索結果をテキスト形式にフォーマットする。

        Args:
            results: 検索結果のリスト

        Returns:
            フォーマットされた検索結果文字列
        """
        if not results:
            return "検索結果が見つかりませんでした。"

        formatted_parts: list[str] = []
        for i, result in enumerate(results, 1):
            formatted_parts.append(
                f"【{i}】{result['title']}\n"
                f"URL: {result['url']}\n"
                f"{result['content']}\n"
            )
        return "\n".join(formatted_parts)
