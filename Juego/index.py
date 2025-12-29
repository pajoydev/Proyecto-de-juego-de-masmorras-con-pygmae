import pygame
import sys
from objetos import * 
from levles import * 
# --- Funciones ---
def process():
    keys = key.get_pressed()
    axis = Vector2()
    axis.x = int(keys[K_RIGHT]) - int(keys[K_LEFT])
    axis.y = int(keys[K_DOWN]) - int(keys[K_UP])
    
    #codigo player
    player.moving()
    player.velocity.x = axis.x
    player.velocity.y = axis.y

def dibujar():
    player.reset(screen)


def make_map():
    for fila in enumerate(tilemap_1):
        for col in enumerate(fila):
            x = col * TILE_SIZE
            y = fila * TILE_SIZE




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
player = ObjetMoving(100,100, 'Player animations/tile_0085.png')
pared = ObjetStatic(100,100,'TileMap/tile_0000.png')


# --- Bucle principal ---
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    process()
    screen.fill(BG_COLOR)
    dibujar()
    pygame.display.flip()

pygame.quit()
sys.exit()
