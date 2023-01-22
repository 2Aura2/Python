import tkinter
from tkinter import *


class Overview_Screen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("960x540")
        self.title("Overview")
        
        self.create_gui()
    
    def create_gui(self):

        self.btn_overview = Button(self,text="Overview",font=("",16),bg='orange',width=17).place(relx=0.2,rely=0.2,anchor='center')
        self.btn_computer_scan = Button(self,text="Computer Scan",font=("",16),bg='orange',width=17).place(relx=0.2,rely=0.35,anchor='center')
        self.btn_Junk_remover = Button(self,text="Junk Files Remover ",font=("",16),bg='orange').place(relx=0.2,rely=0.5,anchor='center')
        self.btn_hisotry = Button(self,text="History",font=("",16),width=17,bg='orange').place(relx=0.2,rely=0.65,anchor='center')
        self.btn_settings = Button(self,text="Settings",font=("",16),width=17,bg='orange').place(relx=0.2,rely=0.8,anchor='center')
        

