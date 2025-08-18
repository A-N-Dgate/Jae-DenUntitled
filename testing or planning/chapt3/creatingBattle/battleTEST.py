import pygame, sys
from devilmalz import *
from select_sprites import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("Battle appearance test")
    framerate = pygame.time.Clock()

    pil = Pil(screen)
    fight = Fight(screen)

    pilGroup = pygame.sprite.Group()
    selectGroup = pygame.sprite.Group()

    pilGroup.add(pil)
    selectGroup.add(fight)
    pil.default()

    background = pygame.image.load("spritesheets/background.png")
    mouse_x = mouse_y = 0

    while True:
        framerate.tick(30)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()

        #key press loop would go here

        screen.blit(background, (0,0))
        pil.update(ticks, 500) #need to also make that a constant
        fight.update(mouse_x, mouse_y)

        pilGroup.draw(screen)
        selectGroup.draw(screen)


        pygame.display.update()


