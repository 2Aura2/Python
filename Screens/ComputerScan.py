import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import os
import hashlib

class Computer_Scan_Screen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("960x540")
        self.title("Computer Scan")
        self.img = Image.open('Images\Anti_Virus_BG.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)

        self.create_gui()

    def create_gui(self):
        self.btn_settings = Button(self,text="Overview",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.2,anchor='center')
        self.btn_settings = Button(self,text="Computer Scan",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.35,anchor='center')
        self.btn_settings = Button(self,text="Junk Files Remover",font=("",18),bg="orange").place(relx=0.2,rely=0.5,anchor='center')
        self.btn_settings = Button(self,text="History",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.65,anchor='center')
        self.btn_settings = Button(self,text="Settings",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.8,anchor='center')
        
        self.btn_startScan = Button(self,text="Scan your computer",font=("",18),width=16,bg="light green").place(relx=0.8,rely=0.2,anchor='center')
        self.btn_ADVScan = Button(self,text="Advanced Scanning",font=("",18),width=16,bg="light green").place(relx=0.8,rely=0.2,anchor='center')


    def Scan(self):
        self.parent.client_socket.send("Scan".encode())
        def generate_md5_hash(file_path):
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()

        def get_all_hashes(root_dir):
            arr_hashes = []
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    md5_hash = generate_md5_hash(file_path)
                    arr_hashes.append(md5_hash)
                    str_hashes = ",".join(arr_hashes)
                    length = str(len(str_hashes)).zfill(10)
                    data = length+str_hashes
                    self.parent.client_socket.send(data.encode())
                    #print(f"File: {file_path} \n MD5 Hash: {md5_hash}")
            length_data = self.parent.client_socket.recv(10).decode()
            virus_hashes_data = self.parent.client.socket.recv(length_data).decode()
            arr_virus_hashes = virus_hashes_data.split(",")
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                        for virus_hash in arr_virus_hashes:
                            if file_hash == virus_hash:
                                os.remove(file_path)
                messagebox.showinfo(title="Viruses", message="All virus have been removed")
                return "Viruses Removed"
            return "The computer is clear"




        root_dir = "E:\\Battle.net" # change this to the drive letter you want to search
        for dir_name, subdir_list, file_list in os.walk(root_dir):
            print(dir_name)
            for file_name in file_list:
                print(f"\t{file_name}")
                file_path = file_name
                length = str(len(file_path)).zfill(10)
                data = length+file_name
                self.parent.client_socket.send(data.encode())



        


