import tkinter
from tkinter import *


class Overview_Screen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("960x540")
        self.title("Overview")
        self.img = Image.open('Images\Anti_Virus_BG.jpg')
        self.resized = self.img.resize((1920,1080), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)
        
        self.create_gui()
    
    def create_gui(self):
        self.btn_settings = Button(self,text="Settings")
        self.btn_settings.pack()
