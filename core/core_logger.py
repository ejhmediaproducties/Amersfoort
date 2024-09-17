import logging
import core.core_folder as cf
from datetime import datetime

"""
This module contains all the functions related to logging operations
"""


def initLog(town:str) -> None:
    """
    Initialize the log file
    :param town:
    :return:
    """

    # Make a new folder for the town if it doesn't exist
    cf.makeFolder("logs", town)

    # Make and configurate a new log file
    logging.basicConfig(filename='logs/' + town + '/logs_' + (datetime.now().strftime("%Y%m%d")) + '.txt',
                        level=logging.INFO,
                        format='%(levelname)s - %(message)s')


def createLog(msg: str, level: str = 'info') -> None:
    """
    Create a new log entrence with given message and level
    :param msg:
    :param level: info | warning | error
    :return:
    """
    if level == 'info':
        logging.info(msg)
    elif level == 'warning':
        logging.warning(msg)
    elif level == 'error':
        logging.error(msg)
