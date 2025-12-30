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
    chest.update(player)

def dibujar(window):
    #colsiones de paredes
    for static in walls:
        static.reset(window, True)
    
    #solo piso no colisiona
    for static in floor:
        static.reset(window, True)
    chest.reset(window, False)
    player.reset(window, True)



def make_map_layers(tile_map):
    floor = sprite.Group()

    for y, fila in enumerate(tile_map):
        for x, col in enumerate(fila):
            if col == '0':
                floor.add(
                    ObjetStatic(
                    x * TILE_SIZE,
                    y * TILE_SIZE,
                    TILE_FLOOR_IMG
                ))
                
    return floor


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
walls = make_map_colision(tilemap_1)
floor = make_map_layers(tilemap_1)
player = Player(100, 100, PLAYER_IMG, 4)
chest = Chest(200, 300, CHEST_IMG)

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
