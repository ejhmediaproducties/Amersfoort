import core.core_permit as cp

"""
Main core module from where we can direct all the permitdata to the correct functions
"""

full_permits_list = {}
filepath_format = None


def makePermits(permits) -> None:
    """
    Generates permits objects
    :param permits:
    :return: None
    """
    global full_permits_list

    for p in permits:
        full_permits_list[p] = cp.CorePermit(p, filepath_format)


def getPermitsList() -> dict:
    """
    Return the list with all the permit objects
    :return: dictionary of permits
    """
    return full_permits_list


def generateFolderStructure():
    """
    Function yet to be scripted where we do things
    :return:
    """
    for p, i in full_permits_list.items():
        print(f"Nieuwe folderstructuur voor {i.permitID} wordt aangemaakt")
