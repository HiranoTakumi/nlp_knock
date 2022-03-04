import os
from logger_functions import *

from q30 import read_mecab_file

def _main():
    mecab_file_path = os.path.join(BASE_DIR, "asset", "neko.txt.mecab")
    mecab_map = read_mecab_file(mecab_file_path)

    words = {}
    for item in mecab_map['map']:
        if item['pos'] == "名詞":
             # or item['pos'] == "動詞" or item['pos'] == "形容詞" or item['pos'] == "形容動詞" or item['pos'] == "副詞" or item['pos'] == "連体詞":
            if item['base'] == "*":
                column = 'surface'
            else:
                column = 'base'
            if item[column] in words.keys():
                words[item[column]] += 1
            else:
                words[item[column]] = 1

    top_10 = sorted(words.items(), key=lambda x:x[1], reverse=True)[0:10]
    logger.info(f"\n{top_10}.")


if __name__ == "__main__":
    """
        文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
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
