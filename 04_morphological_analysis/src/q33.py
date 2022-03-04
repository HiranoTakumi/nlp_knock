import os
from logger_functions import *

from q30 import read_mecab_file

def _main():
    mecab_file_path = os.path.join(BASE_DIR, "asset", "neko.txt.mecab")
    mecab_map = read_mecab_file(mecab_file_path)

    noun_phrases = []
    first_noun = ""
    connector = False
    second_noun = ""
    for item in mecab_map['map']:
        if item['pos'] == "名詞":
            if connector:
                second_noun = item['surface']
                noun_phrases.append(f"{first_noun}の{second_noun}")
                first_noun = second_noun
                second_noun = ""
                connector = False
            else:
                first_noun = item['surface']

        else:
            connector = (item['surface'] == "の" and first_noun != "")
            if not connector:
                first_noun = ""

    noun_phrases_str = "\n".join(noun_phrases)
    output_path = os.path.join(BASE_DIR, "asset", "noun_phrases.txt")
    with open(output_path, "w") as f:
        f.write(noun_phrases_str)

    logger.info(f"noun phrases count = {len(noun_phrases)}")


if __name__ == "__main__":
    """
        2つの名詞が「の」で連結されている名詞句を抽出せよ．
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
