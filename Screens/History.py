import tkinter
from tkinter import *
from PIL import ImageTk, Image
import time
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import os
from tkinter import ttk, messagebox


class History_Screen(tkinter.Toplevel):
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
        self.title("History")
        self.img = Image.open('Images\\White.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)
        self.session_key = os.urandom(16)
        self.wm_iconbitmap('Images\\virus.ico')


        self.create_gui()

    def create_gui(self):
        self.lbl_background = Label(self,bg="light gray",width=45,height=20).place(relx=0.2,rely=0.4,anchor='center')
        self.lbl_text = Label(self,text="History screen allows\n you to see all your\n scans information",font=("ariel",18),bg="light gray").place(relx=0.2,rely=0.25,anchor='center')
        self.btn_previous_window = Button(self,text="Previous Window",font=("",18),width=16,bg="light gray",command=self.previous_window).place(relx=0.15,rely=0.9,anchor='center')

        self.lbl_time = Label(self,bg='light gray' ,font=("", 18))
        self.lbl_time.place(relx = 0.85,rely=0.05, anchor='center')
        self.update_label()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        tree = ttk.Treeview(self)
        tree["columns"] = ("Start", "End", "FindOrNot", "Solution")
        tree.column("#0", width=0, stretch=NO)
        tree.column("Start", width=100)
        tree.column("End", width=100)
        tree.column("FindOrNot", width=100)
        tree.column("Solution", width=100)

        # Create the column headings
        tree.heading("#0", text="")
        tree.heading("Start", text="Start")
        tree.heading("End", text="End")
        tree.heading("FindOrNot", text="FindOrNot")
        tree.heading("Solution", text="Solution")

        data = self.get_Scans()
        rows = [tuple(data[i:i+4]) for i in range(0, len(data), 4)]

        for idx, item in enumerate(rows, start=1):
            tree.insert("", END, text=str(idx), values=item)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        tree.place(x=400, y=120, relheight=0.4, relwidth=0.45)
        scrollbar.pack(side=RIGHT, fill=Y)


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

    def recv_message_arr(self):
        length = self.server.client_socket.recv(10).decode()
        str_arr = self.server.client_socket.recv(int(length)).decode()
        return str_arr.split(",")

    def get_Scans(self):        
        self.server.client_socket.send(b"Show Scans")
        self.send_message(self.UserName)
        arr_Scans = self.recv_message_arr()
        result = [','.join(arr_Scans[i+1:i+5]) for i in range(0, len(arr_Scans), 6)]
        list_result = ",".join(result)
        data = list_result.split(',')
        return data


    
    def update_label(self):
        try:
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%Y-%m-%d")
            self.lbl_time.config(text=f"{current_date} {current_time}")
            self.lbl_time.after(1000, self.update_label)
        except Exception as e:
            print("Error:",e)
            return "Error with getting current time"

    def previous_window(self):
        self.destroy()  # close the second window
        self.parent.deiconify()  # show the main window again
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to exit?"):
            self.server.client_socket.send(b'Quit')
            self.server.destroy()
            self.server.client_socket.close()
        
        
    