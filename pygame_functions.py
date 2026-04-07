from devilmalz import *
from select_sprites import *
from Writer import *
from BattleBox import *
from HeartObject import *
from bullets import *
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

    writer = Writer(screen)

    return (pil, (fight, item, talk), writer)

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

def quit_event():
    """
    pygame event check if you only need to check quitting the game.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()


def player_select_loop(pil, selects, writer):
    """
    Gameplay loop for the player select portion of the battle.
    :param screen: pygame surface object.
    :param background: pygame image object of the bakcground.
    :param pilGroup: pygame sprite group for the enemy, Pil.
    :param selectGroup: pygame sprite group for the select sprites.
    :param writer: writer object to display text on the screen.
    """
    background, screen = screen_setup()
    framerate = pygame.time.Clock()
    not_fight = True
    mouse_x = mouse_y = 0

    RATE = 500
    FRAMERATE = 60
    TEXT_COLOUR = (233,148,243)

    selectGroup = create_group(selects)
    fight, item, talk = selects
    pilGroup = create_group([pil])

    writer.load_text("text/intro.txt")

    while not_fight:
        framerate.tick(FRAMERATE)
        ticks = pygame.time.get_ticks()

        mouse_x, mouse_y, click = mouse_eventcheck(mouse_x, mouse_y)
        if click and fight.check_click(mouse_x, mouse_y):
            not_fight = False
            
        screen.blit(background, (0,0))
        pilGroup.update(ticks, RATE) 
        selectGroup.update(mouse_x, mouse_y)

        pilGroup.draw(screen)
        selectGroup.draw(screen)
        writer.display_text(colour=TEXT_COLOUR)

        pygame.display.update()


def pil_attack_setup(screen, player, pil):
    """
    Setting up the objects needed for Pil's attack ssequence.
    :param screen: pygame surface object representing the screen.
    :param player: character object from ealier in the game.
    :param Pil: Pil object.
    :returns tuple: the battle box, heart and pil objects initialised here.
    """
    box = BattleBox()
    heart = HeartObject(player)
    bullets = BulletsGroup(screen)

    return (box, heart, pil, bullets)

def pil_attack_loop(heart, pil, box, bullets):
    """
    Gameplay loop for Pil's attack and the player dodging.
    :param screen: pygame surface object representing the screen.
    :param background: pygame image for the background.
    :param heart: HeartObject object representing the player.
    :param pil: Pil object.
    :param box: pygame rect object representing the box the heart stays in.
    :param bullets: Bullets Group obejct for Pil's attack.
    """
    bulets_exist = alive = True
    framerate = pygame.time.Clock()
    background, screen = screen_setup()
    
    RATE = 500
    FRAMERATE = 60
    TIME_ALLOWED = 9000

    pil.attack()
    pilGroup = create_group([pil])
    heartGroup = create_group([heart])
    start = pygame.time.get_ticks()

    while bulets_exist and alive:
        framerate.tick(FRAMERATE)
        ticks = pygame.time.get_ticks()

        heart = player_movement(heart, box)

        if heart.check_hit(bullets):
            heart.hit()
            if heart.check_dead():
                end_time = ticks
                alive = False

        if time_out(start, ticks, TIME_ALLOWED):
            bulets_exist = False
            end_time = ticks

        screen.blit(background, (0,0))

        heartGroup.update()
        heartGroup.draw(screen)

        pilGroup.update(ticks, RATE)
        pilGroup.draw(screen)

        bullets.update(ticks, RATE)
        bullets.draw()

        heart.get_healthbar().draw(screen)

        pygame.display.update()
    
    return alive, end_time

def player_movement(player, box):
    """
    Function letting the heart object move.
    :param player: heartObject instansiation.
    :param box: pygame rect obejct representing the box that the heart stays in.
    :returns player: the heart obejct with the updated x and y coordinates.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_w]:
            player.move_up()
        if user_input[pygame.K_s]:
            player.move_down()
        if user_input[pygame.K_d]:
            player.move_right()
        if user_input[pygame.K_a]:
            player.move_left()

        player = heart_bound_check(player, box)

    return player


def heart_bound_check(heart, box):
    """
    Makes sure the heart stays in the box.
    :param heart: heartObject instansication.
    :param box: pygame rect object representing where the heart is allowed to go.
    """
    X_BOUND = (box.get_x() + box.get_width()) - heart.get_rect().width
    Y_BOUND = (box.get_y() + box.get_height() - heart.get_rect().height)
        
    if heart.get_y() < box.get_y():
        heart.set_y(box.get_y())
    if heart.get_y() > Y_BOUND:
        heart.set_y(Y_BOUND)
    if heart.get_x() < box.get_x():
        heart.set_x(box.get_x())
    if heart.get_x() > X_BOUND:
        heart.set_x(X_BOUND)

    return heart

def pil_intermission(start_time, pil, writer):
    """
    Pil's talking inbetween attacks.
    :param screen: pygame surface object representing the screen.
    :param background: pygame image object for the screen background.
    :param start_time: integer when the previous function ended.
    :param pil: pil object.
    :param writer: writer obejct to display text on the screen.
    """

    TIME_ALLOWED = 2500
    FRAMERATE = 60
    RATE = 500
    TEXT_COLOUR = (233,148,243)
    
    writer.load_text("text/intermission.txt")
    pilGroup = create_group([pil])
    intermission = True
    framerate = pygame.time.Clock()

    background, screen = screen_setup()

    while intermission:
        framerate.tick(FRAMERATE)
        ticks = pygame.time.get_ticks()

        quit_event()

        intermission = not time_out(start_time, ticks, TIME_ALLOWED)

        screen.blit(background, (0,0))
        pilGroup.update(ticks, RATE) 

        pilGroup.draw(screen)
        writer.display_text(colour=TEXT_COLOUR)

        pygame.display.update()
        
def time_out(start, ticks, time_allowed):
    """
    checks if the allocated time allowed for a function has passed.
    :param start: integer time start.
    :param ticks: interger current time.
    :param time_allowed: time allocated for the fucnton to run.
    :returns boolean: if the time has enlapsed or not.
    """
    return ticks > start + time_allowed
    
def heart_death(end_time):
    pass


