import os
from logger_functions import *

def _main():
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    single_mark_idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    words = sentence.replace(',', '').replace('.', '').split(' ')
    mark_dict = {}
    i = 0
    for i in range(len(words)):
        if i+1 in single_mark_idx:
            mark_dict[words[i][:1]] = i+1
        else:
            mark_dict[words[i][:2]] = i+1


    logger.info(f"Input: {sentence}")
    logger.info(f"Ouput: {mark_dict}")


if __name__ == "__main__":
    """
        “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
        という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
        取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ
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
