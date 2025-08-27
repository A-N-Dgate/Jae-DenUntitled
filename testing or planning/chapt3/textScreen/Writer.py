from Reader import *
import pygame

class Writer():
    """
    Class used to wrtie text to the 2d graphical screen.
    :attribute screen: pygame display obeject; where the text will be displayed.
    :attribute rect: pygame Rect object showing the bounds of where the texct can go.
    """
    def __init__(self, screen):
        self.screen = screen
        self.text = ""
        self.rect = pygame.Rect(430,400,540,330) #trial and error testedchange for main code

    def load_text(self, filepath):
        """
        Mathiod which takes text from a file and stroes it within the class.
        :attribute filepath: the path of the file where the text is stored.
        """
        file = open(filepath)
        self.text = self.get_text(filepath)

    def display_text(self, colour=(255,255,255)):
        """
        Method for diaplying text onto the screen.
        :attribute x: the x coordinate.
        :attribute y: the y coordinate.
        :attribute colour: the colour of the text.
        """
        font = pygame.font.Font("fonts/VT323.ttf", 50)
        line_no = 0
        for line in self.text:
            imgText = font.render(line, True, colour)
            self.screen.blit(imgText, ((self.rect.x + 5),(self.rect.y + (line_no*50))))
            line_no += 1

    def get_text(self, filepath):
        """
        Method which organises text from a file into a list
        :attribute filepath: the file path to the text.
        """ 

        lines = []
        file = open(filepath)
        for line in file:
            lines.append(line)
        return lines    
