import pygame
import sys
from pygame import sprite
from objetos import *
from levles import *
from objetos_juego.player import *

# --- Funciones ---

def process():
    player.update(walls)

def dibujar(window):
    #colsiones de paredes
    for static in walls:
        static.reset(window)
    
    #solo piso no colisiona
    for static in floor:
        static.reset(window)
    
    player.reset(window)

# --- create maps ---
def make_map_colision(tile_map):
    walls = sprite.Group()

    for y, fila in enumerate(tile_map):
        for x, col in enumerate(fila):
            if col == '1':
                walls.add(
                    ObjetStatic(
                    x * TILE_SIZE,
                    y * TILE_SIZE,
                    TILE_WALL_IMG
                ))
                
    return walls

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


# --- render image ---
TILE_WALL_IMG = pygame.transform.scale(
pygame.image.load('TileMap/tile_0000.png'),
(TILE_SIZE, TILE_SIZE)
)

TILE_FLOOR_IMG = pygame.transform.scale(
    pygame.image.load('TileMap/tile_0049.png'),
    (TILE_SIZE, TILE_SIZE)
)

PLAYER_IMG = pygame.transform.scale(
    pygame.image.load('Player animations/tile_0085.png'),
    (TILE_SIZE, TILE_SIZE)
)

# --- Ready ---
walls = make_map_colision(tilemap_1)
floor = make_map_layers(tilemap_1)
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
