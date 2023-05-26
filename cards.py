from enum import Enum
import random

class Suit(Enum):
    Spade = 0
    Heart = 1
    Diamond = 2
    Clubs= 3

class Card():
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit


NUM_OF_SUITS = 4
suits = ["spades", "hearts", "diamonds", "clubs"]
card_names = ["ace", "two", "three"]
suit_names = ["_of_spades", "_of_hearts", "_of_diamonds", "_of_clubs"]
deck = []
for i in range(NUM_OF_SUITS):
    for card in card_names:
        card += suit_names[i]
        card = Card(card, i +1, Suit(i))
        deck.append(card)

#fix value

spades = deck[:3]
hearts = deck[3:6]
diamonds = deck[6:9]
clubs = deck[9:12]

card1 = random.choice(deck)
print(card1.name, card1.value, card1.suit)