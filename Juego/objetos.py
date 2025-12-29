from pygame import *

TILE_SIZE = 32

class ObjetMoving(sprite.Sprite):
    def __init__(self, x, y, imagee):
        super().__init__()

        self.speed = 4
        self.velocity = Vector2()

        # Imagen (sprite)
        self.image = transform.scale(
            image.load(imagee),
            (TILE_SIZE, TILE_SIZE)
        )

        # Hitbox más pequeña
        self.rect = Rect(
            x + 5,
            y + 5,
            TILE_SIZE - 10,
            TILE_SIZE - 10
        )

    def moving(self):
        self.rect.x += self.velocity.x * self.speed
        self.rect.y += self.velocity.y * self.speed

    def reset(self, window):

        # Centrar sprite sobre la hitbox
        sprite_pos = (
            self.rect.centerx - TILE_SIZE // 2,
            self.rect.centery - TILE_SIZE // 2
        )
        window.blit(self.image, sprite_pos)
        # Dibuja hitbox (solo para debug)
        draw.rect(window, (255, 0, 0), self.rect, 1)


class ObjetStatic(sprite.Sprite):
    def __init__(self, x, y, imagee):
        super().__init__()

        # Imagen (sprite)
        self.image = transform.scale(
            image.load(imagee),
            (TILE_SIZE, TILE_SIZE)
        )

        # Hitbox más pequeña
        self.rect = Rect(
            x,
            y,
            TILE_SIZE,
            TILE_SIZE
        )

    def reset(self, window):

        # Centrar sprite sobre la hitbox
        sprite_pos = (
            self.rect.centerx - TILE_SIZE // 2,
            self.rect.centery - TILE_SIZE // 2
        )
        window.blit(self.image, sprite_pos)
        # Dibuja hitbox (solo para debug)
        draw.rect(window, (255, 0, 0), self.rect, 1)
