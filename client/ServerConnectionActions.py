import socket

class ServerConnectionActions():
    """
    this class are type of mini facade that control about socket communication with server side
    """
    def __init__(self):
        self.PlayerSocket = self.ConnectToServer()

    def ConnectToServer(self):
        HostName = socket.gethostname()
        PlayerSocket = socket.socket()
        PlayerSocket.connect((HostName, 12345))
        return PlayerSocket

    def SendToServer(self, data):
        self.PlayerSocket.send(data.encode('UTF-8'))

    def ReciveFromServer(self):
        return self.PlayerSocket.recv(1024).decode('UTF-8')

    def CloseGame(self):
        self.PlayerSocket.close()