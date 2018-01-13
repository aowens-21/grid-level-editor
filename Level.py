__author__ = 'Alex Owens'

# Levels are a 2D array of Block objects, these blocks are pretty primitive, but the point
# of having a specified object to represent a grid space is we could later specify type of
# space or something: it's extendable. The blocks also make it easier to set up because they have
# their own render function, which means we can render some differently.

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

    def fill_block(self, position):
        x = position[0]
        y = position[1]
        for row in self.level_structure:
            for block in row:
                if block.contains_point(x, y):
                    block.fill_block()
                    return True
        return False

    def empty_block(self, position):
        x = position[0]
        y = position[1]
        for row in self.level_structure:
            for block in row:
                if block.contains_point(x, y):
                    block.empty_block()
                    return True
        return False



class Block:
    def __init__(self, side_length=16, x=0, y=0):
        self.position = (x * side_length, y * side_length)
        self.side_length = side_length
        self.rect = pygame.Rect((self.position), (side_length-SPACE_BETWEEN_BLOCKS, side_length-SPACE_BETWEEN_BLOCKS))
        self.filled = False

    def fill_block(self):
        self.filled = True

    def empty_block(self):
        self.filled = False

    def render_block(self, surface):
        draw_color = (0, 0, 0) if self.filled == False else (255, 255, 255)
        pygame.draw.rect(surface, draw_color, self.rect)

    def contains_point(self, x, y):
        if x >= self.rect.x and x < self.rect.x + self.rect.width and y >= self.rect.y and y < self.rect.y + self.rect.height:
            return True
        else:
            return False

