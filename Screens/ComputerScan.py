import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import os
import hashlib

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
        
        self.btn_startScan = Button(self,text="Scan your computer",font=("",18),width=16,bg="light green").place(relx=0.8,rely=0.2,anchor='center')
        self.btn_ADVScan = Button(self,text="Advanced Scanning",font=("",18),width=16,bg="light green").place(relx=0.8,rely=0.2,anchor='center')


    def Scan(self):
        self.parent.client_socket.send("Scan".encode())


        


