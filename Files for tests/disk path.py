import tkinter as tk
from tkinter import filedialog

def select_path():
    path = filedialog.askdirectory(initialdir = '/')
    print("Selected disk path: ", path)
    # Perform virus scan on the selected disk path here

root = tk.Tk()
root.title("Virus Scanner")

path_button = tk.Button(root, text="Select Disk Path", command=select_path)
path_button.pack()

root.mainloop()


#import os

#def scan_drive(drive):
    #for root, dirs, files in os.walk(drive):
        #for file in files:
            #file_path = os.path.join(root, file)
            #print("Scanning: ", file_path)
            ## Perform virus scan on the file here

#scan_drive("C:\\")