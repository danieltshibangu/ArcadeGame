"""
This is the class for created player sprites
"""

import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

class Player( arcade.Sprite ):
    """ Player class """

   def update(self):
        # the center changes based on displacement by x or y
        self.center_x += self.change_x
        self.center_y += self.change_y

        # these are used to avoid if the sprite moves too far
        # in either the right or left
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        # these are used to avoid if the sprite moves too far
        # in either the top or bottom
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1
