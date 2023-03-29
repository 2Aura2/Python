import tkinter as tk
from tkinter import *
import time

def update_label():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%Y-%m-%d")
    label.config(text=f"{current_date} {current_time}")
    label.after(1000, update_label)

# Create the main window
root = tk.Tk()
root.title("Real Time and Date")

# Create a label to display the current time and date
label = tk.Label(root, font=("Arial", 18), justify="center")
label.pack(padx=50, pady=50)

# Call the update_label function every second to update the label with the current time and date
update_label()

# Run the main loop
root.mainloop()
