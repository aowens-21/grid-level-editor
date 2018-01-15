__author__ = 'Alex Owens'


import pygame

GRID_SIZE = 16
# Pygame uses numeric codes for mouse buttons, so these constants represent the codes
MOUSE_LEFT = 1
MOUSE_RIGHT = 3


""" Editor class will do most of the event handling for level manipulation,
    and it will also provide a separate surface on which to render the level.
"""
class Editor:
    def __init__(self, edited_level, draw_pos=(0, 0)):
        self.edited_level = edited_level
        self.draw_pos = draw_pos
        self.editor_surface = self.init_editor_surface()

    # Takes in an event from the main loop and processes it
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if event.button == MOUSE_LEFT:
                # Offset with draw position so the click position is relative to the editor surface
                self.edited_level.fill_block((mouse_pos[0] - self.draw_pos[0], mouse_pos[1] - self.draw_pos[1]))
            elif event.button == MOUSE_RIGHT:
                self.edited_level.empty_block((mouse_pos[0] - self.draw_pos[0], mouse_pos[1] - self.draw_pos[1]))

    # Initializes editor surface property and its values
    def init_editor_surface(self):
        surface_width = self.edited_level.width_in_blocks * GRID_SIZE + 1
        surface_height = self.edited_level.height_in_blocks * GRID_SIZE + 1
        surface = pygame.Surface((surface_width, surface_height))
        surface = surface.convert()
        surface.fill((255, 255, 255))
        return surface

    def render(self):
        self.edited_level.render_level(self.editor_surface)

    def save_level(self, name):
        self.edited_level.export_as_txt_file(name)

    # Draw position is simply where the editor surface is drawn in the main surface
    def set_draw_pos(self, x, y):
        self.draw_pos = (x, y)

    def get_draw_pos(self):
        return self.draw_pos
