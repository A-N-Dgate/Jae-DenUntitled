import pygame

class HeartObject(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.PLAYER = player
        self.IMAGE = pygame.image.load("spritesheets/heart.png")
        self.HITBOX = self.IMAGE.get_rect()
        self.health = 50
        self.x = 0
        self.y = 0

    def get_player(self): return self.player
    def get_image(self): return self.IMAGE
    def get_hitbox(self): return self.HITBOX
    def get_health(self): return self.health
    def get_x(self): return self.x
    def get_y(self): return self.y

    def set_health(self, value): self.health = value
    def set_x(self, value): self.x = value
    def set_y(self, value): self.y = value

    def Movement(self):
        pass

    def update(self):
        pass

    def draw(self): #need to check if this needs to be here?
        pass

    def check_hit(self, projectile):
        pass

    def hit(self):
        pass

    def check_dead(self):
        pass
