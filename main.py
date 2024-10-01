# Class main

from tkinter import *
from pictures_loader import PictureLoader
import random

# main window
my_window = Tk()
my_window.minsize(300, 300)
my_window.resizable(False, False)
my_window.title("Black Jack")
my_window.config(bg="#64a367")

#Image
# image_label = Label(my_window)
# image_label.place(x = 0, y = 0)

# image_label2 = Label(my_window)
# image_label2.place(x = 150, y =10)

#inicialization picture_loader:
picture= PictureLoader("path")
picture.display_imagine(Label(my_window))

#list of image labels
image_labels = []
max_card = 5

# button for show card
def show_card():
    if len(image_labels) <max_card: # check if count of card is less that than maximum cards in game

        # function to add path to choose random picture for next card
        picture.random_number = (random.randrange(0, len(picture.cards)))
        picture.current_card = picture.cards[picture.random_number]["image_path"]

        #create new card label
        new_image_label = Label(my_window)
        picture.display_imagine(new_image_label)

        # position of new label
        x_position = 10 + len(image_labels) * 50
        new_image_label.place(x = x_position, y = 0)

        # append list of labels
        image_labels.append(new_image_label)

        print(image_labels)

# Button
first_button = Button(my_window, width=7, height=3, text="click", command=show_card)
first_button.place(x=100, y=230)


# Main loop
my_window.mainloop()

