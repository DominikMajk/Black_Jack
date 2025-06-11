from PIL import ImageTk, Image
import json
import random
from tkinter import Label

class PictureLoader:
    def __init__(self, image_path, my_window):
        self.image_path = image_path
        self.my_window = my_window

        # Load cards from JSON file
        with open('cards.json', 'r') as file:
            self.cards = json.load(file)

        # List of image labels for player and opponent
        self.image_labels = []
        self.oponent_image_labels = []
        self.max_card = 5
        self.max_oponent_card = 5

        self.backround = "backround.png"

        # Choose a random card at initialization
        random_number = random.randrange(0, len(self.cards))
        current_card = (self.cards[random_number])

    def display_imagine(self, image_label, scale_factor=6):
        # Open image by path
        img = Image.open(f"PNG-cards-1.3\\{self.current_card['image_path']}")

        # Resize image
        width, height = img.size
        new_width = width // scale_factor
        new_height = height // scale_factor
        img = img.resize((new_width, new_height), Image.LANCZOS)

        # Format image for label
        image_format = ImageTk.PhotoImage(img)
        image_label.config(image=image_format)
        image_label.img = image_format

    def count_score(self, card):
        if "value" not in card:
            return 0  # or handle as needed
        value = int(card["value"])
        if value > 10:
            return 11
        else:
            return value

    def show_card(self):
        if len(self.image_labels) < self.max_card:  # Check if player's card count is less than maximum

            # Choose a random card for the next draw
            self.random_number = random.randrange(0, len(self.cards))
            self.current_card = self.cards[self.random_number]

            # Create new card label and set its position
            new_image_label = Label(self.my_window)
            self.display_imagine(new_image_label)
            x_position = 10 + len(self.image_labels) * 50
            new_image_label.place(x=x_position, y=10)

            # Append to list of player's labels
            self.image_labels.append(new_image_label)

            # Remove displayed card from list (prevent duplicate cards)
            del self.cards[self.random_number]

    def reveal_hidden_card(self):
        if len(self.oponent_image_labels) > 0 and self.hidden_card:
            # Get the first label (background) and replace it with the real card
            hidden_card_label = self.oponent_image_labels[0]
            self.current_card = self.hidden_card  # Set hidden card as current
            self.display_imagine(hidden_card_label)  # Redraw label with real card
            self.hidden_card = None  # Hidden card has been revealed

    def show_oponent_card(self):
        if len(self.oponent_image_labels) < self.max_oponent_card:  # Check if opponent's card count is less than maximum
            self.random_number = random.randrange(0, len(self.cards))

            if len(self.oponent_image_labels) == 0:
                # The first opponent card is hidden (background card)
                self.hidden_card = self.cards[self.random_number]  # Save the hidden card
                self.current_card = {"image_path": self.backround}  # Set background for the first card
            else:
                # Other opponent cards are shown normally
                self.current_card = self.cards[self.random_number]

            # Create new card label and set its position for opponent
            new_image_label = Label(self.my_window)
            self.display_imagine(new_image_label)
            x_position = 10 + len(self.oponent_image_labels) * 50
            new_image_label.place(x=x_position, y=150)

            # Append to list of labels for opponent
            self.oponent_image_labels.append(new_image_label)

            # Remove displayed card from list to prevent showing the same card twice
            del self.cards[self.random_number]

    # Reset all cards and reload cards from JSON file
    def reset_cards(self):
        for label in self.image_labels + self.oponent_image_labels:
            label.destroy()
        self.image_labels = []
        self.oponent_image_labels = []
        self.hidden_card = None
        self.hidden_card_added = False

        # Reload all cards from JSON file
        with open('cards.json', 'r') as file:
            self.cards = json.load(file)