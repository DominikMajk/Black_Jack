import json


with open('cards_in_game.json') as file:
    my_cards = json.load(file)

for key in my_cards.keys():
    print(key)