import random
import arcade
import os

# ------ constants----
SPRITE_SPEED = 10

class Enemy( arcade.Sprite ):

    '''
    This function will move the current spites in
    different directions.
    '''

    def update( self ):
        # the center changes based on displacement by x or y
        self.center_x -= 15

        
    
