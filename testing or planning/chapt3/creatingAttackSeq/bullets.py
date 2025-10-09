from animating_sprites import *
import pygame, math

#this class might be placed with the devilmalz in the actual product / non-testing folders 
class Bullets(my_sprite):
    """
    Class holding the projectiles that Pil, at least, will use.
    """
    def __init__(self, target):
        super().__init__(target)
        self.HEIGHT = self.WIDTH = 30
        self.COLUMNS = 4
        self.load("spritesheets/pilBullets.png", self.WIDTH, self.HEIGHT, self.COLUMNS)
        self.last_frame = self.COLUMNS - 1 #zero indexing ig
        self.angle = 90
        self.rotation_angle = 0 
        self.set_x(900)
        self.set_y(200)

    def update(self, current_time, rate):
        """
        Animation update methiod for the bullet sprite.
        :param current_time: integer time in millisecons since the sequence has started.
        :param rate: rate in milliseconds tha the sprite should update.
        """
        MULTIPLIER = 4 #speed and size of the circle
        TOTAL_DEGREES = 360
        self.angle = (self.angle - 1) % TOTAL_DEGREES 
        dx = math.sin(math.radians(self.angle)) * MULTIPLIER
        dy = math.cos(math.radians(self.angle)) * MULTIPLIER

        self.rotation_angle = (-math.degrees(math.atan2(dy,dx))) % TOTAL_DEGREES

        self.x = (self.get_x() + dx)
        self.y = (self.get_y() + dy)

        super().update(current_time, rate, self.x, self.y)
        self.image = pygame.transform.rotate(self.image, self.rotation_angle) 

        





