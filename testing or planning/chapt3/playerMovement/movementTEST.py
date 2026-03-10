from HeartObject import *
from Character import *
import pygame, sys

if __name__ == "__main__":
    #pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("player movement test")
    framerate = pygame.time.Clock()

    RATE = 500 

    #sprites, objects and groups
    dummyPlayer = Character()
    heart = HeartObject(dummyPlayer)
    background = pygame.image.load("spritesheets/background.png")

    #gameplay loop
    while True:
        framerate.tick(30)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #screen display
        screen.blit(background, (0,0))

        heart.update() 

        pygame.display.update()
