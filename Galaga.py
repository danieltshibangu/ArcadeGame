import arcade
from player import Player
from Explosion import Explosion
import os
from arcade.draw_commands import Texture

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "GALAGA!"

# defines size of the model
SPRITE_SCALING = 0.5

# defines speed of sprite movement
MOVEMENT_SPEED = 10

# this deals with shooting
SPRITE_SCALING_LASER = 0.8
BULLET_SPEED = 10

# gives explosion a texture count
EXPLOSION_TEXTURE_COUNT = 60

class MyGame( arcade.Window ):
    """
    Main application class
    """
    def __init__( self, width, height, title ):
        super().__init__(width, height, title )
        
        # initiate the frame count here
        self.frame_count = 0
        
        # variables that will hold sprite lists
        self.player_list = None
        self.bullet_list = None
        self.enemy_list = None
        self.explosions_list = None

        # set up the player info
        self.player_sprite = None
        self.score = 0
    

        # track the state of which key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        # preload the animation frames
        self.explosion_texture_list = []

        columns = 16
        count = 60
        sprite_width = 256
        sprite_height = 256
        file_name = ":resources:images/spritesheets/explosion.png"

        # load explosions from a sprite sheet
        self.explosion_texture_list = arcade.load_spritesheet( file_name,
                                      sprite_width, sprite_height,
                                      columns, count)

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
        self.enemy_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList() 

        # Set up the player
        self.score = 0
        self.player_sprite = Player( r"C:\Users\Daniel Tshibangu\Desktop\galaga\Resources\airship.png" )
        # this is the starting position of the player
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
                                    
        # updated dimensions of sprite
        self.player_sprite.height = 200
        self.player_sprite.width = 200

        # this controls the dimensions of the hit_box
                                        # LOWER L   LOWER R    UPPER R   UPPER L
        self.player_sprite.set_hit_box([[-60, -50], [38, -50], [38, 38], [-60, 38]])

        # the sprite is then appended to a list of all players
        self.player_list.append( self.player_sprite )
        
        # SET UP THE ENEMIES
        enemy = arcade.Sprite( r"C:\Users\Daniel Tshibangu\Desktop\galaga\Resources\galaga-ship-png-4.png" )
        enemy.height = 200
        enemy.width = 200
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

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
        
        # draws border for hit box
        # self.player_sprite.draw_hit_box( line_thickness = 5 )
        
        # creates a rectangle the size of screen to contain image?
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
                                    
        # call draw() on all sprite lists below
        self.player_list.draw()
        self.enemy_list.draw()
        self.explosions_list.draw()

        # draws border for hit box
        # self.player_sprite.draw_hit_box( line_thickness = 5 )
        self.bullet_list.draw()

        # render the text for score
        arcade.draw_text( f"Score: {self.score}", 10, 20,
                          arcade.color.WHITE, 14 )

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
        
        # call update on explosions
        self.explosions_list.update()
        
        # ENEMY MOVEMENT AND ATTACK LOGIC 

        # initializing the frame count to 1
        self.frame_count += 1
        
        # loop through each enemy
        for enemy in self.enemy_list:

            # Using the modules to trigger an event every 120 frames
            if self.frame_count % 120 == 0:
                bullet = arcade.Sprite( r"C:\Users\Daniel Tshibangu\Desktop\galaga\Resources\missle.png",
                                     SPRITE_SCALING_LASER )

                # change bullet dimensions
                bullet.height = 200
                bullet.width = 100
                    
                bullet.center_x = enemy.center_x
                bullet.top = enemy.bottom
                bullet.change_y = -2
                self.bullet_list.append(bullet)

        # loop through each bullet
        for bullet in self.bullet_list:

            #Check this bullet to see if it hit something
            hit_list = arcade.check_for_collision_with_list( bullet, self.a_list )
            
            # if there was a collision
            if len( hit_list ) > 0:

                # make an explosion
                explosion = Explosion( self.explosion_texture_list )

                # move it to the location of the enemy
                explosion.center_x = hit_list[0].center_x
                explosion.center_y = hit_list[0].center_y


                # call update() to set starting explosion frame
                explosion.update()

                # add a list of sprite to that explosion
                self.explosions_list.append( explosion )

                # get rid of the bullet
                bullet.remove_from_sprite_lists()
                
            # for each enemy we hit, add to score andremove enemy
            for enemy in self.enemy_list:
                if enemy in hit_list:
                    enemy.remove_from_sprite_lists()
                    bullet.remove_from_sprite_lists()
                    self.score += 1
                

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
            
            bullet = arcade.Sprite( r"C:\Users\Daniel Tshibangu\Desktop\galaga\Resources\missle.png",
                                     SPRITE_SCALING_LASER )

            # changed the size of the bullet
            bullet.height = 200
            bullet.width = 100

            # the change in y is equal to the bullet speed set
            bullet.change_y = BULLET_SPEED

            # position of the bullet
            bullet.center_x = self.player_sprite.center_x 
            bullet.bottom = self.player_sprite.top - 2

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


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
