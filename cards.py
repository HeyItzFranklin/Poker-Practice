from enum import Enum
import random
from operator import itemgetter, attrgetter, methodcaller


class Suit(Enum):
    Spade = 0
    Heart = 1
    Diamond = 2
    Club= 3

class Card():
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit


class Hand():
    def __init__(self):
        self.cards = []
        
        self.has_high_card = False
        self.has_pair = False
        self.has_two_pair = False
        self.has_three_pair = False
        self.has_straight = False
        self.has_flush = False
        self.has_full_house = False
        self.has_four_of_a_kind = False
        self.has_staight_flush = False
        self.has_royal_flush = False
        self.is_winning = False



SUIT_NAMES = ["_of_spades", "_of_hearts", "_of_diamonds", "_of_clubs"]
NUM_OF_SUITS = len(SUIT_NAMES)
CARD_NAMES = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
CARDS_PER_SUIT = len(CARD_NAMES)


deck = []
for i in range(NUM_OF_SUITS):
    v = 1
    for card in CARD_NAMES:
        card += SUIT_NAMES[i]
        card = Card(card, v, Suit(i))
        deck.append(card)
        v += 1

# can check for card.suit instead to sort prob better
spades = []
hearts = []
diamonds  = []
clubs = []
for card in deck:
    if card.suit == Suit.Spade:
        spades.append(card)
    elif card.suit == Suit.Heart:
        hearts.append(card)
    elif card.suit == Suit.Diamond:
        diamonds.append(card)
    elif card.suit == Suit.Club:
        clubs.append(card)
        

def deal_card(location, num_of_cards) -> list:
    for i in range(num_of_cards):
        new_card = random.choice(deck)
        deck.pop(deck.index(new_card))
        location.append(new_card)
    
    return location

def check_hand_strength(hero_hand, villian_hand, dealer_cards):
    hero_hand.append(dealer_cards)
    villian_hand.append(dealer_cards)

    # hero_hand = sorted(hero_hand, key=lambda card: card.value)
    for card in hero_hand:
        print(card.name, card.value)

hero = Hand()
hero.cards = deal_card(hero.cards, 2)

villian = Hand()
villian.cards = deal_card(villian.cards, 2)

flop = []
flop = deal_card(flop, 3)

print("HERO CARDS:")
for card in hero.cards:
    print(card.name, card.value, card.suit)
print()
print("VILLIAN CARDS:")
for card in villian.cards:
    print(card.name, card.value, card.suit)
print()
print("THE FLOP:")
for card in flop:
    print(card.name, card.value, card.suit)

print(type(hero.cards))
check_hand_strength(hero.cards, villian.cards, flop)



