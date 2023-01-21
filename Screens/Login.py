import tkinter
from tkinter import *
import socket
from tkinter import ttk, messagebox
import threading
from Register import Register_Screen
from Overview import Overview_Screen
from PIL import ImageTk, Image


class Login_Screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("960x540")
        self.title("Login")
        self.img = Image.open('Images\Anti_Virus_BG.jpg')
        self.resized = self.img.resize((1920,1080), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)

        self.handle_thread_socket()

        self.lbl_Anti_Virus = Label(self, text="Anti Virus",font=('',16)).place(relx=0.5,rely=0.2,anchor='center')

        self.btn_Login = Button(self, text="login",command=self.login_user,font=('',16)).place(relx=0.5,rely=0.8,anchor='center')
        
        self.lbl_Register = Label(self, text="Don't have account, register here:").place(relx=0.5, rely=0.9,anchor='center')
        self.btn_register = Button(self,text="Register",command=self.open_Register_screen)
        self.btn_register.place(relx=0.63,rely=0.9,anchor='center')

        #self.lbl_Username = Label(self, text="Username:").place(relx=0.4, rely=0.6,anchor='center')
        self.enr_Username = Entry(self,font=('',16))
        self.enr_Username.insert(0,"Username")
        self.enr_Username.place(relx=0.5,rely=0.6,anchor='center')

        #self.lbl_Password = Label(self, text="Password:").place(relx=0.4, rely=0.7,anchor='center')
        self.enr_Password = Entry(self,font=('',16))
        self.enr_Password.insert(0,"Password")
        self.enr_Password.place(relx=0.5,rely=0.7,anchor='center')

        
        


    def open_Overview_screen(self):
        window = Overview_Screen(self)
        window.grab_set()
        self.withdraw()
    
    
    def open_Register_screen(self):
        window = Register_Screen(self)
        window.grab_set()
        self.withdraw()

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.creat_socket, args=())
        client_handler.daemon = True
        client_handler.start()
    
    
    def creat_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1",6060))
        data = self.client_socket.recv(1024).decode()
        print("hi", self.client_socket)
    
    
    def login_user(self):
        try:
            if len(self.enr_Username.get())==0 and len(self.enr_Password.get())==0:
                messagebox.showerror("Error","Please write Username and password")
                return
            elif len(self.enr_Username.get())==0:
                messagebox.showerror("Error","Please write Username")
                return
            elif len(self.enr_Password.get())==0:
                messagebox.showerror("Error","Please write password")
                return
            else:
                arr = ["Login", self.enr_Username.get(), self.enr_Password.get()]
                str_arr = ",".join(arr)
                self.client_socket.send(str_arr.encode())
                data = self.client_socket.recv(1024).decode()
                if data == f"Welcome {self.enr_Username.get()}":
                    self.open_Overview_screen()
                else:
                    messagebox.showerror("Error",data)
        except Exception as e:
            print("Error", e)


if __name__ == "__main__":
    app = Login_Screen()
    app.mainloop()
