import os
from logger_functions import *

def _main():
    file_path = os.path.join(BASE_DIR, 'asset', 'popular-names.txt')
    with open(file_path) as f:
        text = f.read()

    logger.info(len(text.split("\n")))


if __name__ == "__main__":
    """
        行数をカウントせよ．確認にはwcコマンドを用いよ．
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
