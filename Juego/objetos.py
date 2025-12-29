from pygame import *

TILE_SIZE = 32

class ObjetMoving(sprite.Sprite):
    def __init__(self, x, y, imagee, speed):
        super().__init__()

        self.speed = speed
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

    def moving(self, static_objects):
        self.rect.x += self.velocity.x * self.speed
        for obj in static_objects:
            if self.rect.colliderect(obj.rect):
                if self.velocity.x > 0:  # derecha
                    self.rect.right = obj.rect.left
                if self.velocity.x < 0:  # izquierda
                    self.rect.left = obj.rect.right
        self.rect.y += self.velocity.y * self.speed
        for obj in static_objects:
            if self.rect.colliderect(obj.rect):
                if self.velocity.y > 0:  # abajo
                    self.rect.bottom = obj.rect.top
                if self.velocity.y < 0:  # arriba
                    self.rect.top = obj.rect.bottom

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
