import os
from logger_functions import *

from q30 import read_mecab_file

def _main():
    mecab_file_path = os.path.join(BASE_DIR, "asset", "neko.txt.mecab")
    mecab_map = read_mecab_file(mecab_file_path)

    noun_sentence = ""
    noun_stream_count = 0
    longest_noun_sentence = ""
    longest_noun_stream_count = 0

    for item in mecab_map['map']:
        if item['pos'] == "名詞":
            noun_sentence += item['surface']
            noun_stream_count += 1
        else:
            if noun_stream_count > longest_noun_stream_count:
                print(noun_sentence)
                print(noun_stream_count)
                longest_noun_sentence = noun_sentence
                longest_noun_stream_count = noun_stream_count

            noun_sentence = ""
            noun_stream_count = 0

    logger.info(f"The longest noun sentence is {longest_noun_sentence}. count = {longest_noun_stream_count}")


if __name__ == "__main__":
    """
        名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
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
