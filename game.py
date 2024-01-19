import random

import pygame

from player import Player

from menu import Menu


class Game:
    def __init__(self, screen, SCREEN_HEIGHT, SCREEN_WIDTH):
        self.screen = screen
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH

    def run(self):
        pygame.key.set_repeat(200, 70)
        bg = pygame.image.load("resources/images/forest.jpg")
        pygame.display.set_caption("Игра")

        player_x = 500
        player_y = 245

        active_sprite_list = pygame.sprite.Group()
        player = Player(self.SCREEN_HEIGHT, player_x, player_y)
        active_sprite_list.add(player)

        def vlo():
            pass

        money = [
            pygame.image.load('images/money/1.png'),
            pygame.image.load('images/money/2.png'),
            pygame.image.load('images/money/3.png'),
            pygame.image.load('images/money/4.png'),
            pygame.image.load('images/money/5.png'),
            pygame.image.load('images/money/6.png')
        ]
        fontt = pygame.font.Font('resources/fonts/arial.ttf', 50)
        money_list = []
        money_anime_count = 0
        money_speed = 10
        money_count = 30
        points = 0
        clock = pygame.time.Clock()
        counter = 0
        running = True
        menu = Menu()
        menu.append_option("Quit", quit)
        menu.append_option("Volume", vlo())

        while running:
            label_points = fontt.render(str(points) + '(30)', False, (193, 196, 199))
            self.screen.blit(bg, (0, 0))
            self.screen.blit(label_points, (600, 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit("QUIT")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        menu.switch(-1)
                    if event.key == pygame.K_s:
                        menu.switch(1)
                    if event.key == pygame.K_RETURN:
                        menu.select()

                self.player_rect = player.image.get_rect(topleft=(player_x, player_y))

                if money_anime_count == 5:
                    money_anime_count = 0
                else:
                    money_anime_count += 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_UP:
                        player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        counter += 1
                    if counter % 2 == 1:
                        menu.draw(self.screen, 100, 100, 75)

            check_money = random.randint(10, 750)
            check_time = random.randint(0, 100)
            if money_count > 0:
                if check_time == 5:
                    money_list.append(money[money_anime_count].get_rect(topleft=(check_money, 0)))
                    money_count -= 1
            if money_list:
                for (i, money_idx) in enumerate(money_list):
                    self.screen.blit(money[money_anime_count], money_idx)
                    if money_idx.y >= 230:
                        money_idx.y -= money_speed
                    if money_idx.colliderect(self.player_rect):
                        money_list.pop(i)
                        points += 1
            active_sprite_list.update()
            active_sprite_list.draw(self.screen)

            if player.rect.right > self.SCREEN_WIDTH:
                player.rect.right = self.SCREEN_WIDTH

            if player.rect.left < 0:
                player.rect.left = 0
            clock.tick(30)
            pygame.display.update()
