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
        self.btn_settings = Button(self,text="Settings")
        self.btn_settings.pack()
