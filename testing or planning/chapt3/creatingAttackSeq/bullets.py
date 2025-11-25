from animating_sprites import *
import pygame, math, random

#this class might be placed with the devilmalz in the actual product / non-testing folders 
class Bullets(my_sprite):
    """
    Class holding the projectiles that Pil, at least, will use.
    """
    def __init__(self, target):
        super().__init__(target)
        self.screen = target
        self.HEIGHT = self.WIDTH = 30
        self.COLUMNS = 4
        self.load("spritesheets/pilBullets.png", self.WIDTH, self.HEIGHT, self.COLUMNS)
        self.last_frame = self.COLUMNS - 1 #zero indexing ig
        self.angle = 90
        self.rotation_angle = 0 
        self.inverse = random.choice([True, False])
        self.set_y(random.randint(100,300)) 
        self.dTheta = random.uniform(1,3)

        if self.inverse:
            self.set_x(450)
        else:
            self.set_x(900)

    def update(self, current_time, rate):
        """
        Animation update method for the bullet sprite.
        :param current_time: integer time in millisecons since the sequence has started.
        :param rate: rate in milliseconds tha the sprite should update.
        """
        if (self.get_x() > self.screen.get_width() or 
            self.get_y() > self.screen.get_height() or
            self.get_x() < 0 or
            self.get_y() < 0): #proabably need to simplify this
            self.kill()

        MULTIPLIER = 8   #speed and size of the circle (not exactly)
        TOTAL_DEGREES = 360
        
        self.angle = (self.angle - self.dTheta) % TOTAL_DEGREES
        #print(self.angle) 
        dx = math.sin(math.radians(self.angle)) * MULTIPLIER
        dy = math.cos(math.radians(self.angle)) * MULTIPLIER

        if self.inverse:
            dx = -dx

        self.rotation_angle = (-math.degrees(math.atan2(dy,dx))) % TOTAL_DEGREES

        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)

        super().update(current_time, rate, self.get_x(), self.get_y())
        self.image = pygame.transform.rotate(self.image, self.rotation_angle) 


class BulletsGroup(): # I don't think this is a sprite clas itself? it contains one
    def __init__(self, screen):
        self.screen = screen
        self.group = pygame.sprite.Group()
        for x in range(10):
            bullet = Bullets(screen)
            self.group.add(bullet)

    def update(self, current_time, rate):
        self.group.update(current_time, rate)

    def draw(self):
        self.group.draw(self.screen)

        





