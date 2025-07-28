import pygame
from pygame.locals import *
from animating_sprites import *

class Devilmalz(my_sprite):
    """
    Class for all of the devilmalz; to show them on screen and how they interact
    """
    #all the devilmalz should have the same animation cycle
    #attack def values 
    #
    def __init__(self):
        my_sprite.__init__()

    #based on the spritesheet I was making earlier
    def default(self):
        """The default animation cycle"""
        self.frame = 0
        self.last_frame = 3

    def attack(self):
        """attack animation cycle"""
        #note: need to double check fighter to see how returning to default works
        self.frame = 4
        self.last_frame = 8

    def hit(self):
        """devilmalz getting hit animation cycle"""
        self.frame = 9
        self.last_frame = 11

    def defeated(self):
        """devilmalz defeated animation cylce"""
        pass




class Pil(Devilmalz):
    #loads their own spritesheet + anything else
    #attack patterns 
    #need probably a class + subclasses for the bullets - problem for later
    def __init__(self):
        pass