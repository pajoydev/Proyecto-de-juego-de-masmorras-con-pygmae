from objetos import * 


class Chest(ObjetcCollectable):
    def __init__(self, x, y, imagee):
        super().__init__(x, y, imagee)
    
    def colision_(self, objt):
        if self.rect.colliderect(objt.rect):
            print("Wiinnnnnnn")
    
    def update(self, player):
        self.colision_(player)