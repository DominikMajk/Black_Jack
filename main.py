# Class main
#xxx
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
    first_button.place_forget()
    third_button.place_forget()
    second_button.place_forget()

    text_result = ""

    if total_score == 21 and opponent_total_score == 21:
        text_result = "remíza"
    elif total_score > opponent_total_score and total_score <= 21:
        text_result = "vyhrál jsi"
    elif total_score < opponent_total_score and opponent_total_score <= 21:
        text_result = "prohrál jsi"
    elif opponent_total_score > 21:
        text_result = "vyhrál jsi"
    elif total_score > 21:
        text_result = "prohrál jsi"

    result_label = Label(my_window, text=text_result, width=8, bg = '#818DF5', relief= "raised", font= ("Helvetica", 12))
    result_label.place(x=30, y=380)

         
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
                    opponent_score_label.config(text=int(opponent_total_score))  # Aktualizuj label
                    print("Hidden card added to opponent score:", opponent_score_value)

            # Přičíst hodnotu aktuální karty oponenta
            score = picture.count_score(picture.current_card)
            opponent_total_score += score
            opponent_score_label.config(text=int(opponent_total_score))
            print("Opponent score updated:", opponent_total_score)

            # Oponent táhne novou kartu pouze pokud je skóre méně než 17
            if opponent_total_score < 17:
                picture.show_oponent_card()
                opponent_game_score()  # Znovu přepočítat skóre oponenta
            else:
                print("Opponent stops drawing cards.")
        else:
            print("Opponent score is 17 or higher, no more cards drawn.")

    except Exception as e:
        print("Score calculation failed:", e)

#Funkce, která rozdá první dvě karty při spuštění hry
def deal_initial_cards():
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
first_button = ttk.Button(my_window, width=8, text="lízni si", style="MyButton.TButton", 
                          command=lambda: [picture.show_card(), game_score(), opponent_game_score()])
first_button.place(x=30, y=380)


second_button = ttk.Button(my_window, width=8, text="konec", style="MyButton.TButton",
                             command = lambda : [end_game(),picture.reveal_hidden_card(), end_game()])

third_button = ttk.Button(my_window, width=8, text="Začít hru", style="MyButton.TButton",
                             command= lambda : [deal_initial_cards(),second_button.place(x=200, y = 380),third_button.place_forget()])
third_button.place(x=30, y=380)

#button for show game rules
rules_button = ttk.Button(my_window, width=2, text="?", style="MyButton.TButton",  
                            command= lambda : show_rules(my_window))
rules_button.place(x=350, y = 20)

# game description labels
score_label = Label(width=8, bg = '#818DF5', relief= "raised", font= ("Helvetica", 12), text = "score")
score_label.place(x = 30, y = 300)

opponent_score_label = Label(width=8, bg = '#818DF5', relief= "raised", font= ("Helvetica", 12), text = "opponent")
opponent_score_label.place(x = 200, y = 300)

# nahradí se tlačítko "začít hru" za "lízni si"
if first_button.winfo_ismapped():
    first_button.place_forget()


# Main loop
my_window.mainloop()


