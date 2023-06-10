import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import os
import hashlib
from tkinter import filedialog
import time
import datetime
from Crypto.Cipher import AES, PKCS1_OAEP
import base64

class Computer_Scan_Screen(tkinter.Toplevel):
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
        self.title("Computer Scan")
        self.img = Image.open('Images\\White.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)
        self.session_key = os.urandom(16)

        self.create_gui()

    def create_gui(self):
        self.lbl_background = Label(self,bg="light gray",width=45,height=20).place(relx=0.2,rely=0.4,anchor='center')
        self.lbl_text = Label(self,text="Scan screen\n allows you to remove\n all viruses from\n the computer",font=("ariel",18),bg="light gray").place(relx=0.2,rely=0.25,anchor='center')
        self.btn_startScan = Button(self,text="Scan your computer",font=("",18),width=16,bg="light gray",command=self.Scan).place(relx=0.8,rely=0.2,anchor='center')
        self.btn_ADVScan = Button(self,text="Advanced Scan",font=("",18),width=16,bg="light gray",command=self.select_path).place(relx=0.8,rely=0.4,anchor='center')
        self.btn_previous_window = Button(self,text="Previous Window",font=("",18),width=16,bg="light gray",command=self.previous_window).place(relx=0.15,rely=0.9,anchor='center')
        
        self.lbl_time = Label(self,bg='light gray' ,font=("", 18))
        self.lbl_time.place(relx = 0.85,rely=0.05, anchor='center')
        self.update_label()

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
        print(encrypted_message)
        encoded_message = base64.b64encode(encrypted_message).decode()
        length = str(len(encoded_message)).zfill(10)
        data = length+encoded_message
        self.server.client_socket.send(data.encode())


    def send_message_arr(self,arr):
        try:
            str_arr = ",".join(arr)
            cipher = PKCS1_OAEP.new(self.public_key)
            encrypted_str_arr = cipher.encrypt(str_arr.encode())
            encoded_str_arr = base64.b64encode(encrypted_str_arr).decode()
            length = str(len(encoded_str_arr)).zfill(10)
            data = length+encoded_str_arr
            self.server.client_socket.send(data.encode()) 
        except Exception as e:
            print("Error:",e)
            return "Error while sending message"

    def recv_message(self):
        length = self.server.client_socket.recv(10).decode()
        return self.server.client_socket.recv(int(length)).decode()
        

    def previous_window(self):
        self.destroy()  # close the second window
        self.parent.deiconify()  # show the main window again

#_____________________________________________________________________________________________________________________________________


    def generate_md5_hash(self,file_path):#"C:\Users\dato0\AppData\Local\Microsoft\WindowsApps\clipchamp.exe"
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5()
                while chunk := f.read(8192):
                    file_hash.update(chunk)
                return file_hash.hexdigest()
        except Exception as e:
            print("Error:",e)
            return "Error while getting MD5 Hash"

    def Scan(self,root_dir):
        try:
            self.server.client_socket.send(b"Scan")
            arr_hashes = []
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    print("starting")
                    file_path = os.path.join(root, file)
                    try:
                        md5_hash = self.generate_md5_hash(file_path)
                        arr_hashes.append(md5_hash)
                    except PermissionError:
                        continue
                    except OSError:
                        continue
        except Exception as e:
            print("Error:",e)
            return "Error while getting array of file hashes"
        str_hashes = ",".join(arr_hashes)
        self.send_message(str_hashes)
        virus_hashes_data = self.recv_message()
        arr_virus_hashes = virus_hashes_data.split(",")
        try:
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                        for virus_hash in arr_virus_hashes:
                            if file_hash == virus_hash:
                                self.arr_viruses_to_remove.append(file_path)
        except Exception as e:
            print("Error:",e)
            return "Error while finding viruses"
        try:
            for virues in self.arr_viruses_to_remove:
                os.remove(virues)
            print("Viruses removed")
            return "Viruses Removed"
        except Exception as e:
            print("Error:",e)
            return "Error while removing viruses"
    


#_________________________________________________________________________________________________________________________
    
    def choose_path(self,root):
        root.withdraw()
        path = filedialog.askdirectory(initialdir = '/')
        print("Selected disk path: ", path)
        self.adv_Scan(path)
        
    
    
    def select_path(self):
        root = Tk()
        root.title("Virus Scanner")
        root.configure(background="grey")
        root.app_width = 500
        root.app_height = 100
        root.screen_width = root.winfo_screenwidth()
        root.screen_height = root.winfo_screenheight()
        root.x = (root.screen_width / 2)-(root.app_width / 2)
        root.y = (root.screen_height / 2)-(root.app_height / 2)
        root.geometry(f"{root.app_width}x{root.app_height}+{int(root.x)}+{int(root.y)}")
        path_button = Button(root, text="Select Disk Path",bg="orange", command=lambda: self.choose_path(root))
        path_button.pack()
        root.mainloop()

    def adv_Scan(self,root_dir):
        self.arr_viruses_to_remove = []
        FindOrNot = ""
        start_time = datetime.datetime.now()
        print(start_time)
        self.server.client_socket.send(b"Scan")
        arr_hashes = []
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                md5_hash = self.generate_md5_hash(file_path)
                arr_hashes.append(md5_hash)
        str_hashes = ",".join(arr_hashes)
        self.send_message(str_hashes)
        virus_hashes_data = self.recv_message()
        print(virus_hashes_data)
        arr_virus_hashes = virus_hashes_data.split(",")
        print(arr_virus_hashes)
        if len(arr_virus_hashes) == 0:
            FindOrNot = "No"
            Solution = "Not Removed"
        else:
            FindOrNot = "Yes"
            Solution = "Removed"
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                    for virus_hash in arr_virus_hashes:
                        if file_hash == virus_hash:
                            self.arr_viruses_to_remove.append(file_path)
        for virues in self.arr_viruses_to_remove:
            os.remove(virues)
        print("Viruses removed")
        end_time = datetime.datetime.now()
        print(end_time)
        arr_history = [start_time, end_time, FindOrNot, Solution, self.UserName]
        self.send_message_arr(arr_history)
        return "Viruses Removed"
    
    


                


    




        


