import socket
import threading
import sys
#str_path = "D://School Project//Python//DataBase_Codes//"
#str_path1 = "C://School Project//Python//DataBase_Codes//"
#sys.path.insert(1,str_path1)
sys.path.append("E:\School Project\Python")
from DataBase_Codes import UserDB
from DataBase_Codes import Viruses_HashDB
import os
import hashlib


class server(object):
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
                clientSocket, client_addresses = self.sock.accept()
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
                    if arr!= None and arr[0]=="Login" and len(arr)==3:
                        server_data = UserDB.users().check_user_by_Username_and_Password(arr[1],arr[2])
                        print("server data:", server_data)
                        if server_data == True:
                            client_socket.send(f"Welcome {arr[1]}".encode())
                        elif server_data == False:
                            client_socket.send("Username or Password are incorrect".encode())
                    elif arr != None and arr[0]=="Register" and len(arr)==4:
                        print("Register")
                        print(arr)
                        server_data = UserDB.users().check_user_by_Username(arr[2])
                        if server_data == True:
                            client_socket.send("The user already exists".encode())
                        elif server_data == False:
                            answer = UserDB.users().insert_user(arr[1],arr[2],arr[3])
                            print(answer)
                            client_socket.send("User created successfully".encode())
                    else:
                        server_data = "False"
                    
                    server_data_scan = client_socket.recv(1024).decode('utf-8')
                    if server_data_scan == "Scan":
                        server_data_length = client_socket.recv(10).decode()
                        server_data_hashes = client_socket.recv(server_data_length).decode()
                        arr_hashes = server_data_hashes.split(",")
                        arr_virus_hashes=[]
                        for hash in arr_hashes:
                            file_hash = hash
                            if file_hash in Viruses_HashDB.hashes():
                                arr_virus_hashes.append(file_hash)
                        length = str(len(arr_virus_hashes)).zfill(10)
                        str_virus_hashes = ",".join(arr_virus_hashes)
                        data = length+str_virus_hashes
                        client_socket.send(data.encode())
                    else:
                        server_data = "False"

                except Exception as e:
                    print("Error",e)
                    not_crash = False
                    break


if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 6060
    s = server(ip,port)
    s.start()



