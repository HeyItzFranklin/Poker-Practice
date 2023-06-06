import pygame
import os
import cards

#Create the Window
pygame.init()
pygame.font.init()
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
RED = (255, 0, 0)

GAME_BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "poker-table.jpg")), (SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_FONT = pygame.font.SysFont("papyrus", 35)
OUTCOME_FONT = pygame.font.SysFont("arialblack", 20)

buttons = []

def TitleScreen():
    SCREEN.fill(BLACK)
    pygame.display.set_caption("Franklins Poker Practice - Title Screen")
    titleScreen = True
    while titleScreen:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                titleScreen = False
                pygame.quit()
            

        pygame.display.flip()

def display_hand(x , y, hand, text, color):
    hero_text = PLAYER_FONT.render(text, 1, color)
    SCREEN.blit(hero_text, (x,  y + cards.CARD_HEIGHT))
    for card in hand:
        SCREEN.blit(card.image, (x, y))
        card.x = x
        card.y = y
        x += cards.CARD_WIDTH

def hide_hand(hand):
    for card in hand:
        SCREEN.blit(card.back, (card.x - 10, card.y - 10))

def display_cards(hero, villian, dealer_cards):
    display_hand(300, 430, hero, "Hero Cards", GOLD)
    display_hand(800, 430, villian, "Villian Cards", RED)

    X = 400
    Y = 100
    hero_text = PLAYER_FONT.render("Table Cards", 1, WHITE)
    SCREEN.blit(hero_text, (X + (1.5 * cards.CARD_WIDTH),  Y - (cards.CARD_HEIGHT // 4)))
    for card in dealer_cards:
        SCREEN.blit(card.image, (X, Y))
        card.x = X
        card.y = Y
        X += cards.CARD_WIDTH

        
def display_winner(winner, hero, villian):
    hero_outcome = "LOSER"
    villian_outcome = "LOSER"
    
    if winner == cards.Winner.Hero:
        hide_hand(villian)
        hero_outcome = "WINNER"
    elif winner == cards.Winner.Villian:
        hide_hand(hero)
        villian_outcome = "WINNER"
    else:
        hide_hand(hero)
        hide_hand(villian)
        hero_outcome = "CHOP POT"
        villian_outcome = "CHOP POT"

    
    hero_outcome = OUTCOME_FONT.render(hero_outcome, 1, WHITE)
    villian_outcome = OUTCOME_FONT.render(villian_outcome, 1, WHITE)
    SCREEN.blit(hero_outcome, (350, 680))
    SCREEN.blit(villian_outcome, (850, 680))


def Play():
    SCREEN.fill(BLACK)
    SCREEN.blit(GAME_BG, (0,0))
    pygame.display.set_caption("Franklins Poker Practice - Game")

    hero = cards.deal_player(2)
    villian = cards.deal_player(2)
    flop = cards.deal_player(3)

    current_board = flop

    display_cards(hero, villian, flop)
    hero_up = True
    villian_up = True

    hero_s = cards.check_hand_strength(hero, flop)
    villain_s = cards.check_hand_strength(villian, flop)
    #cards.cacluate_outs(hero_s, villain_s, flop) # | doubling printing but thats fine cause it wont print later

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
                    current_board = turn
                    display_cards(hero, villian, turn)
                    hero_s = cards.check_hand_strength(hero, turn)
                    villain_s = cards.check_hand_strength(villian, turn)
                    press += 1
                elif press == 2:
                    river = cards.deal_river(hero, villian, turn)
                    current_board = river
                    display_cards(hero, villian, river)
                    hero_s = cards.check_hand_strength(hero, river)
                    villain_s = cards.check_hand_strength(villian, river)
                    press += 1
                elif press == 3:
                    winner = cards.check_winner(hero_s, villain_s)
                    press += 1
                elif press >= 4:
                    display_winner(winner, hero, villian)
                    press += 1
                

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cards.reset_deck(hero, villian, current_board)
                    Play()
                
                if event.key == pygame.K_LSHIFT:
                    if hero_up == False:
                        hero_up = True
                        display_hand(300, 430, hero, "Hero Cards", GOLD)
                    elif hero_up == True:
                        hero_up = False
                        hide_hand(hero)
                
                if event.key == pygame.K_RSHIFT:
                    if villian_up == False:
                        villian_up = True
                        display_hand(800, 430, villian, "Villian Cards", RED)
                    elif villian_up == True:
                        villian_up = False
                        hide_hand(villian)
                
        
        pygame.display.flip()


Play()
