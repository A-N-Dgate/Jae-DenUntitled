import pygame

class selection_sprite(pygame.sprite.Sprite):
    def __init__(self, screen, image_path, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.width = 0
        self.height = 0
        #^overwritten in subclass initialise method

        #for switching image
        self.frame = 0
        self.image_rect = pygame.Rect((self.width * self.frame), 0, self.width, self.height)
        self.master_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.master_image.subsurface(self.image_rect)

    def set_frame(self,mouse_x,mouse_y):
        if self.check_click(mouse_x,mouse_y):
            self.frame = 1
        else:
            self.frame = 0
        
    def check_click(self, mouse_x, mouse_y):
        if self.x < mouse_x < (self.x + self.width) and self.y < mouse_y < (self.y + self.height):
            return True

    def update(self, mouse_x, mouse_y):
        self.set_frame(mouse_x,mouse_y)
        self.image = self.master_image.subsurface(self.image_rect)
        self.image_rect = pygame.Rect((self.width * self.frame), 0, self.width, self.height)

class Fight(selection_sprite):
    def __init__(self, screen):
        X_VALUE = 170
        Y_VALUE = 450
        IMAGE_PATH = "spritesheets/fight.png"
        super().__init__(screen, IMAGE_PATH, X_VALUE, Y_VALUE)
        self.width = 200
        self.height = 100
        self.rect = pygame.Rect(X_VALUE, Y_VALUE, self.width, self.height)

        
