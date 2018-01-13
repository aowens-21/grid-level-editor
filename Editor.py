__author__ = 'Alex Owens'

# The editor will essentially be where all level manipulation occurs,
# it handles addition of new walls and deleting of walls and things like that.

import pygame, sys

class Editor:
    def __init__(self, edited_level, draw_pos=(0, 0), grid_size=16):
        self.edited_level = edited_level
        self.GRID_SIZE = grid_size
        self.draw_pos = draw_pos
        self.editor_surface = self.init_editor_surface()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if event.button == 1:
                # Offset with draw position so the click position is relative to the editor surface
                self.edited_level.fill_block((mouse_pos[0] - self.draw_pos[0], mouse_pos[1] - self.draw_pos[1]))
            elif event.button == 3:
                self.edited_level.empty_block((mouse_pos[0] - self.draw_pos[0], mouse_pos[1] - self.draw_pos[1]))

    def init_editor_surface(self):
        surface_width = self.edited_level.width_in_blocks * self.GRID_SIZE + 1
        surface_height = self.edited_level.height_in_blocks * self.GRID_SIZE + 1
        surface = pygame.Surface((surface_width, surface_height))
        surface = surface.convert()
        surface.fill((255, 255, 255))
        return surface

    def render(self):
        self.edited_level.render_level(self.editor_surface)

    def set_draw_pos(self, x, y):
        self.draw_pos = (x, y)

    def get_draw_pos(self):
        return self.draw_pos





