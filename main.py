import pygame
import os

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

    button1 = button.Button("gradient_2.jpg", "water.jpg", 200, 200)
    buttons.append(button1)
    button2 = button.Button("gradient_2.jpg", "water.jpg", 400, 200)
    buttons.append(button2)

    
    for button in buttons:
        button.draw_button()

    titleScreen = True
    while titleScreen:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                titleScreen = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse_pos)
                for button in buttons:
                    button.checkHover()


        pygame.display.flip()

    


def Play():
    screen.fill(BLACK)
    pygame.display.set_caption("Franklins Poker Practice - Game")
    play = True
    while play:
        for event in pygame.event.get():
            run = False
            pygame.quit()


TitleScreen()

