__author__ = 'Alex Owens'

def setup_level_size():
    width = int(input('Please enter the width of the level(in 16px grid spaces, 32 is a good option): '))
    height = int(input('Please enter the height of the level(in 16px grid spaces, 32 is a good option: '))
    return (width, height)

def setup_level_name():
    name = input('Please enter the name of your level: ')
    return name.strip() + '.txt'
