import pygame.sprite
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_HEIGHT, player_x, player_y):
        super().__init__()
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.image = pygame.image.load('resources/images/beaver.png')
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.direction = 'right'

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95
        if self.rect.y >= self.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = self.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += self.speed
        self.rect.y -= self.speed

    def go_left(self):
        if self.direction != 'left':
            self.direction = 'left'
            self.flip()

        self.rect.x -= self.speed

    def go_right(self):
        if self.direction != 'right':
            self.direction = 'right'
            self.flip()

        self.rect.x += self.speed

    def stop(self):
        self.change_x = 0

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
