from segments import *
from Character import *

player, reader = create()
skip = Introduction()
if skip:
    Chapter3(player)
else:
    Chapter1(reader, player) 
    Chapter2(reader, player)
    Chapter3(player)