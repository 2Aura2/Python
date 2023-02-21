import tkinter
from tkinter import *
from PIL import ImageTk, Image
import ComputerScan
import JunkFiles
import History
import settings


class Overview_Screen(tkinter.Toplevel):
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
        self.title("Overview")
        self.canvas = Canvas(self, width=100, height=100)
        self.canvas.pack()
        self.img = Image.open('Images\\solid3.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)
        self.canvas.lift()
        
        self.create_gui()
    
    def create_gui(self):
        


        #text="Overview",font=("",18),width=16,bg="light blue"
        #self.Overview_btn = PhotoImage(file="Images\\button2.png") 

        self.button_image = PhotoImage(file="Images\\button2.png")
        self.button_image_item = self.canvas.create_image(960, 540, image=self.button_image)
        self.canvas.tag_bind(self.button_image_item, "<Button-1>")


        #self.btn_Overview = Button(self).place(relx=0.2,rely=0.2,anchor='center')
        self.btn_Computer_Scan = Button(self,text="Computer Scan",font=("",18),width=16,bg="orange",command=self.open_Computer_Scan_screen).place(relx=0.2,rely=0.35,anchor='center')
        self.btn_Junk_Files_Remover = Button(self,text="Junk Files Remover",font=("",18),bg="orange",command=self.open_JunkFiles_screen).place(relx=0.2,rely=0.5,anchor='center')
        self.btn_History = Button(self,text="History",font=("",18),width=16,bg="orange",command=self.open_history_screen).place(relx=0.2,rely=0.65,anchor='center')
        self.btn_settings = Button(self,text="Settings",font=("",18),width=16,bg="orange",command=self.open_settings_screen).place(relx=0.2,rely=0.8,anchor='center')

        self.lbl_welcome = Label(self,text="Welcome User",font=("ariel",18),bg="white")
        self.lbl_welcome.config(width=30,height=5)
        self.lbl_welcome.place(relx=0.6,rely=0.2,anchor='center')   

    def open_Computer_Scan_screen(self):
        window = ComputerScan.Computer_Scan_Screen(self,self.parent)
        window.grab_set()
        self.withdraw()

    def open_JunkFiles_screen(self):
        window = JunkFiles.Junk_Files_Screen(self,self.parent)
        window.grab_set()
        self.withdraw()
        
    def open_history_screen(self):
        window = History.History_Screen(self,self.parent)
        window.grab_set()
        self.withdraw()

    def open_settings_screen(self):
        window = settings.Settigns_Screen(self,self.parent)
        window.grab_set()
        self.withdraw()