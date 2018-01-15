__author__ = 'Alex Owens'

# Main handles initialization and our main "game" loop for input and rendering

import pygame
import Level
import Editor
import sys


def main():
    level_width, level_height = setup_level_size()
    level_name = setup_level_name()

    pygame.init()
    editor_screen = pygame.display.set_mode((1024, 800), pygame.RESIZABLE)
    pygame.display.set_caption('Grid Level Editor')

    background = pygame.Surface(editor_screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    level = Level.Level(width=level_width, height=level_height)
    level_editor = Editor.Editor(level)
    level_editor.set_draw_pos(background.get_width() / 2 - level_editor.editor_surface.get_width() / 2,
                              background.get_height() / 2 - level_editor.editor_surface.get_height() / 2)

    background.blit(level_editor.editor_surface, level_editor.get_draw_pos())
    editor_screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                # TODO: Refactor into function
                editor_screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                background = pygame.Surface(editor_screen.get_size())
                background = background.convert()
                background.fill((255, 255, 255))
                level_editor.set_draw_pos(background.get_width() / 2 - level_editor.editor_surface.get_width() / 2,
                                          background.get_height() / 2 - level_editor.editor_surface.get_height() / 2)
            elif event.type == pygame.QUIT:
                level_editor.save_level(level_name)
                sys.exit()
            else:
                level_editor.handle_event(event)

        level_editor.render()

        background.blit(level_editor.editor_surface, level_editor.get_draw_pos())

        editor_screen.blit(background, (0, 0))
        pygame.display.flip()


def setup_level_size():
    width = int(input('Please enter the width of the level(in 16px grid spaces, 32 is a good option): '))
    height = int(input('Please enter the height of the level(in 16px grid spaces, 32 is a good option: '))
    return width, height


def setup_level_name():
    name = input('Please enter the name of your level: ')
    return name.strip() + '.txt'


main()
