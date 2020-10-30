class ShipsBuilder():
    """
    this class are building many types of ships.
    """
    def __init__(self, ShipTypeBuilder):
        self.ShipTypeBuilder = ShipTypeBuilder

    def ConstructShip(self):
        self.ShipTypeBuilder.BuildShipColor()
        self.ShipTypeBuilder.BuildShipName()

    def GetShip(self):
        return self.ShipTypeBuilder.GetShip()
