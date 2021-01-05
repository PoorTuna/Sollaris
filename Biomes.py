from Blocks import *

import ctypes

user32 = ctypes.windll.user32


def generate_forest(biome_place, (width, height)):
    biome_type = "forest"

    block_list = pygame.sprite.Group()
    air_list = pygame.sprite.Group()
    block_detail = []
    biome_length = width / 4
    biome_length = biome_length * biome_place
    biome_height_top = (height / 2) / 50 + 6
    biome_height_bottom = height / 50
    air_height_top = 0
    air_height_bottom = biome_height_top
    for lineHeight1 in xrange(air_height_top, air_height_bottom, 1):
        for lineLength1 in xrange(biome_length - 400, biome_length, 50):
            air_block = Air(lineLength1, lineHeight1 * 50)
            air_list.add(air_block)
            block_detail.append((air_block.get_x(), air_block.get_y()))

    # Generate Blocks:
    for lineHeight in xrange(biome_height_top, biome_height_bottom, 1):
        for lineLength in xrange(biome_length - 400, biome_length, 50):
            if lineHeight == biome_height_top:
                grass_block = Grass(lineLength, lineHeight * 50)
                block_list.add(grass_block)
                block_detail.append((grass_block.get_x(), grass_block.get_y()))

            elif lineHeight == biome_height_top + 3:
                stone_block = Stone(lineLength, lineHeight * 50)
                block_list.add(stone_block)
                block_detail.append((stone_block.get_x(), stone_block.get_y()))

            else:
                dirt_block = Dirt(lineLength, lineHeight * 50)
                block_list.add(dirt_block)
                block_detail.append((dirt_block.get_x(), dirt_block.get_y()))  # Blocks X , Y  coordinate.

    return block_list, biome_type, air_list


def generate_desert(biome_place, (width, height)):
    biome_type = "desert"

    block_list = pygame.sprite.Group()
    air_list = pygame.sprite.Group()
    block_detail = []
    biome_length = width / 4
    biome_length = biome_length * biome_place
    biome_height_top = (height / 2) / 50 + 6
    biome_height_bottom = height / 50
    air_height_top = 0
    air_height_bottom = biome_height_top
    for lineHeight1 in xrange(air_height_top, air_height_bottom, 1):
        for lineLength1 in xrange(biome_length - 400, biome_length, 50):
            air_block = Air(lineLength1, lineHeight1 * 50)
            air_list.add(air_block)
            block_detail.append((air_block.get_x(), air_block.get_y()))

    # Generate Blocks:
    for lineHeight in xrange(biome_height_top, biome_height_bottom, 1):
        for lineLength in xrange(biome_length - 400, biome_length, 50):
            if lineHeight == biome_height_top:
                sand_block = Sand(lineLength, lineHeight * 50)
                block_list.add(sand_block)
                block_detail.append((sand_block.get_x(), sand_block.get_y()))

            elif lineHeight == biome_height_top + 3:
                sandstone_block = Sandstone(lineLength, lineHeight * 50)
                block_list.add(sandstone_block)
                block_detail.append((sandstone_block.get_x(), sandstone_block.get_y()))

            else:
                sand_block = Sand(lineLength, lineHeight * 50)
                block_list.add(sand_block)
                block_detail.append((sand_block.get_x(), sand_block.get_y()))  # Blocks X , Y  coordinate.

    return block_list, biome_type, air_list


def generate_ocean(biome_place, (width, height)):
    biome_type = "ocean"

    block_list = pygame.sprite.Group()
    air_list = pygame.sprite.Group()
    block_detail = []
    biome_length = width / 4
    biome_length = biome_length * biome_place
    biome_height_top = (height / 2) / 50 + 6
    biome_height_bottom = height / 50
    air_height_top = 0
    air_height_bottom = biome_height_top
    for lineHeight1 in xrange(air_height_top, air_height_bottom, 1):
        for lineLength1 in xrange(biome_length - 400, biome_length, 50):
            air_block = Air(lineLength1, lineHeight1 * 50)
            air_list.add(air_block)
            block_detail.append((air_block.get_x(), air_block.get_y()))

    # Generate Blocks:
    for lineHeight in xrange(biome_height_top, biome_height_bottom, 1):
        for lineLength in xrange(biome_length - 400, biome_length, 50):
            if biome_place == 2 or biome_place == 3:
                if (lineHeight == biome_height_top or lineHeight == biome_height_top + 1) and (
                        biome_length - 150 >= lineLength >= 100 + biome_length - 400):
                    water_block = Water(lineLength, lineHeight * 50)
                    block_list.add(water_block)
                    block_detail.append((water_block.get_x(), water_block.get_y()))

                elif lineHeight == biome_height_top + 3:
                    sandstone_block = Sandstone(lineLength, lineHeight * 50)
                    block_list.add(sandstone_block)
                    block_detail.append((sandstone_block.get_x(), sandstone_block.get_y()))

                else:
                    sand_block = Sand(lineLength, lineHeight * 50)
                    block_list.add(sand_block)
                    block_detail.append((sand_block.get_x(), sand_block.get_y()))  # Blocks X , Y  coordinate.

            elif biome_place == 1:
                if (lineHeight == biome_height_top or lineHeight == biome_height_top + 1) and (
                        biome_length - 200 >= lineLength >= 100 + biome_length - 400):
                    water_block = Water(lineLength, lineHeight * 50)
                    block_list.add(water_block)
                    block_detail.append((water_block.get_x(), water_block.get_y()))

                elif lineHeight == biome_height_top + 3:
                    sandstone_block = Sandstone(lineLength, lineHeight * 50)
                    block_list.add(sandstone_block)
                    block_detail.append((sandstone_block.get_x(), sandstone_block.get_y()))

                else:
                    sand_block = Sand(lineLength, lineHeight * 50)
                    block_list.add(sand_block)
                    block_detail.append((sand_block.get_x(), sand_block.get_y()))  # Blocks X , Y  coordinate.

            elif biome_place == 4:
                if (lineHeight == biome_height_top or lineHeight == biome_height_top + 1) and (
                        biome_length >= lineLength >= 100 + biome_length - 250):
                    water_block = Water(lineLength, lineHeight * 50)
                    block_list.add(water_block)
                    block_detail.append((water_block.get_x(), water_block.get_y()))

                elif lineHeight == biome_height_top + 3:
                    sandstone_block = Sandstone(lineLength, lineHeight * 50)
                    block_list.add(sandstone_block)
                    block_detail.append((sandstone_block.get_x(), sandstone_block.get_y()))

                else:
                    sand_block = Sand(lineLength, lineHeight * 50)
                    block_list.add(sand_block)
                    block_detail.append((sand_block.get_x(), sand_block.get_y()))  # Blocks X , Y  coordinate.

    return block_list, biome_type, air_list


def generate_snow(biome_place, (width, height)):
    biome_type = "snow"

    block_list = pygame.sprite.Group()
    air_list = pygame.sprite.Group()
    block_detail = []
    biome_length = width / 4
    biome_length = biome_length * biome_place
    biome_height_top = (height / 2) / 50 + 6
    biome_height_bottom = height / 50
    air_height_top = 0
    air_height_bottom = biome_height_top
    for lineHeight1 in xrange(air_height_top, air_height_bottom, 1):
        for lineLength1 in xrange(biome_length - 400, biome_length, 50):
            air_block = Air(lineLength1, lineHeight1 * 50)
            air_list.add(air_block)
            block_detail.append((air_block.get_x(), air_block.get_y()))

    # Generate Blocks:
    for lineHeight in xrange(biome_height_top, biome_height_bottom, 1):
        for lineLength in xrange(biome_length - 400, biome_length, 50):
            if lineHeight == biome_height_top:
                snow_block = Snow(lineLength, lineHeight * 50)
                block_list.add(snow_block)
                block_detail.append((snow_block.get_x(), snow_block.get_y()))

            elif lineHeight == biome_height_top + 3:
                ice_block = Ice(lineLength, lineHeight * 50)
                block_list.add(ice_block)
                block_detail.append((ice_block.get_x(), ice_block.get_y()))

            else:
                frozen_dirt_block = FrozenDirt(lineLength, lineHeight * 50)
                block_list.add(frozen_dirt_block)
                block_detail.append((frozen_dirt_block.get_x(), frozen_dirt_block.get_y()))  # Blocks X , Y  coordinate.

    return block_list, biome_type, air_list
