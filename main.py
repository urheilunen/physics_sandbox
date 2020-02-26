import pygame
import sys
from point_class import Point

SIZE = (1000, 600)
FPS = 60
pygame.init()
sc = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
point0 = Point(400, 300)
motion_x = 0
motion_y = 0

while 1:
    sc.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and motion_y == 0:
                motion_y = -1
            if event.key == pygame.K_a and motion_x == 0:
                motion_x = -1
            if event.key == pygame.K_s and motion_y == 0:
                motion_y = 1
            if event.key == pygame.K_d and motion_x == 0:
                motion_x = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                motion_y = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                motion_x = 0

    if 0 > point0.rect.x:
        point0.x_speed *= -1
        point0.give_force(1, 0, 3)
    if 0 > point0.rect.y:
        point0.y_speed *= -1
        point0.give_force(0, 1, 3)
    if SIZE[0] < point0.rect.x:
        point0.x_speed *= -1
        point0.give_force(-1, 0, 3)
    if SIZE[1] < point0.rect.y:
        point0.y_speed *= -1
        point0.give_force(0, -1, 3)

    point0.give_force(motion_x, motion_y, 3)
    sc.blit(point0.image, point0.rect)
    point0.update()

    clock.tick(FPS)
    pygame.display.update()
