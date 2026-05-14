from Target import Targets
import pygame, sys

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("Player Attack Test")
    framerate = pygame.time.Clock()

    RATE = 500

    #sprites, objects and groups
    one_target = Targets(screen)
    one_target.default()
    targetGroup = pygame.sprite.Group()
    targetGroup.add(one_target)
    background = pygame.image.load("spritesheets/background.png")

    #gameplay loop
    while True:
        framerate.tick(60)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #screen display
        screen.blit(background, (0,0))

        targetGroup.update(ticks, RATE)
        targetGroup.draw(screen)

        pygame.display.update()
