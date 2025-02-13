import unittest
from Character import *

class CharacterTEST(unittest.TestCase):
    """
    Testing class for character                                                        
    """

    def test_stats(self):
        player = Character()
        stats = str(player)
        self.assertNotEqual("", stats)

    def test_showInvEmpty(self):
        player = Character()
        items_message = player.show_inv()
        self.assertEqual(items_message, "You currently don't have any items")

    def test_showInvWithItems(self):
        player = Character()
        items_message = player.show_inv()
        self.assertIsNotNone(items_message)

    def test_itemsFull(self):
        player = Character()
        for x in range(3):
            player.add_item("item")
            #change to use item object after
        
        message = player.add_item("item")
        self.assertIsNotNone(message)

if __name__ == "__main__":
    unittest.main()
        

