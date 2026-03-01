"""レポートフォーマッターモジュール"""

import os
import subprocess
from datetime import datetime


class ReportFormatter:
    """最終レポートをMarkdown形式にフォーマットし、ファイル出力するクラス。"""

    OUTPUT_DIR = "output"

    def __init__(self) -> None:
        """ReportFormatterを初期化する。"""
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)

    def format_report(
        self,
        query: str,
        dermatologist_response: str,
        supplement_pharma_response: str,
        influencer_response: str,
        gadget_response: str,
        global_response: str,
        evidence_response: str,
        editor_response: str,
    ) -> str:
        """各エージェントの回答を統合してMarkdownレポートを生成する。

        Args:
            query: ユーザーの質問
            dermatologist_response: 美容皮膚科医の回答
            supplement_pharma_response: サプリ・医薬品アドバイザーの回答
            influencer_response: 美容インフルエンサーの回答
            gadget_response: 美容家電オタクの回答
            global_response: 海外美容トレンドハンターの回答
            evidence_response: 論文リサーチャーの回答
            editor_response: 統括エディターの統合分析（サマリー＋総合評価＋アクションプラン）

        Returns:
            フォーマットされたMarkdownレポート文字列
        """
        today = datetime.now().strftime("%Y-%m-%d")

        report = f"""# 美容リサーチレポート
> 生成日: {today}
> クエリ: {query}

## エグゼクティブサマリー

{editor_response}

---

## 1. 医学的見解（美容皮膚科医）

{dermatologist_response}

---

## 2. サプリメント・医薬品ガイド

{supplement_pharma_response}

---

## 3. トレンド・実用ガイド（美容インフルエンサー）

{influencer_response}

---

## 4. 美容家電・デバイス分析（家電オタク）

{gadget_response}

---

## 5. 海外トレンド・グローバル知見

{global_response}

---

## 6. エビデンス・論文レビュー

{evidence_response}

---

## 参考文献・出典

各セクション内の引用・出典をご参照ください。

---

## 免責事項

本レポートは情報提供を目的としたものであり、医療行為の推奨ではありません。
医薬品の使用、特に海外医薬品の個人輸入については、必ず医師・薬剤師にご相談ください。
個人輸入は自己責任となり、健康被害が生じた場合の救済制度（医薬品副作用被害救済制度）の対象外となる可能性があります。
"""
        return report

    def save_report(self, report: str) -> str:
        """レポートをファイルに保存する。

        Args:
            report: Markdownレポート文字列

        Returns:
            保存されたファイルのパス
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"report_{timestamp}.md"
        filepath = os.path.join(self.OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(report)

        return filepath

    def push_and_get_github_url(self, filepath: str) -> str | None:
        """レポートをgit commit & pushし、GitHub上の直リンクを返す。

        Args:
            filepath: レポートファイルのパス

        Returns:
            GitHubのblobページURL。失敗時はNone。
        """
        try:
            filename = os.path.basename(filepath)
            # .gitignoreからoutput/*.mdを除外する必要がある場合は-fで強制add
            subprocess.run(
                ["git", "add", "-f", filepath],
                check=True, capture_output=True, text=True,
            )
            subprocess.run(
                ["git", "commit", "-m", f"report: {filename}"],
                check=True, capture_output=True, text=True,
            )

            # ブランチ名を取得
            branch_result = subprocess.run(
                ["git", "branch", "--show-current"],
                check=True, capture_output=True, text=True,
            )
            branch = branch_result.stdout.strip()

            # push（リトライ付き）
            pushed = False
            for attempt in range(4):
                result = subprocess.run(
                    ["git", "push", "-u", "origin", branch],
                    capture_output=True, text=True,
                )
                if result.returncode == 0:
                    pushed = True
                    break
                import time
                time.sleep(2 ** (attempt + 1))

            if not pushed:
                print("  ⚠ git push に失敗しました")
                return None

            # GitHub URLを構築
            # remote URLからオーナー/リポ名を抽出
            remote_result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                check=True, capture_output=True, text=True,
            )
            remote_url = remote_result.stdout.strip()

            # URLパターン: .../git/OWNER/REPO or github.com/OWNER/REPO
            owner, repo = self._parse_github_owner_repo(remote_url)
            if owner and repo:
                github_url = (
                    f"https://github.com/{owner}/{repo}/blob/{branch}/{filepath}"
                )
                return github_url
            return None
        except Exception as e:
            print(f"  ⚠ GitHub公開に失敗: {e}")
            return None

    @staticmethod
    def _parse_github_owner_repo(remote_url: str) -> tuple[str, str]:
        """git remote URLからオーナーとリポジトリ名を抽出する。

        Args:
            remote_url: git remote URL

        Returns:
            (owner, repo) のタプル。取得できない場合は空文字。
        """
        # http(s)://.../.../OWNER/REPO(.git)
        # or git@github.com:OWNER/REPO.git
        import re

        # プロキシURL: http://...@.../git/OWNER/REPO
        match = re.search(r"/git/([^/]+)/([^/\s]+?)(?:\.git)?$", remote_url)
        if match:
            return match.group(1), match.group(2)

        # 標準GitHub URL: github.com/OWNER/REPO
        match = re.search(r"github\.com[:/]([^/]+)/([^/\s]+?)(?:\.git)?$", remote_url)
        if match:
            return match.group(1), match.group(2)

        return "", ""
