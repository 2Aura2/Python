import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import sys
sys.path.insert(1,'C://School Project//Python//DataBase_Codes//')
import UserDB



class Register_Screen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("960x540")
        self.title("Register")
        self.UserDB = UserDB.users()

        self.create_gui()
        Button(self,text="Login Page",command=self.return_to_Login_page).place(relx=0.75,rely=0.8,anchor='center')


    def create_gui(self):
        self.lbl_Fullname = Label(self,text="Fullname:").place(relx=0.7,rely=0.3,anchor='center')
        self.enr_Fullname = Entry(self)
        self.enr_Fullname.place(relx=0.8,rely=0.3,anchor='center')

        self.lbl_Username = Label(self,text="Username:").place(relx=0.7,rely=0.4,anchor='center')
        self.enr_Username = Entry(self)
        self.enr_Username.place(relx=0.8,rely=0.4,anchor='center')

        self.lbl_Password = Label(self,text="Password:").place(relx=0.7,rely=0.5,anchor='center')
        self.enr_Password = Entry(self)
        self.enr_Password.place(relx=0.8,rely=0.5,anchor='center')

        self.btn_Register = Button(self, text="Register",command=self.register_user).place(relx=0.77,rely=0.6,anchor='center')

        self.lbl_Anti_Virus = Label(self, text="Anti Virus").place(relx=0.5, rely=0.2,anchor='center')

    def register_user(self):
        if len(self.enr_Fullname.get())==0 or len(self.enr_Username.get())==0 or len(self.enr_Password.get())==0:
            messagebox.showerror("Error","Please write everything")
            return
        else:
            arr = ["Register", self.enr_Fullname.get(), self.enr_Username.get(), self.enr_Password.get()]
            str_arr = ",".join(arr)
            self.parent.client_socket.send(str_arr.encode())
            data = self.parent.client_socket.recv(1024).decode()
            if data == "The user already exists":
                messagebox.showerror("Error",data)
                return
            else:
                messagebox.showinfo(title="Register", message=data)
                self.return_to_Login_page()
    

    def return_to_Login_page(self):
        self.parent.deiconify()
        self.destroy()