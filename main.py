import pygame
import sys

W, H = 800, 600
collide = False
n = 0
speed_x = False
speed_y = False
HEIGHT_WIN = False

rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)

circle_radius = 35
circle_pos = (0, 0)

RED = (250, 0, 0, 180)
BLUE = (0, 0, 250, 180)
YELLOW = (250, 250, 0, 180)
BLACK = (0, 0, 0)
BG = (128, 128, 128)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((W, H))
font = pygame.font.Font(None, 32)

surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
rect1 = surface.get_rect()7

ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect(topleft=(0, 0))
print(ball_rect)

clock = pygame.time.Clock()
FPS = 240

run = True

while run:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            circle_pos = e.pos
            rect1.center = e.pos
    ball_rect = ball_rect.move(speed_x, speed_y)
    if ball_rect.left < 0 or ball_rect.right > HEIGHT_WIN:
        speed_x = -speed_x
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT_WIN:
        speed_y = -speed_y
    screen.fill(BG)

    COLOR = RED if collide else BLUE

    rect2 = pygame.draw.rect(screen, COLOR, (rect_pos, rect_size))
    screen.blit(surface, rect1)
    screen.blit(ball, ball_rect)
    screen.blit(font.render(str(num), True, BLACK), (40, 25))
    screen.blit(font.render(str(num1), True, BLACK), (360, 25))
    if rect1.colliderect(rect2):  
        collide = True
        if COLOR == BLUE:
            n += 1
    else:
        collide = False

    pygame.display.update()
    clock.tick(FPS)