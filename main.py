__author__ = 'Alex Owens'

import Level
import Editor
import sys
from setup import *


def main():
    """ Our main function is going to do lots of setup from the setup module,
        it will setup the level size and name, then pygame display information,
        then it will draw everything to the screen and start the "game" loop.
    """

    level_width, level_height = setup_level_size()
    level_name = setup_level_name()

    editor_screen = setup_pygame_display()

    background = setup_background(editor_screen.get_size())

    level = Level.Level(width=level_width, height=level_height)
    level_editor = Editor.Editor(level)

    # Editor draw position will be the center of the screen
    level_editor.set_draw_pos(background.get_width()/2 - level_editor.editor_surface.get_width()/2,
                              background.get_height()/2 - level_editor.editor_surface.get_height()/2)

    background.blit(level_editor.editor_surface, level_editor.get_draw_pos())
    editor_screen.blit(background, (0, 0))

    # Main "game" loop, it handles input and renders the editor(as well as any changes that occur)
    while level_editor.running:
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                editor_screen = setup_pygame_display(event.dict['size'])
                background = setup_background(editor_screen.get_size())
                level_editor.set_draw_pos(background.get_width()/2 - level_editor.editor_surface.get_width()/2,
                                          background.get_height()/2 - level_editor.editor_surface.get_height()/2)
            elif event.type == pygame.QUIT:
                level_editor.save_level(level_name)
                level_editor.close()
            else:
                level_editor.handle_event(event)

        level_editor.render()

        background.blit(level_editor.editor_surface, level_editor.get_draw_pos())

        editor_screen.blit(background, (0, 0))
        pygame.display.flip()

    # Exit when we leave the main loop
    sys.exit()


main()
