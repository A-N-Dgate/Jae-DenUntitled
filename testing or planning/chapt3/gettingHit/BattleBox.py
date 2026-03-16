import pygame 

class BattleBox():
    def __init__(self):
        LEFT = 430
        TOP = 400
        WIDTH = 543
        HEIGHT = 330
        HEART = 32
        self.rect = pygame.Rect(LEFT, TOP, WIDTH, HEIGHT)
        #self.heart_rect = pygame.Rect((LEFT + (HEART // 2)), (TOP + (HEART // 2)), (WIDTH - HEART), (HEIGHT - HEART))

    def get_rect(self): return self.rect
    def get_x(self): return self.rect.x
    def get_y(self): return self.rect.y
    def get_height(self): return self.rect.height
    def get_width(self): return self.rect.width
    #def get_heart_rect(self): return self.heart_rect

    def within_rect(self, opposition):
        return opposition.get_rect().colliderect(self.get_rect())