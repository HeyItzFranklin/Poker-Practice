# import pygame
# import os
# from main import mouse_pos

# pygame.init()
# SCREEN_HEIGHT = 720
# SCREEN_WIDTH = 1280
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# class Button:
#     def __init__(self, bg, hover, x, y):
#         self.bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets", bg)), (100, 50))
#         self.hover = pygame.transform.scale(pygame.image.load(os.path.join("Assets", hover)), (100, 50))
#         self.x = x
#         self.y = y

#     def draw_button(self):
#          screen.blit(self.bg, (self.x, self.y))

#     def checkHover(self):
#             if mouse_pos[0] > self.x and mouse_pos[0] < self.x + 100:
#                 if mouse_pos[1] > self.y and mouse_pos[1] < self.y + 50:
#                     screen.blit(self.hover, (self.x, self.y))
#                     print(mouse_pos)
#                     pygame.display.flip()


