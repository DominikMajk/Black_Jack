# Class PictureLoader
from PIL import ImageTk, Image

class PictureLoader:
    def __init__(self,image_path):
        self.image_path = image_path

    def display_imagine(self, image_label):
        img = Image.open("Images\\1_1.png")
        # images = img.resize((139, 100))
        image_format = ImageTk.PhotoImage(img)
        image_label.config(image=image_format)
        image_label.img = image_format

