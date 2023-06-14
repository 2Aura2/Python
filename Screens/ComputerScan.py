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
import threading


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
        self.wm_iconbitmap('Images\\virus.ico')


        self.create_gui()

    def create_gui(self):
        self.lbl_background = Label(self,bg="light gray",width=45,height=20).place(relx=0.2,rely=0.4,anchor='center')
        self.lbl_text = Label(self,text="Scan screen\n allows you to remove\n all viruses from\n the computer",font=("ariel",18),bg="light gray").place(relx=0.2,rely=0.25,anchor='center')
        self.btn_start_scan = Button(self,text="Scan your computer",font=("",18),width=16,bg="light gray",command=self.start_scan)
        self.btn_start_scan.place(relx=0.8,rely=0.2,anchor='center')
        self.btn_advscan = Button(self,text="Advanced Scan",font=("",18),width=16,bg="light gray",command=self.start_advscan)
        self.btn_advscan.place(relx=0.8,rely=0.4,anchor='center')
        self.btn_previous_window = Button(self,text="Previous Window",font=("",18),width=16,bg="light gray",command=self.previous_window).place(relx=0.15,rely=0.9,anchor='center')
        
        self.progress_bar = ttk.Progressbar(self, mode="indeterminate",length=400)
        self.progress_bar.place(relx=0.65,rely=0.8,anchor='center')


        self.lbl_time = Label(self,bg='light gray' ,font=("", 18))
        self.lbl_time.place(relx = 0.85,rely=0.05, anchor='center')
        self.update_label()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)


    def start_scan(self):
        self.btn_start_scan.config(state=DISABLED)
        self.progress_bar.start(10)  

        scan_thread = threading.Thread(target=self.Scan2)
        scan_thread.start()

    def start_advscan(self):
        self.btn_advscan.config(state=DISABLED)
        self.progress_bar.start(10)  

        scan_thread = threading.Thread(target=self.select_path)
        scan_thread.start()


    def complete_scan(self):
        self.progress_bar.stop()
        self.btn_start_scan.config(state=NORMAL)

    def complete_advscan(self):
        self.progress_bar.stop()
        self.btn_advscan.config(state=NORMAL)


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
  
    def Scan2(self):
        root_dir = "C:\\"
        FindOrNot = ""
        start_time = datetime.datetime.now()
        try:
            self.server.client_socket.send(b"Scan")
            hash_file_dict = {}
            hash_list = []
            print("starting "+start_time)
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        md5_hash = self.generate_md5_hash(file_path)
                        if md5_hash not in hash_list and md5_hash != "Error while getting MD5 Hash":
                            hash_list.append(md5_hash)
                        if md5_hash in hash_file_dict:
                            hash_file_dict[md5_hash].append(file_path)
                        elif md5_hash not in hash_file_dict and md5_hash != "Error while getting MD5 Hash":
                            hash_file_dict[md5_hash] = [file_path]
                    except PermissionError:
                        continue
                    except OSError:
                        continue
        except Exception as e:
            print("Error1:", e)
            return "Error while getting array of file hashes"
        str_hashes = ",".join(hash_list)
        self.send_message(str_hashes)
        virus_hashes_data = self.recv_message()
        list_virus_hashes = virus_hashes_data.split(",")
        list_viruses_to_remove = []
        if len(list_virus_hashes) > 0:
            FindOrNot = "Yes"
            try:
                for virus_hash in list_virus_hashes:
                    if virus_hash in hash_file_dict:
                        list_viruses_to_remove.extend(hash_file_dict[virus_hash])
            except Exception as e:
                print("Error2:", e)
                return "Error while finding viruses"
            try:
                for virus_file in list_viruses_to_remove:
                    os.remove(virus_file)
                    print("removed: " + virus_file)
                end_time = datetime.datetime.now()
                print("Viruses removed "+end_time)
                Solution = "Removed"
                self.complete_scan()
                list_history = [start_time, end_time, FindOrNot, Solution, self.UserName]
                self.send_message_arr(list_history)
                return "Viruses Removed"
            except Exception as e:
                print("Error3:", e)
                self.complete_scan()
                return "Error while removing viruses"
        else:
            FindOrNot = "No"
            Solution = "Not Removed"
        
   
#_________________________________________________________________________________________________________________________
    
    def choose_path(self,root):
        root.withdraw()
        path = filedialog.askdirectory(initialdir = '/')
        print("Selected disk path: ", path)
        self.adv_Scan2(path)
        
    
    
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

    
    def adv_Scan2(self, root_dir):
        FindOrNot = ""
        start_time = datetime.datetime.now()
        try:
            self.server.client_socket.send(b"Scan")
            hash_file_dict = {}
            hash_list = []
            print("starting")
            print(start_time)
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        md5_hash = self.generate_md5_hash(file_path)
                        if md5_hash not in hash_list and md5_hash != "Error while getting MD5 Hash":
                            hash_list.append(md5_hash)
                        if md5_hash in hash_file_dict:
                            hash_file_dict[md5_hash].append(file_path)
                        elif md5_hash not in hash_file_dict and md5_hash != "Error while getting MD5 Hash":
                            hash_file_dict[md5_hash] = [file_path]
                    except PermissionError:
                        continue
                    except OSError:
                        continue
        except Exception as e:
            print("Error1:", e)
            return "Error while getting array of file hashes"
        str_hashes = ",".join(hash_list)
        self.send_message(str_hashes)
        virus_hashes_data = self.recv_message()
        list_virus_hashes = virus_hashes_data.split(",")
        list_viruses_to_remove = []
        if len(list_virus_hashes) > 0:
            FindOrNot = "Yes"
            try:
                for virus_hash in list_virus_hashes:
                    if virus_hash in hash_file_dict:
                        list_viruses_to_remove.extend(hash_file_dict[virus_hash])
            except Exception as e:
                print("Error2:", e)
                return "Error while finding viruses"
            try:
                for virus_file in list_viruses_to_remove:
                    os.remove(virus_file)
                    print("removed: " + virus_file)
                print("Viruses removed")
                Solution = "Removed"
                self.complete_scan()
                end_time = datetime.datetime.now()
                print(end_time)
                list_history = [start_time, end_time, FindOrNot, Solution, self.UserName]
                self.send_message_arr(list_history)
                return "Viruses Removed"
            except Exception as e:
                print("Error3:", e)
                self.complete_scan()
                return "Error while removing viruses"
        else:
            FindOrNot = "No"
            Solution = "Not Removed"


    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to exit?"):
            self.server.client_socket.send(b'Quit')
            self.server.destroy()
            self.server.client_socket.close()


                


    




        


