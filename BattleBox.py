import pygame 

class BattleBox():
    """
    Class representing the box where the Heart stays inside during Pil's attack.
    """
    def __init__(self):
        LEFT = 430
        TOP = 400
        WIDTH = 543
        HEIGHT = 330
        HEART = 32
        self.rect = pygame.Rect(LEFT, TOP, WIDTH, HEIGHT)

    def get_rect(self): return self.rect
    def get_x(self): return self.rect.x
    def get_y(self): return self.rect.y
    def get_height(self): return self.rect.height
    def get_width(self): return self.rect.width