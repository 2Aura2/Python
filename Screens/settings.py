import tkinter
from tkinter import *
from PIL import ImageTk, Image
import traceback
from tkinter import messagebox
import time
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import os
import traceback

class Settigns_Screen(tkinter.Toplevel):
    def __init__(self,parent,server,UserName,public_key):
        super().__init__(parent)
        self.parent = parent
        self.server = server
        self.UserName = UserName
        self.public_key = public_key
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
        self.data = None
        self.session_key = os.urandom(16)
        self.wm_iconbitmap('Images\\virus.ico')

        self.create_gui()

    def create_gui(self):
        self.lbl_background = Label(self,bg="light gray",width=45,height=20).place(relx=0.2,rely=0.4,anchor='center')
        self.lbl_text = Label(self,text="Settings screen allows\n you to change your\n account information and\n Logout from your account",font=("ariel",18),bg="light gray").place(relx=0.2,rely=0.25,anchor='center')
        self.btn_previous_window = Button(self,text="Previous Window",font=("",18),width=16,bg="light gray",command=self.previous_window).place(relx=0.15,rely=0.9,anchor='center')
        self.btn_Logout = Button(self,text="Logout",font=("",18),bg="light gray",command=self.Login_window).place(relx=0.8,rely=0.2,anchor='center')
        
        
        self.btn_AddEmail = Button(self,textvariable=None,font=("",18),width=15,bg="light gray",command=self.AddEmail)
        self.btn_AddEmail.place(relx=0.6,rely=0.2,anchor='center')
        self.textvar = None
        self.EmailExists()
        
        
        self.btn_ChangePassword = Button(self,text="Change Password",font=("ariel",18),command=self.ChangePassword,bg="light gray")
        self.btn_ChangePassword.place(relx=0.6,rely=0.35,anchor='center')
        
        self.btn_ChangeUserName = Button(self,text="Change UserName",font=("ariel",18),command=self.ChangeUserName,bg="light gray")
        self.btn_ChangeUserName.place(relx=0.6,rely=0.5,anchor='center')

        self.lbl_time = Label(self,bg='light gray' ,font=("", 18))
        self.lbl_time.place(relx = 0.85,rely=0.05, anchor='center')
        self.update_label()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_label(self):
        try:
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%Y-%m-%d")
            self.lbl_time.config(text=f"{current_date} {current_time}")
            self.lbl_time.after(1000, self.update_label)
        except Exception as e:
            print("Error:",e)
            return "Error with getting current time"
        
    def send_message(self,message):
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted_message = cipher.encrypt(message.encode())
        encoded_message = base64.b64encode(encrypted_message).decode()
        length = str(len(encoded_message)).zfill(10)
        data = length+encoded_message
        self.server.client_socket.send(data.encode())
    
    def recv_message(self):
        length = self.server.client_socket.recv(10).decode()
        return self.server.client_socket.recv(int(length)).decode()
        
    def ChangeUserName(self):
        self.popup_window = Toplevel(self)
        app_width = 220
        app_height = 100
        screen_width = self.popup_window.winfo_screenwidth()
        screen_height = self.popup_window.winfo_screenheight()
        x = (screen_width / 2)-(app_width / 2)
        y = (screen_height / 2)-(app_height / 2)
        self.popup_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.popup_window.title("Change UserName")
        self.popup_window.config(bg="light grey")
        Label(self.popup_window,text="Enter a new UserName:",font=("ariel",14)).pack()
        popup_entry = Entry(self.popup_window,font=("ariel",14))
        popup_entry.pack()
        Button(self.popup_window, text="Submit",font=("ariel",14),command=lambda:self.Submit_UserName(popup_entry.get(),self.UserName)).pack()
        
    def Submit_UserName(self,NewUserName,UserName):
        try:
            if len(NewUserName) > 0 and NewUserName != UserName:
                self.server.client_socket.send(b'ChangeUserName')
                self.send_message(NewUserName)
                self.send_message(UserName)
                self.data = self.recv_message()
                messagebox.showinfo("Message Box", self.data)
            self.popup_window.destroy()
        except Exception as e:
            print(e)
            traceback.print_exc()
            return "canceled"
    
    
    def ChangePassword(self):
        self.popup_window = Toplevel(self)
        app_width = 220
        app_height = 100
        screen_width = self.popup_window.winfo_screenwidth()
        screen_height = self.popup_window.winfo_screenheight()
        x = (screen_width / 2)-(app_width / 2)
        y = (screen_height / 2)-(app_height / 2)
        self.popup_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.popup_window.title("Change Password")
        self.popup_window.config(bg="light grey")
        Label(self.popup_window,text="Enter a new password:",font=("ariel",14)).pack()
        popup_entry = Entry(self.popup_window,font=("ariel",14))
        popup_entry.pack()
        Button(self.popup_window, text="Submit",font=("ariel",14),command=lambda:self.Submit_Password(popup_entry.get(),self.UserName)).pack()

         
    def Submit_Password(self,Password,UserName):
        try:
            if len(Password) > 0:
                self.server.client_socket.send(b'ChangePassword')
                self.send_message(Password)
                self.send_message(UserName)
                self.recv_message()
                messagebox.showinfo("Message Box", "Password changed successfully")
            self.popup_window.destroy()
        except Exception as e:
            print(e)
            traceback.print_exc()
            return "canceled"
        

    def AddEmail(self):
        self.popup_window = Toplevel(self)
        app_width = 220
        app_height = 100
        screen_width = self.popup_window.winfo_screenwidth()
        screen_height = self.popup_window.winfo_screenheight()
        x = (screen_width / 2)-(app_width / 2)
        y = (screen_height / 2)-(app_height / 2)
        self.popup_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.popup_window.title("AddEmail")
        self.popup_window.config(bg="light grey")
        Label(self.popup_window,text="Enter an Email:",font=("ariel",14)).pack()
        popup_entry = Entry(self.popup_window,font=("ariel",14))
        popup_entry.pack()
        Button(self.popup_window, text="Submit",font=("ariel",14),command=lambda:self.Submit_AddEmail(popup_entry.get())).pack()

    
        
          
    def Submit_AddEmail(self,Email):
        try:
            if len(Email) > 0:
                self.server.client_socket.send("AddEmail".encode())
                self.send_message(Email)
                self.send_message(self.UserName)
            self.popup_window.destroy()
        except Exception as e:
            print(e)
            traceback.print_exc()
            return "canceled"
        
    def EmailExists(self):
        self.server.client_socket.send(b'EmailExists')
        self.send_message(self.UserName)
        answer = self.recv_message()
        if answer == "Exists":
            self.textvar = StringVar(self,"Change Email")
            self.btn_AddEmail.config(textvariable=self.textvar)
        elif answer == "None":
            self.textvar = StringVar(self,"Add Email")
            self.btn_AddEmail.config(textvariable=self.textvar)



    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to exit?"):
            self.server.client_socket.send(b'Quit')
            self.server.destroy()
            self.server.client_socket.close()


    def Login_window(self):
        if messagebox.askokcancel("Logout", "Do you want to Logout?"):
            self.server.client_socket.send(b'Logout')
            self.destroy()
            self.server.deiconify()
        


    def previous_window(self):
        self.destroy()
        self.parent.deiconify() 