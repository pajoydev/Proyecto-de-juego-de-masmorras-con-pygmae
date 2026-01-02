from scripts.objetos import *
from scripts.render_image import *
from scripts.objetos_juego.cofre import *


def make_map_colision(tile_map):
    walls = sprite.Group()
    for y, fila in enumerate(tile_map):
        for x, col in enumerate(fila):
            if col == '1':
                walls.add(
                    ObjetStatic(
                    x * TILE_SIZE,
                    y * TILE_SIZE,
                    TILE_CORNERS_IMAGE_1
                ))
            
            if col == '2':
                walls.add(
                    ObjetStatic(
                        x * TILE_SIZE,
                        y * TILE_SIZE,
                        TILE_CORNERS_IMAGE_2
                    ))
            
            if col == '3':
                walls.add(
                    ObjetStatic(
                    x * TILE_SIZE,
                    y * TILE_SIZE,
                    TILE_CORNERS_IMAGE_3
                ))
            
            if col == '4':
                walls.add(
                    ObjetStatic(
                        x * TILE_SIZE,
                        y * TILE_SIZE,
                        TILE_CORNERS_IMAGE_4
                    ))
            
            if col == '5':
                walls.add(
                    ObjetStatic(
                    x * TILE_SIZE,
                    y * TILE_SIZE,
                    TILE_BORDERS_x_IMAGE_1
                ))
            
            if col == '6':
                walls.add(
                    ObjetStatic(
                        x * TILE_SIZE,
                        y * TILE_SIZE,
                        TILE_BORDERS_x_IMAGE_2
                    ))
            
            if col == '7':
                walls.add(
                    ObjetStatic(
                    x * TILE_SIZE,
                    y * TILE_SIZE,
                    TILE_BORDERS_y_IMAGE_1
                ))
            
            if col == '8':
                walls.add(
                    ObjetStatic(
                        x * TILE_SIZE,
                        y * TILE_SIZE,
                        TILE_BORDERS_y_IMAGE_2
                    ))
    return walls


def make_map_layers(tile_map):
    layers = sprite.Group()
    for y, fila in enumerate(tile_map):
        for x, col in enumerate(fila):
            if col == '0':
                layers.add(
                    ObjetStatic(
                    x * TILE_SIZE,
                    y * TILE_SIZE,
                    TILE_FLOOR_IMG
                ))
                
            if col == '1':
                layers.add(
                    ObjetStatic(
                    x * TILE_SIZE,
                    y * TILE_SIZE,
                    TILE_FOND_IMG,
                ))
                
    return layers

def make_map_objets(tilemap):
    objets = sprite.Group()
    for y, fila in enumerate(tilemap):
        for x, col in enumerate(fila):
            if col == '1':
                objets.add(
                    Chest(
                        x * TILE_SIZE,
                        y * TILE_SIZE,
                        CHEST_IMG,
                    )
                )
    return objets

