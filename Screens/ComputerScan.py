import tkinter
from tkinter import *
import socket
from tkinter import ttk, messagebox
import threading
from Register import Register_Screen
from Overview import Overview_Screen
from PIL import ImageTk, Image

class Computer_Scan_Screen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("960x540")
        self.title("Computer Scan")
        self.img = Image.open('Images\Anti_Virus_BG.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)

        self.create_gui()

    def create_gui(self):
        self.btn_settings = Button(self,text="Overview",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.2,anchor='center')
        self.btn_settings = Button(self,text="Computer Scan",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.35,anchor='center')
        self.btn_settings = Button(self,text="Junk Files Remover",font=("",18),bg="orange").place(relx=0.2,rely=0.5,anchor='center')
        self.btn_settings = Button(self,text="History",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.65,anchor='center')
        self.btn_settings = Button(self,text="Settings",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.8,anchor='center')
        