from Assets import *


class Boss(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, hp=10):
        super(Boss, self).__init__()

        self.image = boss_moon_lord

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.HP = hp

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def return_image(self):
        return self.image

    def set_x(self, x=0):
        self.rect.x = x

    def set_y(self, y=0):
        self.rect.y = y

    def set_moonLord(self):
        self.image = boss_moon_lord

    def set_skeleton(self):
        self.image = boss_skeleton1

    def set_skeleton_prime(self):
        self.image = boss_skeleton2

    def set_brain(self):
        self.image = boss_brain

    def set_pillar(self):
        self.image = boss_pillar

    def set_martian(self):
        self.image = boss_martian
