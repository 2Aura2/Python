import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os
import shutil
import sys
import subprocess


class Junk_Files_Screen(tkinter.Toplevel):
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
        self.title("Junk Files Remover")
        self.img = Image.open('Images\Anti_Virus_BG.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)

        self.create_gui()

    def create_gui(self):
        #self.btn_Overview = Button(self,text="Overview",font=("",18),width=16,bg="orange",command=self.open_overview_screen).place(relx=0.2,rely=0.2,anchor='center')
        #self.btn_Computer_Scan = Button(self,text="Computer Scan",font=("",18),width=16,bg="orange",command=self.open_Computer_Scan_screen).place(relx=0.2,rely=0.35,anchor='center')
        #self.btn_Junk_Files_Remover = Button(self,text="Junk Files Remover",font=("",18),bg="light blue").place(relx=0.2,rely=0.5,anchor='center')
        #self.btn_History = Button(self,text="History",font=("",18),width=16,bg="orange",command=self.open_history_screen).place(relx=0.2,rely=0.65,anchor='center')
        #self.btn_settings = Button(self,text="Settings",font=("",18),width=16,bg="orange",command=self.open_settings_screen).place(relx=0.2,rely=0.8,anchor='center')

        self.btn_startScan = Button(self,text="Clean",font=("",18),width=16,bg="light green").place(relx=0.8,rely=0.2,anchor='center')
        self.btn_ADVScan = Button(self,text="Clean 2",font=("",18),width=16,bg="light green").place(relx=0.8,rely=0.4,anchor='center')
        self.btn_previous_window = Button(self,text="Previous Window",font=("",18),width=16,bg="light blue",command=self.previous_window).place(relx=0.15,rely=0.9,anchor='center')

    def previous_window(self):
        self.destroy()  # close the second window
        self.parent.deiconify()  # show the main window again
        

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

    def disk_cleanup():
        subprocess.run("cleanmgr /sagerun:7 /dWER /dThumbnails /dDownloadedProgramFiles /dTemporaryInternetFiles /dSystemArchive /dSystem", shell=True)

    #/dWER: Windows error reports
    #/dThumbnails: Thumbnails
    #/dDownloadedProgramFiles: Downloaded program files
    #/dTemporaryInternetFiles: Temporary internet files
    #/dSystemArchive: System archived Windows Error Reporting Files
    #/dSystem: System error memory dump files

    