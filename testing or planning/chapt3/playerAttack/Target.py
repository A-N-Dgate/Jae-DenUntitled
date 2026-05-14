import random
from animating_sprites import my_sprite
from select_sprites import selection_sprite
from BattleBox import BattleBox

class Targets(my_sprite, selection_sprite):
    """
    Class represeting the targets that the player has to click.
    """
    def __init__(self, target):
        my_sprite.__init__(self, target)
        self.WIDTH = self.HEIGHT = 64 
        self.COLUMNS = 8
        IMAGE_PATH = "spritesheets/target.png"
        self.load(IMAGE_PATH, self.WIDTH, self.HEIGHT, self.COLUMNS)
        selection_sprite.__init__(self, target, IMAGE_PATH, 0, 0)
        box = BattleBox()
        self.set_x(random.randint(box.get_x(), (box.get_x() + box.get_width()))) 
        self.set_y(200)
        #I think the image setting is fine from selection sprite

    def update(self, current_time, rate):
        """
        Polymorph update method from the inheritted class.
        :param current_time: the current time in ticks.
        :param rate: the rate, in ticks, in which the frame should update. 
        """
        SPEED = 7 #this is being reassinged maybe I should move it after the test passes
        self.set_y(self.get_y() + SPEED)
        my_sprite.update(self, current_time, rate, self.get_x(), self.get_y()) #hopefully thats how you do it 

    def default(self):
        """
        Default animation sequence.
        """
        self.frame = 0
        self.last_frame = 3
        self.animating = False

    def clicked(self):
        "Clicked animation sequence."
        pass





