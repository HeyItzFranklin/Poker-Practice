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
        X += 100
        
    X = 800
    for card in villian:
        screen.blit(card.image, (X, 100))
        X += 100
        
    X = 400
    for card in dealer_cards:
        screen.blit(card.image, (X, 400))
        X += 100



def Play():
    screen.fill(BLACK)
    pygame.display.set_caption("Franklins Poker Practice - Game")
    hero = cards.deal_player(2)
    villian = cards.deal_player(2)
    has_turned = False
    has_rivered = False

    # deal flop
    flop = cards.deal_player(3)
    display_cards(hero, villian, flop)

    play = True
    while play:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if has_turned == False:
                   turn = cards.deal_turn(hero, villian, flop)
                   display_cards(hero, villian, turn)
                   has_turned = True
                elif has_turned == True and has_rivered == False:
                   river = cards.deal_river(hero, villian, turn)
                   display_cards(hero, villian, river)
                   has_rivered = True
                else:
                    pass
        
               
        

        
        pygame.display.flip()


Play()
