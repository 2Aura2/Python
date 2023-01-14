import threading
import tkinter
from tkinter import *
import sys
sys.path.insert(1,'D://School Project//Python//DataBase_Codes//')
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

        self.btn_Register = Button(self, text="Register").place(relx=0.77,rely=0.6,anchor='center')

    def return_to_Login_page(self):
        self.parent.deiconify()
        self.destroy()