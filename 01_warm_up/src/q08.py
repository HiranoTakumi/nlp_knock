import os
from logger_functions import *

def _main():
    text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    logger.info(f"text = {text}")
    coded_text = cipher(text)
    logger.info(f"coded text = {coded_text}")

def cipher(text: str) -> str:
    coded_text = ""
    for c in text:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            coded_text += chr(219 - ord(c))
        else:
            coded_text += c

    return coded_text

if __name__ == "__main__":
    """
        与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
            - 英小文字ならば(219 - 文字コード)の文字に置換
            - その他の文字はそのまま出力
        この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """

    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)

    # Loggerのスタート
    logPath = os.path.join(BASE_DIR, 'log')
    if not os.path.exists(logPath):
        os.mkdir(logPath)
    logger = SetLogger(os.path.join(logPath, 'log.log'))
    logger.info(os.path.abspath(__file__))
    logger_start = time.time()
    StartLog(logger, logger_start)

    # mainの実行
    _main()

    logger_end = time.time()
    EndLog(logger, logger_start, logger_end)
