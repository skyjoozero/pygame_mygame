import pygame
import random

pygame.init()




running = True

white = pygame.image.load("images\\white.png")
white_size = white.get_rect().size
white_width = white_size[0]
white_height = white_size[1]

red = pygame.image.load("images\\red.png")
red_size = red.get_rect().size
red_width = red_size[0]
red_height = red_size[1]

player = []
player_x_pos = random.randint(1, 30)
player_y_pos = random.randint(1, 20)
player.append([player_x_pos, player_y_pos])

to_x = 0
to_y = 0

screen_width = white_width * 30
screen_height = white_width * 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("game")
clock = pygame.time.Clock()



while running:
    dt = clock.tick(20)
    for i in range(1,31):
        for j in range(1,21):
            screen.blit(white, ((i - 1) * white_width, (j - 1) * white_width))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                to_x = -1
                to_y = 0
            elif e.key == pygame.K_RIGHT:
                to_x = 1
                to_y = 0
            elif e.key == pygame.K_DOWN:
                to_y = 1
                to_x = 0
            elif e.key == pygame.K_UP:
                to_y = -1
                to_x = 0



    

    screen.blit(red, ((player_x_pos - 1) * white_width, (player_y_pos - 1) * white_width))


    # player_x_pos += to_x
    # player_y_pos += to_y
    player = [[p[0] + to_x, p[1] + to_y] for p in player]
    print(player)


    if player_x_pos < 0:
        player_x_pos = 30
    if player_x_pos > 30:
        player_x_pos = 0
    if player_y_pos < 0:
        player_y_pos = 20
    if player_y_pos > 20:
        player_y_pos = 0


    pygame.display.update()