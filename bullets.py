from animating_sprites import *
from BattleBox import *
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
        self.last_frame = self.COLUMNS - 1 
        self.rect = self.image.get_rect()     
        self.choice = 0

    def set_choice(self, a): self.choice = a

    def __check_kill(self):
        if (self.get_x() > self.screen.get_width() or 
            self.get_y() > self.screen.get_height() or
            self.get_x() < 0 or
            self.get_y() < 0):
            self.kill()


    def update(self, current_time, rate):
        """
        Animation update method for the bullet sprite.
        :param current_time: integer time in millisecons since the sequence has started.
        :param rate: rate in milliseconds tha the sprite should update.
        """
        match self.choice:
            case 1:
                self.pattern_one(current_time, rate)
            case 2:
                self.pattern_two(current_time, rate)
            case 3:
                self.pattern_three(current_time, rate)
            case _:
                pass
         
    def setup_pattern(self, choice):
        """
        Setting up the initial attribute values each attack pattern.
        :param choice: The attack patern chosen for Pil's next attack.
        """
        box = BattleBox()
        match choice:
            case 1:
                self.inverse = random.choice([True, False])
                self.angle = 90
                self.rotation_angle = 0 
                self.dTheta = random.uniform(1,3)

                if self.inverse:
                    self.set_x(450)
                else:
                    self.set_x(900)
                self.set_y(random.randint(100,300))
            case 2:
                self.inverse = random.choice([True, False])
                self.rotation_angle = 0
                self.set_y(100)
                if self.inverse:
                    self.set_x(random.randint(box.get_x(), (box.get_x() + 200)))
                else:
                    self.set_x(random.randint((box.get_x() + 250), (box.get_y() + box.get_width())))

            case 3:
                self.inverse = random.choice([True, False])

                if self.inverse:
                    self.set_x(box.get_x() + box.get_width() + 20)
                else:
                    self.set_x(box.get_x() - 50)

                self.set_y(box.get_rect().top + (box.get_height() // 2))


    def pattern_one(self, current_time, rate):
        """
        One attack pattern for Pil.
        :param current_time: current tiem in ticks.
        :param rate: rate in which to update in ticks past.
        """
        MULTIPLIER = 9   #speed and size of the circle (not exactly)
        TOTAL_DEGREES = 360
         
        self.__check_kill()

        self.angle = (self.angle - self.dTheta) % TOTAL_DEGREES
        dx = math.sin(math.radians(self.angle)) * MULTIPLIER
        dy = math.cos(math.radians(self.angle)) * MULTIPLIER

        if self.inverse:
            dx = -dx

        self.rotation_angle = (-math.degrees(math.atan2(dy,dx))) % TOTAL_DEGREES

        self.set_x(self.get_x() + dx)
        self.set_y(self.get_y() + dy)

        super().update(current_time, rate, self.get_x(), self.get_y())
        self.image = pygame.transform.rotate(self.image, self.rotation_angle)

    def pattern_two(self, current_time, rate):
        box = BattleBox()
        DA = 5

        self.__check_kill()
        dy = 0

        if box.get_y() < self.get_y() < box.get_y() + box.get_height():
            dy = 15
        else:
            dy = 5

        self.set_y(self.get_y() + dy)
        self.rotation_angle += DA
        super().update(current_time, rate, self.get_x(), self.get_y())
        self.image = pygame.transform.rotate(self.image, self.rotation_angle)

    def pattern_three(self, current_time, rate):
        super().update(current_time, rate, self.get_x(), self.get_y())


class BulletsGroup(): # I don't think this is a sprite clas itself? it contains one
    def __init__(self, screen):
        self.screen = screen
        self.group = pygame.sprite.Group()
        for x in range(10):
            bullet = Bullets(screen)
            self.group.add(bullet)
    
    def get_group(self): return self.group

    def choose_attack(self):
        """
        Selecting the attack pattern randomly.
        """
        choice = random.randint(1,3)
        for sprite in self.get_group():
            sprite.set_choice(choice)
            sprite.setup_pattern(choice)
            

    def update(self, current_time, rate):
        self.get_group().update(current_time, rate)

    def draw(self):
        self.get_group().draw(self.screen)
        





