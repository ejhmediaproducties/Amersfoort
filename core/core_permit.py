class CorePermit(object):
    """
    Core Permit Module which is the blueprint for all the permit objects
    """

    def __init__(self, permitID:str, filepath_format:str) -> None:
        self.permitID = permitID
        self.straatnaam = None
        self.postcode = None
        self.plaatsnaam = None
        self.bouwjaar = None
        self.filepath = filepath_format.replace("{permitID}", permitID)

    def setStraatnaam(self, straatnaam:str) -> None:
        # Hier kan nog een controle komen of de straatnaam volgens het juiste format is
        self.straatnaam = straatnaam

    def setPostcode(self, postcode:str) -> None:
        self.postcode = postcode

    def setPlaatsnaam(self, plaatsnaam:str) -> None:
        self.plaatsnaam = plaatsnaam

    def setBouwjaar(self, bouwjaar:str) -> None:
        self.bouwjaar = bouwjaar

