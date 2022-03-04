import os
from logger_functions import *

def _main():
    word_1 = 'パトカー'
    word_2 = 'タクシー'
    i = 0
    merged = ''
    for i in range(len(word_1)):
        merged += word_1[i] + word_2[i]
    logger.info(f"Input: {word_1}, {word_2}")
    logger.info(f"Ouput: {merged}")


if __name__ == "__main__":
    """
        「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
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
