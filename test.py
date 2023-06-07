class Card():
    def __init__(self, name, value):
        self.name = name
        self.value = value

        
card1 = Card("card1", 14)
card2 = Card("card2", 9)
card3 = Card("card3", 8)
card4 = Card("card4", 8)
card5 = Card("card5", 5)
card6 = Card("card6", 7)
card7 = Card("card7", 2)

HAND_LENGTH = 5
whole_hand = [card1, card2, card3, card4, card5, card6, card7]


