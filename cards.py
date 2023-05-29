from enum import Enum
import random

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
        # Add image
        # Add x pos
        # Add y pos



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

def check_pairs(hero_hand):
    # Check for pairs
    pairs = []
    for i in range(len(hero_hand) - 1):
        for j in range(i + 1, len(hero_hand)):
            if hero_hand[i].value == hero_hand[j].value:
                if hero_hand[i] not in pairs:
                    pairs.append(hero_hand[i])
                if hero_hand[j] not in pairs:
                    pairs.append(hero_hand[j])
    
    for pair in pairs:
        print(pair.name)

    # Distungish between pairs, 2 pair, 3 pair, 4 pair
    # Full house

def check_flush(hero_hand):
    # Check Flush
    has_flush = False
    hand_hearts = []
    hand_diamonds = []
    hand_spades = []
    hand_clubs = []
    for card in hero_hand:
        if card in hearts:
            hand_hearts.append(card)
        elif card in diamonds:
            hand_diamonds.append(card)
        elif card in spades:
            hand_spades.append(card)
        elif card in clubs:
            hand_clubs.append(card)
    
    if len(hand_hearts) >= 5 or len(hand_diamonds) >= 5 or len(hand_spades) >= 5 or len(hand_clubs) >= 5:
        has_flush = True
        print("flush")

    # gotta check flush high   

def check_straight(hero_hand):
    pass
    # 5 over is amount to make a straight
    # is threre a way to calculate 5 fits into 7 3 times
    # check from first card to 5 over
    # check from second card to 5 over
    # check from third carrd to 5 over

            

    


def check_hand_strength(hero_hand, villian_hand, dealer_cards):
    for card in dealer_cards:
        hero_hand.append(card)

    hero_hand = sorted(hero_hand, key=lambda card: card.value, reverse= True)
    
    # need to return something
    check_pairs(hero_hand)
    check_flush(hero_hand)
    # check straight


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
print()

check_hand_strength(hero.cards, villian.cards, flop)


