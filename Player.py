from Assets import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super(Player, self).__init__()
        self.HP = 10
        self.player_image = player_right_img
        self.isJump = True
        self.player_velocity = 0
        self.player_lastPlace = 1
        self.startJumpTime = 0
        self.stopJumpTime = 0

        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_right(self):
        if self.isJump:
            self.player_image = player_jumpRight_img
        else:
            self.player_image = player_right_img

        self.player_lastPlace = 1
        self.rect.x += 3

    def move_left(self):
        if self.isJump:
            self.player_image = player_jumpLeft_img
        else:
            self.player_image = player_left_img

        self.player_lastPlace = 2
        self.rect.x -= 3

    def idle(self):
        if self.player_lastPlace == 1:
            self.player_image = player_right_img
        elif self.player_lastPlace == 2:
            self.player_image = player_left_img

    def jump(self):
        if self.player_lastPlace == 1:
            self.player_image = player_jumpRight_img
        elif self.player_lastPlace == 2:
            self.player_image = player_jumpLeft_img
        self.isJump = True

    def start_jumping(self, time):
        self.startJumpTime = time

        return self.startJumpTime
