import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import os
import hashlib
from tkinter import filedialog


class Computer_Scan_Screen(tkinter.Toplevel):
    def __init__(self,parent,server):
        super().__init__(parent)
        self.parent = parent
        self.server = server
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

        self.create_gui()

    def create_gui(self):
        self.lbl_background = Label(self,bg="light gray",width=45,height=20).place(relx=0.2,rely=0.4,anchor='center')
        self.btn_startScan = Button(self,text="Scan your computer",font=("",18),width=16,bg="light gray",command=self.Scan).place(relx=0.8,rely=0.2,anchor='center')
        self.btn_ADVScan = Button(self,text="Advanced Scan",font=("",18),width=16,bg="light gray",command=self.Adv_Scan).place(relx=0.8,rely=0.4,anchor='center')
        self.btn_previous_window = Button(self,text="Previous Window",font=("",18),width=16,bg="light gray",command=self.previous_window).place(relx=0.15,rely=0.9,anchor='center')

    def send_message(self,message):
        length = str(len(message)).zfill(10)
        data = length+message
        self.server.client_socket.send(data.encode())
    
    def recv_message(self):
        length = self.server.client_socket.recv(10).decode()
        return self.server.client_socket.recv(int(length)).decode()
        

    def previous_window(self):
        self.destroy()  # close the second window
        self.parent.deiconify()  # show the main window again

    def Scan(self):
        def generate_md5_hash(file_path):#"C:\Users\dato0\AppData\Local\Microsoft\WindowsApps\clipchamp.exe"
             with open(file_path, 'rb') as f:
                file_hash = hashlib.md5()
                while chunk := f.read(8192):
                    file_hash.update(chunk)
                return file_hash.hexdigest()

        def get_all_hashes(root_dir):
            self.server.client_socket.send(b"Scan")
            arr_hashes = []
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    print("starting")
                    file_path = os.path.join(root, file)
                    try:
                        md5_hash = generate_md5_hash(file_path)
                        arr_hashes.append(md5_hash)
                    except PermissionError:
                        continue
            str_hashes = ",".join(arr_hashes)
            self.send_message(str_hashes)
            virus_hashes_data = self.recv_message()
            arr_virus_hashes = virus_hashes_data.split(",")
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'rb') as f:
                            file_hash = hashlib.md5(f.read()).hexdigest()
                            for virus_hash in arr_virus_hashes:
                                if file_hash == virus_hash:
                                    os.remove(file_path)
                                    print("Removed")
                    except PermissionError:
                        continue
                messagebox.showinfo(title="Viruses", message="All virus have been removed")
                return "Viruses Removed"
            print("Scan Done")
            return "The computer is clear"

        #get_all_hashes("C:\\")


    def Adv_Scan(self):
        
        def choose_path(root):
            root.withdraw()
            path = filedialog.askdirectory(initialdir = '/')
            print("Selected disk path: ", path)
            get_all_hashes(path)
            

        
        def select_path():
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
            path_button = Button(root, text="Select Disk Path",bg="orange", command=lambda: choose_path(root))
            path_button.pack()
            root.mainloop()


        def generate_md5_hash(file_path):
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()

        def get_all_hashes(root_dir):
            self.server.client_socket.send(b"Scan")
            arr_hashes = []
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    md5_hash = generate_md5_hash(file_path)
                    arr_hashes.append(md5_hash)
            str_hashes = ",".join(arr_hashes)
            self.send_message(str_hashes)
            virus_hashes_data = self.recv_message()
            print(virus_hashes_data)
            arr_virus_hashes = virus_hashes_data.split(",")
            print(arr_virus_hashes)
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                        for virus_hash in arr_virus_hashes:
                            if file_hash == virus_hash:
                                try:
                                    print(file_path)
                                    os.remove(file_path)
                                except PermissionError:
                                    os.unlink(file_path)
                    return "Viruses Removed"
                messagebox.showinfo(title="Viruses", message="All virus have been removed")
                return "Viruses Removed"
            return "The computer is clear"

        select_path()




        #root_dir = "E:\\Battle.net" # change this to the drive letter you want to search
        #for dir_name, subdir_list, file_list in os.walk(root_dir):
            #print(dir_name)
            #for file_name in file_list:
                #print(f"\t{file_name}")
                #file_path = file_name
                #length = str(len(file_path)).zfill(10)
                #data = length+file_name
                #self.parent.client_socket.send(data.encode())
                


    




        


