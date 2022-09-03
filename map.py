import pygame
from tilecreater import Tile
import csv
from collectible import Flask

tile_map = open("tiled.csv")
file_reader = csv.reader(tile_map)
tile_data = list(file_reader)
print(tile_data)
tile_size = 70


class Level:
    def __init__(self, level_data, surface):
        self.tiles = pygame.sprite.Group()
        self.flasks = pygame.sprite.Group()
        self.surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size + 225

                if cell == 'C':
                    flask = Flask(x, y, self.surface)
                    self.flasks.add(flask)

                if cell != "C":
                    if cell != "-1":
                        tile_type = cell
                        tile = Tile((x, y), tile_size, tile_type)
                        self.tiles.add(tile)

    def __iter__(self):
        return iter(self.tiles)

    def scroll(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.world_shift = 2
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and self.collision != "side":
            self.world_shift = -10
        else:
            self.world_shift = 0

    def run(self, collision):
        self.collision = collision
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.surface)
        self.flasks.update(0.25, self.world_shift)
        self.flasks.draw(self.surface)
        self.scroll()
