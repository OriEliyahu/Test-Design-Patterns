from ClientConnectionActions import ClientConnectionActions


class GameProccess():
    """
    this class responsible for the game process.
    """
    def __init__(self):
        self.ClientsConnection = 0

    def StartGameinit(self):
        self.ClientsConnection = ClientConnectionActions()
        self.ClientsConnection.ConnectToClients()


    def CheckEndGame(self):
        return (self.ClientsConnection.ReciveFromPlayer1() == 'EMPTY' or self.ClientsConnection.ReciveFromPlayer2() == 'EMPTY')
        

    def SendGuessesToPlayers(self):

        GuessPlayer1 = self.ClientsConnection.ReciveFromPlayer1()
        GuessPlayer2 = self.ClientsConnection.ReciveFromPlayer2()

        self.ClientsConnection.SendToPlayer1(GuessPlayer2)
        self.ClientsConnection.SendToPlayer2(GuessPlayer1)


    def PlayGame(self):
        self.ClientsConnection.SendToBothClients('START')

        while True:
            self.ClientsConnection.SendToBothClients('CONTINUE')

            self.SendGuessesToPlayers()

            if self.CheckEndGame():
                self.ClientsConnection.SendToBothClients('STOP')
                break
            
        self.ClientsConnection.CloseGame()
    


