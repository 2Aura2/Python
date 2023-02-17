import tkinter
from tkinter import *
from PIL import ImageTk, Image
import Overview
import ComputerScan
import JunkFiles
import os
import shutil
import sys
import subprocess
import settings


class History_Screen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.app_width = 960
        self.app_height = 540
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2)-(self.app_width / 2)
        self.y = (self.screen_height / 2)-(self.app_height / 2)
        self.geometry(f"{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}")
        self.title("History")
        self.img = Image.open('Images\Anti_Virus_BG.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)

        self.create_gui()

    def create_gui(self):
        self.btn_Overview = Button(self,text="Overview",font=("",18),width=16,bg="orange",command=self.open_overview_screen).place(relx=0.2,rely=0.2,anchor='center')
        self.btn_Computer_Scan = Button(self,text="Computer Scan",font=("",18),width=16,bg="orange",command=self.open_Computer_Scan_screen).place(relx=0.2,rely=0.35,anchor='center')
        self.btn_Junk_Files_Remover = Button(self,text="Junk Files Remover",font=("",18),bg="orange",command=self.open_JunkFiles_screen).place(relx=0.2,rely=0.5,anchor='center')
        self.btn_History = Button(self,text="History",font=("",18),width=16,bg="light blue").place(relx=0.2,rely=0.65,anchor='center')
        self.btn_settings = Button(self,text="Settings",font=("",18),width=16,bg="orange",command=self.open_settings_screen).place(relx=0.2,rely=0.8,anchor='center')
        
        
        
        
        
    def open_overview_screen(self):
        window = Overview.Overview_Screen(self.parent)
        window.grab_set()
        self.withdraw()

    def open_Computer_Scan_screen(self):
        window = ComputerScan.Computer_Scan_Screen(self.parent)
        window.grab_set()
        self.withdraw()
        
    def open_JunkFiles_screen(self):
        window = JunkFiles.Junk_Files_Screen(self.parent)
        window.grab_set()
        self.withdraw()

    def open_settings_screen(self):
        window = settings.Settigns_Screen(self.parent)
        window.grab_set()
        self.withdraw()