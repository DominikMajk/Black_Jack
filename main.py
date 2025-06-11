# Class main
from tkinter import *
from tkinter import ttk
from game_rules import show_rules
from pictures_loader import PictureLoader
from PIL import Image, ImageTk
from gui import run_app

# main window
my_window = Tk()
my_window.minsize(400, 450)
my_window.resizable(False, False)
my_window.title("Black Jack")

# Load and set dark wood background image
wood_img = Image.open("wood_bg.jpg").resize((400, 450))
wood_bg = ImageTk.PhotoImage(wood_img)
bg_label = Label(my_window, image=wood_bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#labbel and button design
style = ttk.Style(my_window)

# Use a theme that supports more styling options
style.theme_use('clam')

# Fancy button style
style.configure(
    "FancyButton.TButton",
    font=("Helvetica", 11, "bold"),
    foreground="#ffffff",
    background="#4D5DB5",
    borderwidth=2,
    focusthickness=3,
    focuscolor="#818DF5",
    padding=8,
    relief="raised"
)
style.map(
    "FancyButton.TButton",
    background=[("active", "#818DF5"), ("pressed", "#2E386B")],
    foreground=[("active", "#FFD700"), ("pressed", "#FFD700")],
    relief=[("pressed", "sunken"), ("!pressed", "raised")]
)

# funkce která se zavolá na konci hry a vyhodnotí hru  
def end_game():
    # zmizení tlačítek
    first_button.place_forget()
    third_button.place_forget()
    second_button.place_forget()
    text_result = ""

    if total_score == opponent_total_score:
        text_result = "DRAW"
        my_window.config(bg="#46b10d",)
    elif total_score > opponent_total_score and total_score <= 21:
        text_result = "WIN!!!"
        my_window.config(bg="#c46f14",)
    elif total_score < opponent_total_score and opponent_total_score <= 21:
        text_result = "LOSS"
        my_window.config(bg="#724cac",)
    elif opponent_total_score > 21:
        text_result = "WIN!!!"
        my_window.config(bg="#c46f14",)
    elif total_score > 21:
        text_result = "LOSS"
        my_window.config(bg="#724cac",)

    # Choose style based on result - win draw or loss
    if text_result == "WIN!!!":
        result_bg = "#FFD700"   # Gold
        result_fg = "#232946"   # Dark text
    elif text_result == "LOSS":
        result_bg = "#e74c3c"   # Red
        result_fg = "#ffffff"   # White text
    else:  # DRAW
        result_bg = "#818DF5"   # Blue
        result_fg = "#ffffff"   # White text

    result_label = Label(
        my_window,
        text=text_result,
        width=10,
        bg=result_bg,
        fg=result_fg,
        relief="ridge",
        font=("Helvetica", 18, "bold"),
        bd=4,
        padx=12,
        pady=8
    )
    result_label.place(x=200, y=170)

    global play_again_button
    play_again_button = ttk.Button(my_window, width=10, text="Play Again", style="FancyButton.TButton",
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
first_button = ttk.Button(my_window, width=8, text="Hit", style="FancyButton.TButton", 
                          command=lambda: [picture.show_card(), game_score(), opponent_draw()])
first_button.place(x=30, y=380)

# tlačítko pro ukončení hry
second_button = ttk.Button(my_window, width=8, text="End", style="FancyButton.TButton",
                             command = lambda : [end_game(),picture.reveal_hidden_card()])

# tlačítko pro začátek hry
third_button = ttk.Button(my_window, width=8, text="start", style="FancyButton.TButton",
                             command= lambda : [deal_initial_cards_for_player(), second_button.place(x=200, y = 380),third_button.place_forget()])
third_button.place(x=30, y=380)

#button for show game rules
rules_button = ttk.Button(my_window, width=2, text="?", style="FancyButton.TButton",  
                            command= lambda : show_rules(my_window))
rules_button.place(x=350, y = 20)

# Labels for scores
score_label = Label(
    my_window,
    width=8,
    bg="#232946",           # Dark background
    fg="#FFD700",           # Gold text
    relief="groove",        # 3D border
    font=("Helvetica", 12, "bold"),
    bd=3,                   # Border width
    padx=10,                # Horizontal padding
    pady=5,                 # Vertical padding
    text="Score"
)
score_label.place(x=30, y=300)

opponent_score_label = Label(
    my_window,
    width=8,
    bg="#232946",
    fg="#FFD700",
    relief="groove",
    font=("Helvetica", 12, "bold"),
    bd=3,
    padx=10,
    pady=5,
    text="Bot score"
)
opponent_score_label.place(x=200, y=300)

# Main loop
my_window.mainloop()


