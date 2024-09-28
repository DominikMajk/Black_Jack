from tkinter import *
from PIL import ImageTk, Image

# main window
my_window = Tk()
my_window.minsize(300, 300)
my_window.resizable(False, False)
my_window.title("Black Jack")

#image def
def load_image():
    img = Image.open("Images\\1_1.png")
    # images = img.resize((139, 100))
    image_format = ImageTk.PhotoImage(img)
    image_label.config(image = image_format)
    image_label.img = image_format

    image_label2.config(image = image_format)
    image_label2.img = image_format




# Text label
text_label = Label(my_window, font=("Helvetica", 10), text="text place")
text_label.place(x= 20,y= 0)

# Button
first_button = Button(my_window, width=7, height=3, text="click")
first_button.place(x=20, y=230)

#Image
image_label = Label(my_window)
image_label2 = Label(my_window)
image_label.grid(column = 1, row = 1)
image_label2.place(x = 30, y =10)

# Main loop
load_image()
my_window.mainloop()
