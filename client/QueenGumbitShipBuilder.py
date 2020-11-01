from Ship import Ship

# builder pattern
class QueenGumbitBuilder():
    """
    dhis class building ship from QueenGumbit type.
    """
    def __init__(self):
        self.ship = Ship()

    def BuildShipColor(self):
        self.ship.SetShipColor("Black")
    
    def BuildShipName(self):
        self.ship.SetShipName("Queen Gumbit")

    def GetShip(self):
        return self.ship