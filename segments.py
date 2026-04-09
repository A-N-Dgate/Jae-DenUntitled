from suporting_functions import *
from pygame_functions import *
from bullets import *

#constants? idk how to organsie this correctly in python...
fileName = None
isParagraph = False
intro = True

def Introduction():
    input("""
=====================================INTRODUCTION======================================
Welcome to the first test build of this game! this initial test is to see if everything
feels okay within the 2 completed sections, and the just started 3rd.
    
For everything to work smoothly, please make sure that your CMD window is no smaller
than the line indicated with the ===, and set the font size and colour to something 
that is comfortable for you to use.
          
Once that is done, press Enter to continue.
>""")
    
    choice = ""
    while choice != "n" and choice != "y":
        choice = input("Do you want to skip chapters 1 and 2? (y/n)").lower()
        
    return choice == "y"

def Chapter1(reader, player):
    display_text(reader, "chapterI", fileName, isParagraph, intro)
    string_parsing1(reader, player)


def Chapter2(reader, player):
    display_text(reader, "ChapterII", fileName, isParagraph, intro)
    chapter = 2
    player = create_room(player, chapter) #not sure where to put this since the previous was 
    #put in create, but here looks good?
    string_parsing2(reader, player)
    time.sleep(5)

def Chapter3(player):
    background, screen = screen_setup()
    introduction_pil(screen)
    pil, selects, writer = player_select_setup(screen)
    box, heart, pil, bullets = pil_attack_setup(screen, player, pil)

    alive = True
    end_time = pygame.time.get_ticks()
    while alive:
        pil_intermission(end_time, pil, writer)
        player_select_loop(pil, selects, writer) 
        bullets = BulletsGroup(screen)
        alive, end_time = pil_attack_loop(heart, pil, box, bullets)

    if not alive:
        heart_death(end_time, heart, pil, bullets)
        
    
    

