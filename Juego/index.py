import pygame
import sys
from objetos import * 
from levles import *
from objetos_juego.player import * 
# --- Funciones ---
def ready():
    pass

def process():
    pass

def dibujar(window):
    for static in grupo_static:
        static.reset(window)


def make_map():
    for y, fila in enumerate(tilemap_1):
        for x, col in enumerate(fila):
            if col == '1':
                pared = ObjetStatic(x*TILE_SIZE, 
                                    y*TILE_SIZE, 
                                    'TileMap/tile_0000.png')
                grupo_static.add(pared)





# --- Configuración ---
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (20, 20, 20)
TITLE = "Pantalla base"

# --- Inicialización ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

grupo_static = sprite.Group()
make_map()


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
