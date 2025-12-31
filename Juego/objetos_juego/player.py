from objetos import *
from pygame import *
from render_image import PLAYER_IMG

class Player(ObjetMoving):
    def __init__(self, x, y, imagee, speed, name):
        super().__init__(x, y, imagee, speed)
        self.name = name

    def get_axis(self):
        keys = key.get_pressed()

        axis_x = int(keys[K_d] or keys[K_RIGHT]) - int(keys[K_a] or keys[K_LEFT])
        axis_y = int(keys[K_s] or keys[K_DOWN]) - int(keys[K_w] or keys[K_UP])

        axis = Vector2(axis_x, axis_y)

        if axis.length() != 0:
            axis = axis.normalize()

        return axis
    
    def update(self, static_objects):
        self.velocity = self.get_axis()
        self.moving(static_objects)

player = Player(100,100, PLAYER_IMG, 4, 'Alfredo')