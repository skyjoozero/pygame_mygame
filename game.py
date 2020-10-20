import pygame
import random
################################생성된 객체가 처음것을 따라가게 만들기###################################
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

green = pygame.image.load("images\\green.png")
green_size = green.get_rect().size
green_width = green_size[0]
green_height = green_size[1]

players = []
score = 1
player_x_pos = random.randint(1, 30)
player_y_pos = random.randint(1, 20)
players.append([player_x_pos, player_y_pos])

to_x = 0
to_y = 0

screen_width = white_width * 30
screen_height = white_width * 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

enemy_on = True

while running:
    dt = clock.tick(20)
    temp = score
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



    ############랜덤등장###############################
    if enemy_on:
        rand_x = random.randint(0,29)
        rand_y = random.randint(0,19)
        
        enemy_on = False
    
    
    
    ############캐릭터 좌표설정####################

    
    
    # players = [[p[0][0] + to_x, p[0][1] + to_y] for p in players]

    players[0][0] += to_x
    players[0][1] += to_y

    for i in range(0, score):
        player_x = int(players[i][0])
        player_y = int(players[i][1])
        screen.blit(red, ((player_x - 1) * white_width, (player_y - 1) * white_width))
        if players[i][0] < 0:
            players[i][0] = 30
        if players[i][0] > 30:
            players[i][0] = 0
        if players[i][1] < 0:
            players[i][1] = 20
        if players[i][1] > 20:
            players[i][1] = 0
    
    screen.blit(green, (rand_x * green_width, rand_y * green_height))


    # players_x_pos += to_x
    # players_y_pos += to_y
    # if score > temp:
    #     players.append([[players_x_pos], [players_y_pos]])
    # print(len(players))
    # print(players)


    ################점수추가 충돌계산 충동설정 enemy_on설정 score += 1######################

    red_rect = red.get_rect()
    red_rect.left = (players[0][0] - 1) * red_width
    red_rect.top = (players[0][1] - 1) * red_height

    green_rect = green.get_rect()
    green_rect.left = rand_x * green_width
    green_rect.top = rand_y * green_height
    
    if red_rect.colliderect(green_rect):
        score += 1
        enemy_on = True
        if to_x > 0 and to_y == 0:
            players.append([players[int(len(players)) - 1][0] - 1, players[int(len(players)) - 1][1]])
        if to_x < 0 and to_y == 0:
            players.append([players[int(len(players)) - 1][0] + 1, players[int(len(players)) - 1][1]])
        if to_x == 0 and to_y > 0:
            players.append([players[int(len(players)) - 1][0], players[int(len(players)) - 1][1] + 1])
        if to_x == 0 and to_y < 0:
            players.append([players[int(len(players)) - 1][0], players[int(len(players)) - 1][1] - 1])
    
    
    print(players)


    pygame.display.update()