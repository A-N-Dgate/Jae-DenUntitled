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
        self.animating = False
        self.X_VALUE = 620
        self.Y_VALUE = 120
        #put more constants here for the final product

    def update(self, current_time, rate):
        #overwrite the method in the super-class: polymorphism
        self.old_frame = self.frame - 1
        if current_time > self.last_time + rate:
            #this section is being entered
            self.frame += 1
            if self.frame > self.last_frame:
                if self.animating:
                    self.default()
                else:
                    self.frame = self.first_frame
            self.last_time = current_time 

        #build on current frame, only if it has been changed
        if self.frame != self.old_frame:
            #gets current frame by covering up the master image
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            self.rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(self.rect)
            self.old_frame = self.frame 

        self.set_x(self.X_VALUE)
        self.set_y(self.Y_VALUE) 

    #based on the spritesheet I was making earlier
    def default(self):
        """The default animation cycle"""
        self.frame = 0
        self.last_frame = 3
        self.animating = False

    def attack(self):
        """attack animation cycle"""
        self.frame = 4
        self.last_frame = 6
        self.animating = True

    def hit(self):
        """devilmalz getting hit animation cycle"""
        self.frame = 7
        self.last_frame = 10
        self.animating = True

    def defeated(self):
        """devilmalz defeated animation cylce"""
        self.frame = 11
        self.last_frame = 17
        self.animating = True


class Pil(Devilmalz):
    #loads their own spritesheet + anything else
    #attack patterns 
    #need probably a class + subclasses for the bullets - problem for later
    def __init__(self, target):
        super().__init__(target)
        self.load("spritesheets/pil.png", 192, 192, 18) #magic numbers?

    #testing animation here so I don't think there's much else to do 