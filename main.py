import pygame
import sys
from data import Point, SIZE, distance_between_two_dots
from applications import Car

FPS = 60
pygame.init()
sc = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
# init game objects here
game_objects = [Car(400, 400)]

motion_x = 0
motion_y = 0
force = 1

while 1:
    sc.fill((10, 10, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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

    if motion_y == -1:
        game_objects[0].throttle(force)
    if motion_y == 1:
        game_objects[0].throttle(-force)
    if motion_x == 1:
        game_objects[0].turn(True)
    if motion_x == -1:
        game_objects[0].turn(False)

    for game_object in game_objects:
        # sc.blit(game_object.image, game_object.rect)
        game_object.update(sc)

    clock.tick(FPS)
    pygame.display.update()
