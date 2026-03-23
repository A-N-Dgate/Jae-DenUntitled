from Healthbar import *
import pygame

class HeartObject(pygame.sprite.Sprite):
    """
    Class representing the 2d form of the player
    """
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        CENTER_X = 689
        CENTER_Y = 547
        self.player = player
        self.image = pygame.image.load("spritesheets/heart.png")
        self.rect = self.image.get_rect()
        self.health = 50
        self.healthbar = Healthbar(self)
        self.rect.x = CENTER_X
        self.rect.y = CENTER_Y
        self.__MOVE_PIXELS = 5

    def get_player(self): return self.player
    def get_image(self): return self.image
    def get_rect(self): return self.rect
    def get_health(self): return self.health
    def get_healthbar(self): return self.healthbar
    def get_x(self): return self.rect.x
    def get_y(self): return self.rect.y

    def set_health(self, value): self.health = value
    def set_x(self, value): self.rect.x = value
    def set_y(self, value): self.rect.y = value

    def move_right(self):
        self.set_x(self.get_x() + self.__MOVE_PIXELS)
    
    def move_left(self):
        self.set_x(self.get_x() - self.__MOVE_PIXELS)

    def move_up(self):
        self.set_y(self.get_y() - self.__MOVE_PIXELS)

    def move_down(self):
        self.set_y(self.get_y() + self.__MOVE_PIXELS)

    def update(self):
        pygame.sprite.Sprite.update(self)

    #def draw(self): #need to check if this needs to be here?
        #pass

    def check_hit(self, projectileGroup):
        """
        Check if the heart had collided wih any projectiles.
        :param projectileGroup: container class for a pygame sprite group.
        :returns boolean: whether heart hit something or not.
        """
        return pygame.sprite.spritecollideany(self, projectileGroup.get_group())

    def hit(self):
        """
        Decreases the health by a fixed amount.
        """
        self.set_health(self.get_health() - 3)
        self.get_healthbar().set_health_rect()

    def check_dead(self):
        """
        Checks if the heart's health is below 0.
        :returns bool: whether health is below 0.
        """
        return self.get_health() < 0