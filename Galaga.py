import arcade
import player
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "GALAGA!"

# defines size of the model
SPRITE_SCALING = 0.5

# defines speed of sprite movement
MOVEMENT_SPEED = 10

# this deals with shooting
SPRITE_SCALING_LASER = 0.8
BULLET_SPEED = 10

class MyGame( arcade.Window ):
    """
    Main application class
    """
    def __init__( self, width, height, title ):
        super().__init__(width, height, title )
        
        # variables that will hold sprite lists
        self.player_list = None
        self.bullet_list = None

        # set up the player info
        self.player_sprite = None
    

        # track the state of which key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        #add gun sounds here
        """
        self.gun_sound = arcade.load_sound( "some resource" )
        self.hit_sound = arcade.load_sound( "some resource" )
        """
        
        # sets the background color
        arcade.set_background_color( arcade.color.AMAZON )
      
    def setup(self):
        #create your sprites and sprite lists here
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player

        self.player_sprite = Player(":resources:images/space_shooter/playerShip1_orange.png" )
        # this is the starting position of the player
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50

        # the sprite is then appended to a list of all players
        self.player_list.append( self.player_sprite )

    def on_draw( self ):
        """
        render the screen.
        """

        # This command should be open before drawing.
        # it will clear the screen to bg color, and erase
        # last drawn. It also gives permission for other things
        # to be drawn 
        arcade.start_render()

         # call draw() on all sprite lists below
        self.player_list.draw()
        self.bullet_list.draw()

    def on_update( self, delta_time):
        """
        All the logic to move, and the game logic goes here
        Normally, you'll call update() on the sprite lists
        that need it.
        """
        # calculate speed based on keys pressed
        # initiates change in sprite position to 0
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        # these are how far we move if pressed in a direction
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        # call update to move the sprite
        self.player_list.update()

        # call update on bullet sprites
        self.bullet_list.update()

        # loop through each bullet
        for bullet in self.bullet_list:

            #Check this bullet to see if it hit something
            """
            hit_list = arcade.check_for_collision_with_list( bullet, self.a_list )
            """

            # if the bullet flies of the screen it must be removed
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

    def on_key_press( self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed
        """
        
        # when a key is pressed, the movement is registered as True
        # and position gets updated
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        # if the key pressed is the spacebar, the player shoots up
        if key == arcade.key.SPACE:
            
            bullet = arcade.Sprite( ":resources:images/space_shooter/laserBlue01.png",
                                     SPRITE_SCALING_LASER )

            # changing the bullet angle to start at 90, upwards
            bullet.angle = 90

            # the change in y is equal to the bullet speed set
            bullet.change_y = BULLET_SPEED

            # position of the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top

            # add the bullet to it's list once more
            self.bullet_list.append(bullet)

    def on_key_release( self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

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
