"""オーケストレーターモジュール。6エージェントの並列実行と統合を管理する。"""

import asyncio

from src.agents.dermatologist import DermatologistAgent
from src.agents.influencer import InfluencerAgent
from src.agents.gadget import GadgetAgent
from src.agents.evidence import EvidenceAgent
from src.agents.supplement_pharma import SupplementPharmaAgent
from src.agents.global_beauty import GlobalBeautyAgent
from src.agents.editor import EditorAgent
from src.utils.report_formatter import ReportFormatter


class Orchestrator:
    """6エージェントの並列実行とエディターによる統合を管理するクラス。

    処理フロー:
    ユーザー入力 → [6エージェント並列実行] → editor_agent統合 → Markdownレポート出力
    """

    def __init__(self) -> None:
        """Orchestratorを初期化する。"""
        # 6体の専門家エージェント
        self._dermatologist = DermatologistAgent()
        self._influencer = InfluencerAgent()
        self._gadget = GadgetAgent()
        self._evidence = EvidenceAgent()
        self._supplement_pharma = SupplementPharmaAgent()
        self._global_beauty = GlobalBeautyAgent()

        # 統括エディター
        self._editor = EditorAgent()

        # レポートフォーマッター
        self._formatter = ReportFormatter()

    async def run(self, query: str) -> str:
        """クエリに対して全エージェントを実行し、最終レポートを生成する。

        Args:
            query: ユーザーの質問

        Returns:
            保存されたレポートファイルのパス
        """
        print(f"\n{'='*60}")
        print(f"クエリ: {query}")
        print(f"{'='*60}")

        # ステップ1: 6エージェントを並列実行
        print("\n🔍 6人の専門家エージェントが分析中...")
        agent_responses = await self._run_agents_parallel(query)

        # 各エージェントの完了を表示
        for agent_name in agent_responses:
            print(f"  ✓ {agent_name} 完了")

        # ステップ2: エディターが統合分析
        print("\n📝 統括エディターが統合分析中...")
        editor_response = await self._editor.run_with_agent_responses(
            query, agent_responses
        )
        print("  ✓ 統合分析 完了")

        # ステップ3: レポート生成・保存
        print("\n📄 レポートを生成中...")
        report = self._formatter.format_report(
            query=query,
            dermatologist_response=agent_responses.get("dermatologist", "取得失敗"),
            supplement_pharma_response=agent_responses.get("supplement_pharma", "取得失敗"),
            influencer_response=agent_responses.get("influencer", "取得失敗"),
            gadget_response=agent_responses.get("gadget", "取得失敗"),
            global_response=agent_responses.get("global_beauty", "取得失敗"),
            evidence_response=agent_responses.get("evidence", "取得失敗"),
            editor_response=editor_response,
        )
        filepath = self._formatter.save_report(report)
        print(f"  ✓ レポート保存完了: {filepath}")

        return filepath

    async def _run_agents_parallel(self, query: str) -> dict[str, str]:
        """6エージェントを並列実行して回答を収集する。

        Args:
            query: ユーザーの質問

        Returns:
            各エージェント名をキー、回答を値とするdict
        """
        agents = {
            "dermatologist": self._dermatologist,
            "influencer": self._influencer,
            "gadget": self._gadget,
            "evidence": self._evidence,
            "supplement_pharma": self._supplement_pharma,
            "global_beauty": self._global_beauty,
        }

        # asyncio.gatherで並列実行
        tasks = {
            name: asyncio.create_task(agent.run(query))
            for name, agent in agents.items()
        }

        results: dict[str, str] = {}
        for name, task in tasks.items():
            try:
                results[name] = await task
            except Exception as e:
                print(f"  ✗ {name} エラー: {e}")
                results[name] = f"⚠ {name}の回答取得に失敗しました。エラー: {e}"

        return results
