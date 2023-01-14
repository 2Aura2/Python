import tkinter
from tkinter import *
import socket
from tkinter import ttk, messagebox

class Login(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("960x540")
        self.title("Login")

        self.lbl_Anti_Virus = Label(self, text="Anti Virus").place(relx=0.5, rely=0.2,anchor='center')

        self.btn_Login = Button(self, text="login").place(relx=0.5,rely=0.8,anchor='center')
        
        self.lbl_Username = Label(self, text="Username:").place(relx=0.4, rely=0.6,anchor='center')
        self.enr_Username = Entry(self)
        self.enr_Username.place(relx=0.5,rely=0.6,anchor='center')

        self.lbl_Password = Label(self, text="Password:").place(relx=0.4, rely=0.7,anchor='center')
        self.enr_Password = Entry(self)
        self.enr_Password.place(relx=0.5,rely=0.7,anchor='center')

    def login_user(self):
        try:
            if len(self.enr_Username.get())==0 and len(self.enr_Password.get())==0:
                messagebox.showerror("Please write Username and password","Error")
                return
            print("Login")
            arr = ["Login", self.enr_Username.get(), self.enr_Password.get()]
            str_arr = ",".join(arr)
            print(str_arr)
            self.client_scoket.send(str_arr.encode())
            #data = self.client_socket.recv(1024).decode()
            #print(data)
            #self.textvar.set(data)
        except Exception as e:
            print("Error", e)


if __name__ == "__main__":
    app = Login()
    app.mainloop()
