from devilmalz import *
from select_sprites import *
from Writer import *
import pygame, sys

def screen_setup():
    """
    function to return a pygame surface and the background.
    :returns pygame display: screen, where everything will be drawn.
    :returns pygame image: background, the backgorundf used in this segment of the game.
    """
    pygame.init()
    screen = pygame.display.set_mode((1440,810))
    pygame.display.set_caption("Chapter 3 test build")

    background = pygame.image.load("spritesheets/background.png")
    return background, screen

def create_group(sprites):
    """
    Creates a pygame sprite group obejct.
    :param spriteArr: tuple of sprite objects to be added to the group.
    :returns group: pygame group object.
    """
    group = pygame.sprite.Group()
    for sprite in sprites:
        group.add(sprite)

    return group

def introduction_pil(screen):
    """
    Procedure for Pil's introduction.
    :param screen: pygame surface object, where everythign will be displayed.
    """
    #use this to animate a little thing of jae entering the room and pil noticing
    #remember to blit black before ending the procedure.
    pass

def exit_game():
    """
    Procedure for exiting the game.
    """
    pygame.quit()
    sys.exit()

def player_select_setup(screen):
    """
    Function sets up the sprites for the player select screen.
    :param screen: pygame surface representing the screen.
    :returns tuple sprites: returns the pil sprite object and a tuple of the selects sprite objects.
    """
    pil = Pil(screen)
    fight = Fight_sel(screen)
    item = Item_sel(screen)
    talk = Talk_sel(screen)
    pil.default()

    pilGroup = pygame.sprite.Group()
    pilGroup.add(pil)

    writer = Writer(screen)
    writer.load_text("text/intro.txt")

    return (pilGroup, (fight, item, talk), writer)

def mouse_eventcheck(mouse_x, mouse_y):
    """
    The pygame event check for loop for checking mouse position.
    :param mouse_x: integer value of mouse x coordinate.
    :param mouse_y: integer value of mouse y coordinate.
    :returns (int, int): new x and y coordinates for the mouse.
    """
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            click = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            click = True

    return mouse_x, mouse_y, click


def player_select_loop(screen, background, pil, selects, writer):
    """
    Gameplay loop for the player select portion of the battle.
    :param screen: pygame surface object.
    :param background: pygame image object of the bakcground.
    :param pilGroup: pygame sprite group for the enemy, Pil.
    :param selectGroup: pygame sprite group for the select sprites.
    :param writer: writer object to display text on the screen.
    """
    framerate = pygame.time.Clock()
    not_fight = True
    mouse_x = mouse_y = 0

    RATE = 500
    FRAMERATE = 60
    TEXT_COLOUR = (233,148,243)

    selectGroup = create_group(selects)
    fight, item, talk = selects

    while not_fight:
        framerate.tick(FRAMERATE)
        ticks = pygame.time.get_ticks()

        mouse_x, mouse_y, click = mouse_eventcheck(mouse_x, mouse_y)
        if click and fight.check_click(mouse_x, mouse_y):
            not_fight = False
            
        screen.blit(background, (0,0))
        pil.update(ticks, RATE) 
        selectGroup.update(mouse_x, mouse_y)

        pil.draw(screen)
        selectGroup.draw(screen)
        writer.display_text(colour=TEXT_COLOUR)

        pygame.display.update()

