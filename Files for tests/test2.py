import tkinter as tk
from tkinter import ttk

# Create the main Tkinter window
root = tk.Tk()
root.title("Table Example")

# Create a Treeview widget
tree = ttk.Treeview(root)

# Define the columns
tree["columns"] = ("Time1", "Time2", "Option1", "Option2")

# Format the columns
tree.column("#0", width=0, stretch=tk.NO)  # Hide the first empty column
tree.column("Time1", width=100)
tree.column("Time2", width=100)
tree.column("Option1", width=100)
tree.column("Option2", width=100)

# Create the column headings
tree.heading("#0", text="")
tree.heading("Time1", text="Time 1")
tree.heading("Time2", text="Time 2")
tree.heading("Option1", text="Option 1")
tree.heading("Option2", text="Option 2")

# Sample data as a flat list
data = [
    '12:30', '13:00', 'Yes', 'Removed',
    '9:15', '9:20', 'No', 'Nothing',
    '15:00', '15:10', 'No', 'Nothing'
]

# Restructure the flat list into tuples representing each row
rows = [tuple(data[i:i+4]) for i in range(0, len(data), 4)]

# Insert data rows using a for loop
for idx, item in enumerate(rows, start=1):
    tree.insert("", tk.END, text=str(idx), values=item)

# Create a vertical scroll bar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Pack the Treeview widget and scroll bar
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start the Tkinter event loop
root.mainloop()









        
