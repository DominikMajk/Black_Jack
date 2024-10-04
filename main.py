# Class main
from tkinter import *

from game_rules import show_rules
from pictures_loader import PictureLoader


# main window
my_window = Tk()
my_window.minsize(400, 450)
my_window.resizable(False, False)
my_window.title("Black Jack")
my_window.config(bg="#64a367",)

#inicialization picture_loader:
picture= PictureLoader("path",my_window)
total_score = 0
opponent_total_score = 0

def game_score(tt = 0):
    score = picture.count_score(picture.current_card)
    global total_score
    total_score += score

    if total_score == 21:
        score_label.config(text=str("výhra"))
    elif total_score > 21:
        score_label.config(text=str("prohrál jsi"))
    else:
        score_label.config(text=int(total_score))

def opponent_game_score():
    try:
        score = picture.count_score(picture.current_card)
        global opponent_total_score
        opponent_total_score += score
        opponent_score_label.config(text = int(opponent_total_score))
        print("A")
    except : print("score se nepodařilo dopočítat")



def deal_initial_cards():
    """Funkce, která rozdá první dvě karty při spuštění hry"""
    # První karta pro hráče
    picture.show_card()
    game_score()

    # První karta pro oponenta
    picture.show_oponent_card()
    opponent_game_score()

    # Druhá karta pro hráče
    picture.show_card()
    game_score()

    # Druhá karta pro oponenta
    picture.show_oponent_card()
    opponent_game_score()





# Button
first_button = Button(my_window, width=8, height=2, text="draw card", command= lambda : [picture.show_card(), game_score(), picture.show_oponent_card(), opponent_game_score()])
first_button.place(x=30, y=380)

second_button = Button(my_window, width=8, height=2, text="konec", command= my_window.destroy)

third_button = Button(my_window, width=8, height=2, text="Start game", command= lambda : [deal_initial_cards(),second_button.place(x=200, y = 380),third_button.place_forget()])
third_button.place(x=30, y=380)

score_label = Label(width=8, height= 2, font= ("Helvetica", 12), text = "score")
score_label.place(x = 30, y = 300)

opponent_score_label = Label(width=8, height= 2, font= ("Helvetica", 12), text = "opponent")
opponent_score_label.place(x = 200, y = 300)

#button for show game rules
rules_button = Button(my_window, width=2, height=1, text="?", command= lambda : show_rules(my_window))
rules_button.place(x=350, y = 20)

if first_button.winfo_ismapped():
    first_button.place_forget()
# Main loop
my_window.mainloop()


