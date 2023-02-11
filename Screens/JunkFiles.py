import tkinter
from tkinter import *
from PIL import ImageTk, Image
import Overview
import ComputerScan
import os
import shutil
import sys



class Junk_Files_Screen(tkinter.Toplevel):
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
        self.title("Computer Scan")
        self.img = Image.open('Images\Anti_Virus_BG.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)

        self.create_gui()

    def create_gui(self):
        self.btn_Overview = Button(self,text="Overview",font=("",18),width=16,bg="orange",command=self.open_overview_screen).place(relx=0.2,rely=0.2,anchor='center')
        self.btn_Computer_Scan = Button(self,text="Computer Scan",font=("",18),width=16,bg="orange",command=self.open_Computer_Scan_screen).place(relx=0.2,rely=0.35,anchor='center')
        self.btn_Junk_Files_Remover = Button(self,text="Junk Files Remover",font=("",18),bg="light blue").place(relx=0.2,rely=0.5,anchor='center')
        self.btn_History = Button(self,text="History",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.65,anchor='center')
        self.btn_settings = Button(self,text="Settings",font=("",18),width=16,bg="orange").place(relx=0.2,rely=0.8,anchor='center')
        

    def BasicClean(self):
        folder_path = sys.argv[1]
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

    def remove_temp_files(self):
        temp_dir = os.environ["TEMP"]
        if os.path.exists(temp_dir):
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except PermissionError:
                        pass


    def remove_browser_cache():
        cache_dirs = [
            os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Default\Cache"),
            os.path.expanduser(r"~\AppData\Local\Mozilla\Firefox\Profiles"),
            os.path.expanduser(r"~\AppData\Local\Microsoft\Edge\User Data\Default\Cache")
        ]
        for cache_dir in cache_dirs:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)



    def open_overview_screen(self):
        window = Overview.Overview_Screen(self)
        window.grab_set()
        self.withdraw()

    def open_Computer_Scan_screen(self):
        window = ComputerScan.Computer_Scan_Screen(self)
        window.grab_set()
        self.withdraw()