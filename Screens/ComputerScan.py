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
        self.img = Image.open('Images\\thumb-1920-77840.jpg')
        self.resized = self.img.resize((1920,1080), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)