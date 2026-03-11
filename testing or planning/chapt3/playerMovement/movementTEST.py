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
    heartGroup = pygame.sprite.Group()
    heartGroup.add(heart)
    background = pygame.image.load("spritesheets/background.png")

    #gameplay loop
    while True:
        framerate.tick(60)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            user_input = pygame.key.get_pressed()

            if user_input[pygame.K_w]:
                heart.move_up()
            if user_input[pygame.K_s]:
                heart.move_down()
            if user_input[pygame.K_d]:
                heart.move_right()
            if user_input[pygame.K_a]:
                heart.move_left()


        #screen display
        screen.blit(background, (0,0))

        heartGroup.update() 
        heartGroup.draw(screen)

        pygame.display.update()
