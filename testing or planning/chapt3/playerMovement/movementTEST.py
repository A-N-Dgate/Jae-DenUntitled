from HeartObject import *
from Character import *
from BattleBox import *
import pygame, sys

if __name__ == "__main__":
    #pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("player movement test")
    framerate = pygame.time.Clock()

    RATE = 500 

    #sprites, objects and groups
    box = BattleBox()
    dummyPlayer = Character()
    heart = HeartObject(dummyPlayer)
    heartGroup = pygame.sprite.Group()
    heartGroup.add(heart)
    background = pygame.image.load("spritesheets/background.png")

    X_BOUND = (box.get_x() + box.get_width()) - heart.get_rect().width
    Y_BOUND = (box.get_y() + box.get_height() - heart.get_rect().height)

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

            #boundcheck - this will be a function so the constants will be declared before the loop here
            # but in the method it'll be before these if statements
            if heart.get_y() < box.get_y():
                heart.set_y(box.get_y())
            if heart.get_y() > Y_BOUND:
                heart.set_y(Y_BOUND)
            if heart.get_x() < box.get_x():
                heart.set_x(box.get_x())
            if heart.get_x() > X_BOUND:
                heart.set_x(X_BOUND)


        #screen display
        screen.blit(background, (0,0))

        heartGroup.update() 
        heartGroup.draw(screen)

        #pygame.draw.rect(screen, (0,0,255), box.get_rect(), width=3)

        pygame.display.update()
