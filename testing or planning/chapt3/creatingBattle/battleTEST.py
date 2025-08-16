import pygame, sys
from devilmalz import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("Battle appearance test")
    framerate = pygame.time.Clock()

    pil = Pil(screen)
    group = pygame.sprite.Group()
    group.add(pil)
    pil.default()

    background = pygame.image.load("spritesheets/background.png")

    while True:
        framerate.tick(30)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #key press loop would go here

        screen.blit(background, (0,0))
        group.update(ticks, 500)
        group.draw(screen)

        pygame.display.update()


