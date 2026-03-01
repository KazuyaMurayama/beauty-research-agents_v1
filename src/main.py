"""美容リサーチエージェントシステムのエントリーポイント。"""

import asyncio
import sys

from dotenv import load_dotenv

from src.orchestrator import Orchestrator
from src.utils.report_formatter import ReportFormatter


def main() -> None:
    """CLIアプリケーションのメイン関数。"""
    # .envファイルから環境変数を読み込み
    load_dotenv()

    print("=" * 60)
    print("  美容・アンチエイジング マルチエージェント リサーチシステム")
    print("  6人の専門家が並列分析し、統合レポートを自動生成します")
    print("=" * 60)

    # クエリの取得（引数またはインタラクティブ入力）
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        print("\n美容・アンチエイジングに関する質問を入力してください:")
        query = input("> ").strip()

    if not query:
        print("質問が入力されませんでした。終了します。")
        sys.exit(1)

    # オーケストレーターを実行
    orchestrator = Orchestrator()
    filepath = asyncio.run(orchestrator.run(query))

    # レポートをGitHubにpushして直リンクを表示
    formatter = ReportFormatter()
    print("\n🚀 GitHubにアップロード中...")
    github_url = formatter.push_and_get_github_url(filepath)

    print(f"\n{'='*60}")
    print(f"✅ レポートが生成されました: {filepath}")
    if github_url:
        print(f"\n📎 GitHub: {github_url}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
