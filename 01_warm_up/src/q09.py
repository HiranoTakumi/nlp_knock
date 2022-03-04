import os
import random
import time
from logger_functions import *

def _main():
    text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = text.split(' ', '')
    logger.info(f"text = {text}")
    
    coded_text = cipher(text)
    logger.info(f"coded text = {coded_text}")

    print(make_typoglycemia_word('hearts'))

def make_typoglycemia_word(word: str) -> str:
    if len(word) < 5:
        return word
    else:
        random_word = word[0]
        idx_list = [i+1 for i in range(len(word)-2)]
        random_idx = random.sample(idx_list, len(idx_list))
        for idx in random_idx:
            random_word += word[idx]
        random_word += word[-1]

        return random_word

if __name__ == "__main__":
    """
        スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
        ただし，長さが４以下の単語は並び替えないこととする．
        適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
    """

    BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
    random_seed = time.time()
    random.seed(random_seed)

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
