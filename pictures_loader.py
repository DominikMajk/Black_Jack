# Class PictureLoader
import random

from PIL import ImageTk, Image
import json
import random

class PictureLoader:
    def __init__(self,image_path):
        self.image_path = image_path

    # json cards download
    with open('cards.json', 'r') as file:
        cards = json.load(file)

    random_number = random.randrange(0,len(cards))
    current_card = (cards[random_number]["image_path"])

    def display_imagine(self, image_label,scale_factor = 10):
        img = Image.open((f"PNG-cards-1.3\\{self.current_card}"))
        # images = img.resize((139, 100))
        width, height = img.size
        new_width = width//scale_factor
        new_height = height//scale_factor
        img = img.resize((new_width,new_height), Image.LANCZOS)
        image_format = ImageTk.PhotoImage(img)
        image_label.config(image=image_format)
        image_label.img = image_format

