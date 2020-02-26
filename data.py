import pygame
import math

SIZE = (1000, 600)
FRICTION = 0.1


def distance_between_two_dots(x1, y1, x2, y2):
    dstx = x2 - x1
    dsty = y2 - y1
    dstx **= 2
    dsty **= 2
    dst = dstx + dsty
    dst = math.sqrt(dst)
    return dst


def vector_to_another_dot(x1, y1, x2, y2):
    i_vector = x2 - x1
    j_vector = y2 - y1
    max_arg = max(abs(i_vector), abs(j_vector))
    i_vector /= max_arg
    j_vector /= max_arg
    return i_vector, j_vector


class Point(pygame.sprite.Sprite):
    def __init__(self, x, y, detached_to_1=None, detached_to_2=None, mass=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('dot.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.x = self.rect.x
        self.y = self.rect.y
        self.x_speed = 0
        self.y_speed = 0
        self.mass = mass

        # links to another points
        self.detached_to = []
        self.needed_distances_to_detached_to = []

        if detached_to_1:
            self.detached_to.append(detached_to_1)
            self.needed_distances_to_detached_to.append(distance_between_two_dots(
                detached_to_1.x,
                detached_to_1.y,
                self.x,
                self.y,
            ))
        if detached_to_2:
            self.detached_to.append(detached_to_2)
            self.needed_distances_to_detached_to.append(distance_between_two_dots(
                detached_to_2.x,
                detached_to_2.y,
                self.x,
                self.y,
            ))

    def give_force(self, x_vector, y_vector, newtons):
        self.x_speed += round(newtons / self.mass) * x_vector
        self.y_speed += round(newtons / self.mass) * y_vector

    def update(self):
        if self.detached_to:
            for point, needed_distance in zip(self.detached_to, self.needed_distances_to_detached_to):
                vector = vector_to_another_dot(self.x, self.y, point.x, point.y)
                actual_distance_to_detached_to = distance_between_two_dots(
                    point.x,
                    point.y,
                    self.x,
                    self.y,
                )
                force = (actual_distance_to_detached_to - needed_distance) / 10
                eps = 10
                if needed_distance < actual_distance_to_detached_to - eps:
                    # here this dot should be given force towards another dot
                    self.give_force(vector[0], vector[1], force)
                    point.give_force(-vector[0], -vector[1], force)
                    # print('to')
                    self.x += vector[0]
                    self.y += vector[1]
                    point.x -= vector[0]
                    point.y -= vector[1]
                elif needed_distance > actual_distance_to_detached_to + eps:
                    # # here this dot should be given force away from another dot
                    self.give_force(vector[0], vector[1], force)
                    point.give_force(-vector[0], -vector[1], force)
                    # print('away')
                    self.x -= vector[0]
                    self.y -= vector[1]
                    point.x += vector[0]
                    point.y += vector[1]

        # protecting object from getting outside the screen
        if 0 > self.rect.x:
            self.x = 0
            self.x_speed /= 2
        if 0 > self.rect.y:
            self.y = 0
            self.y_speed /= 2
        if SIZE[0] < self.rect.x:
            self.x = SIZE[0]
            self.x_speed /= 2
        if SIZE[1] < self.rect.y:
            self.y = SIZE[1]
            self.y_speed /= 2
        self.x_speed *= 1 - FRICTION
        self.y_speed *= 1 - FRICTION
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
