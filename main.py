import pygame
from pygame import Surface
from pygame.locals import *
from player import Player
from game import Game

SCREEN_WIDTH = 1060
SCREEN_HEIGHT = 547
clock = pygame.time.Clock()
money = [
    pygame.image.load('images/money/1.png'),
    pygame.image.load('images/money/2.png'),
    pygame.image.load('images/money/3.png'),
    pygame.image.load('images/money/4.png'),
    pygame.image.load('images/money/5.png'),
    pygame.image.load('images/money/6.png')
]
money_list = []
money_anime_count = 0
money_speed = 10
money_count = 30
points = 0


class Button:
    def __init__(self, text, position):
        self.font = pygame.font.Font(None, 36)
        self.color = pygame.Color("white")
        self.text = self.font.render(text, True, self.color)
        self.rect = self.text.get_rect(center=position)

    def draw(self, surface):
        surface.blit(self.text, self.rect)


def main_menu():
    pygame.init()
    DISPLAY = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(DISPLAY)
    bg = pygame.image.load("resources/images/forest.jpg")
    pygame.display.set_caption("Игра")

    play_button = Button("Играть", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    exit_button = Button("Выйти из игры", (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 50))

    active_sprite_list = pygame.sprite.Group()
    player = Player(SCREEN_HEIGHT, 0, 0)
    active_sprite_list.add(player)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit("QUIT")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    game = Game(screen, SCREEN_HEIGHT, SCREEN_WIDTH)
                    game.run()
                elif exit_button.rect.collidepoint(event.pos):
                    raise SystemExit("QUIT")

        screen.blit(bg, (0, 0))
        play_button.draw(screen)
        exit_button.draw(screen)
        # active_sprite_list.draw(screen)

        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    main_menu()
