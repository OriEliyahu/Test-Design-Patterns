from ClientConnectionActions import ClientConnectionActions


class GameProccess():
    """
    this class responsible for the game process.
    """
    def __init__(self):
        self.PlayersConnection = 0 # null

    def StartGameinit(self): # initialization the game
        self.PlayersConnection = ClientConnectionActions()
        self.PlayersConnection.ConnectToPlayers()


    def CheckEndGame(self): # return true if one of the players are lose
        return (self.PlayersConnection.ReciveFromPlayer1() == 'EMPTY' or self.PlayersConnection.ReciveFromPlayer2() == 'EMPTY')
        

    def SendGuessesToPlayers(self): # this function are send the guesses between the players

        GuessPlayer1 = self.PlayersConnection.ReciveFromPlayer1()
        GuessPlayer2 = self.PlayersConnection.ReciveFromPlayer2()

        self.PlayersConnection.SendToPlayer1(GuessPlayer2)
        self.PlayersConnection.SendToPlayer2(GuessPlayer1)


    def PlayGame(self):
        self.PlayersConnection.SendToBothPlayers('START')

        while True:
            self.PlayersConnection.SendToBothPlayers('CONTINUE')

            self.SendGuessesToPlayers()

            if self.CheckEndGame():
                self.PlayersConnection.SendToBothPlayers('STOP')
                break
            
        self.PlayersConnection.CloseGame()
    


