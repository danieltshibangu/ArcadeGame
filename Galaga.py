"""
Starting Template
"""

import arcade
import player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "GALAGA!"

class MyGame( arcade.Window ):
    """
    Main application class
    """
    def __init__( self, width, height, title ):
        super().__init__(width, height, title )

        arcade.set_background_color( arcade.color.AMAZON )

        # sprite lists should be created here and
        # set to None

    def setup(self):
        #create your sprites and sprite lists here
        pass

    def on_draw( self ):
        """
        render the screen.
        """

        # This command should be open before drawing.
        # it will clear the screen to bg color, and erase
        # last drawn
        arcade.start_render()

        # call draw() on all sprite lists below

    def on_update( self, delta_time):
        """
        All the logic to move, and the game logic goes here
        Normally, you'll call update() on the sprite lists
        that need it.
        """
        pass

    def on_key_press( self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed
        """

    def on_key_release( self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
