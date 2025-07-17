import unittest
from Item import *
from Character import *

class ItemTEST(unittest.TestCase):
    """
    Testing class for item
    """

    def test_pickupItem(self):
        print("\npicking up item test")
        player = Character()
        print("\n",player.show_inv())
        item = Item("item one", "This is item one")
        player.add_item(item)
        item.picked_up()
        print("\n",player.show_inv())
        self.assertTrue(item.get_picked())

    def test_itemName(self):
        print("\nShowing the item name")
        item = Item("Item two", "This is item two, showing that the descriptions work")
        itemDesc = item.get_desc()
        print("\n",itemDesc)
        self.assertEqual(itemDesc, "This is item two, showing that the descriptions work")

    def test_itemDropped(self):
        print("\nDropping item test")
        player = Character()
        item = Item("item one", "This is item one")
        player.add_item(item)
        print("\n",player.show_inv())
        #there isn't a player dropItem method yet - put htat here when done
        item.dropped()
        self.assertFalse(item.get_picked())

if __name__ == "__main__":
    unittest.main()
        

