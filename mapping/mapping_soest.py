import core.core_main as cm

"""
This file contains all the mapping actions needed to feed the core modules
"""


# This function is required in the mapping module
def startMapping() -> None:
    print("Start mapping module Soest...")

    # In de mapping bepalen we de specifieke paden per gemeente
    cm.filepath_format = "/iets/ergens/{permitID}/"

    #Voorbeeld van hoe we nieuwe objecten maken
    permit_list = ["1200", "1201", "1202", "1203", "1204", "1205", "1206"] #deze data kan uit een XML komen
    cm.makePermits(permit_list)

    # Haal alle permits objecten terug
    full_pm = cm.getPermitsList()

    # Vul ieder permitobject met de juiste data
    full_pm["1201"].setStraatnaam("Amersfoortseweg")

    # Uiteindelijk kunnen we de permitdata lezen, en verwerken
    #print(full_pm["1201"].filepath)
    cm.generateFolderStructure()

