import argparse
import os
from logger_functions import *

def _main():
    args = arg_requirement("入力された文字を逆に（末尾から先頭に向かって）並べた文字列を得る")
    reversed = reverse_word(args.word)
    logger.info(f"Input: {args.word}")
    logger.info(f"Ouput: {reversed}")

def reverse_word(word: str) -> str:
    word_len = len(word)
    reversed = ''
    i = 0
    for i in range(len(word)):
        reversed += word[-(i+1)]
    return reversed

def arg_requirement(description: str) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('word', help='入力する文字')
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    """
        文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
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
