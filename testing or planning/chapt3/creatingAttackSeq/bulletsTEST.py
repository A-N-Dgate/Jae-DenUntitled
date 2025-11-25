from bullets import *
import pygame, sys

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("Bullet test")
    framerate = pygame.time.Clock()

    RATE = 500

    #sprites, objects and groups
    bullet_group = BulletsGroup(screen)
    
    background = pygame.image.load("spritesheets/background.png")

    while True:
        framerate.tick(30)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        screen.blit(background, (0,0))
        
        bullet_group.update(ticks, RATE)
        bullet_group.draw()

        pygame.display.update() 