from enum import Enum

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

card_names = ["ace", "two", "three"]
spades = []
hearts = []
diamonds = []
clubs = []
deck = [spades, hearts, diamonds, clubs]

cards = []
for i in range(NUM_OF_SUITS):
    for card in card_names:
        card = Card(card, i + 1, Suit(i))
        if i == 0:
            spades.append(card)
        elif i == 1:
            hearts.append(card)
        elif i == 2:
            diamonds.append(card)
        elif i == 3:
            clubs.append(card)

print(deck[0])
print(spades)
print(hearts)



# spades = [ace, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen]
# hearts = [ace, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen]
# diamonds = [ace, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen]
# clubs = [ace, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen]









#Deck = [spades + hearts + diamonds + clubs]
