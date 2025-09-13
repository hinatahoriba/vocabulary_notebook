import os
import deepl
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からDeepL APIキーを取得
api_key = os.getenv("DEEPL_API_KEY")

if not api_key:
    # APIキーが設定されていない場合は、プログラムを終了する
    raise ValueError("エラー: .envファイルに 'DEEPL_API_KEY' が設定されていません。")

# 翻訳クライアントを初期化（一度だけ行う）
try:
    translator = deepl.Translator(api_key)
except deepl.exceptions.DeepLException as e:
    raise RuntimeError(f"DeepL APIクライアントの初期化に失敗しました: {e}")

def translate_japanese_to_english(text_to_translate: str) -> str:
    """
    日本語のテキストをDeepL APIで英語に翻訳し、結果の文字列を返します。

    Args:
        text_to_translate (str): 翻訳したい日本語の文字列。

    Returns:
        str: 翻訳された英語の文字列。

    Raises:
        deepl.exceptions.DeepLException: 翻訳中にAPIエラーが発生した場合。
    """
    try:
        # 翻訳を実行。DeepLが元の言語を自動検出
        result = translator.translate_text(text_to_translate, target_lang="EN-US")
        return result.text
    except deepl.exceptions.DeepLException as e:
        print(f"翻訳中にエラーが発生しました: {e}")
        # エラー発生時は、例外を再発生させるか、空文字列などを返す
        raise

# ----------------------------------------------------
# 関数の呼び出しと動作確認
# ----------------------------------------------------
if __name__ == "__main__":
    try:
        japanese_text = "桜が満開です。とても美しい。"
        translated_text = translate_japanese_to_english(japanese_text)

        print(f"元のテキスト: {japanese_text}")
        print(f"翻訳結果: {translated_text}")

        print("-" * 20)

        japanese_text_2 = "この関数は、引数として日本語の文字列を受け取ります。"
        translated_text_2 = translate_japanese_to_english(japanese_text_2)

        print(f"元のテキスト: {japanese_text_2}")
        print(f"翻訳結果: {translated_text_2}")

    except (ValueError, RuntimeError, deepl.exceptions.DeepLException) as e:
        print(f"プログラムの実行中に致命的なエラーが発生しました: {e}")