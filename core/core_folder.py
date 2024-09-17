import os

"""
This module contains all the functions related to folder operations
"""


def makeFolder(path:str, foldername:str) -> None:
    """
    Create the folder if it doesn't exist
    :param path: path to the new folder
    :param foldername: name of the new folder
    :return:
    """
    if not os.path.exists(os.path.join(path, foldername)):
        os.makedirs(os.path.join(path, foldername))