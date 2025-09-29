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

    def readChapt(self):
        """
        Method which displays paragraphs of text onto the screen.
        also includes a time between displaying each line.
        """
        for line in self.get_file():
            print(line)
            time.sleep(3)

    def readParag(self):
        """
        Method which displays text in a paragraph, without the timeout.
        """
        text = combineText(self.get_file())
        print(text)

    def returnParag(self):
        """
        Method which returns text in a paragraph
        """

        text = combineText(self.get_file())
        return text
        

    def readLine(self):
        """
        Method which displays one line of text onto the screen.
        """
        lines = []
        for line in self.get_file():
            lines.append(line)
        
        print("\n%s"%(lines[0]))
        #inefficient but oh well


#it might be best to make a singleton class
class globalReader():
    """
    Class used to make sure that there is one reader object in the code
    so that its easier to track its state
    """

    def __init__(self):
        self.reader = Reader()

    def getReader(self):
        return self.reader


def combineText(fileIttr):
    #this can be used outside of the class
    lines = []
    for line in fileIttr:
        lines.append("\n%s"%(line.rstrip()))
    #combine into one string
    text = "".join(lines)

    return text



    