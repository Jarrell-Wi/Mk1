import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Test Game')

BG = pygame.transform.scale(pygame.image.load('BG.jpg'), (WIDTH, HEIGHT))
Gravity = 3

def Draw(BG):
    WIN.blit(BG, (0, 0))

def Main():
    run = True
    while run:
        Draw(BG)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()



if __name__ == '__main__':
    Main()