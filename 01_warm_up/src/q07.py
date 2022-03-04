import argparse
import os
from logger_functions import *

def _main():
    args = arg_requirement("Inputs")
    logger.info(f"x={args.x}, y={args.y}, z={args.z}")
    logger.info(f"{args.x}時の{args.y}は{args.z}")


def arg_requirement(description: str) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('x', help='時間')
    parser.add_argument('y', help='コンテンツ')
    parser.add_argument('z', help='値')

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    """
        引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
        さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
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
