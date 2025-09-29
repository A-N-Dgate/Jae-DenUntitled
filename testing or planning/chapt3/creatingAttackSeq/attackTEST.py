from devilmalz import *
from select_sprites import *
from Writer import *

import sys

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("Attack test")
    framerate = pygame.time.Clock()

    #sprites, objects and groups
    writer = Writer(screen)
    writer.load_text("text/intro.txt")
    #^might be building on this during this test

    pil = Pil(screen)
    fight = Fight_sel(screen)
    item = Item_sel(screen)
    talk = Talk_sel(screen)

    pilGroup = pygame.sprite.Group()
    selectGroup = pygame.sprite.Group()

    pilGroup.add(pil)
    selectGroup.add(fight)
    selectGroup.add(item)
    selectGroup.add(talk)

    pil.default()
    mouse_x = mouse_y = 0

    background = pygame.image.load("spritesheets/background.png")
    
    while True:
        framerate.tick(30)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()


        screen.blit(background, (0,0))
        pil.update(ticks, 500)
        selectGroup.update(mouse_x, mouse_y)

        pilGroup.draw(screen)
        selectGroup.draw(screen)
        writer.display_text(colour=(223,148,243))

        pygame.display.update()

