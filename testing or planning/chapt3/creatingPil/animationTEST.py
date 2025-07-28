from animating_sprites import *
from devilmalz import *
import pygame, sys

#visual test because I don't know how else to test it...

if __name__ == "__main__":
    #pygame refresher ig
    pygame.init()
    screen = pygame.display.set_mode((600,500))
    pygame.display.set_caption("animation test for PIL")
    framerate = pygame.time.Clock()
    
    pil = Pil()
    #pil.default()
    group = pygame.sprite.Group() #capital or object lower for method?
    group.add(pil)

    while True:
        framerate.tick(30)
        ticks = pygame.time.get_ticks()

        #quit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()


        #all I need to do is update Pil? 
        screen.fill((0,0,255))
        pil.update(ticks, 30)
        group.draw(screen)
        
        pygame.display.update()
        