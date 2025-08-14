from animating_sprites import *
from devilmalz import *
import pygame, sys

#idk where else to put this and it won't  be used in the real product...
def print_text(screen,  x, y, text, colour = (255,255,255)):
    font = pygame.font.Font(None, 40)
    imgText = font.render(text, True, colour)
    screen.blit(imgText, (x,y))

#visual test because I don't know how else to test it...

if __name__ == "__main__":
    #pygame refresher ig
    pygame.init()
    screen = pygame.display.set_mode((600,500))
    pygame.display.set_caption("animation test for PIL")
    framerate = pygame.time.Clock()
    
    pil = Pil(screen)
    group = pygame.sprite.Group() #capital for object lower for method?
    group.add(pil)

    pil.default()

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

            #2nd test: make Pil change animation cycle depending on a key pressed
            if keys[K_1]:
                pil.attack()
            if keys[K_2]:
                pil.hit()
            if keys[K_3]:
                pil.defeated()


        #all I need to do is update Pil? 
        screen.fill((0,0,255))
        print_text(screen, 0, 400, "1 - attack")
        print_text(screen, 0, 430, "2 - hit")
        print_text(screen, 0, 460, "3 - defeated")
        group.update(ticks, 500) #makes no differnce if its pil or group
        group.draw(screen)
        
        pygame.display.update()
        