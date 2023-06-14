import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os
import shutil
import sys
import subprocess
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import tempfile
from tkinter import messagebox



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
        self.img = Image.open('Images\\White.jpg')
        self.resized = self.img.resize((1920,1080), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized)
        self.IMGLabel = Label(self, image=self.bg)
        self.IMGLabel.pack(expand=YES)
        self.wm_iconbitmap('Images\\virus.ico')

        self.create_gui()

    def create_gui(self):
        self.lbl_background = Label(self,bg="light gray",width=45,height=20).place(relx=0.2,rely=0.4,anchor='center')
        self.lbl_text = Label(self,text="Junk Files Remover screen\n allows you to remove all\n unneeded files from\n the computer",font=("ariel",18),bg="light gray").place(relx=0.2,rely=0.25,anchor='center')
        self.btn_Temp = Button(self,text="Clean temp files",font=("",18),width=16,bg="light gray",command=self.delete_temp_files).place(relx=0.8,rely=0.2,anchor='center')
        self.btn_Cache = Button(self,text="Clean browser cache",font=("",18),width=16,bg="light gray",command=self.remove_browser_cache).place(relx=0.8,rely=0.4,anchor='center')
        self.btn_UninstallUtility = Button(self,text="Uninstallation Program",font=("",17),width=17,bg="light gray",command=self.Uninstallation_utility).place(relx=0.8,rely=0.6,anchor='center')
        self.btn_previous_window = Button(self,text="Previous Window",font=("",18),width=16,bg="light gray",command=self.previous_window).place(relx=0.15,rely=0.9,anchor='center')
        
        
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
        
        
    def previous_window(self):
        self.destroy()  # close the second window
        self.parent.deiconify()  # show the main window again
        

    # def BasicClean(self):
    #     folder_path = sys.argv[1]
    #     for root, dirs, files in os.walk(folder_path):
    #         for file in files:
    #             file_path = os.path.join(root, file)
    #             if os.path.getsize(file_path) == 0:
    #                 os.remove(file_path)
    #             elif os.path.isdir(file_path):
    #                 shutil.rmtree(file_path)


    def remove_browser_cache(self):
        cache_dirs = [
            os.path.expanduser(r"~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache"),
            os.path.expanduser(r"~\\AppData\\Local\\Mozilla\\Firefox\\Profiles"),
            os.path.expanduser(r"~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache")
        ]
        for cache_dir in cache_dirs:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
                print("removed")
    

    def Uninstallation_utility(self):
        # def uninstall_program():
        #     selected_program = programs_listbox.get(ACTIVE)
        #     command = f'wmic product where "name like \'{selected_program}%%\'" call uninstall'
        #     subprocess.call(command, shell=True)

        def uninstall_program():
            try:
                selected_program = programs_listbox.get(ACTIVE)
                command = f'wmic product where "name like \'{selected_program}%%\'" call uninstall'
                subprocess.check_call(command, shell=True)
                print(f'{selected_program} successfully uninstalled.')
            except subprocess.CalledProcessError as e:
                print(f'Error: {e}')

        command = "wmic product get name"
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        program_list = result.stdout.decode("latin-1").split("\n")[1:-1]


        root = Tk()
        root.title("Uninstall Programs")
        programs_listbox = Listbox(root, height=20,width=50)
        for program in program_list:
            programs_listbox.insert(END, program.strip())
        programs_listbox.pack()


        uninstall_button = Button(root, text="Uninstall", command=uninstall_program)
        uninstall_button.pack()


        root.mainloop()
            
            

    def delete_temp_files(self):
        temp_dir = os.path.join(tempfile.gettempdir())
        for root, dirs, files in os.walk(temp_dir, topdown=False):
            for file in files:
                if file.endswith((".tmp", ".log", ".bak", ".cache", ".png", ".txt", ".html", ".exe", ".dat", ".bin", ".ses", ".db", ".json", ".lock", ".cpuprofile", ".ico")):
                    try:
                        os.remove(os.path.join(root, file))
                        print(f"Deleted file: {os.path.join(root, file)}")
                    except PermissionError as e:
                        print(f"Error deleting file {file}: {e}")
                        pass
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir))
                    print(f"Deleted directory: {os.path.join(root, dir)}")
                except OSError as e:
                    print(f"Error deleting directory {dir}: {e}")
                    pass
        messagebox.showinfo("Window", "All temp files were cleaned")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to exit?"):
            self.parent.client_socket.send(b'Logout')
            self.server.destroy()

    # def disk_cleanup():
    #     subprocess.run("cleanmgr /sagerun:7 /dWER /dThumbnails /dDownloadedProgramFiles /dTemporaryInternetFiles /dSystemArchive /dSystem", shell=True)

    #/dWER: Windows error reports
    #/dThumbnails: Thumbnails
    #/dDownloadedProgramFiles: Downloaded program files
    #/dTemporaryInternetFiles: Temporary internet files
    #/dSystemArchive: System archived Windows Error Reporting Files
    #/dSystem: System error memory dump files

    