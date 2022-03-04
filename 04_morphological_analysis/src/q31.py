import os
from logger_functions import *

from q30 import read_mecab_file

def _main():
    mecab_file_path = os.path.join(BASE_DIR, "asset", "neko.txt.mecab")
    mecab_map = read_mecab_file(mecab_file_path)

    verbs_surface = []
    for item in mecab_map['map']:
        if item['pos'] == "動詞":
            verbs_surface.append(item['surface'])

    verbs_str = "\n".join(verbs_surface)
    output_path = os.path.join(BASE_DIR, "asset", "verbs_surface.txt")
    with open(output_path, "w") as f:
        f.write(verbs_str)

    logger.info(f"verbs count = {len(verbs_surface)}")


if __name__ == "__main__":
    """
        動詞の表層形をすべて抽出せよ．
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
