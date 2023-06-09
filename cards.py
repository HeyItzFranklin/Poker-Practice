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


class Winner(Enum):
    Hero = 0
    Villian = 1
    Tie = 2


class Card():
    def __init__(self, name, value, suit, image, back):
        self.name = name
        self.value = value
        self.suit = suit
        self.image = image
        self.back = back
        self.x_pos = 0
        self.y_pos = 0


CARD_WIDTH = 100
CARD_HEIGHT = 200
SUIT_NAMES = ["_of_spades", "_of_hearts", "_of_diamonds", "_of_clubs"]
NUM_OF_SUITS = len(SUIT_NAMES)
CARD_NAMES = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
CARDS_PER_SUIT = len(CARD_NAMES)
HAND_LENGTH = 5
back = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Card_back.png")), (120, 220))

# Addes the name of the card, the v(alue) of the card and the suit of the card to the deck
deck = []
for i in range(NUM_OF_SUITS):
    v = 2
    for card in CARD_NAMES:
        card += SUIT_NAMES[i]
        image = card + ".png"
        card = Card(card, v, Suit(i), pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Card-Images", image)), (CARD_WIDTH, CARD_HEIGHT)), back)
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
        
    
# Sorts the hand + table cards into descending order
def sort_hand(whole_hand, original_hand, dealer_cards):
    for card in original_hand:
        whole_hand.append(card)

    for card in dealer_cards:
        whole_hand.append(card)

    whole_hand = sorted(whole_hand, key=lambda card: card.value, reverse= True)
    return whole_hand

# Creates a hand with pairs and the next best cards until the hand is full
def fill_pairs_hand(pairs, whole_hand):
    i = 0
    while len(pairs) < HAND_LENGTH:
        if whole_hand[i] not in pairs:
            pairs.append(whole_hand[i])
        i += 1


# Checks if the hand has a pair, 2 pair, 3 of a kind, or 4 pair.
def check_pairs(whole_hand):
    pairs = []
    for i in range(len(whole_hand) - 1):
        for j in range(i + 1, len(whole_hand)):
            if whole_hand[i].value == whole_hand[j].value:
                if whole_hand[i] not in pairs:
                    pairs.append(whole_hand[i])
                if whole_hand[j] not in pairs:
                    pairs.append(whole_hand[j])
    
    pair_len = len(pairs)
    if pair_len == 0:
        best_hand = [10]
        best_hand.append(whole_hand[:HAND_LENGTH - pair_len])
        return best_hand
    elif pair_len == 2:
        best_hand = [9]
        fill_pairs_hand(pairs, whole_hand)
        best_hand.append(pairs)
        return best_hand
    elif pair_len == 3:
        best_hand = [7]
        fill_pairs_hand(pairs, whole_hand)
        best_hand.append(pairs)
        return best_hand
    elif pair_len == 4:
        quad = True
        for card in pairs:
            if card.value != pairs[0].value:
                quad = False
                break
        if quad == True:
            best_hand = [3]
            fill_pairs_hand(pairs, whole_hand)
            best_hand.append(pairs)
            return best_hand
        else:
            best_hand = [8]
            fill_pairs_hand(pairs, whole_hand)
            best_hand.append(pairs)
            return best_hand
    elif pair_len == 5:
        best_hand = [4]
        best_hand.append(pairs)
        return best_hand
    elif pair_len == 6:
        unique_pairs = {}
        for card in pairs:
            if card.value not in unique_pairs:
                unique_pairs[card.value] = 1
            else:
                unique_pairs[card.value] += 1

            if len(unique_pairs) == 3:
                best_hand = [8]
                for i in range (2):
                    pairs.pop()
                fill_pairs_hand(pairs, whole_hand)
                best_hand.append(pairs)
                return best_hand
            else:
                for key in unique_pairs:
                    if unique_pairs[key] == 4:
                        if pairs[0] == pairs[3]:
                            for i in range(2):
                                pairs.pop()
                            best_hand = [3]
                            fill_pairs_hand(pairs, whole_hand)
                            best_hand.append(pairs)
                            return best_hand
                        else:
                            for i in range(2):
                                pairs.pop(0)
                            best_hand = [3]
                            fill_pairs_hand(pairs, whole_hand)
                            best_hand.append(pairs)
                            return best_hand
        
                best_hand = [4]
                best_hand.append(pairs[:HAND_LENGTH])
                return best_hand
            
    elif pair_len == 7:
        unique_pairs = {}
        for card in pairs:
            if card.value not in unique_pairs:
                unique_pairs[card.value] = 1
            else:
                unique_pairs[card.value] += 1
        
        if len(unique_pairs) == 3:
            if pairs[0] == pairs[2] or pairs[2] == pairs[4]:
                for i in range(2):
                    pairs.pop()
            else:
                for i in range(2):
                    pairs.pop(2)

            best_hand = [4]
            fill_pairs_hand(pairs, whole_hand)
            best_hand.append(pairs)
            return best_hand
        else:
            if pairs[0] == [pairs[3]]:
                for i in range(3):
                    pairs.pop()
                best_hand = [3]
                fill_pairs_hand(pairs, whole_hand)
                best_hand.append(pairs)
                return best_hand


# Checks if the hand has a flush
def check_flush(whole_hand):
    has_flush = False
    hand_hearts = []
    hand_diamonds = []
    hand_spades = []
    hand_clubs = []
    for card in whole_hand:
        if card in hearts:
            hand_hearts.append(card)
        elif card in diamonds:
            hand_diamonds.append(card)
        elif card in spades:
            hand_spades.append(card)
        elif card in clubs:
            hand_clubs.append(card)
    
    if len(hand_hearts) >= HAND_LENGTH or len(hand_diamonds) >= HAND_LENGTH or len(hand_spades) >= HAND_LENGTH or len(hand_clubs) >= HAND_LENGTH:
        has_flush = True
        best_hand = [5]
        best_hand.append(whole_hand[:HAND_LENGTH])
        return best_hand
    
    return [-1, []]

# Calculates how many times you can check 5 consectutive cards in the hand
def get_chances(x, y):
    ans = 0
    for i in range(y):
        if i + x <= y:
            ans += 1
        else:
            return ans


# Check if hand has a straight
def check_straight(whole_hand):
    straight_hand = []
    for card in whole_hand:
        if card.value not in straight_hand:
            straight_hand.append(card)
    
    chances = get_chances(HAND_LENGTH, len(straight_hand))
    straight = False

    low_straight_values = [5, 4, 3, 2, 14]
    low_straight = 0
    low_straight_cards = []
    for i in range(HAND_LENGTH):
        for card in straight_hand:
            if card.value == low_straight_values[i]:
                low_straight_cards.append(card)
                low_straight += 1
                break
    
    if low_straight == 5:
        return [6, low_straight_cards]


    for i in range(chances):
        if straight == False:
            straight_cards = []
            s = 1
            for j in range(i, i + HAND_LENGTH - 1):
                if straight_hand[j].value == straight_hand[j + 1].value + 1:
                    i += 1
                    s += 1
                    straight_cards.append(straight_hand[j])
                    if s == HAND_LENGTH:
                        straight_cards.append(straight_hand[j + 1])
                        straight = True
                        break
                else:
                    break
    
    if straight == True:
        # check if its a flush
        flush_check = check_flush(whole_hand)
        if flush_check[0] == 5:
            if flush_check[1][0].value == 1:
                return [1, straight_cards]
            else:
                return [2, straight_cards]
        else:
            return [6, straight_cards]      
    

    return [-1 ,[]]


# Checks how strong hand is and returns hand rating and strongest 5 cards
def check_hand_strength(player_hand, dealer_cards):
    whole_player_hand = []
    whole_player_hand = sort_hand(whole_player_hand, player_hand, dealer_cards)
    
    pair_strength = check_pairs(whole_player_hand)
    flush_strength = check_flush(whole_player_hand)
    straight_strength = check_straight(whole_player_hand)

    if straight_strength[0] == 1 or straight_strength[0] == 2:
        print(straight_strength[0])
        return straight_strength
    
    if pair_strength[0] == 3 or pair_strength[0] == 4:
        print(pair_strength[0])
        return pair_strength
    
    if flush_strength[0] == 5:
        print(flush_strength[0])
        return flush_strength
    
    if straight_strength[0] == 6:
        print(straight_strength[0])
        return straight_strength
    
    print(pair_strength[0])
    return pair_strength
        

# Deals cards to a hand
def deal_player(cards):
    player = []
    player = deal_card(player, cards)
    return player
    

# Deals the 4th card to the table
def deal_turn(hero_hand, villian_hand, dealer_cards):
    turn = deal_card(dealer_cards, 1)
    return turn


# Deaks the 5th card to the table
def deal_river(hero_hand, villian_hand, dealer_cards):
    river = deal_card(dealer_cards, 1)
    return river

# Checks which hand is stronger
def check_winner(hero_s, villian_s):
    print(hero_s[0])
    print(villian_s[0])
    winner = -1
    if hero_s[0] < villian_s[0]:
        winner = Winner.Hero
        return winner
    elif hero_s[0] > villian_s[0]:
        winner = Winner.Villian
        return winner
    elif hero_s[0] == villian_s[0]:
        for i in range(HAND_LENGTH):
            if hero_s[1][i].value > villian_s[1][i].value:
                winner = Winner.Hero
                return winner
            elif hero_s[1][i].value < villian_s[1][i].value:
                winner = Winner.Villian
                return winner
            else:
                continue
        winner = Winner.Tie
        return winner


def cacluate_outs(player_s, opponent_s, dealer_cards):
    rule = 0
    if len(dealer_cards) == 3:
        rule = 4
    elif len(dealer_cards) == 4:
        rule = 2

    winner = check_winner(player_s, opponent_s)
  
# Adds all the cards back into the deck
def reset_deck(hero_cards, villian_cards, dealer_cards):
    for card in hero_cards:
        deck.append(card)
    
    for card in villian_cards:
        deck.append(card)
    
    for card in dealer_cards:
        deck.append(card)
