import logging
from logging import Logger, getLogger, StreamHandler, FileHandler
import time
import traceback

def SetLogger(logPath) -> Logger:
    logger = getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')

    fhandler = FileHandler(filename=logPath)
    fhandler.setLevel(logging.DEBUG)
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)

    shandler = StreamHandler()
    shandler.setLevel(logging.INFO)
    shandler.setFormatter(formatter)
    logger.addHandler(shandler)
    return logger



def StartLog(logger: Logger, start: time) -> None:
    logger.info(time.strftime(
        'Start time: %b %d %Y %H:%M:%S', time.localtime(start)))
    pass  # end def


def EndLog(logger: Logger, start: time, end: time) -> None:
    logger.info(time.strftime(
        'End time: %b %d %Y %H:%M:%S', time.localtime(end)))
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    timelog = f'Batch time: {int(hours):0>2}:{int(minutes):0>2}:{seconds:05.3f}'
    logger.info(timelog)
    pass  # end def
