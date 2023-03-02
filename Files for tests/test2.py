import tkinter as tk
from PIL import Image, ImageTk

class Example(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill='both', expand=True)
        
        # Load and set the background image for the window
        self.bg_image = Image.open('Images\\solid3.jpg')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a transparent button
        self.button_image = Image.open('Images\\button2.1.png')
        self.button_image = self.button_image.convert('RGBA')
        self.button_photo = ImageTk.PhotoImage(self.button_image)
        self.button = tk.Button(self, image=self.button_photo, bd=0, highlightthickness=0, command=self.on_button_click)
        self.button.place(x=100, y=100)

    def on_button_click(self):
        print('Button clicked')

root = tk.Tk()
app = Example(root)
app.mainloop()
