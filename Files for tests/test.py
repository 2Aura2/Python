import tkinter
from tkinter import *



class app():
    def __init__(self):
        root = Tk()
        root.geometry("960x540")
        root.title("Sign In")
        


        self.namelabel = Label(root, text="hello").place(x=100,y=100)
        self.entry = Entry(root,text="Username").place(x=440,y=100)


        root.mainloop()

app = app()

