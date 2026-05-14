#adjusted from More Python Programming for the Absolute Beginner book
import pygame
from pygame.locals import *

class my_sprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None
        self.image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0

    #I don't think the devilmalz need to move, but I'll keep these here for now
    def get_x(self): return self.rect.x
    def set_x(self, value): self.rect.x = value

    def get_y(self): return self.rect.y
    def set_y(self, value): self.rect.y = value

    def load(self, filename, width, height, columns):
        #so this will be in the init of the devilmalz
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.rect = Rect(0, 0, width, height)
        self.image = self.master_image.subsurface(self.rect)
        self.frame_width = width
        self.frame_height = height
        self.columns = columns

    def update(self, current_time, rate, x, y): 
        #again, not sure if I need the x and y bc the devilmalz will stay in place
        #need x and y for bullets?
        self.old_frame = self.frame - 1
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
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

        self.set_x(x)
        self.set_y(y) 
        #so that the frames are in the right place



