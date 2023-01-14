import socket
import threading
from DataBase_Codes import UserDB as UDB
#from UDB import UserDB

class Server(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.count = 0
        self.running = True

    def start(self):
        try:
            print(f"server starting up on ip {self.ip} port {self.port}")
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.ip,self.port))
            self.sock.listen(3)

            while True:
                print("Watinig for a new client")
                clientSocket, client_addresses = self.socket.accept()
                print("new client entered")
                clientSocket.send("Hello, this is server".encode())
                self.count += 1
                print(self.count)
                self.handleClient(clientSocket, self.count)
        except socket.error as e:
            print(e)

    def handleClient(self,clientSock,current):
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
        client_handler.start()

    def handle_client_connection(self, client_socket, current):
        not_crash = True
        while self.running:
            while not_crash:
                try:
                    server_data = client_socket.recv(1024).decode('utf-8')
                    arr = server_data.split(",")
                    print(server_data)
                    if arr!= None and arr[0]=="Login" and len(arr)==3:
                        print("Login\n"+arr)
                        server_data = self.UserDB.check_user_by_Username_and_Password()
                except:
                    print("error")
                    not_crash = False
                    break