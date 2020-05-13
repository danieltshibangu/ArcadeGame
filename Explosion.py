import arcade

class Explosion( arcade.Sprite ):
    ''' this class creates an explosion animation'''

    def __init__( self, texture_list ):
        super().__init__()

        # start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update( self ):
        # Update to the next frame of the animation.
        # If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1

        # if the current frame number is less than the total
        # number of frames the animation is supposed to show
        # set the total frame number to the current one
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            # otherwise delete it ?
            self.remove_from_sprite_lists()

