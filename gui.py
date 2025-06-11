from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pictures_loader import PictureLoader
from game_rules import show_rules
from game_logic import GameLogic

def run_app():
    my_window = Tk()
    my_window.minsize(400, 450)
    my_window.resizable(False, False)
    my_window.title("Black Jack")

    # Background
    wood_img = Image.open("wood_bg.jpg").resize((400, 450))
    wood_bg = ImageTk.PhotoImage(wood_img)
    bg_label = Label(my_window, image=wood_bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Style
    style = ttk.Style(my_window)
    style.theme_use('clam')
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

    # Picture loader a logika
    picture = PictureLoader("path", my_window)
    logic = GameLogic(picture, my_window)

    # Score labels
    score_label = Label(
        my_window, width=8, bg="#232946", fg="#FFD700", relief="groove",
        font=("Helvetica", 12, "bold"), bd=3, padx=10, pady=5, text="Score"
    )
    score_label.place(x=30, y=300)

    opponent_score_label = Label(
        my_window, width=8, bg="#232946", fg="#FFD700", relief="groove",
        font=("Helvetica", 12, "bold"), bd=3, padx=10, pady=5, text="Bot score"
    )
    opponent_score_label.place(x=200, y=300)

    # Buttons
    first_button = ttk.Button(
        my_window, width=8, text="Hit", style="FancyButton.TButton",
        command=lambda: [logic.player_draw(score_label), logic.opponent_draw(opponent_score_label)]
    )
    first_button.place(x=30, y=380)

    second_button = ttk.Button(
        my_window, width=8, text="End", style="FancyButton.TButton",
        command=lambda: logic.end_game(score_label, opponent_score_label, first_button, second_button, third_button)
    )

    third_button = ttk.Button(
        my_window, width=8, text="Start", style="FancyButton.TButton",
        command=lambda: [logic.deal_initial_cards(score_label, opponent_score_label, first_button, second_button, third_button)]
    )
    third_button.place(x=30, y=380)

    rules_button = ttk.Button(
        my_window, width=2, text="?", style="FancyButton.TButton",
        command=lambda: show_rules(my_window)
    )
    rules_button.place(x=350, y=20)

    my_window.mainloop()