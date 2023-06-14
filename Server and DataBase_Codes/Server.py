import socket
import threading
import UserDB
import Viruses_HashDB
import traceback
import HistoryDB
import os
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import signal
import sys

class server(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.client_count = 0
        self.running = True
        self.connected_clients = {}

    def start(self):
        def signal_handler(sig, frame):
            print('Closing server...')
            self.sock.close()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)


        try:
            print(f"server starting up on ip {self.ip} port {self.port}")
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.ip,self.port))
            self.sock.listen(10)

            while True:
                filename1 = "receiver.pem"
                filename2 = "private.pem"
                self.key = RSA.generate(2048)
                if os.path.isfile(filename1) and os.path.isfile(filename2):
                    file1 = open("receiver.pem","r")
                    self.public_key_bytes = file1.read().encode()
                    file2 = open("private.pem","r")
                    self.private_key_bytes = file2.read().encode()
                else:
                    self.private_key_bytes = self.key.export_key()
                    file_out = open("private.pem", "wb")
                    file_out.write(self.private_key_bytes)
                    file_out.close()

                    self.public_key_bytes = self.key.publickey().export_key()
                    file_out = open("receiver.pem", "wb")
                    file_out.write(self.public_key_bytes)
                    file_out.close()

                self.public_key = RSA.import_key(self.public_key_bytes)
                self.private_key = RSA.import_key(self.private_key_bytes)
                clientSocket, addr = self.sock.accept()
                clientSocket.send("Hello, this is server".encode())
                clientSocket.send(self.public_key_bytes)
                self.handleClient(clientSocket,self.public_key,self.private_key,addr)
        except socket.error as e:
            print(e)

    def handleClient(self,clientSock,public_key,private_key,addr):
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, public_key, private_key,addr,))
        client_handler.start()

    

    def handle_client_connection(self, client_socket, public_key, private_key,addr):
        
        def send_message(message):
            length = str(len(message)).zfill(10)
            data = length+message
            client_socket.send(data.encode())
        
        def send_message_arr(arr):
            str_arr = ",".join(arr)
            length = str(len(str_arr)).zfill(10)
            data = length+str_arr
            client_socket.send(data.encode())

        def recv_message():
            length = client_socket.recv(10).decode()
            encoded_data = client_socket.recv(int(length)).decode()
            decoded_data = base64.b64decode(encoded_data.encode())
            cipher = PKCS1_OAEP.new(self.private_key)
            decrypted_data = cipher.decrypt(decoded_data)
            return decrypted_data.decode()
        
        def recv_message_arr():
            length = client_socket.recv(10).decode()
            encoded_str_arr = client_socket.recv(int(length)).decode()
            decoded_data = base64.b64decode(encoded_str_arr.encode())
            cipher = PKCS1_OAEP.new(self.private_key)
            decrypted_data = cipher.decrypt(decoded_data)
            data = decrypted_data.decode()
            arr = data.split(",")
            return arr

        def decrypt_data(enc_session_key, nonce, tag, ciphertext):
            # Decrypt the session key with the private RSA key
            private_key = RSA.import_key(open("private.pem").read())
            cipher_rsa = PKCS1_OAEP.new(private_key)
            session_key = cipher_rsa.decrypt(enc_session_key)

            # Decrypt the data with the AES session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)

            return data
        
        def recv_data():
            enc_session_key = client_socket.recv(256)
            nonce = client_socket.recv(16)
            tag = client_socket.recv(16)
            ciphertext = client_socket.recv(4096)

            # Decrypt the received data
            data = decrypt_data(enc_session_key, nonce, tag, ciphertext)
            print("Received data from client:", data.decode("utf-8"))
            return data.decode("utf-8")

        def encrypt_data(data):
            # Encrypt the data
            recipient_key = RSA.import_key(open("receiver.pem").read())
            session_key = get_random_bytes(16)

            # Encrypt the session key with the public RSA key
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            enc_session_key = cipher_rsa.encrypt(session_key)

            # Encrypt the data with the AES session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)

            return enc_session_key, cipher_aes.nonce, tag, ciphertext
    

        def send_data(data):
            # Select a file to encrypt and send
            # file_path = filedialog.askopenfilename()
            # with open(file_path, "rb") as file:
            #     data = file.read()

            # Encrypt the data
            enc_session_key, nonce, tag, ciphertext = self.encrypt_data(data.encode())

            client_socket.sendall(enc_session_key)
            client_socket.sendall(nonce)
            client_socket.sendall(tag)
            client_socket.sendall(ciphertext)
            client_socket.close()


        not_crash = True
        while self.running:
            while not_crash:
                try:
                    server_data = client_socket.recv(1024).decode('utf-8')
#1______________________________________________________________________________________________________________________________
                    if server_data == "Login":
                        arr = recv_message_arr()
                        if arr!= None and len(arr)==2:
                            data = UserDB.users().check_user_by_Username_and_Password(arr[0],arr[1])
                            print("server data:", data)
                            if data == True:
                                send_message(f"Welcome {arr[0]}")
                                self.connected_clients[client_socket] = addr
                                self.client_count += 1
                                print(self.client_count)
                            elif data == False:
                                send_message("Username or Password are incorrect")
                                
#2______________________________________________________________________________________________________________________________

                    elif server_data == "Register":
                        arr = recv_message_arr()
                        if arr != None and len(arr)==3:
                            server_data = UserDB.users().check_user_by_Username(arr[1])
                            if server_data == True:
                                send_message("The user already exists")
                            elif server_data == False:
                                answer = UserDB.users().insert_user(arr[0],arr[1],arr[2])
                                send_message("User created successfully")

#3______________________________________________________________________________________________________________________________


                    elif server_data == "Scan":
                        server_data_hashes = recv_message()
                        arr_hashes = server_data_hashes.split(",")
                        arr_virus_hashes=[]
                        for hash in arr_hashes:
                            file_hash = hash
                            all_existing_viruses = Viruses_HashDB.hashes().select_all_hashes()
                            if file_hash in all_existing_viruses:
                                arr_virus_hashes.append(file_hash)
                        str_virus_hashes = ",".join(arr_virus_hashes)
                        send_message(str_virus_hashes)
                        arr_history = recv_message_arr()
                        UserId = UserDB.users().GetUserIdByUserName(arr_history[4])
                        HistoryDB.history().AddScan(arr_history[0],arr_history[1],arr_history[2],arr_history[3], UserId)
#4______________________________________________________________________________________________________________________________


                    elif server_data == "Show Scans":
                        UserName = recv_message()
                        UserId = UserDB.users().GetUserIdByUserName(UserName)
                        print(UserId)
                        Scans = HistoryDB.history().get_scan_by_UserId(UserId)
                        send_message_arr(Scans)
#5______________________________________________________________________________________________________________________________



                    elif server_data == "AddEmail":
                        Email_data = recv_message()
                        UserName_data = recv_message()
                        UserDB.users().UpdateEmailByUserName(Email_data,UserName_data)
                        print("Success")
#6______________________________________________________________________________________________________________________________


                    elif server_data == "EmailExists":
                        UserName = recv_message()
                        answer = UserDB.users().GetEmailByUserName(UserName)
                        if answer == "Exists":
                            send_message("Exists")
                        elif answer == "None":
                            send_message("None")    
#7______________________________________________________________________________________________________________________________


                    elif server_data == "ChangePassword":
                        password = recv_message()
                        UserName = recv_message()
                        answer = UserDB.users().ChangePassword(password,UserName)
                        print(answer)
                        send_message(answer)
#8______________________________________________________________________________________________________________________________


                    elif server_data == "ChangeUserName":
                        NewUserName = recv_message()
                        UserName = recv_message()
                        answer = UserDB.users().ChangeUserName(NewUserName,UserName)
                        send_message(answer)
#9______________________________________________________________________________________________________________________________
                    elif server_data == "Quit" or server_data == "Logout":
                        if self.client_count != 0:
                            if server_data == "Quit":
                                del self.connected_clients[client_socket]
                                not_crash = False
                            self.client_count -= 1
                            print(self.client_count)
                            
                    else:
                        server_data = "False"
                except Exception as e:
                    print("Error:",e)
                    not_crash = False
                    traceback.print_exc()
                    break
        
        

if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 6060
    s = server(ip,port)
    s.start()



