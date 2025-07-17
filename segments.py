from suporting_functions import *

def Introduction():
    pass

def Chapter1(reader, player):
    display_text(reader, "ChapterI", None, False, True)
    string_parsing1(reader, player)


def Chapter2(reader, player):
    display_text(reader, "ChapterII", None, False, True)
    player = create_room(player, 2) #not sure where to put this since the previous was 
    #put in create, but here looks good?
    string_parsing2(reader, player)