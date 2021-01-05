from Assets import *


class Sand(pygame.sprite.Sprite):  # Sand block sprite
    def __init__(self, x=0, y=0):
        super(Sand, self).__init__()

        self.image = pygame.image.load(SAND_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y


class Sandstone(pygame.sprite.Sprite):  # SandStone block sprite
    def __init__(self, x=0, y=0):
        super(Sandstone, self).__init__()

        self.image = pygame.image.load(SANDSTONE_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y


class Stone(pygame.sprite.Sprite):  # Stone block sprite
    def __init__(self, x=0, y=0):
        super(Stone, self).__init__()

        self.image = pygame.image.load(STONE_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y


class Ice(pygame.sprite.Sprite):  # Stone block sprite
    def __init__(self, x=0, y=0):
        super(Ice, self).__init__()

        self.image = pygame.image.load(ICE_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y


class Grass(pygame.sprite.Sprite):  # Grass block sprite
    def __init__(self, x=0, y=0):
        super(Grass, self).__init__()

        self.image = pygame.image.load(GRASS_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y


class Snow(pygame.sprite.Sprite):  # Snow block sprite
    def __init__(self, x=0, y=0):
        super(Snow, self).__init__()

        self.image = pygame.image.load(SNOW_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y


class Dirt(pygame.sprite.Sprite):  # Dirt block sprite
    def __init__(self, x=0, y=0):
        super(Dirt, self).__init__()

        self.image = pygame.image.load(DIRT_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y


class FrozenDirt(pygame.sprite.Sprite):  # FrozenDirt block sprite
    def __init__(self, x=0, y=0):
        super(FrozenDirt, self).__init__()

        self.image = pygame.image.load(FROZENDIRT_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y


class Air(pygame.sprite.Sprite):  # Wood block sprite
    def __init__(self, x=0, y=0):
        super(Air, self).__init__()

        self.image = pygame.image.load(AIR_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.isWood = 0

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y

    def set_wood(self):
        self.isWood = 1
        self.image = pygame.image.load(WOOD_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))


class Water(pygame.sprite.Sprite):  # Water block sprite
    def __init__(self, x=0, y=0):
        super(Water, self).__init__()

        self.image = pygame.image.load(CLEANWATER_DST)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_alpha(180)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    def set_pos(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y

    def set_clean(self):
        self.image = pygame.image.load(CLEANWATER_DST)
        self.image.set_alpha(180)

    def set_dirty(self):
        self.image = pygame.image.load(DIRTYWATER_DST)
        self.image.set_alpha(180)

    def set_frozen(self):
        self.image = pygame.image.load(FROZENWATER_DST)
        self.image.set_alpha(180)

    def set_bloody(self):
        self.image = pygame.image.load(BLOODYWATER_DST)
        self.image.set_alpha(180)
