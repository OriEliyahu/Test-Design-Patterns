import socket

class ClientConnectionActions():
    """
    this class are type of mini facade that control about socket communication with client side
    """

    def __init__(self):
        self.server_socket = self.CreateServerSocket()
        self.Player1_socket = 0
        self.Player2_socket = 0


    def CreateServerSocket(self):
        HostName = socket.gethostname()
        server_socket = socket.socket()
        server_socket.bind((HostName, 12345))
        server_socket.listen(1)
        return server_socket

    def ConnectToClients(self):
        print('Wating for connection ...')
        self.Player1_socket , AddressPlayer1 = self.server_socket.accept()
        self.Player2_socket , AddressPlayer2 = self.server_socket.accept()
        print('Got connection from : ' + str(AddressPlayer1) + " " + str(AddressPlayer2))


    def SendToBothClients(self, data):
            self.Player1_socket.send(data.encode('UTF-8'))
            self.Player2_socket.send(data.encode('UTF-8'))



    def SendToPlayer1(self, data):
        self.Player1_socket.send(data.encode('UTF-8'))

    def SendToPlayer2(self, data):
        self.Player2_socket.send(data.encode('UTF-8'))



    def ReciveFromPlayer1(self):
        return self.Player1_socket.recv(1024).decode('UTF-8')

    def ReciveFromPlayer2(self):
        return self.Player2_socket.recv(1024).decode('UTF-8')



    def CloseGame(self):
        self.Player1_socket.close()
        self.Player2_socket.close()
        self.server_socket.close()
