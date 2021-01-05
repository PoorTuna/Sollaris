import pygame

# import os

WIDTH = 1600
HEIGHT = 1000

FOLDER_URL = "D:\Users\Student\Desktop\Sollaris"

# Backgrounds DST :

MENU_backgroundSRC = FOLDER_URL + r"\Models\menu\Menu.png"

BEACH_backgroundSRC = FOLDER_URL + r"\Models\background\ocean_background.jpg"
DESERT_backgroundSRC = FOLDER_URL + r"\Models\background\desert_background.jpg"
FOREST_backgroundSRC = FOLDER_URL + r"\Models\background\forest_background.jpg"
SNOW_backgroundSRC = FOLDER_URL + r"\Models\background\snow_background.jpg"
NIGHT_backgroundSRC = FOLDER_URL + r"\Models\background\night_background.jpg"

BEACH_underbackgroundSRC = FOLDER_URL + r"\Models\background\subOcean_background.jpg"
DESERT_underbackgroundSRC = FOLDER_URL + r"\Models\background\subDesert_background.jpg"
FOREST_underbackgroundSRC = FOLDER_URL + r"\Models\background\subForest_background.jpg"
SNOW_underbackgroundSRC = FOLDER_URL + r"\Models\background\subSnow_background.jpg"
NIGHT_underbackgroundSRC = FOLDER_URL + r"\Models\background\subNight_background.jpg"

GRAVEYARD_backgroundSRC = FOLDER_URL + r"\Models\Background\GraveYard.jpg"

# Clouds DST :

CLOUD1_DST = FOLDER_URL + r"\Models\background\Cloud1.png"
CLOUD2_DST = FOLDER_URL + r"\Models\background\Cloud2.png"
CLOUD3_DST = FOLDER_URL + r"\Models\background\Cloud3.png"

# Music DST :

FOREST_MUSIC = FOLDER_URL + r"\Sounds\Day\Forest\Forest_RAIN.mp3"
DESERT_MUSIC = FOLDER_URL + r"\Sounds\Day\Desert\Desert_OST.mp3"
SNOW_MUSIC = FOLDER_URL + r"\Sounds\Day\Snow\Snow_ICE.mp3"
OCEAN_MUSIC = FOLDER_URL + r"\Sounds\Day\Ocean\Ocean_BEACH.mp3"

NIGHT_MUSIC = FOLDER_URL + r"\Sounds\Night\Night_EERIE.mp3"

BOSS_MUSIC1 = FOLDER_URL + r"\Sounds\Boss\Boss_ARCHETYPE.mp3"
BOSS_MUSIC2 = FOLDER_URL + r"\Sounds\Boss\Boss_DARKS.mp3"
BOSS_MUSIC3 = FOLDER_URL + r"\Sounds\Boss\Boss_RUN.mp3"
BOSS_MUSIC4 = FOLDER_URL + r"\Sounds\Boss\Boss_SECONDT.mp3"

MENU_MUSIC1 = FOLDER_URL + r"\Sounds\Menu\Menu_BRAVE.mp3"
MENU_MUSIC2 = FOLDER_URL + r"\Sounds\Menu\Menu_VAULT.mp3"
EASTEREGG_MUSIC = FOLDER_URL + r"\Sounds\EasterEgg\Secret_BTT.mp3"

YOU_DIED_MUSIC = FOLDER_URL + r"\Sounds\Misc\You_Died.mp3"

# Sound Effects DST:

DIG1_SFX = FOLDER_URL + r"\Sounds\Misc\Dig1.wav"
DIG2_SFX = FOLDER_URL + r"\Sounds\Misc\Dig2.wav"
DIG3_SFX = FOLDER_URL + r"\Sounds\Misc\Dig3.wav"
WATERDIG_SFX = FOLDER_URL + r"\Sounds\Misc\WaterDig.wav"
WATERSPLASH_SFX = FOLDER_URL + r"\Sounds\Misc\Splash_0.wav"
PLAYERKILLED_SFX = FOLDER_URL + r"\Sounds\Player\Hurt\Player_Killed.wav"
PLAYERHIT_SFX = FOLDER_URL + r"\Sounds\Player\Hurt\Player_Hit.wav"
MENUCLICK_SFX = FOLDER_URL + r"\Sounds\Misc\Menu_Tick.wav"

# [CONSTANTS] models destination for Blocks DST:

SAND_DST = FOLDER_URL + r"\Models\sand\Sand.png"  # Sand
SANDSTONE_DST = FOLDER_URL + r"\Models\sandstone\Sandstone.jpg"  # SandStone
STONE_DST = FOLDER_URL + r"\Models\stone\Stone.png"  # Stone
GRASS_DST = FOLDER_URL + r"\Models\grass\Grass.png"  # Grass
DIRT_DST = FOLDER_URL + r"\Models\dirt\Dirt.png"  # Dirt
FROZENDIRT_DST = FOLDER_URL + r"\Models\dirt\Frozen_Dirt.png"  # Frozen Dirt
ICE_DST = FOLDER_URL + r"\Models\ice\Ice.jpg"  # Ice
SNOW_DST = FOLDER_URL + r"\Models\grass\Snow.jpg"  # Snow
AIR_DST = FOLDER_URL + r"\Models\air\Air.png"  # Air
WOOD_DST = FOLDER_URL + r"\Models\air\Wood.png"  # Wood

CLEANWATER_DST = FOLDER_URL + r"\Models\water\WaterClean.jpg"  # Clean Water
DIRTYWATER_DST = FOLDER_URL + r"\Models\water\WaterDirty.jpg"  # Dirty Water
FROZENWATER_DST = FOLDER_URL + r"\Models\water\WaterFrozen.jpg"  # Frozen Water
BLOODYWATER_DST = FOLDER_URL + r"\Models\water\WaterBloody.jpg"  # Bloody Water

# Player Skin DST :

PLAYER_LEFT = FOLDER_URL + r"\Models\player\player_left.png"  # Player Left
PLAYER_RIGHT = FOLDER_URL + r"\Models\player\player_right.png"  # Player Right
PLAYER_JUMPLEFT = FOLDER_URL + r"\Models\player\player_jump1.png"  # Player Jump Left
PLAYER_JUMPRIGHT = FOLDER_URL + r"\Models\player\player_jump2.png"  # Player Jump Right

# Boss Skin DST :

BOSS_BRAIN = FOLDER_URL + r"\Models\boss\BrainBoss.png"
BOSS_SKELETON1 = FOLDER_URL + r"\Models\boss\SkeletronBoss.png"
BOSS_SKELETON2 = FOLDER_URL + r"\Models\boss\SkeletronPrimeBoss.png"
BOSS_MOON_LORD = FOLDER_URL + r"\Models\boss\MoonBoss.png"
BOSS_MARTIAN = FOLDER_URL + r"\Models\boss\MartianBoss.png"
BOSS_PILLAR = FOLDER_URL + r"\Models\boss\SollarBoss.png"

# Icons DST:

PLAYER_HPIMAGE = FOLDER_URL + r"\Models\background\HeartHP.png"
BLOCKS_ICON = FOLDER_URL + r"\Models\background\WoodICON.png"

GAME_ICON = FOLDER_URL + r"\Models\menu\GameLogo.png"

# Sun & Moon DST:

MOON_DST = FOLDER_URL + r"\Models\background\Moon.png"
SUN_DST = FOLDER_URL + r"\Models\background\Sun.png"

# Py_game IMAGE load:

# Py_game Upper backgrounds:

menu_bc = pygame.image.load(MENU_backgroundSRC)
menu_bc = pygame.transform.scale(menu_bc, (WIDTH, HEIGHT))

graveyard_bc = pygame.image.load(GRAVEYARD_backgroundSRC)
graveyard_bc = pygame.transform.scale(graveyard_bc, (WIDTH, HEIGHT))

beach_bc = pygame.image.load(BEACH_backgroundSRC)
beach_bc = pygame.transform.scale(beach_bc, (WIDTH, HEIGHT - 200))

desert_bc = pygame.image.load(DESERT_backgroundSRC)
desert_bc = pygame.transform.scale(desert_bc, (WIDTH, HEIGHT - 200))

forest_bc = pygame.image.load(FOREST_backgroundSRC)
forest_bc = pygame.transform.scale(forest_bc, (WIDTH, HEIGHT - 200))

snow_bc = pygame.image.load(SNOW_backgroundSRC)
snow_bc = pygame.transform.scale(snow_bc, (WIDTH, HEIGHT - 200))

night_bc = pygame.image.load(NIGHT_backgroundSRC)
night_bc = pygame.transform.scale(night_bc, (WIDTH, HEIGHT - 200))

# Py_game Bottom backgrounds:

beach_ubc = pygame.image.load(BEACH_underbackgroundSRC)
beach_ubc = pygame.transform.scale(beach_ubc, (WIDTH, HEIGHT - 200))

desert_ubc = pygame.image.load(DESERT_underbackgroundSRC)
desert_ubc = pygame.transform.scale(desert_ubc, (WIDTH, 200))

forest_ubc = pygame.image.load(FOREST_underbackgroundSRC)
forest_ubc = pygame.transform.scale(forest_ubc, (WIDTH, 200))

snow_ubc = pygame.image.load(SNOW_underbackgroundSRC)
snow_ubc = pygame.transform.scale(snow_ubc, (WIDTH, 200))

night_ubc = pygame.image.load(NIGHT_underbackgroundSRC)
night_ubc = pygame.transform.scale(night_ubc, (WIDTH, 200))

# Py_game Clouds Images :

cloud1_img = pygame.image.load(CLOUD1_DST)
cloud1_img = pygame.transform.scale(cloud1_img, (120, 40))

cloud2_img = pygame.image.load(CLOUD2_DST)
cloud2_img = pygame.transform.scale(cloud2_img, (60, 40))

cloud3_img = pygame.image.load(CLOUD3_DST)
cloud3_img = pygame.transform.scale(cloud3_img, (60, 40))

# Py_game Sun & Moon Images :

sun_img = pygame.image.load(SUN_DST)
sun_img = pygame.transform.scale(sun_img, (75, 75))

moon_img = pygame.image.load(MOON_DST)
moon_img = pygame.transform.scale(moon_img, (50, 50))

# Py_game Player Images Skins :

player_left_img = pygame.image.load(PLAYER_LEFT)
player_left_img = pygame.transform.scale(player_left_img, (51, 75))

player_right_img = pygame.image.load(PLAYER_RIGHT)
player_right_img = pygame.transform.scale(player_right_img, (51, 75))

player_jumpLeft_img = pygame.image.load(PLAYER_JUMPLEFT)
player_jumpLeft_img = pygame.transform.scale(player_jumpLeft_img, (51, 75))

player_jumpRight_img = pygame.image.load(PLAYER_JUMPRIGHT)
player_jumpRight_img = pygame.transform.scale(player_jumpRight_img, (51, 75))

# Py_game Boss Image Skins :
boss_moon_lord = pygame.image.load(BOSS_MOON_LORD)
boss_moon_lord = pygame.transform.scale(boss_moon_lord, (350, 300))

boss_brain = pygame.image.load(BOSS_BRAIN)
boss_brain = pygame.transform.scale(boss_brain, (350, 300))

boss_skeleton1 = pygame.image.load(BOSS_SKELETON1)
boss_skeleton1 = pygame.transform.scale(boss_skeleton1, (350, 300))

boss_skeleton2 = pygame.image.load(BOSS_SKELETON2)
boss_skeleton2 = pygame.transform.scale(boss_skeleton2, (350, 300))

boss_martian = pygame.image.load(BOSS_MARTIAN)
boss_martian = pygame.transform.scale(boss_martian, (350, 300))

boss_pillar = pygame.image.load(BOSS_PILLAR)
boss_pillar = pygame.transform.scale(boss_pillar, (350, 300))

# Py_game Icon Images :

player_hpImage = pygame.image.load(PLAYER_HPIMAGE)
player_hpImage = pygame.transform.scale(player_hpImage, (25, 25))

wood_icon = pygame.image.load(BLOCKS_ICON)
wood_icon = pygame.transform.scale(wood_icon, (25, 25))

game_logo = pygame.image.load(GAME_ICON)
game_logo = pygame.transform.scale(game_logo, (550, 150))

# Py_game SoundEffect Load:
pygame.mixer.init()

digEffect1 = pygame.mixer.Sound(DIG1_SFX)
digEffect2 = pygame.mixer.Sound(DIG2_SFX)
digEffect3 = pygame.mixer.Sound(DIG3_SFX)
water_digEffect = pygame.mixer.Sound(WATERDIG_SFX)

menuClick = pygame.mixer.Sound(MENUCLICK_SFX)

playerDie = pygame.mixer.Sound(PLAYERKILLED_SFX)
playerHit = pygame.mixer.Sound(PLAYERHIT_SFX)

waterSplash = pygame.mixer.Sound(WATERSPLASH_SFX)
