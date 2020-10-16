import pygame
import sys
import random


def opponent_animation():
    if opponent.top > ball.y:
        opponent.top -= opponent_speed
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    if opponent.top <= 0:
        opponent.top = 0


def player_animation():
    player.y += player_speed
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if player.top <= 0:
        player.top = 0


def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width // 2, screen_height // 2)
    ball_speed_x *= random.choice([1, -1])
    ball_speed_y *= random.choice([1, -1])


def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score
    # Ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Boundaries
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        if ball.left <= 0:
            player_score += 1
        else:
            opponent_score += 1
        ball_restart()

    # Collisions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Rectangles
ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
opponent = pygame.Rect(screen_width - 20, screen_height // 2 - 70, 10, 140)
player = pygame.Rect(10, screen_height // 2 - 70, 10, 140)

# Speeds
ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
opponent_speed = 7

# Text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.SysFont(name="comicsansms", size=35)

# color
bg_colour = pygame.Color("grey12")
light_grey = (200, 200, 200)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7
    ball_animation()
    player_animation()
    opponent_animation()

    # Visualization
    screen.fill(bg_colour)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    player_text = game_font.render(str(player_score), False, light_grey)
    screen.blit(player_text, (660, 470))
    opponent_text = game_font.render(str(opponent_score), False, light_grey)
    screen.blit(opponent_text, (600, 470))

    pygame.display.flip()
    clock.tick(60)
