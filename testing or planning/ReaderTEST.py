import unittest
import Reader

class ReaderTEST(unittest.TestCase):
    def __init__(self):
        super.__init__()
        self.reader = Reader()

    def isFileNone(self, filename):
        self.reader.load_file(filename)
        file = self.reader.get_file()

