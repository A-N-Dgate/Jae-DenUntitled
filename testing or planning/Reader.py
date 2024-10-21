import time


class Reader():
    """
    Class used to display the text from files to 
    the screen, which will be used to further the 
    plot of the game.
    :attribute file: the file that the reader is currently reading from 
    """
    def __init__(self):
        self.file = None

    def get_file(self):
        """
        fetches the file currently being read.
        :returns file: 
        """
        return self.file
    
    def load_file(self, filepath):
        self.file = open(filepath)

    def read(self):
        """
        Method which actually displays the text onto screen.
        """
        for line in self.get_file():
            print(line)
            time.sleep(3)