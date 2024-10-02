# Class main
from tkinter import *
from pictures_loader import PictureLoader

# main window
my_window = Tk()
my_window.minsize(300, 300)
my_window.resizable(False, False)
my_window.title("Black Jack")
my_window.config(bg="#64a367")

def set_title():
    my_window.title("Bboy")

#inicialization picture_loader:
picture= PictureLoader("path",my_window)

# Button
first_button = Button(my_window, width=7, height=3, text="click", command= picture.show_card,)
first_button.place(x=100, y=230)

second_button = Button(my_window, width=7, height=3, text="konec", command= my_window.destroy)
second_button.place(x=200, y = 230)
# Main loop
my_window.mainloop()

