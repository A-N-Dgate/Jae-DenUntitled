import pygame

class Healthbar():
    """
    Class used to display a health bar for the heart.
    """
    def __init__ (self, heart):
        self.heart = heart
        self.LEFT = 600
        self.TOP = 750
        self.WIDTH = 200
        self.HEIGHT = 20
        self.original_health = self.heart.get_health()
        self.full_rect = pygame.Rect(self.LEFT, self.TOP, self.WIDTH, self.HEIGHT)
        self.health_rect = self.full_rect

    def get_heart(self): return self.heart
    def get_full_rect(self): return self.full_rect
    def get_original_health(self): return self.original_health
    def get_health_rect(self): return self.health_rect

    def set_health_rect(self):
        """
        Changes the health bar when the heart gets hit.
        """
        #static 3 in the heart class, change this with the next enemy
        new_value = self.get_heart().get_health()
        total = self.get_original_health()
        percentage = new_value / total
        width = int(self.WIDTH * percentage) 
        self.health_rect = pygame.Rect(self.LEFT, self.TOP, width, self.HEIGHT)

    def draw(self, screen):
        """
        Draws the rectangles representing the helath bar onto the screen.
        :param screen: pygame surface representing the screen.
        """
        pygame.draw.rect(screen, (255,0,0), self.get_full_rect())
        pygame.draw.rect(screen, (255,255,0), self.get_health_rect())
