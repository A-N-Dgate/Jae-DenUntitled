import pygame

class HeartObject(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pygame.image.load("spritesheets/heart.png")
        self.rect = self.image.get_rect()
        self.health = 50
        self.rect.x = self.rect.y = 100
        self.__MOVE_PIXELS = 3

    def get_player(self): return self.player
    def get_image(self): return self.image
    def get_rect(self): return self.rect
    def get_health(self): return self.health
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

    def check_hit(self, projectile):
        pass

    def hit(self):
        pass

    def check_dead(self):
        pass
