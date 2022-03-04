import os
from logger_functions import *

from q05 import gen_n_gram

def _main():
    text_a = 'paraparaparadise'
    text_b = 'paragraph'
    X = set(gen_n_gram(text_a, 2))
    Y = set(gen_n_gram(text_b, 2))

    logger.info(f"X:\t{X}")
    logger.info(f"Y:\t{Y}")

    logger.info(f"Union set:\t{X|Y}")
    logger.info(f"Intersection set:\t{X&Y}")
    logger.info(f"Deference set:\t{X-Y}")

    logger.info(f"`se` in X:\t{'se' in X}")
    logger.info(f"`se` in Y:\t{'se' in Y}")

if __name__ == "__main__":
    """
        “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
        さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ
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
