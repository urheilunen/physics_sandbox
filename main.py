import pygame
import sys
from data import Point, SIZE, distance_between_two_dots

FPS = 60
pygame.init()
sc = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
points = [None,
          Point(500, 300)]
points[0] = Point(400, 300, points[1])
motion_x = 0
motion_y = 0
force = 1

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
            if event.key == pygame.K_f:
                try:
                    force = float(input('Force: '))
                except ValueError:
                    print('Only float value!')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                motion_y = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                motion_x = 0

    points[0].give_force(motion_x, motion_y, force)

    for point in points:
        sc.blit(point.image, point.rect)
        point.update()

    clock.tick(FPS)
    pygame.display.update()
