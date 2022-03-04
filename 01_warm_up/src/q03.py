import os
from logger_functions import *

def _main():
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words_len = list(map(lambda x: len(x), sentence.replace(',', '').replace('.', '').split(' ')))

    logger.info(f"Input: {sentence}")
    logger.info(f"Ouput: {words_len}")


if __name__ == "__main__":
    """
        “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
        という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
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
