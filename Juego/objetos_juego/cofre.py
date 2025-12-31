from objetos import * 
import pygame 


class Chest(ObjetcCollectable):
    def __init__(self, x, y, imagee):
        super().__init__(x, y, imagee)
    
    def colision_(self, objt):
        teclas = pygame.key.get_pressed()
        if self.rect.colliderect(objt.rect):
            if teclas[K_x]:

                print("Wiinnnnnnn")
    
    def update(self, player):
        self.colision_(player)