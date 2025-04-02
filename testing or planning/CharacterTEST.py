import unittest
from Character import *

class CharacterTEST(unittest.TestCase):
    """
    Testing class for character                                                        
    """

    def test_stats(self):
        player = Character()
        stats = str(player)
        self.assertEqual("You are currently level 1", stats)
        print("\n stats test:")
        print(stats)

    def test_showInvEmpty(self):
        player = Character()
        items_message = player.show_inv()
        print("\n show empty test ")
        print(items_message)
        self.assertEqual(items_message, "You currently don't have any items")

    def test_showInvWithItems(self):
        player = Character()
        player.add_item("item")
        player.add_item("another item")
        items_message = player.show_inv()
        print("\n show some items test")
        print(items_message)
        self.assertIsNotNone(items_message)
        
    
    def test_addItem(self):
        player = Character()
        print(player.add_item("item"))
        print("\n add items check")
        player.show_inv()
        self.assertEqual(1, player.get_itemNo())

    def test_itemsFull(self):
        player = Character()
        print("\n inv full test")
        for x in range(4):
            player.add_item("item")
            #change to use item object after
        
        message = player.add_item("item")
        self.assertIsNotNone(message)
        print(message)

if __name__ == "__main__":
    unittest.main()
        

