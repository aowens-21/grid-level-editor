__author__ = 'Alex Owens'

# Levels are essentially just two-dimensional arrays of integers.
# They will have clearly defined width and height. 0 will represent an
# empty space in the level, whereas non-zero integers will represent something else
# 1 being a basic wall.


class Level:
    def __init__(self, width=32, height = 32):
        self.width = width
        self.height = height
        self.level_structure = self.init_level_structure()

    # Simply creates an empty level with given width and height
    def init_level_structure(self):
        return [[0 for x in range(self.width)] for y in range(self.height)]