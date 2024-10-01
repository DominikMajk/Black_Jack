import json

# json cards download
with open('cards.json', 'r') as file:
    cards = json.load(file)

current_card = (cards[1]["image_path"])
print(cards[1]["image_path"])
print(f"PNG-cards-1.3\\{current_card}")
