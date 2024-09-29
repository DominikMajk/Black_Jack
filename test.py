from tkinter import *

from pictures_loader import PictureLoader

# main window
my_window = Tk()
my_window.minsize(300, 300)
my_window.resizable(False, False)
my_window.title("Black Jack")
my_window.config(bg="#64a367")


first_label = Label(my_window)
first_label.pack(pady = 20)

pictures_loader = PictureLoader("PNG-cards-1.3\\2_of_hearts.png")
pictures_loader.display_imagine(first_label)

my_window.mainloop()