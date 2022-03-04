import os
from logger_functions import *

def _main():
    word = 'パタトクカシーー'
    extracted = word[0] + word[2] + word [4] + word[6]
    logger.info(f"Input: {word}")
    logger.info(f"Ouput: {extracted}")


if __name__ == "__main__":
    """
        「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
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
