import pygame
from graphics import Tile
import csv

tile_map = open("tiled.csv")
file_reader = csv.reader(tile_map)
tile_data = list(file_reader)
print(tile_data)
tile_size = 60


class Level:
    def __init__(self, level_data, surface):
        self.tiles = pygame.sprite.Group()
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size + 225

                if cell != "-1":
                    tile_type = cell
                    tile = Tile((x, y), tile_size, tile_type)
                    self.tiles.add(tile)

    def __iter__(self):
        return iter(self.tiles)

    def takein(self, collided):
        self.collided = collided

    def scroll(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.world_shift = 2
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.world_shift = -10
        else:
            self.world_shift = 0

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll()
        print(self.tiles)

