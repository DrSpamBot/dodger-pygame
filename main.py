import pygame
from random import randint

pygame.init()
pygame.font.init()

WIDTH = 600
HEIGHT = 600

playerXDefault = 300
playerYDefault = 500

playerSpeed = 2
zombieFallSpeed = 2

bg = pygame.image.load('images/fond.png')
player = pygame.image.load('images/player.png')
zombie = pygame.image.load('images/mechant.png')

playerRect = player.get_rect()

scoreFont = pygame.font.SysFont('Segoe UI', 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def restartGame():
    global zombies, score
    score = 0
    playerRect.centerx = playerXDefault
    playerRect.centery = playerYDefault
    zombies = []

restartGame()

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(bg, (0, 0))
    screen.blit(player, (playerRect))

    if playerRect.centerx <= 0 or playerRect.centerx >= WIDTH or playerRect.centery <= 0 or playerRect.centery >= HEIGHT:
        restartGame()

    if randint(1, 23) == 1:
        zombies.append(zombie.get_rect())
        zombies[-1].centery = 0
        zombies[-1].centerx = randint(0, WIDTH)
    for z in zombies:
        screen.blit(zombie, (z))
        z.centery += zombieFallSpeed
        if z.centery >= 600:
            zombies.remove(z)
        if z.colliderect(playerRect):
            restartGame()

    scoreText = scoreFont.render('Score: '+str(score), False, (255,255,255))
    screen.blit(scoreText, (0, 0))
    score += 1

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        playerRect.centerx -= playerSpeed
    if pressed[pygame.K_RIGHT]:
        playerRect.centerx += playerSpeed
    if pressed[pygame.K_UP]:
        playerRect.centery -= playerSpeed
    if pressed[pygame.K_DOWN]:
        playerRect.centery += playerSpeed

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
