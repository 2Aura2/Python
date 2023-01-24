import tkinter as tk
from tkinter import filedialog

def select_path():
    path = filedialog.askopenfilename()
    print("Selected file path: ", path)
    # Perform virus scan on the selected file path here

root = tk.Tk()
root.title("Virus Scanner")

path_button = tk.Button(root, text="Select File Path", command=select_path)
path_button.pack()

root.mainloop()