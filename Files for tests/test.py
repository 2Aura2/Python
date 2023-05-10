import shutil 
import tempfile
import os
import tkinter as tk
import subprocess

#temp_dir = os.path.join(tempfile.gettempdir())
def delete_temp_files():
        temp_dir = os.path.join(tempfile.gettempdir())
        for root, dirs, files in os.walk(temp_dir, topdown=False):
            for file in files:
                if file.endswith((".tmp", ".log", ".bak", ".cache", ".png", ".txt", ".html", ".exe", ".dat", ".bin", ".ses", ".db")):
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

#print(temp_dir)
#delete_temp_files()




# Define the function to uninstall the selected program
def uninstall_program():
    # Get the selected program from the listbox widget
    selected_program = programs_listbox.get(tk.ACTIVE)
    
    # Construct the command to uninstall the program using wmic
    command = f"wmic product where name='{selected_program}' call uninstall"
    
    # Run the command in a subprocess
    subprocess.call(command, shell=True)

# Get the list of installed programs using wmic
command = "wmic product get name"
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
program_list = result.stdout.decode("utf-8").split("\n")[1:-1]

# Create the Tkinter window and listbox widget
root = tk.Tk()
root.title("Uninstall Programs")
programs_listbox = tk.Listbox(root, height=500,width=500)
for program in program_list:
    programs_listbox.insert(tk.END, program.strip())
programs_listbox.pack()

# Create the "Uninstall" button
uninstall_button = tk.Button(root, text="Uninstall", command=uninstall_program)
uninstall_button.pack()

# Start the Tkinter main loop
root.mainloop()
