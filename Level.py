__author__ = 'Alex Owens'

import pygame


class Level:
    """ The Level class is a structure that holds a 2D array of Block objects (defined below),
        levels will hold functionality to manipulate individual blocks in the array, as well as
        rendering all the blocks at a time. Levels are also exportable to an integer array which
        will be written to a text file.
    """

    def __init__(self, width=32, height=32):
        self.width_in_blocks = width
        self.height_in_blocks = height
        self.level_structure = self.init_level_structure()

    # Creates a 2D array of blocks using list comprehension
    def init_level_structure(self):
        return [[Block(x=x, y=y) for x in range(self.width_in_blocks)] for y in range(self.height_in_blocks)]

    # Renders each block in the level_structure
    def render_level(self, surface):
        for row in self.level_structure:
            for block in row:
                block.render_block(surface)

    def fill_block(self, position):
        return self.change_block(position, True)

    def empty_block(self, position):
        return self.change_block(position, False)

    # Change block looks up a block's position and fills or empties
    def change_block(self, position, fill):
        x = position[0]
        y = position[1]
        for row in self.level_structure:
            for block in row:
                if block.contains_point(x, y):
                    block.fill_block() if fill else block.empty_block()
                    return True
        return False

    # Exports the levels as a text file using 1 to represent a filled block, 0 to represent empty
    def export_as_txt_file(self, name):
        integer_level = self.get_integer_level_representation()
        with open('{}'.format(name), 'w') as file:
            for row in integer_level:
                for col in row:
                    file.write(str(col) + ' ')
                file.write('\n')

    def get_integer_level_representation(self):
        txt_level = [[0 for x in range(self.width_in_blocks)] for y in range(self.height_in_blocks)]
        for x, row in enumerate(self.level_structure):
            for y, block in enumerate(row):
                txt_level[x][y] = 1 if block.filled else 0
        return txt_level


# Constants for rendering blocks
BLOCK_SIDE_LENGTH = 16
SPACE_BETWEEN_BLOCKS = 2


class Block:
    """ The Block class is a very primitive structure that represents one grid space in a level.
        The purpose of having a structure to hold each block is that it simplifies rendering, manipulation, and
        it can be extended pretty easily.
    """

    def __init__(self, x=0, y=0):
        self.position = (x * BLOCK_SIDE_LENGTH, y * BLOCK_SIDE_LENGTH)
        self.side_length = BLOCK_SIDE_LENGTH
        self.rect = pygame.Rect(self.position,
                                (BLOCK_SIDE_LENGTH-SPACE_BETWEEN_BLOCKS, BLOCK_SIDE_LENGTH-SPACE_BETWEEN_BLOCKS))
        self.filled = False

    def fill_block(self):
        self.filled = True

    def empty_block(self):
        self.filled = False

    def render_block(self, surface):
        draw_color = (255, 0, 0) if self.filled else (0, 0, 0)
        pygame.draw.rect(surface, draw_color, self.rect)

    # Checks if the mouse pointer (x,y) is inside the block's rect
    def contains_point(self, x, y):
        return True if x >= self.rect.x and x < self.rect.x + self.rect.width and \
                       y >= self.rect.y and y < self.rect.y + self.rect.height else False
