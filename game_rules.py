from tkinter import *

# tato třída vytvoří nové okno, kde budou vysvětlena pravidla hry

def show_rules(my_window):
    rules_window = Toplevel(my_window)  # Create a new top-level window
    rules_window.minsize(900, 380)
    rules_window.title("Rules")

    rules_text = """
    Krátká pravidla hry Blackjack:

    1. Cíl hry:
       - Vaším cílem je mít v ruce karty s celkovou hodnotou co nejblíže 21, aniž byste tuto hodnotu překročili. Současně musíte mít lepší skóre než oponent (krupiér).

    2. Hodnota karet:
       - Číselné karty (2–10) mají svou nominální hodnotu.
       - Karty král, dáma, kluk (J, Q, K) mají hodnotu 10.
       - Eso (A) má v této verze hry hodnotu 11.

    3. Průběh hry:
       - Každý hráč (včetně krupiéra) dostane na začátku dvě karty. Krupiér má jednu kartu odhalenou.
       - Hráč se rozhodne, zda si vezme další kartu (Hit), nebo zůstane u aktuálního skóre (Stand).

    4. Překročení hodnoty:
       - Pokud hráč překročí hodnotu 21, prohrává (Bust).

    5. Konec hry:
       - Když hráč přestane brát karty, krupiér si bere další karty, dokud nemá alespoň 17 bodů.
       - Kdo má skóre bližší 21, vyhrává. Pokud mají hráč a krupiér stejnou hodnotu, hra končí remízou (Push).

    Poznámka: Blackjack je kombinace esa a karty s hodnotou 10, která okamžitě vyhrává, pokud ji nemá i krupiér.
    """

    rules_label = Label(rules_window, text=rules_text, justify=LEFT)
    rules_label.place(x=5, y=5)