__author__ = 'Alex Owens'

import pygame

START_SCREEN_SIZE = (800, 600)
BG_COLOR = (255, 255, 255)


def setup_pygame_display(display_size=START_SCREEN_SIZE):
    """ Initializes pygame, sets caption, and returns display of passed(or default) size."""

    pygame.init()
    pygame.display.set_caption('Level Editor')
    return pygame.display.set_mode(display_size, pygame.RESIZABLE)


def setup_background(game_surface_size):
    """ Sets up the background surface to render on, is the size of the game_surface."""

    background = pygame.Surface(game_surface_size)
    background = background.convert()
    background.fill(BG_COLOR)
    return background


def setup_level_size():
    """ Gets input from the user and uses that to return the level width and height in a tuple."""

    width = int(input('Please enter the width of the level(in 16px grid spaces, 32 is a good option): '))
    height = int(input('Please enter the height of the level(in 16px grid spaces, 32 is a good option: '))
    return width, height


def setup_level_name():
    """ Gets level name from user and returns 'name'.txt."""

    name = input('Please enter the name of your level: ')
    return name.strip() + '.txt'
