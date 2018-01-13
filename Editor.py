__author__ = 'Alex Owens'

# The editor will essentially be where all level manipulation occurs,
# it handles addition of new walls and deleting of walls and things like that.

import pygame, sys

class Editor:
    def __init__(self, edited_level, grid_size=16):
        self.edited_level = edited_level
        self.GRID_SIZE = grid_size
        self.editor_surface = self.init_editor_surface()
        self.edited_level.render_level(self.editor_surface)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

    def init_editor_surface(self):
        surface_width = self.edited_level.width_in_blocks * self.GRID_SIZE + 1
        surface_height = self.edited_level.height_in_blocks * self.GRID_SIZE + 1
        surface = pygame.Surface((surface_width, surface_height))
        surface = surface.convert()
        surface.fill((255, 255, 255))
        return surface





