import pygame
from classes import show_selection, menu_selection, player_info, boss_info, projectiles, tile, interactables, torch, ice_block

# Initialising Pygame
pygame.init()


# Variables for the program
clock = pygame.time.Clock()
fps = 60

width = 1600
height = 900

black = (0, 0, 0)
white = (225, 225, 225)
grey = (200, 200, 200)
blue = (0, 91, 150)
green = (44, 94, 26)
dark_green = (26, 67, 20)
grey_green = (117, 129, 107)
dark_grey_green = (88, 87, 79)

orange_red = (173, 47, 69)
rose = (234, 61, 98)
dusty_pink = (184, 84, 106)
brown = (133, 88, 97)

# Displaying screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JOURNEY OF SOUP")





# Main Menu
# Menu Images
title_img = pygame.image.load('./sprites/Title.png').convert_alpha()
load_save_img = pygame.image.load('./sprites/LoadSave.png').convert_alpha()

quit_img = pygame.image.load('./sprites/Quit.png').convert_alpha()

    # Menu images list
menu_images = [
    [title_img, ((18/64 * width), (5/30 * height))], 
    [load_save_img, ((25/64 * width), (1/2 * height))],
    [quit_img, ((25/64 * width), (26/45 * height))]
]

# Menu Objects
s_main_menu = menu_selection(1, 0)
s_new_save = menu_selection(3, 0)

load_save_highlight = show_selection((25/64 * width), (1/2 * height), 350, 50)
quit_highlight = show_selection((25/64 * width), (26/45 * height), 350, 50)

save_1_highlight = show_selection((5/32 * width), (17/120 * height), 1100, 150)
save_2_highlight = show_selection((5/32 * width), (39/120 * height), 1100, 150)
save_3_highlight = show_selection((5/32 * width), (61/120 * height), 1100, 150)
save_4_highlight = show_selection((5/32 * width), (83/120 * height), 1100, 150)




# Save Screen
# Rects
background_rect = pygame.Rect((1/8 * width), (1/8 * height), 1200, 675)

emptysave_1_rect = pygame.Rect((5/32 * width), (17/120 * height), 1100, 150)
emptysave_2_rect = pygame.Rect((5/32 * width), (39/120 * height), 1100, 150)
emptysave_3_rect = pygame.Rect((5/32 * width), (61/120 * height), 1100, 150)
emptysave_4_rect = pygame.Rect((5/32 * width), (83/120 * height), 1100, 150)

save_1_rect = pygame.Rect((5/32 * width), (17/120 * height), 1100, 150)
save_2_rect = pygame.Rect((5/32 * width), (39/120 * height), 1100, 150)
save_3_rect = pygame.Rect((5/32 * width), (61/120 * height), 1100, 150)
save_4_rect = pygame.Rect((5/32 * width), (83/120 * height), 1100, 150)

back_img = pygame.image.load('./sprites/back.png').convert_alpha()
select_img = pygame.image.load('./sprites/select.png').convert_alpha()

    # lists of rects all the same colour
smenu_rose_rects = (
    save_1_rect, 
    save_2_rect, 
    save_3_rect, 
    save_4_rect)
    
smenu_dusty_pink_rects = (
    emptysave_1_rect, 
    emptysave_2_rect,
    emptysave_3_rect, 
    emptysave_4_rect)

smenu_images = [
    [back_img, ((1/8 * width), (22/24 * height))],
    [select_img, ((10/32 * width), (22/24 * height))]
]




# Options Screen

# Options Images
options_backdrop_img = pygame.image.load('./sprites/Backdrop.png').convert_alpha()
options_controls_img = pygame.transform.scale((pygame.image.load('./sprites/Controls.png').convert_alpha()), (175, 25))
options_quit_img = pygame.transform.scale((pygame.image.load('./sprites/Quit.png').convert_alpha()), (175, 25))

# Options Objects
options_menu = menu_selection(1,0)

options_controls_highlight = show_selection((57/128 * width), (1/2 * height),175,25)
options_quit_highlight = show_selection((57/128 * width), (5/9 * height),175,25)

options_images = [
    [options_controls_img, ((57/128 * width), (1/2 * height))], 
    [options_quit_img, ((57/128 * width), (5/9 * height))]
]





# Player
# Player Images
player_up = pygame.image.load('./sprites/breadman-up.png').convert_alpha()
player_down = pygame.image.load('./sprites/breadman-down.png').convert_alpha()
player_left = pygame.image.load('./sprites/breadman-left.png').convert_alpha()
player_right = pygame.image.load('./sprites/breadman-right.png').convert_alpha()
player_roll = pygame.image.load('./sprites/roll-temp.png').convert_alpha()

player_images = (player_up, player_down, player_left, player_right, player_roll)


# Player objects
player = player_info(100, 45, 100, 100, 6, "up", None, 750, 300, player_images)



# Game screen
# Game images
Ground_image = pygame.image.load('./sprites/Ground.png').convert_alpha()
Wall_image = pygame.image.load('./sprites/Wall.png').convert_alpha()
Ice_image = pygame.image.load('./sprites/Ice.png').convert_alpha()
Door_image = pygame.image.load('./sprites/Door.png').convert_alpha()
Torch_on_image = pygame.image.load('./sprites/Torch_on.png').convert_alpha()
Torch_off_image = pygame.image.load('./sprites/Torch_off.png').convert_alpha()
ice_block_image = pygame.image.load('./sprites/ice_block.png').convert_alpha()

# Game objects
torch1 = torch(4, 4, Torch_on_image, Torch_off_image, False)
torch2 = torch(11, 4, Torch_on_image, Torch_off_image, False)

ice_block1 = ice_block(8, 5, ice_block_image)
ice_block2 = ice_block(4, 2, ice_block_image)

room1_objects = []
room2_objects = []
room3_objects = [ice_block2]
room4_objects = [torch1, torch2]
room5_objects = [ice_block1]

# Game background cast lists

# North is left
# South is right
# East is downwards
# West is upwards

room1_cast = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"], 
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "I", "T", "I", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "I", "T", "T", "W"], 
    ["W", "T", "T", "T", "T", "I", "T", "T", "W"], 
    ["DN", "T", "T", "T", "T", "I", "T", "T", "w"], 
    ["DN", "T", "I", "T", "I", "T", "T", "T", "w"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W"]]

room2_cast = [
    ["W", "W", "W", "W", "DW", "W", "W", "W", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"], 
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "I", "T", "T", "T", "W"], 
    ["W", "T", "I", "T", "I", "T", "I", "T", "W"], 
    ["DN", "T", "T", "T", "I", "T", "T", "T", "DS"], 
    ["DN", "T", "I", "I", "I", "I", "I", "T", "DS"],
    ["W", "T", "T", "T", "I", "T", "T", "T", "W"], 
    ["W", "T", "I", "T", "I", "T", "I", "T", "W"], 
    ["W", "T", "T", "T", "I", "T", "T", "T", "W"], 
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"], 
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"], 
    ["W", "W", "W", "W", "DE", "W", "W", "W", "W"]]

room3_cast = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"], 
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "I", "I", "I", "I", "T", "T", "W"],
    ["W", "T", "I", "T", "T", "I", "T", "T", "W"], 
    ["W", "T", "I", "T", "T", "I", "T", "T", "W"], 
    ["W", "T", "I", "T", "T", "I", "T", "T", "DS"], 
    ["W", "T", "I", "T", "T", "I", "T", "T", "DS"],
    ["W", "T", "I", "I", "T", "I", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "I", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "I", "T", "T", "W"],
    ["W", "T", "I", "I", "I", "I", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W"]]

room4_cast = [
    ["W", "W", "W", "W", "DW", "W", "W", "W", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "O", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "O", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "T", "T", "T", "T", "T", "T", "T", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W"]]

room5_cast = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "I", "I", "I", "I", "I", "I", "I", "W"],
    ["W", "W", "W", "W", "DE", "W", "W", "W", "W"]]

# map of rooms
# north is downwards
# south is upwards
# east is right
# west is left

# The coordinate composition is (y, x) 
# This is so that the "y" still controls vertical movement and "x" still controls horizontal movement
rooms = [
        [None, room1_cast, None],
        [room5_cast, room2_cast, room4_cast],
        [None, room3_cast, None]
        ]

room_objects = [
        [None, room1_objects, None],
        [room5_objects, room2_objects, room4_objects],
        [None, room3_objects, None]
        ]

# Save game data
# def save_game(game_state, file_name):

# Display rects on screen
def draw_rects(list, colour):
    for i in list:
        pygame.draw.rect(screen, colour, i)

# Display images on screen
def blit_images(list):
    for image in range(len(list)):
        screen.blit(list[image][0], list[image][1])

# Display object images on screen
def draw_objects(list):
    for object in list:
        object.draw()

# Load all core tiles
def load_core():
    core_tiles = []
    for x in range (0,16):
        column = []
        for y in range (0, 9):
            new_tile = tile(x*100, y*100)
            column.append(new_tile)
        core_tiles.append(column)
    return core_tiles

# Cast all core tiles
def cast_core(room_cast, core_tiles):
    x = 0
    y = 0
    for column in room_cast:
        for tile_type in column:
            if tile_type.upper() == "T":
                core_tiles[x][y].cast(True, False, Ground_image)
            elif tile_type.upper() == "W":
                core_tiles[x][y].cast(False, False, Wall_image)
            elif tile_type.upper() == "I":
                core_tiles[x][y].cast(True, True, Ice_image)
            elif tile_type.upper() == "DN" or tile_type.upper() == "DS" or tile_type.upper() == "DE" or tile_type.upper() == "DW":
                core_tiles[x][y].cast(False, True, Door_image)
            elif tile_type.upper() == "O":
                core_tiles[x][y].cast(False, False, Ground_image)
            
            y += 1  
        x += 1
        y = 0
    return core_tiles

# Draw all tiles on screen
def draw_core(core_tiles):
    for column in core_tiles:
        for tile in column:
            tile.draw()

# Update stat bars in accordance with player's stats
def load_statbars():

        healthbar_border = pygame.Rect(20, 15, (player.get_stat("max health") * 4 +10), 30)
        healthbar = pygame.Rect(25, 20, (player.get_stat("max health") * 4), 20)
        current_healthbar = pygame.Rect(25, 20, (player.get_stat("current health") * 4), 20)

        staminabar_border = pygame.Rect(20, 55, (player.get_stat("max stamina") * 4 +10), 30)
        staminabar = pygame.Rect(25, 60, (player.get_stat("max stamina") * 4), 20)
        current_staminabar = pygame.Rect(25, 60, (player.get_stat("current stamina") * 4), 20)

        return healthbar_border, healthbar, current_healthbar, staminabar_border, staminabar, current_staminabar

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

# Screens
# All methods of the game screen
def game():
    # Variables
    run = True
    loops = 0
    roll_cooldown = 0
    map_y = 0
    map_x = 1
    current_cast = rooms[map_y][map_x]
    current_objects = ()
    core_tiles = load_core()
    core_tiles = cast_core(current_cast, core_tiles)

    while run:

        # Setting/updating the size of the healthbars with reference to the correlating attributes in the player class
        healthbar_border, healthbar, current_healthbar, staminabar_border, staminabar, current_staminabar = load_statbars()

        draw_core(core_tiles)
        draw_objects(current_objects)

        # Drawing all images and rects on screen
        player.draw()
        pygame.draw.rect(screen, white, healthbar_border)
        pygame.draw.rect(screen, dusty_pink, healthbar)
        pygame.draw.rect(screen, rose, current_healthbar)

        pygame.draw.rect(screen, white, staminabar_border)


        # Allowing for visual difference between the stamina bar when exhausted 
        # player cannot use any action that requires stamina when exhausted
        if not player.get_stat("exhausted"):
            pygame.draw.rect(screen, green, staminabar)
            pygame.draw.rect(screen, dark_green, current_staminabar)
        else:
            pygame.draw.rect(screen, grey_green, staminabar)
            pygame.draw.rect(screen, dark_grey_green, current_staminabar)

        # Checking whether player is pressing any keys that can be held down
        key = pygame.key.get_pressed()

        # Stopping player from being able to walk or run if rolling
        if not player.get_stat("rolling"):
            if key[pygame.K_w] or key[pygame.K_s] or key[pygame.K_a] or key[pygame.K_d]:
                
                if key[pygame.K_w]:
                    player.update_stat("facing", "up")
                elif key[pygame.K_s]:
                    player.update_stat("facing", "down")
                elif key[pygame.K_a]:    
                    player.update_stat("facing", "left")
                elif key[pygame.K_d]:
                    player.update_stat("facing", "right")
                
                if check_tiles("walkable", None, player.next_tiles(core_tiles)):
                    player.move()

            if key[pygame.K_LSHIFT] and not player.get_stat("exhausted"):
                player.update_stat("speed", 10)
                player.update_stat("stamina draining", True)
        
            else:
                player.update_stat("speed", 6)
                player.update_stat("stamina draining", False)

        # counting number of loops so that the roll can only
        loops = player.roll(loops, core_tiles)

        # Method for reducing the roll cooldown each loop
        if roll_cooldown > 0:
            roll_cooldown -= 1 
        
        # Updating stamina each loop
        player.stam_change()

        for object in current_objects:
            try:
                if object.is_moving():
                    object.move(core_tiles)
            except:
                pass


        # Event manager
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.KEYDOWN:

                # Runs the options screen method
                if event.key == pygame.K_ESCAPE:
                    options()

                # Activates roll
                elif event.key == pygame.K_SPACE:
                    if roll_cooldown == 0 and player.get_stat("current stamina") >= 10 and not player.get_stat("exhausted"):
                        player.update_stat("rolling", True)
                        loops = 0
                        roll_cooldown = 15
                    
                # Room switch
                elif event.key == pygame.K_e:

                    # going to a room northwards
                    if check_tiles("tile_type", "DN", player.next_tiles(current_cast)):
                        map_y += 1
                        current_cast = rooms[map_y][map_x]
                        current_objects = room_objects[map_y][map_x]
                        core_tiles = cast_core(current_cast, core_tiles)
                        player.update_stat("y", 700)

                    elif check_tiles("tile_type", "DS", player.next_tiles(current_cast)):
                        map_y -= 1
                        current_cast = rooms[map_y][map_x]
                        current_objects = room_objects[map_y][map_x]
                        core_tiles = cast_core(current_cast, core_tiles)
                        player.update_stat("y", 100)

                    elif check_tiles("tile_type", "DE", player.next_tiles(current_cast)):
                        map_x += 1
                        current_cast = rooms[map_y][map_x]
                        current_objects = room_objects[map_y][map_x]
                        core_tiles = cast_core(current_cast, core_tiles)
                        player.update_stat("x", 100)

                    elif check_tiles("tile_type", "DW", player.next_tiles(current_cast)):
                        map_x -= 1
                        current_cast = rooms[map_y][map_x]
                        current_objects = room_objects[map_y][map_x]
                        core_tiles = cast_core(current_cast, core_tiles)
                        player.update_stat("x", 1450)

                    elif check_tiles("tile_type", "O", player.next_tiles(current_cast)) or check_tiles("tile_type", "I", player.next_tiles(current_cast)):
                        interact_tiles = player.next_tiles(core_tiles)
                        interacting = True
                        t = 0
                        while interacting and t < 4:
                            tile = interact_tiles[t]
                            t += 1
                            for object in current_objects:
                                if tile.get_location() == object.get_location():
                                    object.interact(player)
                                    interacting = False


        pygame.display.update()
        clock.tick(60)

# All methods of the options screen
def options():
    # Variables
    run = True
    selection = 0
    alpha = 200

    # Setting opacity for the background image aswell as displaying said image so it covers the whole screen
    options_backdrop_img.set_alpha(alpha)
    screen.blit(options_backdrop_img, (0, 0))

    while run:

        # Highlighting the appropriate button when selected in reference to the value of the "selection" value
        if selection == 0:
            options_controls_highlight.draw_highlight(orange_red)
            options_quit_highlight.draw_highlight(white)
  
        elif selection == 1:
            options_quit_highlight.draw_highlight(orange_red)
            options_controls_highlight.draw_highlight(white)

        # Displaying the options and quit buttons
        blit_images(options_images)

        # Events manager
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
                
            elif event.type == pygame.KEYDOWN:

                # Letting player exit the pause menu via use of the esc key or q
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_q:
                    run = False

                # Navigation between the buttons, setting the selection value appropriately
                if event.key == pygame.K_w:
                    selection = options_menu.select_up(selection)

                if event.key == pygame.K_s:
                    selection = options_menu.select_down(selection)

                # Checking value of "selection" and carrying out the correct procedure
                if event.key == pygame.K_e:
                    if selection == 0:
                        controls()
                    if selection == 1:
                        main_menu()


        pygame.display.update()
        clock.tick(60)

# Controls option screen
def controls():
    # Variables
    run = True
    while run:
        screen.blit(white)

            # Events manager
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
                
            elif event.type == pygame.KEYDOWN:

                # Letting player exit the pause menu via use of the esc key or q
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_q:
                    run = False

        pygame.display.update()
        clock.tick(60)

# All methods of the load save screen
def load_save():
    # Variables
    selection = 0
    run = True
    
    while run:
        
        # Displaying all rects and images on screen
        screen.fill(white)

        pygame.draw.rect(screen, brown, background_rect)

        blit_images(smenu_images)

        # Highlighting the appropriate button when selected in reference to the value of the "selection" value
        if selection == 0:
            save_1_highlight.draw_highlight(white)
        elif selection == 1:
            save_2_highlight.draw_highlight(white)
        elif selection == 2:
            save_3_highlight.draw_highlight(white)
        elif selection == 3:
            save_4_highlight.draw_highlight(white)

        draw_rects(smenu_dusty_pink_rects, dusty_pink)


        # Event manager
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.KEYDOWN:

                # Opening game screen - will be developed further once save files are introduced
                if event.key == pygame.K_e:
                    game()

                # Navigation back to main menu
                if event.key == pygame.K_q:
                    run = False
            
                # Navigation between the buttons, setting the selection value appropriately
                if event.key == pygame.K_w:
                    selection = s_new_save.select_up(selection)
                    print(selection)

                if event.key == pygame.K_s:
                    selection = s_new_save.select_down(selection)
                    print(selection)


            
        pygame.display.update()
        clock.tick(60)

# All methods of the main menu
def main_menu():
    # setting selection as a variable to check which button the user is selecting
    selection = 0
    while True:

        screen.fill(white)
    
        # using the selection variable to show which button is selected
        if selection == 0:
            load_save_highlight.draw_highlight(orange_red)
            quit_highlight.draw_highlight(grey)

        elif selection == 1:
            quit_highlight.draw_highlight(orange_red)
            load_save_highlight.draw_highlight(grey)

          
        # Displaying all images for the main menu
        blit_images(menu_images)

        # Event handling
        for event in pygame.event.get():
            # To quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
                
            # check if keys are pressed and act accordingly
            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_w:
                    selection = s_main_menu.select_up(selection)

                elif event.key == pygame.K_s:
                    selection = s_main_menu.select_down(selection)

                elif event.key == pygame.K_e:
                    if selection == 0:
                        load_save()
                    elif selection == 1:
                        pygame.quit()
                        raise SystemExit


        
        pygame.display.update()
        clock.tick(60)


# Main

main_menu()
    