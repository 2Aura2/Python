import tkinter
from tkinter import *
from PIL import ImageTk, Image
import Login
import traceback
from tkinter import messagebox
class Settigns_Screen(tkinter.Toplevel):
    def __init__(self,parent,server,UserName):
        super().__init__(parent)
        self.parent = parent
        self.server = server
        self.UserName = UserName
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

        self.create_gui()

    def create_gui(self):
        self.lbl_background = Label(self,bg="light gray",width=45,height=20).place(relx=0.2,rely=0.4,anchor='center')
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

        
    def send_message(self,message):
        length = str(len(message)).zfill(10)
        data = length+message
        self.server.client_socket.send(data.encode())
    
    def recv_message(self):
        length = self.server.client_socket.recv(10).decode()
        return self.server.client_socket.recv(int(length)).decode()
        
    def ChangeUserName(self):
        self.popup_window = Toplevel(self)
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
                messagebox.showinfo("Message Box", self.data)
            self.popup_window.destroy()
        except Exception as e:
            print(e)
            traceback.print_exc()
            return "canceled"
        

    def AddEmail(self):
        self.popup_window = Toplevel(self)
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






    def Login_window(self):
        self.destroy()  # close the second window
        self.server.deiconify()  # show the main window again


    def previous_window(self):
        self.destroy()  # close the second window
        self.parent.deiconify()  # show the main window again