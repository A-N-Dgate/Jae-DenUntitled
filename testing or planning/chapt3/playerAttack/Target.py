import random
from animating_sprites import my_sprite
from select_sprites import selection_sprite

class Targets(my_sprite, selection_sprite):
    """
    Class represeting the targets that the player has to click.
    """
    def __init__(self, target):
        my_sprite.__init__(self, target)
        X_VALUE = 0
        Y_VALUE = 0
        IMAGE_PATH = "spritesheets/target.png"
        selection_sprite.__init__(self, target, IMAGE_PATH, X_VALUE, Y_VALUE)
        self.WIDTH = self.HEIGHT = 64 
        self.COLUMNS = 8
        self.load(IMAGE_PATH, self.WIDTH, self.HEIGHT, self.COLUMNS)
        #I think the image setting is fine from selection sprite

    def update(self, current_time, rate):
        """
        Polymorph update method from the inheritted class.
        :param current_time: the current time in ticks.
        :param rate: the rate, in ticks, in which the frame should update. 
        """
        pass

    def default(self):
        """
        Default animation sequence.
        """
        pass

    def clicked(self):
        "Clicked animation sequence."
        pass





