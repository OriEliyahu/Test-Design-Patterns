
from GameSetupControl import SetupGame
from ServerConnectionActions import ServerConnectionActions

class GameProccess():
    """
    this class responsible for the game process.
    """
    def __init__(self):
        self.GamePreparation = SetupGame()
        self.ServerConnection = 0 #null
        self.PlayerShipsDict = {}

    def StartGameinit(self):
        self.GamePreparation.ShowGameBoard()
        self.GamePreparation.AddShipsPosition()
        self.PlayerShipsDict = self.GamePreparation.GetPlayerShipDict()
        self.ServerConnection = ServerConnectionActions()

    def PlayGame(self):
        self.WaitForConnection()
        
        while self.ServerConnection.ReciveFromServer() != 'STOP':
            GuessingBoardPosition = input('enter number for position guessing: ')

            self.ServerConnection.SendToServer(GuessingBoardPosition)
            EnemyGuessPosition = self.ServerConnection.ReciveFromServer()

            self.CheckEnemyGuess(EnemyGuessPosition)
            self.SendStatusGameToServer()
        
        self.CheckWin()
        self.ServerConnection.CloseGame()



    def WaitForConnection(self):
        while self.ServerConnection.ReciveFromServer() != 'START':
            pass
        print("Got Connection!")



    def CheckEnemyGuess(self, EnemyGuessPosition):
        if EnemyGuessPosition in self.PlayerShipsDict.keys():
            del self.PlayerShipsDict[EnemyGuessPosition]

    def SendStatusGameToServer(self):
        if len(self.PlayerShipsDict) == 0:
            self.ServerConnection.SendToServer('EMPTY')
            print('You Lose')

        else:
            self.ServerConnection.SendToServer('NOT EMPTY')
        

    def CheckWin(self):
        if len(self.PlayerShipsDict) > 0:
            print('You Won!')



            


        
    












