import MeCab
import os
import re
from logger_functions import *

def _main():
    file_path = os.path.join(BASE_DIR, "asset", "neko.txt")
    with open(file_path) as f:
        text = f.read()

    mecab_path = os.path.join(BASE_DIR, "default")
    tagger = MeCab.Tagger(f"-d {mecab_path}")
    parse = tagger.parse(text)

    output_path = os.path.join(BASE_DIR, "asset", "neko.txt.mecab")
    with open(output_path, "w") as f:
        f.write(parse)

    mecab_map = read_mecab_file(output_path)
    logger.info(len(mecab_map['map']))

def read_mecab_file(path: str) -> dict:
    with open(path) as f:
        parse = f.read()

    mecab_map = {'map': []}
    lines = parse.split("\n")
    items = [re.split('[\t,]', line) for line in lines]
    for item in items:
        if len(item) < 2: continue
        info = {
            'surface'   : item[0],
            'base'      : item[7],
            'pos'       : item[1],
            'pos1'      : item[2]
        }
        mecab_map['map'].append(info)

    return mecab_map

if __name__ == "__main__":
    """
        形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
        ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
        第4章の残りの問題では，ここで作ったプログラムを活用せよ．
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
