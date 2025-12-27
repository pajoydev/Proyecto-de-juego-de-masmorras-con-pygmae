from pygame import *

class OnjetsMoving(sprite.Sprite):
    def __init__(self, image):
        sprite.Sprite.__init__(self)
        self.hitbox = Rect(
            self.rect.x + 4,
            self.rect.y + 4,
            self.rect.whidth - 8,
            self.rect.height - 8
        )
    
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))