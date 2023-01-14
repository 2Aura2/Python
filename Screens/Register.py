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
        self.lbl_Fullname = Label(self,text="Fullname:").place(relx=0.7,rely=0.7,anchor='center')
        self.enr_Fullname = Entry(self)
        self.enr_Fullname.place(relx=0.8,rely=0.7,anchor='center')


    def return_to_Login_page(self):
        self.parent.deiconify()
        self.destroy()