__author__ = 'Alex Owens'

# Main handles initialization and our main "game" loop for input and rendering

import pygame
from pygame.locals import *


def main():
    pygame.init()
    editor_screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Grid Level Editor')

