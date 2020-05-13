import arcade
from GameView import GameView
import os

WIDTH = 800
HEIGHT = 600

class MenuView( arcade.View ):
    # this is the starting color when the screen shows
    def on_show(self):
        arcade.set_background_color( arcade.color.WHITE )

    # displays menu text and color 
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text( "GALAGA - click to advance", WIDTH/2,
                          HEIGHT/2, arcade.color.BLACK, font_size=30,
                          anchor_x="center" )

    def on_key_press( self, key, key_modifiers ):
        game_view = GameView()
        game_view.setup()
        self.window.show_view( game_view )

def main():
    """ Main method """
     window = arcade.Window( WIDTH, HEIGHT, "INTRO" )
    menu_view = MenuView()
    window.show_view( menu_view )
    arcade.run()

if __name__ == "__main__":
    main()
