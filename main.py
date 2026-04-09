from segments import *
from Character import *

player, reader = create()
skip = Introduction()
if skip:
    Chapter3(player)
else:
    player = Chapter1(reader, player) 
    player = Chapter2(reader, player)
    Chapter3(player)