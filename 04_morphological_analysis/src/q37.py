import MeCab
import os
import re
from logger_functions import *

from q30 import read_mecab_file

def _main():
    file_path = os.path.join(BASE_DIR, "asset", "neko.txt")
    with open(file_path) as f:
        text = f.read()

    mecab_path = os.path.join(BASE_DIR, "default")
    tagger = MeCab.Tagger(f"-d {mecab_path}")
    words = {}

    for sentence in text.split("\n"):
        if "猫" in sentence:
            parse = tagger.parse(sentence)
            lines = parse.split("\n")
            items = [re.split('[\t,]', line) for line in lines]
            for item in items:
                if len(item) < 2: continue
                if item[0] == "猫": continue
                if item[1] == "名詞":
                    if item[7] in words.keys():
                        words[item[7]] += 1
                    else:
                        words[item[7]] = 1

    top_10 = sorted(words.items(), key=lambda x:x[1], reverse=True)[0:10]
    logger.info(f"\n{top_10}.")


if __name__ == "__main__":
    """
        「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
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
