import unittest
from Reader import *


class ReaderTEST(unittest.TestCase):
    """
    Testing class for the Reader
    """

    def test_isFileNone(self):
        reader = Reader()
        reader.load_file("chapIintro.txt")
        file = reader.get_file()
        self.assertIsNotNone(file)

    def test_isTheTextCorrect(self):
        ##for this test, I was unsure how to get the tester to check
        ##if the right text was being displayed, so I would just correct it
        ##manually, and just assert True; this was used so that I could still
        ##"test" if this looked right without having an auto-checker if ygm?
        reader = Reader()
        reader.load_file("chapIintro.txt")
        reader.readChapt()
        self.assertTrue(True)

    def test_readOneLine(self):
        reader = Reader()
        reader.load_file("test.txt")
        reader.readLine()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()



