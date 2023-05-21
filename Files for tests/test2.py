import tkinter as tk
from tkinter import messagebox

def show_message_box():
    messagebox.showinfo("change", " Email changed successfully")

# Create the main window
window = tk.Tk()

# Create a button widget
button = tk.Button(window, text="Click me!", command=show_message_box)
button.pack()

# Start the Tkinter event loop
window.mainloop()
        










        
