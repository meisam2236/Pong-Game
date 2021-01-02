import pygame, sys, random

def ball_restart():
    global ballSpeedX, ballSpeedY
    ball.center = (ScreenWidth/2, ScreenHeight/2)
    ballSpeedY *= random.choice((1, -1))
    ballSpeedX *= random.choice((1, -1))

def ball_animation():
    global ballSpeedX, ballSpeedY
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    if ball.top <= 0 or ball.bottom >= ScreenHeight:
        ballSpeedY *= -1
    if ball.left <= 0 or ball.right >= ScreenWidth:
        # game over
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(oponent):
        ballSpeedX *= -1

def player_animation():
    player.y += playerSpeed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= ScreenHeight:
        player.bottom = ScreenHeight

def oponent_animation():
    if oponent.top < ball.y:
        oponent.top += oponenetSpeed
    if oponent.bottom > ball.y:
        oponent.bottom -= oponenetSpeed
    if oponent.top <= 0:
        oponent.top = 0
    if oponent.bottom >= ScreenHeight:
        player.bottom = ScreenHeight

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
ScreenWidth = 1280
ScreenHeight = 960
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Ping Pong')

# Game Rectangles
ball = pygame.Rect(int(ScreenWidth/2) - 15, int(ScreenHeight/2) - 15, 30, 30)
player = pygame.Rect(ScreenWidth - 20, int(ScreenHeight/2) - 70, 10, 140)
oponent = pygame.Rect(10, int(ScreenHeight/2) - 70, 10, 140)
backgroundColor = pygame.Color('grey12')
lightGray = (200, 200, 200)

ballSpeedX = 7 * random.choice((1, -1))
ballSpeedY = 7 * random.choice((1, -1))
playerSpeed = 0
oponenetSpeed = 7

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7
            if event.key == pygame.K_UP:
                playerSpeed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed +=7

    ball_animation()
    player_animation()
    oponent_animation()
        
    # Visuals
    screen.fill(backgroundColor)
    pygame.draw.rect(screen, lightGray, player)
    pygame.draw.rect(screen, lightGray, oponent)
    pygame.draw.ellipse(screen, lightGray, ball)
    pygame.draw.aaline(screen, lightGray, (ScreenWidth/2, 0), (ScreenWidth/2, ScreenHeight))
    # Updating the window
    pygame.display.flip()
    clock.tick(60)
