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
    def __init__(self, target):
        super().__init__(target)

    #based on the spritesheet I was making earlier
    def default(self):
        """The default animation cycle"""
        self.frame = 0
        self.last_frame = 3

    def attack(self):
        """attack animation cycle"""
        self.frame = 4
        self.last_frame = 6

    def hit(self):
        """devilmalz getting hit animation cycle"""
        self.frame = 7
        self.last_frame = 10

    def defeated(self):
        """devilmalz defeated animation cylce"""
        self.frame = 11
        self.last_frame = 17


class Pil(Devilmalz):
    #loads their own spritesheet + anything else
    #attack patterns 
    #need probably a class + subclasses for the bullets - problem for later
    def __init__(self, target):
        super().__init__(target)
        self.load("spritesheets/pil.png", 128, 128, 18) #magic numbers?

    #testing animation here so I don't think there's much else to do 