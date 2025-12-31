from objetos import *
from pygame import *
from objetos_juego.player import *
from render_image import ENEMY_IMG
from math import *

class Enemy(ObjetMoving):
    def __init__(self, x, y, imagee, speed, id):
        super().__init__(x, y, imagee, speed)
        self.player = player  # 👈 referencia directa
        self.id = id
        self.rect = Rect(
            x + 5,
            y + 5,
            (TILE_SIZE - 10) * 2,
            (TILE_SIZE - 10) * 2
        )
        self.detection_radius = TILE_SIZE * 2

    def get_axis(self):
        # Vector desde enemy hacia player

        axis = Vector2(
            self.player.rect.centerx - self.rect.centerx,
            self.player.rect.centery - self.rect.centery
        )

        if axis.length() != 0:
            axis = axis.normalize()

        return axis
    

    def detection(self):
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        distance_sq = dx ** 2 + dy ** 2

        if distance_sq < self.detection_radius**2:
            self.velocity = Vector2(0,0)
        else:
            self.velocity = self.get_axis() * self.speed
        

    def update(self, static_objects):
        self.detection()

        self.velocity = self.get_axis()
        self.moving(static_objects)

enemy = Enemy(200, 100, ENEMY_IMG, 2, 'Ciclope')