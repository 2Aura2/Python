import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import sys
import time
from PIL import ImageTk, Image
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class Register_Screen(tkinter.Toplevel):
    def __init__(self,parent,public_key):
        super().__init__(parent)
        self.parent = parent
        self.public_key = public_key
        self.app_width = 960
        self.app_height = 540
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2)-(self.app_width / 2)
        self.y = (self.screen_height / 2)-(self.app_height / 2)
        self.geometry(f"{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}")
        self.title("Register")
        #self.UserDB = UserDB.users()
        self.img = Image.open('..\\Images\\White.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)




        self.create_gui()
        Button(self,text="Login Page",font=("ariel",14),width=10,command=self.return_to_Login_page).place(relx=0.75,rely=0.8,anchor='center')


    def create_gui(self):
        self.lbl_background = Label(self,bg="light gray",width=45,height=20).place(relx=0.2,rely=0.4,anchor='center')
        self.lbl_background = Label(self,bg="light gray",width=45,height=30).place(relx=0.8,rely=0.5,anchor='center')
        self.lbl_text = Label(self,text="Here you can create\n your account with\n which you have access\n to the program",font=("ariel",18),bg="light gray").place(relx=0.2,rely=0.25,anchor='center')

        self.lbl_Fullname = Label(self,text="Fullname:",font=("ariel",14),width=10,bg="light gray").place(relx=0.7,rely=0.3,anchor='center')
        self.enr_Fullname = Entry(self,font=("ariel",14),width=14)
        self.enr_Fullname.place(relx=0.85,rely=0.3,anchor='center')

        self.lbl_Username = Label(self,text="Username:",font=("ariel",14),width=10,bg="light gray").place(relx=0.7,rely=0.4,anchor='center')
        self.enr_Username = Entry(self,font=("ariel",14),width=14)
        self.enr_Username.place(relx=0.85,rely=0.4,anchor='center')

        self.lbl_Password = Label(self,text="Password:",font=("ariel",14),width=10,bg="light gray").place(relx=0.7,rely=0.5,anchor='center')
        self.enr_Password = Entry(self,font=("ariel",14),width=14)
        self.enr_Password.place(relx=0.85,rely=0.5,anchor='center')

        self.btn_Register = Button(self, text="Register",font=("ariel",14),width=10,command=self.register_user).place(relx=0.77,rely=0.6,anchor='center')

        self.lbl_Anti_Virus = Label(self, text="Anti Virus",font=('ariel',14),bg='light gray').place(relx=0.5,rely=0.1,anchor='center')

        self.lbl_time = Label(self,bg='light gray' ,font=("", 18))
        self.lbl_time.place(relx = 0.85,rely=0.05, anchor='center')
        self.update_label()

    def update_label(self):
        try:
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%Y-%m-%d")
            self.lbl_time.config(text=f"{current_date} {current_time}")
            self.lbl_time.after(1000, self.update_label)
        except Exception as e:
            print("Error:",e)
            return "Error with getting current time"

    def send_message(self,message):
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted_message = cipher.encrypt(message.encode())
        print(encrypted_message)
        encoded_message = base64.b64encode(encrypted_message).decode()
        length = str(len(encoded_message)).zfill(10)
        data = length+encoded_message
        self.parent.client_socket.send(data.encode())
    
    def send_message_arr(self,arr):
        try:
            str_arr = ",".join(arr)
            cipher = PKCS1_OAEP.new(self.public_key)
            encrypted_str_arr = cipher.encrypt(str_arr.encode())
            encoded_str_arr = base64.b64encode(encrypted_str_arr).decode()
            length = str(len(encoded_str_arr)).zfill(10)
            data = length+encoded_str_arr
            self.parent.client_socket.send(data.encode()) 
        except Exception as e:
            print("Error:",e)
            return "Error while sending message"


    def recv_message(self):
        length = self.parent.client_socket.recv(10).decode()
        return self.parent.client_socket.recv(int(length)).decode()
        

    def register_user(self):
        if len(self.enr_Fullname.get())==0 or len(self.enr_Username.get())==0 or len(self.enr_Password.get())==0:
            messagebox.showerror("Error","Please write everything")
            return "Error"
        else:
            self.parent.client_socket.send(b"Register")
            arr = [self.enr_Fullname.get(), self.enr_Username.get(), self.enr_Password.get()]
            self.send_message_arr(arr)
            data = self.recv_message()
            if data == "The user already exists":
                messagebox.showerror("Error",data)
                return "Error"
            else:
                messagebox.showinfo(title="Register", message=data)
                self.return_to_Login_page()
    

    def return_to_Login_page(self):
        self.parent.deiconify()
        self.destroy()
