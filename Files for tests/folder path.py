import tkinter as tk
from tkinter import filedialog

def select_path():
    path = filedialog.askdirectory()
    print("Selected folder path: ", path)
    # Perform virus scan on the selected folder path here

root = tk.Tk()
root.title("Virus Scanner")

path_button = tk.Button(root, text="Select Folder Path", command=select_path)
path_button.pack()

root.mainloop()