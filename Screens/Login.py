import tkinter
from tkinter import *
import socket
from tkinter import ttk, messagebox
import threading
from Register import Register_Screen
import Overview
from PIL import ImageTk, Image
import traceback
import time
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import os
from tkinter import filedialog

class Login_Screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.app_width = 960
        self.app_height = 540
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2)-(self.app_width / 2)
        self.y = (self.screen_height / 2)-(self.app_height / 2)
        self.geometry(f"{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}")
        self.title("Login")
        self.img = Image.open('..\\Images\\White.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)
        self.wm_iconbitmap('..\\Images\\virus.ico')

        

        self.handle_thread_socket()

        self.lbl_Anti_Virus = Label(self, text="Anti Virus",font=('',16),bg='light gray').place(relx=0.5,rely=0.2,anchor='center')

        self.btn_Login = Button(self, text="Login",command=self.login_user,font=('',16),bg='light gray').place(relx=0.5,rely=0.8,anchor='center')
        
        self.lbl_Register = Label(self, text="Don't have an account, register here:",bg='light gray',font=('',10)).place(relx=0.49, rely=0.9,anchor='center')
        self.btn_register = Button(self,text="Register",bg='light gray',font=('',8),command=self.open_Register_screen)
        self.btn_register.place(relx=0.63,rely=0.9,anchor='center')

        #self.lbl_Username = Label(self, text="Username:",font=('',16),bg='light green').place(relx=0.3, rely=0.6,anchor='center')
        self.enr_Username = Entry(self,font=('',16))
        self.enr_Username.place(relx=0.5,rely=0.6,anchor='center')
        self.enr_Username.insert(0,"Username")
        self.enr_Username.bind('<FocusIn>',  self.Username_enter)
        self.enr_Username.bind('<FocusOut>', self.Username_leave)

        #self.lbl_Password = Label(self, text="Password:",font=('',16),bg='light green').place(relx=0.3, rely=0.7,anchor='center')
        self.enr_Password = Entry(self,font=('',16))
        self.enr_Password.place(relx=0.5,rely=0.7,anchor='center')
        self.enr_Password.insert(0,"Password")
        self.enr_Password.bind('<FocusIn>',  self.Password_enter)
        self.enr_Password.bind('<FocusOut>', self.Password_leave)
        
        self.lbl_time = Label(self,bg='light gray' ,font=("", 18))
        self.lbl_time.place(relx = 0.85,rely=0.05, anchor='center')
        self.update_label()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_label(self):
        try:
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%Y-%m-%d")
            self.lbl_time.config(text=f"{current_date} {current_time}")
            self.lbl_time.after(1000, self.update_label)
        except Exception as e:
            print("Error:",e)
            return "Error with getting current time"
        
    
    def Username_enter(self,event):
        self.enr_Username.delete(0,END)
        
        
    def Username_leave(self,event):
        current_Username = self.enr_Username.get()
        if current_Username == '':
            self.enr_Username.insert(0,"Username")
            
    def Password_enter(self,event):
        self.enr_Password.delete(0,END)
        self.enr_Password.config(show="*")
        
    def Password_leave(self,event):
        current_Password = self.enr_Password.get()
        if current_Password == '':
            self.enr_Password.config(show="")
            self.enr_Password.insert(0,"Password")


    def open_Overview_screen(self):
        window = Overview.Overview_Screen(self,self.enr_Username.get(),self.public_key)
        window.grab_set()
        window.focus_set()
        self.withdraw()
    
    
    def open_Register_screen(self):
        window = Register_Screen(self,self.public_key)
        window.grab_set()
        self.withdraw()

    def send_message(self,message):
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted_message = cipher.encrypt(message.encode())
        encoded_message = base64.b64encode(encrypted_message).decode()
        length = str(len(encoded_message)).zfill(10)
        data = length+encoded_message
        self.client_socket.send(data.encode())

    def send_message_arr(self,arr):
        try:
            str_arr = ",".join(arr)
            cipher = PKCS1_OAEP.new(self.public_key)
            encrypted_str_arr = cipher.encrypt(str_arr.encode())
            encoded_str_arr = base64.b64encode(encrypted_str_arr).decode()
            length = str(len(encoded_str_arr)).zfill(10)
            data = length+encoded_str_arr
            self.client_socket.send(data.encode()) 
        except Exception as e:
            print("Error:",e)
            return "Error while sending message"
    
    def recv_message(self):
        length = self.client_socket.recv(10).decode()
        return self.client_socket.recv(int(length)).decode()
    
    def recv_message_arr(self):
            length = self.client_socket.recv(10).decode()
            str_arr = self.client_socket.recv(int(length)).decode()
            return str_arr.split(",")


    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()
    
    
    def create_socket(self):        
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(("10.81.205.93",6060))
            data = self.client_socket.recv(1024).decode()
            print(data, self.client_socket)
            self.public_key_bytes = self.client_socket.recv(2048)
            self.public_key = RSA.import_key(self.public_key_bytes)
            self.session_key = os.urandom(16)
        except:
            if messagebox.showerror("Error","Server is currently offline"):
                self.destroy()
                self.client_socket.close()
    

    def encrypt_data(self,data):
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
    

    def send_data(self,data):
        # Select a file to encrypt and send
        # file_path = filedialog.askopenfilename()
        # with open(file_path, "rb") as file:
        #     data = file.read()

        # Encrypt the data
        enc_session_key, nonce, tag, ciphertext = self.encrypt_data(data.encode())

        self.client_socket.sendall(enc_session_key)
        self.client_socket.sendall(nonce)
        self.client_socket.sendall(tag)
        self.client_socket.sendall(ciphertext)
        self.client_socket.close()

        print("Data sent to server.")
    


    def login_user(self):
        try:
            if (self.enr_Username.get() == "Username" or len(self.enr_Username.get()) == 0) and (self.enr_Password.get() == "Password" or len(self.enr_Password.get()) == 0):
                messagebox.showerror("Error","Please write Username and password")
                return "Error"
            elif len(self.enr_Password.get())>0 and (self.enr_Username.get()=="Username" or len(self.enr_Username.get())==0):
                messagebox.showerror("Error","Please write Username")
                return "Error"
            elif len(self.enr_Username.get())>0 and (self.enr_Password.get()=="Password" or len(self.enr_Password.get())==0):
                messagebox.showerror("Error","Please write password")
                return "Error"
            else:
                self.client_socket.send(b"Login")
                arr = [self.enr_Username.get(), self.enr_Password.get()]
                self.send_message_arr(arr)
                data = self.recv_message()
                if data == f"Welcome {self.enr_Username.get()}":
                    self.open_Overview_screen()
                else:
                    messagebox.showerror("Error",data)
                    print("Error:",data)
        except Exception as e:
            print("Error:", e)
            traceback.print_exc()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to exit?"):
            self.client_socket.send(b'Quit')
            self.destroy()
            self.client_socket.close()


if __name__ == "__main__":
    app = Login_Screen()
    app.mainloop()
