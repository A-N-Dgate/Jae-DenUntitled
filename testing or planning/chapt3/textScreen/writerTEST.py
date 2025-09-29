from Writer import *
import pygame, sys

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("Display text test")
    framerate = pygame.time.Clock()

    background = pygame.image.load("spritesheets/background.png")
    mouse_x = mouse_y = 0 #might do a little cheating here...

    writer = Writer(screen)
    writer.load_text("text/intro.txt")

    while True:
        framerate.tick(30)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x, mouse_y)
                #to get the coordinates of the box; a bit of a silly trick

        
        screen.blit(background, (0,0))
        writer.display_text(colour=(223,148,243))
        pygame.draw.rect(screen, (0,0,255), writer.rect, width=3)

        pygame.display.update()