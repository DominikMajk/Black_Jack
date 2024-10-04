# Class PictureLoader

from PIL import ImageTk, Image
import json
import random
from tkinter import Label

class PictureLoader:
    def __init__(self,image_path,my_window):
        self.image_path = image_path
        self.my_window = my_window

        # json cards download
        with open('cards.json', 'r') as file:
            self.cards = json.load(file)

        # list of image labels
        self.image_labels = []
        self.oponent_image_labels = []
        self.max_card = 5
        self.max_oponent_card = 5

        # function to add path to choose random picture
        random_number = random.randrange(0,len(self.cards))
        current_card = (self.cards[random_number])

    def display_imagine(self, image_label,scale_factor = 6):
        #open path
        img = Image.open((f"PNG-cards-1.3\\{self.current_card["image_path"]}"))

        # images resize define
        width, height = img.size
        new_width = width//scale_factor
        new_height = height//scale_factor
        img = img.resize((new_width,new_height), Image.LANCZOS)

        #picture format to fit to image_label
        image_format = ImageTk.PhotoImage(img)
        image_label.config(image=image_format)
        image_label.img = image_format

    def count_score(self, card):
        value = int(card["value"])
        if value > 10:
            return 11
        else:
            return value

    def show_card(self):
        if len(self.image_labels) < self.max_card:  # check if count of card is less that than maximum cards in game

            # function to add path to choose random picture for next card
            self.random_number = random.randrange(0, len(self.cards))
            self.current_card = self.cards[self.random_number]

            # create new card label and position of label
            new_image_label = Label(self.my_window)
            self.display_imagine(new_image_label)
            x_position = 10 + len(self.image_labels) * 50
            new_image_label.place(x=x_position, y=10)

            # append list of labels
            self.image_labels.append(new_image_label)

            # remove display card from list (dont show card twice)
            del self.cards[self.random_number]

    def show_oponent_card(self):
        if len(self.oponent_image_labels) < self.max_oponent_card:  # check if opponent's card count is less than maximum cards

            # function to add path to choose random picture for next card
            self.random_number = random.randrange(0, len(self.cards))
            self.current_card = self.cards[self.random_number]

            # create new card label and position of label for opponent
            new_image_label = Label(self.my_window)
            self.display_imagine(new_image_label)
            x_position = 10 + len(self.oponent_image_labels) * 50
            new_image_label.place(x=x_position, y=150
                                  )  # place the opponent's cards at y=150

            # append list of opponent's labels
            self.oponent_image_labels.append(new_image_label)

            # remove displayed card from list to prevent showing the same card twice
            del self.cards[self.random_number]







