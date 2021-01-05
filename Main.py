##############################################################
# Sollaris v1.0                                              #
# Author = Oren                                              #
# MADE FOR THE FINAL CYBER PROJECT IN 2019                   #
# Credits :                                                  #
# Terraria,StarBound,Battleblock Theater,Dark Souls | Assets #
#                                                            #
##############################################################

# Imports from classes:
from Player import Player
from Biomes import *
from Assets import *
from Boss import Boss
import os

# Import from py_game and python modules:
import random
import pygame

# Py_game Constants:
WIDTH = 1600
HEIGHT = 1000

REFRESH_RATE = 165

LEFT = 3
MIDDLE = 2
RIGHT = 1

TEXT_FONT = r"C:\Users\Oren\Desktop\Sollaris\Models\fonts\Andy Bold.ttf"

# Colors :
GRAY = (100, 100, 100)
LIME = (170, 242, 0)
CRIMSON_RED = (220, 20, 60)
LIGHT_BLUE = (0, 172, 240)
ORANGE = (249, 161, 28)
YELLOW = (255, 255, 0)

# Py_game Variables:

RunningGame = True
RunningMenu = True
RunningLose = True
Biome_Random = True
biome_order = []

# Py_game Menu :
menu_image1_X = 0
menu_image1_Y = 0
menu_image2_X = WIDTH
menu_image2_Y = 0

# Buttons :
start_button_color = GRAY
start_hover_time = 0

folder_button_color = GRAY
folder_hover_time = 0

settings_button_color = GRAY
settings_hover_time = 0

exit_button_color = GRAY
exit_hover_time = 0

# Player Idle Check & Jumping states:
idle_check = 0
jump_start = False
jump_timeStart = 0
jump_timeStop = 0
block_is_above = 0

# Water Mechanism:
waterCheck = 0
notWaterCount = 0
waterSurfaceCount = 0
playerBlock = 1

# Music Mechanism:
music_counter = 0

# Breaking Mechanism:
breakTimeFirst = 0
breakTimeLast = 0
breakPercent = 0
blocks_broken = 0

# Day and Night Cycle :
days_count = 0
day_time = 30
isNight = False
turn_cycle_moon = 0
turn_cycle_sun = 0
day_start_time = 0
day_specific_time = 0

sunX = 0
sunY = HEIGHT / 2 - 300

moonX = 0
moonY = HEIGHT / 2 - 300

# Boss Mechanism:
spawn_once = 0
boss_defeat = True
boss = ""
boss_HP = 10
# Clouds Mechanism:
cloud_velocity = 0.2

cloud1X = 0
cloud1Y = 50

cloud2X = cloud1X + 300
cloud2Y = cloud1Y

cloud3X = cloud2X + 180
cloud3Y = cloud1Y

# Player block placed list:
wood_list = pygame.sprite.Group()
wood_inv = 0

# Settings:

size = [WIDTH, HEIGHT]
Clock = pygame.time.Clock()
player = Player(50, 725)

# Maybe after the game is done make a txt file for it
screen = pygame.display.set_mode(size)
game_name = pygame.display.set_caption("Sollaris")

biome_type = beach_ubc
subBiome_type = beach_ubc
music_type = NIGHT_MUSIC
menu_music_type = "'"
currentMusic_type = NIGHT_MUSIC

# Biome Order:

while Biome_Random:
    number = random.randint(1, 4)
    if number not in biome_order:
        biome_order.append(number)
    if len(biome_order) == 4:
        Biome_Random = False

# Py_game init()

pygame.init()
pygame.mixer.init()

# World Generation :
blocksList1, type1, airList1 = generate_forest(biome_order[0], size)
blocksList2, type2, airList2 = generate_desert(biome_order[1], size)
blocksList3, type3, airList3 = generate_snow(biome_order[2], size)
blocksList4, type4, airList4 = generate_ocean(biome_order[3], size)

# HP generation FIRST:
hp_list = []
hp_image = player_hpImage
player.HP = 10
for heart in xrange(0, player.HP, 1):
    hp_list.append(heart * 25)

# Main Menu Initializer:
while RunningMenu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunningMenu = False
            RunningGame = False
            pygame.quit()
    # Py_game mouse :
    mouse_pos = pygame.mouse.get_pos()
    Buttons = pygame.mouse.get_pressed()

    # Menu music system :
    if currentMusic_type != menu_music_type:
        menu_music_load = pygame.mixer_music.load(MENU_MUSIC2)
        menu_music = pygame.mixer_music.play(-1)

    currentMusic_type = menu_music_type

    # Menu FPS Counter:
    fps = int(Clock.get_fps())
    fps_counter = pygame.font.SysFont(TEXT_FONT, 36)
    fps_counter = fps_counter.render("FPS : " + str(fps), 1, LIME)

    # Play Button :
    start_button = pygame.font.SysFont(TEXT_FONT, 48)
    start_button = start_button.render("Play", 1, start_button_color)
    start_button_Rect = start_button.get_rect()
    start_button_Rect[0] = WIDTH / 2 - 50
    start_button_Rect[1] = HEIGHT / 2 - 100

    if start_button_Rect.collidepoint(mouse_pos):
        start_button_color = YELLOW
        if start_hover_time == 0:
            pygame.mixer.Sound.play(menuClick)
        if Buttons[RIGHT - 1]:
            RunningMenu = False
        start_hover_time += 1

    else:
        start_button_color = GRAY
        start_hover_time = 0

    # Open Folder Button :
    folder_button = pygame.font.SysFont(TEXT_FONT, 48)
    folder_button = folder_button.render("Open Folder", 1, folder_button_color)
    folder_button_Rect = folder_button.get_rect()
    folder_button_Rect[0] = start_button_Rect[0] - 65
    folder_button_Rect[1] = start_button_Rect[1] + 60

    if folder_button_Rect.collidepoint(mouse_pos):
        folder_button_color = YELLOW
        if folder_hover_time == 0:
            pygame.mixer.Sound.play(menuClick)
        if Buttons[RIGHT - 1]:
            os.startfile(FOLDER_URL)
        folder_hover_time += 1

    else:
        folder_button_color = GRAY
        folder_hover_time = 0
    # Settings Button :
    settings_button = pygame.font.SysFont(TEXT_FONT, 48)
    settings_button = settings_button.render("Settings", 1, settings_button_color)
    settings_button_Rect = settings_button.get_rect()
    settings_button_Rect[0] = start_button_Rect[0] - 30
    settings_button_Rect[1] = folder_button_Rect[1] + 60

    if settings_button_Rect.collidepoint(mouse_pos):
        settings_button_color = YELLOW
        if settings_hover_time == 0:
            pygame.mixer.Sound.play(menuClick)
        if Buttons[RIGHT - 1]:
            os.startfile(FOLDER_URL + r"\settings.ini")
        settings_hover_time += 1

    else:
        settings_button_color = GRAY
        settings_hover_time = 0

    # Exit Button :
    exit_button = pygame.font.SysFont(TEXT_FONT, 48)
    exit_button = exit_button.render("Exit", 1, exit_button_color)
    exit_button_Rect = exit_button.get_rect()
    exit_button_Rect[0] = start_button_Rect[0]
    exit_button_Rect[1] = settings_button_Rect[1] + 60

    if exit_button_Rect.collidepoint(mouse_pos):
        exit_button_color = YELLOW
        if exit_hover_time == 0:
            pygame.mixer.Sound.play(menuClick)
        if Buttons[RIGHT - 1]:
            RunningMenu = False
            RunningGame = False
            RunningLose = False
            exit("Why would you even launch the game? :/")
        exit_hover_time += 1

    else:
        exit_button_color = GRAY
        exit_hover_time = 0

    # Menu image loop :
    screen.blit(menu_bc, (menu_image1_X, menu_image1_Y))
    screen.blit(menu_bc, (menu_image2_X, menu_image2_Y))
    menu_image1_X -= 0.5
    menu_image2_X -= 0.5

    if menu_image2_X <= 0:
        menu_image2_X = WIDTH
        menu_image1_X = 0

    screen.blit(game_logo, (WIDTH / 2 - 320, HEIGHT / 2 - 300))
    screen.blit(fps_counter, (WIDTH - 120, 10))
    screen.blit(start_button, (start_button_Rect[0], start_button_Rect[1]))
    screen.blit(folder_button, (folder_button_Rect[0], folder_button_Rect[1]))
    screen.blit(settings_button, (settings_button_Rect[0], settings_button_Rect[1]))
    screen.blit(exit_button, (exit_button_Rect[0], exit_button_Rect[1]))

    Clock.tick(REFRESH_RATE)
    pygame.display.flip()
    # Main Game Initializer :

while RunningGame:
    screen.blit(biome_type, (0, 0))
    screen.blit(subBiome_type, (0, 800))

    blocksList1.draw(screen)
    blocksList2.draw(screen)
    blocksList3.draw(screen)
    blocksList4.draw(screen)
    wood_list.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunningGame = False
            RunningLose = False
            exit("Thank you for playing Sollaris!")

        if not hp_list:
            pygame.mixer.Sound.play(playerDie)
            RunningGame = False

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and player.isJump is False:
                jump_start = True
                jump_timeStart = pygame.time.get_ticks()
            if event.key == pygame.K_h:
                print "Going hardcore huh?"
                pygame.mixer.Sound.play(playerHit)
                hp_list.pop(-1)
                player.HP -= 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                breakTimeFirst = pygame.time.get_ticks()

    Keys = pygame.key.get_pressed()
    Buttons = pygame.mouse.get_pressed()

    # GAME BASIC FUNCTIONS SECTION :

    # Player Movement:

    if Keys[pygame.K_d] or Keys[pygame.K_RIGHT]:
        player.move_right()

    if Keys[pygame.K_a] or Keys[pygame.K_LEFT]:
        player.move_left()

    for key in Keys:
        if key != 0:
            idle_check = 1
    if idle_check == 0 and player.isJump is False:
        player.idle()

    # Player Collisions:

    blockCollision1 = pygame.sprite.spritecollide(player, blocksList1, False)
    blockCollision2 = pygame.sprite.spritecollide(player, blocksList2, False)
    blockCollision3 = pygame.sprite.spritecollide(player, blocksList3, False)
    blockCollision4 = pygame.sprite.spritecollide(player, blocksList4, False)
    woodCollision = pygame.sprite.spritecollide(player, wood_list, False)

    # Block Placing System:
    mouse_pos = pygame.mouse.get_pos()

    if Buttons[RIGHT - 1] and wood_inv > 0:
        for air_block in airList1:
            if abs(air_block.rect.x - player.rect.x) <= 100 and (abs(air_block.rect.y - (player.rect.y + 75)) <= 50
                                                                 or abs(air_block.rect.y - player.rect.y) <= 50):
                if pygame.Rect.collidepoint(air_block.rect, mouse_pos[0], mouse_pos[1]) and air_block.isWood != 1:
                    air_block.set_wood()
                    wood_list.add(air_block)
                    wood_inv -= 1

        for air_block in airList2:
            if abs(air_block.rect.x - player.rect.x) <= 100 and (abs(air_block.rect.y - (player.rect.y + 75)) <= 50
                                                                 or abs(air_block.rect.y - player.rect.y) <= 50):
                if pygame.Rect.collidepoint(air_block.rect, mouse_pos[0], mouse_pos[1]) and air_block.isWood != 1:
                    air_block.set_wood()
                    wood_list.add(air_block)
                    wood_inv -= 1

        for air_block in airList3:
            if abs(air_block.rect.x - player.rect.x) <= 100 and (abs(air_block.rect.y - (player.rect.y + 75)) <= 50
                                                                 or abs(air_block.rect.y - player.rect.y) <= 50):
                if pygame.Rect.collidepoint(air_block.rect, mouse_pos[0], mouse_pos[1]) and air_block.isWood != 1:
                    air_block.set_wood()
                    wood_list.add(air_block)
                    wood_inv -= 1

        for air_block in airList4:
            if abs(air_block.rect.x - player.rect.x) <= 100 and (abs(air_block.rect.y - (player.rect.y + 75)) <= 50
                                                                 or abs(air_block.rect.y - player.rect.y) <= 50):
                if pygame.Rect.collidepoint(air_block.rect, mouse_pos[0], mouse_pos[1]) and air_block.isWood != 1:
                    air_block.set_wood()
                    wood_list.add(air_block)
                    wood_inv -= 1

    # Block Breakage System:
    if Buttons[LEFT - 1]:
        breakTimeLast = pygame.time.get_ticks() - breakTimeFirst

        break_counter = pygame.font.SysFont(TEXT_FONT, 36)
        break_counter = break_counter.render(str(breakPercent), 1, LIGHT_BLUE)

        for block in wood_list:
            # Player Distance:
            if abs(block.rect.x - player.rect.x) <= 100 and (
                    abs(block.rect.y - (player.rect.y + 75)) <= 50 or abs(block.rect.y - player.rect.y) <= 50):

                if pygame.Rect.collidepoint(block.rect, mouse_pos[0], mouse_pos[1]):
                    pygame.mixer.Sound.play(digEffect1)
                    pygame.mixer.Sound.play(digEffect2)
                    pygame.mixer.Sound.play(digEffect3)

                    breakPercent = (breakTimeLast / 1000) * 33.333
                    if breakPercent > 99.99999999:
                        breakPercent = 100
                        screen.blit(break_counter, (player.rect.x, player.rect.y - 30))

                    break_counter = pygame.font.SysFont(TEXT_FONT, 36)
                    break_counter = break_counter.render(str(breakPercent), 1, LIGHT_BLUE)

                    if 3 <= breakTimeLast / 1000.0 <= 3.1:
                        airList1.add(Air(block.rect.x, block.rect.y))
                        wood_list.remove(block)
                        breakTimeLast = 0
                        blocks_broken += 1
                        wood_inv += 1

                    if breakPercent < 99.99999999:
                        screen.blit(break_counter, (player.rect.x, player.rect.y - 30))

        for block in blocksList1:
            # Player Distance:
            if abs(block.rect.x - player.rect.x) <= 100 and (
                    abs(block.rect.y - (player.rect.y + 75)) <= 50 or abs(block.rect.y - player.rect.y) <= 50):

                if pygame.Rect.collidepoint(block.rect, mouse_pos[0], mouse_pos[1]):
                    pygame.mixer.Sound.play(digEffect1)
                    pygame.mixer.Sound.play(digEffect2)
                    pygame.mixer.Sound.play(digEffect3)

                    breakPercent = (breakTimeLast / 1000) * 33.333
                    if breakPercent > 99:
                        breakPercent = 100
                        screen.blit(break_counter, (player.rect.x, player.rect.y - 30))

                    break_counter = pygame.font.SysFont(TEXT_FONT, 36)
                    break_counter = break_counter.render(str(breakPercent), 1, LIGHT_BLUE)

                    if 3 <= breakTimeLast / 1000.0 <= 3.1:
                        airList1.add(Air(block.rect.x, block.rect.y))
                        blocksList1.remove(block)
                        breakTimeLast = 0
                        blocks_broken += 1

                    if breakPercent < 99:
                        screen.blit(break_counter, (player.rect.x, player.rect.y - 30))

        for block in blocksList2:
            if abs(block.rect.x - player.rect.x) <= 100 and (
                    abs(block.rect.y - (player.rect.y + 75)) <= 50 or abs(block.rect.y - player.rect.y) <= 50):

                if pygame.Rect.collidepoint(block.rect, mouse_pos[0], mouse_pos[1]):
                    pygame.mixer.Sound.play(digEffect1)
                    pygame.mixer.Sound.play(digEffect2)
                    pygame.mixer.Sound.play(digEffect3)

                    breakPercent = (breakTimeLast / 1000) * 33.333
                    if breakPercent >= 99:
                        breakPercent = 100
                        screen.blit(break_counter, (player.rect.x, player.rect.y - 30))

                    break_counter = pygame.font.SysFont(TEXT_FONT, 36)
                    break_counter = break_counter.render(str(breakPercent), 1, LIGHT_BLUE)

                    if 3 <= breakTimeLast / 1000.0 <= 3.1:
                        airList2.add(Air(block.rect.x, block.rect.y))
                        blocksList2.remove(block)
                        breakTimeLast = 0
                        blocks_broken += 1

                    if breakPercent < 99:
                        screen.blit(break_counter, (player.rect.x, player.rect.y - 30))

        for block in blocksList3:
            # Player Distance:
            if abs(block.rect.x - player.rect.x) <= 100 and (
                    abs(block.rect.y - (player.rect.y + 75)) <= 50 or abs(block.rect.y - player.rect.y) <= 50):

                if pygame.Rect.collidepoint(block.rect, mouse_pos[0], mouse_pos[1]):
                    if isinstance(block, Ice):
                        pygame.mixer.Sound.play(water_digEffect)
                    else:
                        pygame.mixer.Sound.play(digEffect1)
                        pygame.mixer.Sound.play(digEffect2)
                        pygame.mixer.Sound.play(digEffect3)

                        breakPercent = (breakTimeLast / 1000) * 33.333
                        if breakPercent >= 99:
                            breakPercent = 100

                        break_counter = pygame.font.SysFont(TEXT_FONT, 36)
                        break_counter = break_counter.render(str(breakPercent), 1, LIGHT_BLUE)

                        if 3 <= breakTimeLast / 1000.0 <= 3.1:
                            airList3.add(Air(block.rect.x, block.rect.y))
                            blocksList3.remove(block)
                            breakTimeLast = 0
                            blocks_broken += 1

                        screen.blit(break_counter, (player.rect.x, player.rect.y - 30))

        for block in blocksList4:
            # Player Distance:
            if abs(block.rect.x - player.rect.x) <= 100 and (
                    abs(block.rect.y - (player.rect.y + 75)) <= 50 or abs(block.rect.y - player.rect.y) <= 50):

                if pygame.Rect.collidepoint(block.rect, mouse_pos[0], mouse_pos[1]):
                    if isinstance(block, Water):
                        pygame.mixer.Sound.play(water_digEffect)

                        breakPercent = (breakTimeLast / 1000) * 33.333
                        if breakPercent >= 99:
                            breakPercent = 100

                        break_counter = pygame.font.SysFont(TEXT_FONT, 36)
                        break_counter = break_counter.render(str(breakPercent), 1, LIGHT_BLUE)

                        if 3 <= breakTimeLast / 1000.0 <= 3.1:
                            airList4.add(Air(block.get_x(), block.get_y()))
                            blocksList4.remove(block)
                            breakTimeLast = 0
                            blocks_broken += 1

                        screen.blit(break_counter, (player.rect.x, player.rect.y - 30))

                    else:
                        pygame.mixer.Sound.play(digEffect1)
                        pygame.mixer.Sound.play(digEffect2)
                        pygame.mixer.Sound.play(digEffect3)

                        breakPercent = (breakTimeLast / 1000) * 33.333
                        if breakPercent >= 99:
                            breakPercent = 100

                        break_counter = pygame.font.SysFont(TEXT_FONT, 36)
                        break_counter = break_counter.render(str(breakPercent), 1, LIGHT_BLUE)

                        if 3 <= breakTimeLast / 1000.0 <= 3.1:
                            airList4.add(Air(block.rect.x, block.rect.y))
                            blocksList4.remove(block)
                            blocks_broken += 1

                        screen.blit(break_counter, (player.rect.x, player.rect.y - 30))

    # isJump Check

    if len(blockCollision1) > 0 or len(blockCollision2) > 0 or len(blockCollision3) > 0 or (len(
            blockCollision4) > 0) or player.rect.y + 75 > HEIGHT - 10 or len(woodCollision) > 0:
        player.isJump = False

    # Jumping
    if jump_start:
        player.jump()
        jump_timeStop = pygame.time.get_ticks() - jump_timeStart
        if jump_timeStop / 1000.0 < 0.25 and block_is_above == 0:
            player.rect.y -= 14
        if block_is_above == 1:
            player.rect.y += 20
            block_is_above = 0
            jump_start = False

        if jump_timeStop / 1000.0 > 0.25:
            jump_start = False

    elif not jump_start:
        block_is_above = 0

    # Fix landing:
    if not jump_start:
        for collided in blockCollision1:
            if collided.rect.y + 25 >= player.rect.y + 75 > collided.rect.y + 1:
                player.rect.y = player.rect.y / 1
                player.rect.y -= 1

        for collided in blockCollision2:
            if collided.rect.y + 25 >= player.rect.y + 75 > collided.rect.y + 1:
                player.rect.y = player.rect.y / 1
                player.rect.y -= 1

        for collided in blockCollision3:
            if collided.rect.y + 25 >= player.rect.y + 75 > collided.rect.y + 1:
                player.rect.y = player.rect.y / 1
                player.rect.y -= 1

        for collided in blockCollision4:
            if (collided.rect.y + 25 >= player.rect.y + 75 > collided.rect.y + 1) and not isinstance(collided, Water):
                player.rect.y = player.rect.y / 1
                player.rect.y -= 1

        for collided in woodCollision:
            if collided.rect.y + 25 >= player.rect.y + 75 > collided.rect.y + 1:
                player.rect.y = player.rect.y / 1
                player.rect.y -= 1

    # Gravity:
    if (len(blockCollision1) <= 0 and len(blockCollision2) <= 0 and len(blockCollision3) <= 0 and len(
            blockCollision4) <= 0 and len(woodCollision) <= 0 and not jump_start) or (block_is_above == 1):
        player.rect.y += 10

    # Water Gravity :

    for obj in blockCollision4:
        if isinstance(obj, Sand) or isinstance(obj, Sandstone):
            waterCheck = 1
            notWaterCount += 1

    for obj in woodCollision:
        if isinstance(obj, Air) and obj.isWood == 1:
            waterCheck = 1
            notWaterCount += 1

    if len(blockCollision4) > 0 and not jump_start:
        if waterCheck == 0:
            player.rect.y += 2
        waterSurfaceCount += 1

    # Background Check:

    if len(blockCollision1) > 0:
        if type1 == "forest" and not isNight:
            biome_type = forest_bc
            subBiome_type = forest_ubc
            music_type = FOREST_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_clean()

        elif type1 == "desert" and not isNight:
            biome_type = desert_bc
            subBiome_type = desert_ubc
            music_type = DESERT_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_dirty()

        elif type1 == "snow" and not isNight:
            biome_type = snow_bc
            subBiome_type = snow_ubc
            music_type = SNOW_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_frozen()

        elif type1 == "ocean" and not isNight:
            biome_type = beach_bc
            subBiome_type = beach_ubc
            music_type = OCEAN_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_clean()

    if len(blockCollision2) > 0:
        if type2 == "forest" and not isNight:
            biome_type = forest_bc
            subBiome_type = forest_ubc
            music_type = FOREST_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_clean()

        elif type2 == "desert" and not isNight:
            biome_type = desert_bc
            subBiome_type = desert_ubc
            music_type = DESERT_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_dirty()

        elif type2 == "snow" and not isNight:
            biome_type = snow_bc
            subBiome_type = snow_ubc
            music_type = SNOW_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_frozen()

        elif type2 == "ocean" and not isNight:
            biome_type = beach_bc
            subBiome_type = beach_ubc
            music_type = OCEAN_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_clean()

    if len(blockCollision3) > 0:
        if type3 == "forest" and not isNight:
            biome_type = forest_bc
            subBiome_type = forest_ubc
            music_type = FOREST_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_clean()

        elif type3 == "desert" and not isNight:
            biome_type = desert_bc
            subBiome_type = desert_ubc
            music_type = DESERT_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_dirty()

        elif type3 == "snow" and not isNight:
            biome_type = snow_bc
            subBiome_type = snow_ubc
            music_type = SNOW_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_frozen()

        elif type3 == "ocean" and not isNight:
            biome_type = beach_bc
            subBiome_type = beach_ubc
            music_type = OCEAN_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_clean()

    if len(blockCollision4) > 0:
        if type4 == "forest" and not isNight:
            biome_type = forest_bc
            subBiome_type = forest_ubc
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_clean()

            music_type = FOREST_MUSIC
        elif type4 == "desert" and not isNight:
            biome_type = desert_bc
            subBiome_type = desert_ubc
            music_type = DESERT_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_dirty()

        elif type4 == "snow" and not isNight:
            biome_type = snow_bc
            subBiome_type = snow_ubc
            music_type = SNOW_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_frozen()

        elif type4 == "ocean" and not isNight:
            biome_type = beach_bc
            subBiome_type = beach_ubc
            music_type = OCEAN_MUSIC
            for obj in blocksList4:
                if isinstance(obj, Water):
                    obj.set_clean()

    # Music System:

    if music_type != currentMusic_type:
        pygame.mixer_music.load(music_type)
        pygame.mixer_music.play(-1)

    currentMusic_type = music_type

    # Player Borders [Water,Underground,WorldBorders]:

    if player.rect.x + 50 >= WIDTH:  # >X
        player.rect.x -= 3

    elif player.rect.x <= 0:  # <X
        player.rect.x += 3

    if player.rect.y + 70 >= HEIGHT:  # >Y
        player.rect.y -= 10

    elif player.rect.y <= 0:  # <Y
        player.rect.y += 14

    for collided in blockCollision1:
        if player.rect.y <= collided.rect.y + 30 <= player.rect.y + 70:
            playerBlock = 0
        if collided.rect.y + 25 <= player.rect.y <= collided.rect.y + 50:
            block_is_above = 1

    for collided in blockCollision2:
        if player.rect.y <= collided.rect.y + 30 <= player.rect.y + 70:
            playerBlock = 0
        if collided.rect.y + 25 <= player.rect.y <= collided.rect.y + 50:
            block_is_above = 1

    for collided in blockCollision3:
        if player.rect.y <= collided.rect.y + 30 <= player.rect.y + 70:
            playerBlock = 0
        if collided.rect.y + 25 <= player.rect.y <= collided.rect.y + 50:
            block_is_above = 1

    for collided in blockCollision4:
        if player.rect.y <= collided.rect.y + 30 <= player.rect.y + 70 and not isinstance(collided, Water):
            playerBlock = 0
        if collided.rect.y + 25 <= player.rect.y <= collided.rect.y + 50 and not isinstance(collided, Water):
            block_is_above = 1

        # Wood collisions:
    for collided in woodCollision:
        if player.rect.y <= collided.rect.y <= player.rect.y + 70:
            playerBlock = 0
        elif player.rect.y <= collided.rect.y + 50 <= player.rect.y + 70:
            playerBlock = 0

        if collided.rect.y + 25 <= player.rect.y <= collided.rect.y + 50:
            block_is_above = 1

    if len(blockCollision1) >= 0 or len(blockCollision2) >= 0 or len(blockCollision3) >= 0 or len(
            blockCollision4) >= 0 or len(woodCollision) >= 0:

        if (Keys[pygame.K_d] or Keys[pygame.K_RIGHT]) and playerBlock == 0:
            player.rect.x -= 3
        if notWaterCount <= 3 and len(blockCollision4) > 0:
            player.rect.x += 3

        if (Keys[pygame.K_a] or Keys[pygame.K_LEFT]) and playerBlock == 0:
            player.rect.x += 3
        if notWaterCount <= 3 and len(blockCollision4) > 0:
            player.rect.x -= 3

    # GAME IN GAME FUNCTIONS SECTION :

    # Day And Night Cycle
    dn_cycle = pygame.time.get_ticks()

    if sunX >= WIDTH and not isNight:
        isNight = True
        biome_type = night_bc
        subBiome_type = night_ubc
        music_type = NIGHT_MUSIC
        day_start_time = pygame.time.get_ticks()
        sunX = 0
        sunY = HEIGHT / 2 - 300

        for obj in blocksList4:
            if isinstance(obj, Water):
                obj.set_bloody()

    elif moonX >= WIDTH and isNight:
        isNight = False
        days_count += 1
        wood_inv += 10
        day_start_time = pygame.time.get_ticks()
        moonX = 0
        moonY = HEIGHT / 2 - 300

    # Sun & Moon :
    if not isNight:
        spawn_once = 0
        boss_defeat = False
        day_specific_time = (pygame.time.get_ticks() - day_start_time) / 1000.0
        if sunX >= WIDTH / 2:
            turn_cycle_sun = 1
        elif sunX <= WIDTH / 2:
            turn_cycle_sun = 0

        if turn_cycle_sun == 0 and (0.02 >= day_specific_time % 1 >= 0):
            sunX += (WIDTH / 2) / (day_time / 2)
            sunY -= ((HEIGHT / 2) - 300) / (day_time / 2)
        elif turn_cycle_sun == 1 and (0.02 >= day_specific_time % 1 >= 0):
            sunX += (WIDTH / 2) / (day_time / 2)
            sunY += ((HEIGHT / 2) - 300) / (day_time / 2)

        screen.blit(sun_img, (sunX, sunY))

    elif isNight:
        boss_defeat = True
        day_specific_time = (pygame.time.get_ticks() - day_start_time) / 1000.0
        if moonX >= WIDTH / 2:
            turn_cycle_moon = 1
        elif moonX <= WIDTH / 2:
            turn_cycle_moon = 0

        if turn_cycle_moon == 0 and (0.02 >= day_specific_time % 1 >= 0):
            moonX += (WIDTH / 2) / (day_time / 2)
            moonY -= ((HEIGHT / 2) - 300) / (day_time / 2)
        elif turn_cycle_moon == 1 and (0.02 >= day_specific_time % 1 >= 0):
            moonX += (WIDTH / 2) / (day_time / 2)
            moonY += ((HEIGHT / 2) - 300) / (day_time / 2)

        if spawn_once == 0 and not boss_defeat:
            boss_HP += 1
            random_boss = random.randint(1, 6)
            boss = Boss(WIDTH / 2, HEIGHT / 2)

            # Boss set skin :
            if random_boss == 1:
                boss.set_brain()
            elif random_boss == 2:
                boss.set_martian()
            elif random_boss == 3:
                boss.set_moonLord()
            elif random_boss == 4:
                boss.set_skeleton()
            elif random_boss == 5:
                boss.set_skeleton_prime()
            elif random_boss == 6:
                boss.set_pillar()

        spawn_once += 1

        screen.blit(moon_img, (moonX, moonY))

    # Clouds System :
    cloud1X += cloud_velocity
    cloud2X += cloud_velocity
    cloud3X += cloud_velocity

    if cloud1X >= WIDTH:
        cloud1X = 0
    if cloud2X >= WIDTH:
        cloud2X = 0
    if cloud3X >= WIDTH:
        cloud3X = 0

    screen.blit(cloud1_img, (cloud1X, cloud1Y))
    screen.blit(cloud2_img, (cloud2X, cloud2Y))
    screen.blit(cloud3_img, (cloud3X, cloud3Y))

    if boss != "":
        # Boss AI :
        if boss.rect.x > player.rect.x:
            boss.rect.x -= 1
        elif boss.rect.x < player.rect.x:
            boss.rect.x += 1
        if boss.rect.y > player.rect.y:
            boss.rect.y -= 1
        elif boss.rect.y < player.rect.y:
            boss.rect.y += 1

        # Boss HP :
        # Player Distance:
        if abs(boss.rect.x - player.rect.x) <= 100 and (
                abs(boss.rect.y - (player.rect.y + 75)) <= 50 or abs(boss.rect.y - player.rect.y) <= 50):
            if Buttons[RIGHT - 1]:
                if pygame.Rect.collidepoint(boss.rect, mouse_pos[0], mouse_pos[1]):
                    boss.HP -= 1

        # Draw Boss :
        if boss.HP > 0 and boss_defeat:
            screen.blit(boss.image, (boss.rect.x, boss.rect.y))

    # Draw Player
    screen.blit(player.player_image, (player.rect.x, player.rect.y))

    # GUI SECTION :

    # HP Counter
    index = 0
    for heart in hp_list:
        screen.blit(hp_image, (hp_list[index] + 20, 10))
        index += 1
    # Blocks Broken Counter :
    broken_counter = pygame.font.SysFont(TEXT_FONT, 36)
    broken_counter = broken_counter.render("Blocks Broken: " + str(blocks_broken), True, GRAY)
    screen.blit(broken_counter, (25, 40))

    # Inv Counter :
    inv_counter = pygame.font.SysFont(TEXT_FONT, 36)
    inv_counter = inv_counter.render("Quantity : " + str(wood_inv), True, ORANGE)
    screen.blit(wood_icon, (WIDTH / 2 - 30, 10))
    screen.blit(inv_counter, (WIDTH / 2, 10))

    # Game FPS Counter:
    fps = int(Clock.get_fps())
    fps_counter = pygame.font.SysFont(TEXT_FONT, 36)
    fps_counter = fps_counter.render("FPS: " + str(fps), True, LIME)
    screen.blit(fps_counter, (WIDTH - 100, 10))

    # HP updater
    if len(hp_list) != player.HP:
        hp_list.append(hp_list[-1] + 25)

    # Days Gone Counter:

    day_text = pygame.font.SysFont(TEXT_FONT, 36)
    day_text = day_text.render("Days: " + str(days_count), True, CRIMSON_RED)
    screen.blit(day_text, (WIDTH - 100, 35))

    # Variable Reset :
    waterCheck = 0
    notWaterCount = 0
    idle_check = 0
    playerBlock = 1
    breakBlock = False
    breakPercent = 0

    # Py_game Update Frame :

    Clock.tick(REFRESH_RATE)
    pygame.display.flip()

pygame.mixer_music.stop()

play_once = 0

while RunningLose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            RunningLose = False
            print "HAHA NOOV TEAM"
            exit("Loser!")
    # You died text :
    died_txt = pygame.font.SysFont(TEXT_FONT, 200, True)
    died_txt = died_txt.render("YOU DIED", True, GRAY)
    if play_once == 0:
        pygame.mixer_music.load(YOU_DIED_MUSIC)
        pygame.mixer_music.play()
        play_once += 1

    # Screen Fill :
    screen.blit(graveyard_bc, (0, 0))
    screen.blit(died_txt, (WIDTH / 2 - 350, HEIGHT / 2 - 100))
    pygame.display.flip()
# Stop Py_game :
pygame.quit()
