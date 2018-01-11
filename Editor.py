__author__ = 'Alex Owens'

# The editor will essentially be where all level manipulation occurs,
# it handles addition of new walls and deleting of walls and things like that.


class Editor:
    def __init__(self, edited_level):
        self.edited_level = edited_level