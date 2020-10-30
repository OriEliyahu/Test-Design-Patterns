from ShipsBuilder import ShipsBuilder
from QueenGumbitShipBuilder import QueenGumbitBuilder

class SetupGame():
    """
    this class are responsible to create Ships list for the player and init the game.
    """
    def __init__(self):
        self.Ship = self.CreateShip()
        self.PlayerShipDict = {}

    def CreateShip(self):
        shipbuilder = ShipsBuilder(QueenGumbitBuilder())
        shipbuilder.ConstructShip()
        return shipbuilder.GetShip()

    def AddShipsPosition(self):
        while len(self.PlayerShipDict) < 10:

            ShipBoardPosition = input("please enter a number for ship position: ")

            if self.CheckPositionNumber(ShipBoardPosition): #check if the input is a good number
                self.PlayerShipDict[ShipBoardPosition] =  self.Ship
                print("Added")

            else:
                print("Error at position number")


    def CheckPositionNumber(self, ShipBoardPosition):

        if ShipBoardPosition.isnumeric():
            if int(ShipBoardPosition) > 0 and int(ShipBoardPosition) < 101:
                if ShipBoardPosition not in self.PlayerShipDict.keys():
                    return True
        return False

    def GetPlayerShipDict(self):
        return self.PlayerShipDict

    def ShowGameBoard(self):
        Row1 = "---------------------------------------------------\n"
        Row2 = "| 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 |\n---------------------------------------------------\n"
        Row3 = "| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |\n---------------------------------------------------\n"
        Row4 = "| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |\n---------------------------------------------------\n"
        Row5 = "| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |\n---------------------------------------------------\n"
        Row6 = "| 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |\n---------------------------------------------------\n"
        Row7 = "| 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 |\n---------------------------------------------------\n"
        Row8 = "| 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 |\n---------------------------------------------------\n"
        Row9 = "| 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 |\n---------------------------------------------------\n"
        Row10 = "| 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 |\n---------------------------------------------------\n"
        Row11 = "| 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 |100 |\n"
        Row12 = "---------------------------------------------------"
        TotalBoard = Row1+Row2+Row3+Row4+Row5+Row6+Row7+Row8+Row9+Row10+Row11+Row12
        print('Your Board:\n' + TotalBoard)


