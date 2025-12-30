import pygame
from objetos import TILE_SIZE

# --- render image ---

TILE_BORDERS_y_IMAGE_1 = pygame.transform.scale(
pygame.image.load('TileMap/tile_0002.png'),
(TILE_SIZE, TILE_SIZE)
)

TILE_BORDERS_y_IMAGE_2 = pygame.transform.scale(
pygame.image.load('TileMap/tile_0026.png'),
(TILE_SIZE, TILE_SIZE)
)

TILE_BORDERS_x_IMAGE_1 = pygame.transform.scale(
pygame.image.load('TileMap/tile_0015.png'),
(TILE_SIZE, TILE_SIZE)
)

TILE_BORDERS_x_IMAGE_2 = pygame.transform.scale(
pygame.image.load('TileMap/tile_0013.png'),
(TILE_SIZE, TILE_SIZE)
)

TILE_CORNERS_IMAGE_1 = pygame.transform.scale(
pygame.image.load('TileMap/tile_0004.png'),
(TILE_SIZE, TILE_SIZE)
)

TILE_CORNERS_IMAGE_2 = pygame.transform.scale(
pygame.image.load('TileMap/tile_0005.png'),
(TILE_SIZE, TILE_SIZE)
)

TILE_CORNERS_IMAGE_3 = pygame.transform.scale(
pygame.image.load('TileMap/tile_0016.png'),
(TILE_SIZE, TILE_SIZE)
)

TILE_CORNERS_IMAGE_4 = pygame.transform.scale(
pygame.image.load('TileMap/tile_0017.png'),
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

CHEST_IMG = pygame.transform.scale(
    pygame.image.load('Objetos animations/tile_0089.png'),
    (TILE_SIZE, TILE_SIZE)
)