__author__ = 'Alex Owens'

# Levels are essentially just two-dimensional arrays of integers.
# They will have clearly defined width and height. 0 will represent an
# empty space in the level, whereas non-zero integers will represent something else
# 1 being a basic wall.

import pygame

SPACE_BETWEEN_BLOCKS = 2


class Level:
    def __init__(self, width=32, height=32):
        self.width_in_blocks = width
        self.height_in_blocks = height
        self.level_structure = self.init_level_structure()

    def init_level_structure(self):
        return [[Block(x=x, y=y) for x in range(0, self.width_in_blocks - 1)] for y in range(0, self.height_in_blocks - 1)]

    def render_level(self, surface):
        for row in self.level_structure:
            for block in row:
                block.render_block(surface)


class Block:
    def __init__(self, side_length=16, x=0, y=0):
        self.position = (x * side_length, y * side_length)
        self.side_length = side_length
        self.rect = pygame.Rect((self.position), (side_length, side_length))
        self.filled = False

    def fill_block(self):
        self.filled = True

    def render_block(self, surface):
        draw_color = (0, 0, 0) if self.filled == False else (255, 255, 255)
        pygame.draw.rect(surface, draw_color, self.rect)
