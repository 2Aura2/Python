import tkinter
from tkinter import *
import socket

class Sign_in(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("960x540")
        self.title("Sign In")

        self.btn_login = Button(self, text="login").pack()




if __name__ == "__main__":
    app = Sign_in()
    app.mainloop()
