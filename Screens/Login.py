import tkinter
from tkinter import *
import socket
from tkinter import ttk, messagebox
import threading
from Register import Register_Screen
from Overview import Overview_Screen
from PIL import ImageTk, Image


class Login_Screen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.app_width = 960
        self.app_height = 540
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2)-(self.app_width / 2)
        self.y = (self.screen_height / 2)-(self.app_height / 2)
        self.geometry(f"{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}")
        self.title("Login")
        self.img = Image.open('Images\\thumb-1920-77840.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)
        

        self.handle_thread_socket()

        self.lbl_Anti_Virus = Label(self, text="Anti Virus",font=('',16),bg='light green').place(relx=0.5,rely=0.2,anchor='center')

        self.btn_Login = Button(self, text="login",command=self.open_Overview_screen,font=('',16),bg='light green').place(relx=0.5,rely=0.8,anchor='center')
        
        self.lbl_Register = Label(self, text="Don't have an account, register here:",bg='light green',font=('',10)).place(relx=0.49, rely=0.9,anchor='center')
        self.btn_register = Button(self,text="Register",bg='light green',font=('',8),command=self.open_Register_screen)
        self.btn_register.place(relx=0.63,rely=0.9,anchor='center')

        #self.lbl_Username = Label(self, text="Username:",font=('',16),bg='light green').place(relx=0.3, rely=0.6,anchor='center')
        self.enr_Username = Entry(self,font=('',16))
        self.enr_Username.place(relx=0.5,rely=0.6,anchor='center')
        self.enr_Username.insert(0,"Username")
        self.enr_Username.bind('<FocusIn>',  self.Username_enter)
        self.enr_Username.bind('<FocusOut>', self.Username_leave)

        #self.lbl_Password = Label(self, text="Password:",font=('',16),bg='light green').place(relx=0.3, rely=0.7,anchor='center')
        self.enr_Password = Entry(self,font=('',16))
        self.enr_Password.place(relx=0.5,rely=0.7,anchor='center')
        self.enr_Password.insert(0,"Password")
        self.enr_Password.bind('<FocusIn>',  self.Password_enter)
        self.enr_Password.bind('<FocusOut>', self.Password_leave)

        
    
    def Username_enter(self,event):
        self.enr_Username.delete(0,END)
        
        
    def Username_leave(self,event):
        current_Username = self.enr_Username.get()
        if current_Username == '':
            self.enr_Username.insert(0,"Username")
            
    def Password_enter(self,event):
        self.enr_Password.delete(0,END)
        self.enr_Password.config(show="*")
        
    def Password_leave(self,event):
        current_Password = self.enr_Password.get()
        if current_Password == '':
            self.enr_Password.config(show="")
            self.enr_Password.insert(0,"Password")


    

    def open_Overview_screen(self):
        window = Overview_Screen(self)
        window.grab_set()
        self.withdraw()
    
    
    def open_Register_screen(self):
        window = Register_Screen(self)
        window.grab_set()
        self.withdraw()

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.creat_socket, args=())
        client_handler.daemon = True
        client_handler.start()
    
    
    def creat_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1",6060))
        data = self.client_socket.recv(1024).decode()
        print("hi", self.client_socket)
    
    
    def login_user(self):
        try:
            if len(self.enr_Username.get())==0 and len(self.enr_Password.get())==0:
                messagebox.showerror("Error","Please write Username and password")
                return
            elif len(self.enr_Username.get())==0:
                messagebox.showerror("Error","Please write Username")
                return
            elif len(self.enr_Password.get())==0:
                messagebox.showerror("Error","Please write password")
                return
            else:
                arr = ["Login", self.enr_Username.get(), self.enr_Password.get()]
                str_arr = ",".join(arr)
                self.client_socket.send(str_arr.encode())
                data = self.client_socket.recv(1024).decode()
                if data == f"Welcome {self.enr_Username.get()}":
                    self.open_Overview_screen()
                else:
                    messagebox.showerror("Error",data)
                    return
        except Exception as e:
            print("Error", e)


if __name__ == "__main__":
    app = Login_Screen()
    app.mainloop()
