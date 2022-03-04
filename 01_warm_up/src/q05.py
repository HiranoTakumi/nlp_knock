import argparse
import os
from logger_functions import *

def _main():
    args = arg_requirement("N-gramを作成")
    n = int(args.n)
    sentence = "I am an NLPer"
    words = sentence.replace(',', '').replace('.', '').split(' ')
    n_gram_word = gen_n_gram(words, n)
    n_gram_char = gen_n_gram(sentence, n)

    logger.info(f"Input: {sentence}")
    logger.info(f"word {n}-gram: {n_gram_word}")
    logger.info(f"char {n}-gram: {n_gram_char}")

def gen_n_gram(sentence, n: int) -> list:
    results = []
    i = 0
    for i in range(len(sentence)):
        if len(sentence[i:n+i]) < n: break
        results.append(sentence[i:n+i])

    return results

def arg_requirement(description: str) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('n', help='分割数')
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    """
        与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
        この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
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
