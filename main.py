import pygame
import os
import cards

#Create the Window
pygame.init()
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

buttons = []

def TitleScreen():
    screen.fill(BLACK)
    pygame.display.set_caption("Franklins Poker Practice - Title Screen")
    titleScreen = True
    while titleScreen:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                titleScreen = False
                pygame.quit()
            

        pygame.display.flip()


def display_cards(hero, villian, dealer_cards):
    X = 300
    for card in hero:
        screen.blit(card.image, (X, 100))
        card.x = X
        card.y = 100
        X += 100
        
    X = 800
    for card in villian:
        screen.blit(card.image, (X, 100))
        card.x = X
        card.y = 100
        X += 100
        
    X = 400
    for card in dealer_cards:
        screen.blit(card.image, (X, 400))
        card.x = X
        card.y = 100
        X += 100

        
def display_winner(winner, hero, villian):
    if winner == cards.Winner.Hero:
        for card in villian:
            screen.blit(card.back, (card.x - 10, card.y - 10))
    elif winner == cards.Winner.Villian:
        for card in hero:
            screen.blit(card.back, (card.x - 10, card.y - 10))
    else:
        print("tied")


def Play():
    screen.fill(BLACK)
    pygame.display.set_caption("Franklins Poker Practice - Game")
    hero = cards.deal_player(2)
    villian = cards.deal_player(2)

    # deal flop
    flop = cards.deal_player(3)
    display_cards(hero, villian, flop)
    hero_s = cards.check_hand_strength(hero, flop)
    villain_s = cards.check_hand_strength(villian, flop)

    # cards.cacluate_outs(hero_s, villain_s, flop) | doubling printing but thats fine cause it wont print later


    play = True
    press = 1
    while play:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if press == 1:
                    turn = cards.deal_turn(hero, villian, flop)
                    display_cards(hero, villian, turn)
                    hero_s = cards.check_hand_strength(hero, turn)
                    villain_s = cards.check_hand_strength(villian, turn)
                   
                    press += 1
                elif press == 2:
                    river = cards.deal_river(hero, villian, turn)
                    display_cards(hero, villian, river)
                    hero_s = cards.check_hand_strength(hero, river)
                    villain_s = cards.check_hand_strength(villian, river)
                    press += 1
                elif press == 3:
                    winner = cards.check_winner(hero_s, villain_s)
                    press += 1
                elif press >= 4:
                    display_winner(winner, hero, villian)
        

        
        pygame.display.flip()


Play()
