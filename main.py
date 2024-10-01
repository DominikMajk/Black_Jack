# Class main

from tkinter import *
from pictures_loader import PictureLoader

# main window
my_window = Tk()
my_window.minsize(300, 300)
my_window.resizable(False, False)
my_window.title("Black Jack")
my_window.config(bg="#64a367")

y = 0
# button for show card
def show_card():
    global y
    picture.display_imagine(image_label2)
    y += 1
    print(y)


# Text label
#text_label = Label(my_window, font=("Helvetica", 10), text="text place")
#text_label.place(x= 100,y= 100)

# Button
first_button = Button(my_window, width=7, height=3, text="click", command=show_card)
first_button.place(x=100, y=230)

#Image
image_label = Label(my_window)
image_label2 = Label(my_window)
image_label.place(x = 20, y = 0)
image_label2.place(x = 30, y =10)

#inicialization picture_loader:
picture= PictureLoader("path")

# Main loop
picture.display_imagine(image_label)
my_window.mainloop()

