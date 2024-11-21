from Reader import *

def display_text(chapter_name):
    reader = Reader()
    #i was about to Reader reader = new Reader(); isnt that insane...
    reader.load_file("descriptions/chapterIntro/%s.txt"%(chapter_name))
    reader.read()
    #end 

def string_parsing1():
    #one just in case I need to make more / create a general one
    pass
