import os
import matplotlib.pyplot as plt
from logger_functions import *

from q30 import read_mecab_file

def _main():
    mecab_file_path = os.path.join(BASE_DIR, "asset", "neko.txt.mecab")
    mecab_map = read_mecab_file(mecab_file_path)

    words = {}
    for item in mecab_map['map']:
        if item['base'] == "*":
            column = 'surface'
        else:
            column = 'base'
        if item[column] in words.keys():
            words[item[column]] += 1
        else:
            words[item[column]] = 1


    data = list(words.values())
    plt.hist(data, bins=500, range=(0, 500), log=True)
    plt.show()


if __name__ == "__main__":
    """
        単語の出現頻度のヒストグラムを描け．
        ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
        縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
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
