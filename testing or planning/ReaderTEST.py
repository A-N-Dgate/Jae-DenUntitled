import unittest
import Reader


class ReaderTEST(unittest.TestCase):
    """
    Testing class for the Reader
    """

    def test_isFileNone(self):
        reader = Reader()
        reader.load_file("chapIintro")
        file = self.reader.get_file()
        self.assertIsNotNone(file)

    def test_isTheTextCorrect(self):
        reader = Reader()
        reader.load_file("chapIintro")
        file = self.reader.get_file()
        self.assertEquals(file[0],"==================CHAPTER I - HOME?======================")


if __name__ == "__main__":
    unittest.main()



