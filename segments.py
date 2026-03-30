from suporting_functions import *
from pygame_functions import *

#constants? idk how to organsie this correctly in python...
fileName = None
isParagraph = False
intro = True

def Introduction():
    pass

def Chapter1(reader, player):
    display_text(reader, "chapterI", fileName, isParagraph, intro)
    string_parsing1(reader, player)


def Chapter2(reader, player):
    display_text(reader, "ChapterII", fileName, isParagraph, intro)
    chapter = 2
    player = create_room(player, chapter) #not sure where to put this since the previous was 
    #put in create, but here looks good?
    string_parsing2(reader, player)

def Chapter3(player):
    background, screen = screen_setup()
    introduction_pil(screen)
    pil, selects, writer = player_select_setup(screen)
    player_select_loop(screen, background, pil, selects, writer)

