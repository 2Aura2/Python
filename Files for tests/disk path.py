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