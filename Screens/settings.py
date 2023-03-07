import tkinter
from tkinter import *
from PIL import ImageTk, Image
import Login

class Settigns_Screen(tkinter.Toplevel):
    def __init__(self,parent,server):
        super().__init__(parent)
        self.parent = parent
        self.server = server
        self.app_width = 960
        self.app_height = 540
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2)-(self.app_width / 2)
        self.y = (self.screen_height / 2)-(self.app_height / 2)
        self.geometry(f"{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}")
        self.title("Settings")
        self.img = Image.open('Images\\White.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)

        self.create_gui()

    def create_gui(self):
        self.btn_previous_window = Button(self,text="Previous Window",font=("",18),width=16,bg="light gray",command=self.previous_window).place(relx=0.15,rely=0.9,anchor='center')
        self.btn_LogOut = Button(self,text="Logout",font=("",18),bg="light gray",command=self.Login_window).place(relx=0.8,rely=0.2,anchor='center')
        
        
        
        
        
    def Login_window(self):
        self.destroy()  # close the second window
        self.server.deiconify()  # show the main window again


    def previous_window(self):
        self.destroy()  # close the second window
        self.parent.deiconify()  # show the main window again