import unittest
from Room import *
from Character import * 
from Reader import *

class RoomTEST(unittest.TestCase):
    """Testing class for Room, specifically for chapter 2"""
    
    def test_room1(self):
        print("\nRoom1 test")
        player = Character()
        player = create_room(player, 1)
        print(player.get_currentRoom())
        self.assertTrue(True)

    def test_room2(self):
        print("\nRoom2 test")
        player = Character()
        player = create_room(player, 2)
        print(player.get_currentRoom())
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
        


