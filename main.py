__author__ = 'Alex Owens'

# Main handles initialization and our main "game" loop for input and rendering

import pygame
import Level, Editor


def main():
    pygame.init()
    editor_screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Grid Level Editor')

    background = pygame.Surface(editor_screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    level = Level.Level(width=16, height=8)
    level_editor = Editor.Editor(level)
    level_editor.set_draw_pos(background.get_width() / 2 - level_editor.editor_surface.get_width() / 2, background.get_height() / 2 - level_editor.editor_surface.get_height() / 2)

    background.blit(level_editor.editor_surface, level_editor.get_draw_pos())
    editor_screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            level_editor.handle_event(event)

        level_editor.render()

        background.blit(level_editor.editor_surface, level_editor.get_draw_pos())

        editor_screen.blit(background, (0, 0))
        pygame.display.flip()


main()