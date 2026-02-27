"""レポートフォーマッターモジュール"""

import os
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
            editor_response: 統括エディターの回答

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
