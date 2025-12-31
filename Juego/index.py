import pygame
import sys
from pygame import sprite
from objetos import *
from levles import *
from objetos_juego.player import *
from create_levles import *
from objetos_juego.cofre import *

# --- Funciones ---

def process():
    player.update(walls)

    for objt in objets:
        objt.update(player)

def dibujar(window):
    
    
    #solo piso no colisiona
    for static in floor:
        static.reset(window, False)
    
    #colsiones de paredes
    for static in walls:
        static.reset(window, False)
    
    for objt in objets:
        objt.reset(window, True)
    
    player.reset(window, False)







# --- Configuración ---
WIDTH, HEIGHT = 640, 384
FPS = 60
BG_COLOR = (20, 20, 20)
TITLE = "Pantalla base"

# --- Inicialización ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()




# --- Ready ---
print("")
walls = make_map_colision(tilemap_1_colision)
floor = make_map_layers(tilemap_1_layers)
objets = make_map_objets(tilemap_1_objets)
player = Player(100, 100, PLAYER_IMG, 4)

# --- Bucle principal ---
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    process()
    screen.fill(BG_COLOR)
    dibujar(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
