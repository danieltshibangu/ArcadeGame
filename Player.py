"""
This is the class for the sprite class
"""

import arcade
import os
import math

# the size of the sprite
SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5
ANGLE_SPEED = 5

class Player( arcade.Sprite ):
    """ Player class """

    def __init__( self, image, scale ):
        """ set up the player """

        # Call the parent init
        super().__init__(image, scale )

        # create a variable to hold our speed+
        self.speed = 0

    def update(self):
        #convert angle in degrees to radians
        angle_rad = math.radians(self.angle)

        #rotate the ship
        self.angle += self.change_angle

        # use math to find our change based on speed and angle
        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += slef.speed * math.cos(angle_rad )
