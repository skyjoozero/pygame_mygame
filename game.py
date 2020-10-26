import pygame
import random
################################ 97 ~ 98번째줄 고민###################################
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

enemy = pygame.image.load("images\\red.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

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
    dt = clock.tick(10)
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
        
        while [rand_x, rand_y] in players:
            rand_x = random.randint(0,29)
            rand_y = random.randint(0,19)


        enemy_on = False
    
    
    ############캐릭터 좌표설정####################

    
    tmp_player_x = players[0][0] + to_x
    tmp_player_y = players[0][1] + to_y

    players.insert(0, [tmp_player_x, tmp_player_y])
    del players[score]


    for i in range(0, score):
        
        
        
        
        
        if players[i][0] <= 0:
            players[i][0] = 30
        if players[i][0] > 30:
            players[i][0] = 1
        if players[i][1] <= 0:
            players[i][1] = 20
        if players[i][1] > 20:
            players[i][1] = 1

        screen.blit(red, ((players[i][0] - 1) * white_width, (players[i][1] - 1) * white_width))
    

    
    screen.blit(green, (rand_x * green_width, rand_y * green_height))
    temp_end_x = players[score - 1][0]
    temp_end_y = players[score - 1][1]


    ################점수추가 충돌계산 충동설정 enemy_on설정 score += 1######################

    red_rect = red.get_rect()
    red_rect.left = (players[0][0] - 1) * (red_width - 0.1)
    red_rect.top = (players[0][1] - 1) * (red_height - 0.1)
    
    for i in range(1, score):
        enemy_rect = enemy.get_rect()
        enemy_rect.left = (players[i][0]) * enemy_width
        enemy_rect.top = (players[i][1]) * enemy_height

        if red_rect.colliderect(enemy_rect):
            running = False

    green_rect = green.get_rect()
    green_rect.left = rand_x * green_width
    green_rect.top = rand_y * green_height
    
    if red_rect.colliderect(green_rect):
        score += 1
        enemy_on = True
        if to_x > 0 and to_y == 0:
            players.append([players[len(players) - 1][0] - 1, players[len(players) - 1][1]])
        if to_x < 0 and to_y == 0:
            players.append([players[len(players) - 1][0] + 1, players[len(players) - 1][1]])
        if to_x == 0 and to_y > 0:
            players.append([players[len(players) - 1][0], players[len(players) - 1][1] - 1])
        if to_x == 0 and to_y < 0:
            players.append([players[len(players) - 1][0], players[len(players) - 1][1] + 1])
    
    

    pygame.display.update()