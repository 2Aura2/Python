import tkinter
from tkinter import *
from PIL import ImageTk, Image
import ComputerScan
import JunkFiles
import History
import settings
import time

class Overview_Screen(tkinter.Toplevel):
    def __init__(self,parent,UserName):
        super().__init__(parent)
        self.parent = parent
        self.UserName = UserName
        self.app_width = 960
        self.app_height = 540
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2)-(self.app_width / 2)
        self.y = (self.screen_height / 2)-(self.app_height / 2)
        self.geometry(f"{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}")
        self.title("Overview")

        self.img = Image.open('..\\Images\\White.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)

        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)

        self.create_gui()
    def create_gui(self):

        
        #self.btn_Overview = Button(self,,bg="light blue").place(relx=0.2,rely=0.2,anchor='center')

        
        self.btn_Computer_Scan = Button(self,text="Computer Scan",font=("ariel",20),width=19,bg="light gray",command=self.open_Computer_Scan_screen).place(relx=0.2,rely=0.2,anchor='center')
        
        
        self.btn_Junk_Files_Remover = Button(self,text="Junk Files Remover",font=("ariel",20),width=19,bg="light gray",command=self.open_JunkFiles_screen).place(relx=0.2,rely=0.35,anchor='center')
        
        
        self.btn_History = Button(self,text="History",font=("ariel",20),width=19,bg="light gray",command=self.open_history_screen).place(relx=0.2,rely=0.5,anchor='center')
       
        
        self.btn_settings = Button(self,text="Settings",font=("ariel",20),width=19,bg="light gray",command=self.open_settings_screen).place(relx=0.2,rely=0.65,anchor='center')

        self.lbl_welcome = Label(self,text=f"Welcome {self.UserName}",font=("ariel",18),bg="light gray")
        self.lbl_welcome.config(width=30,height=5)
        self.lbl_welcome.place(relx=0.7,rely=0.2,anchor='center')   

        self.lbl_time = Label(self,bg='light gray' ,font=("", 18))
        self.lbl_time.place(relx = 0.85,rely=0.05, anchor='center')
        self.update_label()

    def update_label(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y-%m-%d")
        self.lbl_time.config(text=f"{current_date} {current_time}")
        self.lbl_time.after(1000, self.update_label)
        
    def open_Computer_Scan_screen(self):
        window = ComputerScan.Computer_Scan_Screen(self, self.parent, self.UserName)
        window.grab_set()
        self.withdraw()

    def open_JunkFiles_screen(self):
        window = JunkFiles.Junk_Files_Screen(self,self.parent)
        window.grab_set()
        self.withdraw()
        
    def open_history_screen(self):
        window = History.History_Screen(self,self.parent,self.UserName)
        window.grab_set()
        self.withdraw()

    def open_settings_screen(self):
        window = settings.Settigns_Screen(self,self.parent,self.UserName)
        window.grab_set()
        self.withdraw()


