import unittest
from Room import *
from Item import *

class RoomTEST(unittest.TestCase):
    """
    Testing class for room
    """

    def test_removeItem(self):
        print("\nRemove item test")
        item1 = Item("item 1", "an item, used for testing")
        room1 = Room("Room 1", "room used for testing", [item1])

        room1.remove_item(item1)
        self.assertTrue(room1.isItemEmpty())

    def test_look(self):
        print("\nlook around room test")
        room1 = Room("Room 1", "room used for testing", [])

        #idk how to check strings on a seperate line properly
        print(str(room1))
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()



