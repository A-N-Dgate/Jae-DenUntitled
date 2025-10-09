from bullets import *
import pygame, sys

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("Bullet test")
    framerate = pygame.time.Clock()

    #sprites, objects and groups 
    bullet = Bullets(screen)
    bulletGroup = pygame.sprite.Group()
    bulletGroup.add(bullet)
    
    background = pygame.image.load("spritesheets/background.png")

    while True:
        framerate.tick(30)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        screen.blit(background, (0,0))
        bulletGroup.update(ticks, 500)

        bulletGroup.draw(screen)

        pygame.display.update() 