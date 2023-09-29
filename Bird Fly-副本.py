import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jump")

# Colors
blue = (0, 0, 255)
green = (34,139,34)
grey = (169,169,169)
# Bird
bird_x = 100
bird_y = screen_height // 2
bird_speed = 5
dotJump = 1

# Pipe
pipe_width = 50
pipe_gap = 150
pipe_speed = 3
pipes = []
pipeCount = 0
clock = pygame.time.Clock()


def side():
    
        if event.key == pygame.K_DOWN:
            dotJump == 1

running = True
while running:
    screen.fill(grey)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y -= 75
    bird_y += bird_speed
    pygame.draw.circle(screen, blue, (bird_x, bird_y), 20)
    
    if len(pipes) == 0 or pipes[-1][0] < screen_width - 200:
        pipe_height = random.randint(100, screen_height - pipe_gap - 100)
        pipes.append([screen_width, pipe_height])
        pipeCount += 1

    for pipe in pipes:
        pipe[0] -= pipe_speed
        pygame.draw.rect(screen, green, (pipe[0], 0, pipe_width, pipe[1]))
        pygame.draw.rect(screen, green, (pipe[0], pipe[1] + pipe_gap, pipe_width, screen_height - pipe[1] - pipe_gap))

    for pipe in pipes:
        if pipe[0] < bird_x < pipe[0] + pipe_width and (bird_y < pipe[1] or bird_y > pipe[1] + pipe_gap):
            running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
print(pipeCount - 4)