import pygame
import sys

# --- Funciones ---
def process():
    pass

def dibujar():
    pass

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
