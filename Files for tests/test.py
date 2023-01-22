import tkinter
from tkinter import *
import sys
sys.path.insert(1,'D://School Project//Python//DataBase_Codes')
import UserDB
from PIL import ImageTk, Image

class Login_Screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("960x540")
        self.title("Login")
        #self.img = Image.open('Images\\thumb-1920-77840.jpg')
        #self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        #self.bg = ImageTk.PhotoImage(self.resized)
        #self.IMGLabel = Label(self, image=self.bg)
        #self.IMGLabel.pack(expand=YES)

        self.lbl_Anti_Virus = Label(self, text="Anti Virus",font=('',16)).pack()
        self.lbl_Anti_Virus2 = Label(self, text="Anti Virus",font=('',16)).pack(padx=100,pady=10)




if __name__ == "__main__":
    app = Login_Screen()
    app.mainloop()




