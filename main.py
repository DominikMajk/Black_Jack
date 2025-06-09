# Class main
from tkinter import *
from tkinter import ttk
from game_rules import show_rules
from pictures_loader import PictureLoader

# main window
my_window = Tk()
my_window.minsize(400, 450)
my_window.resizable(False, False)
my_window.title("Black Jack")
my_window.config(bg="#64a367",)

#labbel and button design
style = ttk.Style(my_window)
#button designs
style.configure("MyButton.TButton",
                font=("Helvetica", 10),
                foreground="Black",
                background="#818DF5",
                #bordercolor = "#4D5DB5",
                #borderwidth = 20,
                padding=4,
                relief="sunken")

# funkce která se zavolá na konci hry a vyhodnotí hru  
def end_game():
    # zmizení tlačítek
    first_button.place_forget()
    third_button.place_forget()
    second_button.place_forget()
    text_result = ""

    if total_score == 21 and opponent_total_score == 21:
        text_result = "DRAW"
    elif total_score > opponent_total_score and total_score <= 21:
        text_result = "WIN!!!"
    elif total_score < opponent_total_score and opponent_total_score <= 21:
        text_result = "LOSS"
    elif opponent_total_score > 21:
        text_result = "WIN!!!"
    elif total_score > 21:
        text_result = "LOSS"

    result_label = Label(my_window, text=text_result, width=8, bg = '#818DF5', relief= "raised", font= ("Helvetica", 12))
    result_label.place(x=30, y=380)

    global play_again_button
    play_again_button = ttk.Button(my_window, width=10, text="Play Again", style="MyButton.TButton",
                                   command=play_again)
    play_again_button.place(x=120, y=380)

    opponent_score_label.config(text=int(opponent_total_score))  # Aktualizuj label score oponenta

         
#inicialization picture_loader:
picture = PictureLoader("path",my_window)

total_score = 0
opponent_total_score = 0

# score hrače
def game_score(tt = 0):
    score = picture.count_score(picture.current_card)
    global total_score
    total_score += score
    score_label.config(text=int(total_score))

# score oponenta
def opponent_game_score():
    global opponent_total_score
    # Vypočítat skóre oponenta
    try:
        # Kontrola, zda je skóre oponenta méně než 17
        if opponent_total_score < 17:
            # Pokud je první karta oponenta skrytá, přičteme její hodnotu k celkovému skóre
            if len(picture.oponent_image_labels) > 0 and picture.hidden_card:
                # Pokud ještě nebyla skrytá karta přičtena k skóre
                if "hidden_card_added" not in picture.__dict__ or not picture.hidden_card_added:
                    opponent_score_value = picture.count_score(picture.hidden_card)  # Získání hodnoty skryté karty
                    opponent_total_score += opponent_score_value  # Přičteme hodnotu skryté karty
                    picture.hidden_card_added = True  # Označte, že skrytá karta byla přičtena
                    #opponent_score_label.config(text=int(opponent_total_score))  # Aktualizuj label
                    print("Hidden card added to opponent score:", opponent_score_value)

            # Přičíst hodnotu aktuální karty oponenta
            score = picture.count_score(picture.current_card)
            opponent_total_score += score
            #opponent_score_label.config(text=int(opponent_total_score))
            print("Opponent score updated:", opponent_total_score)

        else:
            print("Opponent score is 17 or higher, no more cards drawn.")

    except Exception as e:
        print("Score calculation failed:", e)

#Funkce, která rozdá první dvě karty pro hráče a oponenta
def deal_initial_cards_for_player():
    # První karta pro hráče
    picture.show_card()
    game_score()
    # Druhá karta pro hráče
    picture.show_card()
    game_score()

    # karty pro oponenta
    picture.show_oponent_card()
    opponent_game_score()
    picture.show_oponent_card()
    opponent_game_score()

    first_button.place(x=30, y=380)

# funkce pro lizaní karet oponenta
def opponent_draw():
    if opponent_total_score <= 16 and total_score <= 21:
        picture.show_oponent_card()
        opponent_game_score()

# funkce pro znovuhratelnost hry!
def play_again():
    global total_score, opponent_total_score
    total_score = 0
    opponent_total_score = 0

    # Reset skóre v GUI
    score_label.config(text="Score")
    opponent_score_label.config(text="Bot score")

    # Smaž všechny obrázky karet
    picture.reset_cards()

    # Schovej výsledek (najdi způsob, jak ho uklidit)
    for widget in my_window.place_slaves():
        if isinstance(widget, Label) and widget["text"] in ("WIN!!!", "LOSS", "DRAW"):
            widget.destroy()

    # Obnov tlačítka
    first_button.place_forget()
    second_button.place_forget()
    play_again_button.place_forget()
    first_button.place_forget()
    third_button.place(x=30, y=380)

# tlačítko pro líznutí karty
first_button = ttk.Button(my_window, width=8, text="draw", style="MyButton.TButton", 
                          command=lambda: [picture.show_card(), game_score(), opponent_draw()])
first_button.place(x=30, y=380)

# tlačítko pro ukončení hry
second_button = ttk.Button(my_window, width=8, text="end", style="MyButton.TButton",
                             command = lambda : [end_game(),picture.reveal_hidden_card()])

# tlačítko pro začátek hry
third_button = ttk.Button(my_window, width=8, text="start", style="MyButton.TButton",
                             command= lambda : [deal_initial_cards_for_player(), second_button.place(x=200, y = 380),third_button.place_forget()])
third_button.place(x=30, y=380)

#button for show game rules
rules_button = ttk.Button(my_window, width=2, text="?", style="MyButton.TButton",  
                            command= lambda : show_rules(my_window))
rules_button.place(x=350, y = 20)

# game description labels, label je informativní a ve finální verzi není aplikovaný
score_label = Label(width=8, bg = '#818DF5', relief= "raised", font= ("Helvetica", 12), text = "Score")
score_label.place(x = 30, y = 300)

opponent_score_label = Label(width=8, bg = '#818DF5', relief= "raised", font= ("Helvetica", 12), text = "Bot score")
opponent_score_label.place(x = 200, y = 300)

# # nahradí se tlačítko "začít hru" za "lízni si"
# if first_button.winfo_ismapped():
#     first_button.place_forget()

# Main loop
my_window.mainloop()


