from enum import Enum
import random
import pygame
import os

pygame.init()

class Suit(Enum):
    Spade = 0
    Heart = 1
    Diamond = 2
    Club = 3


class Card():
    def __init__(self, name, value, suit, image):
        self.name = name
        self.value = value
        self.suit = suit
        self.image = image
        self.x_pos = 0
        self.y_pos = 0

# class Hand():
#     def __init__(self):
#         self.cards = []   

        # self.has_high_card = False
        # self.has_pair = False
        # self.has_two_pair = False
        # self.has_three_pair = False
        # self.has_straight = False
        # self.has_flush = False
        # self.has_full_house = False
        # self.has_four_of_a_kind = False
        # self.has_staight_flush = False
        # self.has_royal_flush = False
        # self.is_winning = False


SUIT_NAMES = ["_of_spades", "_of_hearts", "_of_diamonds", "_of_clubs"]
NUM_OF_SUITS = len(SUIT_NAMES)
CARD_NAMES = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
CARDS_PER_SUIT = len(CARD_NAMES)

# Addes the name of the card, the v(alue) of the card and the suit of the card to the deck
deck = []
for i in range(NUM_OF_SUITS):
    v = 1
    for card in CARD_NAMES:
        card += SUIT_NAMES[i]
        image = card + ".png"
        card = Card(card, v, Suit(i), pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Card-Images", image)), (100, 200)))
       
        deck.append(card)
        v += 1


# Classifies the cards into their respective suits
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
        

# Deals cards and removes them from the deck
def deal_card(location, num_of_cards) -> list:
    for i in range(num_of_cards):
        new_card = random.choice(deck)
        deck.pop(deck.index(new_card))
        location.append(new_card)
    
    return location
        

def display_cards(hero_hand, villian_hand, dealer_cards):
    # Print Hero cards
    print("HERO CARDS:")
    for card in hero_hand:
        print(card.name, card.value, card.suit)
    print()

    # Print Villian cards
    print("VILLIAN CARDS:")
    for card in villian_hand:
        print(card.name, card.value, card.suit)
    print()

    # Print the table cards
    if len(dealer_cards) == 3:
        print("THE FLOP:")
    elif len(dealer_cards) == 4:
        print("THE TURN:")
    elif len(dealer_cards) == 5:
        print("THE RIVER:")
    for card in dealer_cards:
        print(card.name, card.value, card.suit)
    print()
    

def sort_hand(whole_hand, original_hand, dealer_cards):
    for card in original_hand:
        whole_hand.append(card)

    for card in dealer_cards:
        whole_hand.append(card)

    whole_hand = sorted(whole_hand, key=lambda card: card.value, reverse= True)
    return whole_hand

def check_pairs(whole_hand):
    # NEED TO CHECK HOW STRONG THE PAIRS ARE

    # Check for pairs
    pairs = []
    for i in range(len(whole_hand) - 1):
        for j in range(i + 1, len(whole_hand)):
            if whole_hand[i].value == whole_hand[j].value:
                if whole_hand[i] not in pairs:
                    pairs.append(whole_hand[i])
                if whole_hand[j] not in pairs:
                    pairs.append(whole_hand[j])
    
    # for pair in pairs:
    #     print(pair.name)

    if len(pairs) == 2:
        print("one pair")
    elif len(pairs) == 3:
        print("three of a kind")
    elif len(pairs) == 4:
        quad = True
        for card in pairs:
            if card.value != pairs[0].value:
                quad = False
                break
        if quad == True:
            print("four of a kind")
        else:
            print("2 pair")
    elif len(pairs) == 5:
        print("full house")



def check_flush(hero_hand):
    # NEED TO CHECK HOW STRONG THE FLUSH IS 

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


def check_straight(hero_hand):
    # STILL NEED TO CATCH ACE KING CASE 
    # STILL NEED TO CHECK HOW STRONG THE STRAIGHT IS

    # might be able to get chances without hard coding numbers not sure

    chances = 1
    if len(hero_hand) == 5:
        chances = 1
    elif len(hero_hand) == 6:
        chances = 2
    elif len(hero_hand) == 7:
        chances == 3
    
    straight_len = 5
    straight = False
    for i in range(chances):
        if straight == False:
            s = 1
            for j in range(i + 1, i + straight_len):
                if hero_hand[j].value == hero_hand[i].value - 1:
                    i += 1
                    s += 1
                    if s == 5:
                        straight = True
                        break
                else:
                    break
    
    if straight == True:
        print("straight")

def check_hand_strength(hero_hand, villian_hand, dealer_cards):
    whole_hero_hand = []
    whole_villian_hand = []
    whole_hero_hand = sort_hand(whole_hero_hand, hero_hand, dealer_cards)
    whole_villian_hand = sort_hand(whole_villian_hand, villian_hand, dealer_cards)
    
    print("Hero")
    check_pairs(whole_hero_hand)
    check_flush(whole_hero_hand)
    check_straight(whole_hero_hand)
    print()
    print("villian")
    check_pairs(whole_villian_hand)
    check_flush(whole_villian_hand)
    check_straight(whole_villian_hand)
    print()
    

def deal_player(cards):
    player = []
    player = deal_card(player, cards)

    return player
    

# display_cards(hero, villian, flop)
# check_hand_strength(hero, villian, flop)

# button for this
# next_deal = str(input("Deal next card?: "))
# if next_deal == "y":
#     deal_turn(hero, villian, flop)



def deal_turn(hero_hand, villian_hand, dealer_cards):
    turn = deal_card(dealer_cards, 1)
    display_cards(hero_hand, villian_hand, turn)
    check_hand_strength(hero_hand, villian_hand, turn)
    return turn


def deal_river(hero_hand, villian_hand, dealer_cards):
    river = deal_card(dealer_cards, 1)
    display_cards(hero_hand, villian_hand, river)
    check_hand_strength(hero_hand, villian_hand, river)
    return river
