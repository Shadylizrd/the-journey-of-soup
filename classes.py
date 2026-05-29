import pygame, time

# Initialising Pygame
pygame.init()

width = 1600
height = 900

black = (0, 0, 0)
white = (225, 225, 225)
blue = (0, 91, 150)
green = (46, 143, 63)
rose = (234, 61, 98)
dusty_pink = (184, 84, 106)
brown = (133, 88, 97)

# Displaying screen
screen = pygame.display.set_mode((width, height))

# Checks the attributes in a group of tiles
def check_tiles(attr, value, tiles):

    result = False
    has_counter = False

    for tile in tiles:
        # Only works if the tiles are strings not objects
        if attr == "tile_type":
            if tile == value:
                result = True
            
        # Only works if the tiles are objects from the tile class
        if attr == "walkable":
            if tile.is_walkable() and not has_counter:
                result = True
            else:    
                result = False
                has_counter = True

    return result 

# Class to display the rect around the selected button
class show_selection():
    def __init__ (self, my_x, my_y, my_width, my_height):

        # Attributes for size and location of the highlight
        self.x = my_x -4
        self.y = my_y -4
        self.width = my_width +8
        self.height =  my_height +8
        self.highlight = pygame.Rect(self.x, self.y ,self.width, self.height)

    # drawing the button
    def draw_highlight(self, colour):
        pygame.draw.rect(screen, colour, self.highlight)

    def flicker(self):
        pygame.draw.rect(screen, white, self.highlight)
 
# Class to change selection and stop users from going past the set limits for selection
class menu_selection():
    def __init__ (self, my_upper_lim, my_lower_lim):
        self.upper_lim = my_upper_lim
        self.lower_lim = my_lower_lim
	
    # Select the next button upwards
    def select_up(self, selected):
        if selected > self.lower_lim:
            selected -= 1
        return selected

    # Select the next button downwards
    def select_down(self, selected):
        if selected < self.upper_lim:
            selected += 1
        return selected

# Class for all player information
class player_info():
    def __init__(self, Max_Health, Current_Health, Max_Stamina, Current_Stamina, Speed, Facing, Hitbox, X_pos, Y_pos, Images):
        # Attributes
        self.max_health = Max_Health
        self.current_health = Current_Health
        self.max_stamina = Max_Stamina
        self.current_stamina = Current_Stamina
        self.stamina_draining = False
        self.exhausted = False
        self.stam_regen_cd = 0
        self.speed = Speed
        self.rolling = False
        self.facing = Facing
        self.hitbox = Hitbox
        self.hitbox_active = True
        self.x = X_pos
        self.y = Y_pos
        self.x_right = self.x + 50
        self.images = Images

    # Method to get the value of an attribute depending on what you enter for the "stat" perameter
    def get_stat(self, stat):
        if stat == "max health":
            return self.max_health
        elif stat == "current health":
            return self.current_health
        elif stat == "max stamina":
            return self.max_stamina
        elif stat == "current stamina":
            return self.current_stamina
        elif stat == "stamina draining":
            return self.stamina_draining
        elif stat == "exhausted":
            return self.exhausted
        elif stat == "speed":
            return self.speed
        elif stat == "rolling":
            return self.rolling
        elif stat == "facing":
            return self.facing 
        elif stat == "x":
            return self.x
        elif stat == "y":
            return self.y 
    
    # Method to change the value of an attribute depending on what you enter for the "stat" perameter    
    def update_stat(self, stat, new_value):
        if stat == "max health":
            self.max_health = new_value
        elif stat == "current health":
            self.current_health = new_value
        elif stat == "max stamina":
            self.max_stamina = new_value
        elif stat == "current stamina":
            self.current_stamina = new_value
        elif stat == "stamina draining":
            self.stamina_draining = new_value
        elif stat == "speed":
            self.speed = new_value
        elif stat == "rolling":
            self.rolling = new_value
        elif stat == "facing":  
            self.facing = new_value
        elif stat == "hitbox active":
            self.hitbox_active = new_value     
        elif stat == "x":
            self.x = new_value
        elif stat == "y":
            self.y  = new_value
       
    # Method to change the coordinates of the player sprite
    def move(self):
        # This method changes the value of the "x" or "y" attributes based on the direction passed into the "direction" parameter
        # Sets the "direction" attribute according to direction player has moved. useful for blitting the character sprite

        if self.facing == "up":
            self.y -= self.speed

        elif self.facing == "down": 
            self.y += self.speed

        elif self.facing == "left" :
            self.x -= self.speed

        elif self.facing == "right":
            self.x += self.speed


    # Method to update stamina
    def stam_change(self):

        if self.stamina_draining:
            # If stamina is draining then -1 to the "current_stamina" attribute until it reaches 0
            if self.current_stamina > 0:
                self.current_stamina -= 1
            # Otherwise sets "exhausted" to True
            else:
                self.exhausted = True
            # sets stamina regen cooldown to 45 each time "stamina_draining" is True
            self.stam_regen_cd = 45
        else:
            # Checks if stamina regen cooldown has hit
            if self.stam_regen_cd == 0:
                if self.current_stamina < self.max_stamina:
                    self.current_stamina += 1
                else:
                    self.exhausted = False
            else:
                self.stam_regen_cd -= 1

    # Method so player can roll
    def roll(self, loops, core_tiles):
            if self.rolling:
                old_speed = self.speed
                self.speed = 15

                if check_tiles("walkable", None, self.next_tiles(core_tiles)):
                    self.move()
                    loops += 1
                else:
                    loops = 10

                self.hitbox_active = False
                self.stamina_draining = True
                self.speed = old_speed
                
                
                if loops == 10:
                    self.rolling = False
                return loops

    def get_hit(self, damage):
        if self.hitbox_active:
            self.current_health -= damage

    def draw(self):
        if self.rolling:
            if self.facing == "up":
                screen.blit(self.images[4], (self.x, self.y))

            elif self.facing == "down":
                screen.blit(self.images[4], (self.x, self.y))

            elif self.facing == "left":
                screen.blit(self.images[4], (self.x, self.y))

            elif self.facing == "right":
                screen.blit(self.images[4], (self.x, self.y))

        else:
            if self.facing == "up":
                screen.blit(self.images[0], (self.x, self.y))

            elif self.facing == "down":
                screen.blit(self.images[1], (self.x, self.y))

            elif self.facing == "left":
                screen.blit(self.images[2], (self.x, self.y))

            elif self.facing == "right":
                screen.blit(self.images[3], (self.x, self.y))

    def tile_location(self, player_x, player_y):
        x = player_x // 100
        y = player_y // 100
        return x, y
    
    def next_tiles(self, core_tiles):
        new_x = self.x
        new_y = self.y
        if self.facing == "up":
            new_y = self.y - self.speed
        elif self.facing == "down":
            new_y = self.y + self.speed
        elif self.facing == "left":
            new_x = self.x - self.speed
        elif self.facing == "right":
            new_x = self.x + self.speed

        # Getting the locations of the 4 possible tiles that the player could be on; top left, top right, bottom left, bottom right
        tl_next_tile_pos = [new_x//100, new_y//100]
        tr_next_tile_pos = [(new_x + 50)//100, new_y//100]
        bl_next_tile_pos = [new_x//100, (new_y + 90)//100]
        br_next_tile_pos = [(new_x + 50)//100, (new_y + 90)//100]

        tile_positions = [tl_next_tile_pos, tr_next_tile_pos, bl_next_tile_pos, br_next_tile_pos] 

        try:
            next_tiles = []
            for next_tile_pos in tile_positions:
                next_tiles.append(core_tiles[next_tile_pos[0]][next_tile_pos[1]])
  
        except:
            print("The player has exited the boundaries.")
        return next_tiles

# Class for all boss information
class boss_info():
    def __init__(self, Max_Health, Health, X_pos, Y_pos):
        self.max_health = Max_Health
        self.current_health = Health
        self.x = X_pos
        self.y = Y_pos

        self.boss = {
            "Max_Health": self.max_health,
            "Current_Health": self.current_health,
            "X_Position": self.x,
            "Y_Position": self.y
        }

# Class for all projectile attacks
class projectiles():
    def __init__(self, X_pos, Y_pos):
        self.x = X_pos
        self.y = Y_pos

# Class for displaying all tiles
class tile():
    def __init__(self, my_x, my_y):
        self.x = my_x
        self.y = my_y
        self.walkable = False
        self.slidable = False
        self.image = None

    def get_location(self):
        return self.x / 100, self.y / 100

    def cast(self, new_walkable, new_slidable, new_image):
        self.walkable = new_walkable
        self.slidable = new_slidable
        self.image = new_image
        
    def is_slidable(self):
        return self.slidable
        
    def is_walkable(self):
        return self.walkable  

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Class for all interactable objects
class interactables():
    def __init__(self, my_x, my_y, my_image):
        self.x = my_x
        self.y = my_y
        self.image = my_image

    def get_location(self):
        return self.x, self.y
    
    def interact(self, player):
        None

    def draw(self):
        screen.blit(self.image, (self.x * 100, self.y * 100))

class torch(interactables):
    def __init__(self, my_x, my_y, my_image_on, my_image_off, my_active):
        interactables.__init__(self, my_x, my_y, my_image_off)
        self.image_on = my_image_on
        self.image_off = my_image_off
        self.active = my_active

    def interact(self, player):
        if self.active:
            self.active = False
            self.image = self.image_off
        else:
            self.active = True
            self.image = self.image_on

class ice_block(interactables):
    def __init__(self, my_x, my_y, my_image):
        interactables.__init__(self, my_x, my_y, my_image)
        self.moving = False
        self.direction = ""

    def interact(self, player):
        self.moving = True
        self.direction = player.get_stat("facing")

    def move(self, core_tiles):
        if self.direction == "right":
            if core_tiles[self.x + 1][self.y].is_slidable():
                self.x += 1
            else:
                self.moving = False

        elif self.direction == "left":
            if core_tiles[self.x - 1][self.y].is_slidable():
                print(self.x)
                self.x -= 1
            else:
                self.moving = False

        elif self.direction == "up":
            if core_tiles[self.x][self.y - 1].is_slidable():
                self.y -= 1
            else:
                self.moving = False

        elif self.direction == "down":
            if core_tiles[self.x][self.y + 1].is_slidable():
                self.y += 1
            else:
                self.moving = False

    def is_moving(self):
        return self.moving

    def get_location(self):
        return self.x, self.y


