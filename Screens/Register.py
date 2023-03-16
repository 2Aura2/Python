import threading
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import sys
#str_path = "D://School Project//Python//DataBase_Codes//"
#str_path1 = "C://School Project//Python//DataBase_Codes//"
#sys.path.insert(1,str_path1)
#import UserDB
from PIL import ImageTk, Image


class Register_Screen(tkinter.Toplevel):
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
        self.title("Register")
        #self.UserDB = UserDB.users()
        self.img = Image.open('Images\\White.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)




        self.create_gui()
        Button(self,text="Login Page",font=("ariel",14),width=10,command=self.return_to_Login_page).place(relx=0.75,rely=0.8,anchor='center')


    def create_gui(self):

        self.lbl_background = Label(self,bg="light gray",width=45,height=30).place(relx=0.8,rely=0.5,anchor='center')

        self.lbl_Fullname = Label(self,text="Fullname:",font=("ariel",14),width=10,bg="light gray").place(relx=0.7,rely=0.3,anchor='center')
        self.enr_Fullname = Entry(self,font=("ariel",14),width=14)
        self.enr_Fullname.place(relx=0.85,rely=0.3,anchor='center')

        self.lbl_Username = Label(self,text="Username:",font=("ariel",14),width=10,bg="light gray").place(relx=0.7,rely=0.4,anchor='center')
        self.enr_Username = Entry(self,font=("ariel",14),width=14)
        self.enr_Username.place(relx=0.85,rely=0.4,anchor='center')

        self.lbl_Password = Label(self,text="Password:",font=("ariel",14),width=10,bg="light gray").place(relx=0.7,rely=0.5,anchor='center')
        self.enr_Password = Entry(self,font=("ariel",14),width=14)
        self.enr_Password.place(relx=0.85,rely=0.5,anchor='center')

        self.btn_Register = Button(self, text="Register",font=("ariel",14),width=10,command=self.register_user).place(relx=0.77,rely=0.6,anchor='center')

        self.lbl_Anti_Virus = Label(self, text="Anti Virus",font=('ariel',14),bg='light gray').place(relx=0.5,rely=0.1,anchor='center')


    def send_message(self,message):
        length = str(len(message)).zfill(10)
        data = length+message
        self.server.client_socket.send(data.encode())
    
    def recv_message(self):
        length = self.server.client_socket.recv(10).decode()
        return self.server.client_socket.recv(int(length)).decode()
        

    def register_user(self):
        if len(self.enr_Fullname.get())==0 or len(self.enr_Username.get())==0 or len(self.enr_Password.get())==0:
            messagebox.showerror("Error","Please write everything")
            return "Error"
        else:
            arr = ["Register", self.enr_Fullname.get(), self.enr_Username.get(), self.enr_Password.get()]
            str_arr = ",".join(arr)
            self.parent.client_socket.send(str_arr.encode())
            data = self.parent.client_socket.recv(1024).decode()
            if data == "The user already exists":
                messagebox.showerror("Error",data)
                return "Error"
            else:
                messagebox.showinfo(title="Register", message=data)
                self.return_to_Login_page()
    

    def return_to_Login_page(self):
        self.parent.deiconify()
        self.destroy()
