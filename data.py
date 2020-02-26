import pygame
import math

SIZE = (1000, 600)
FRICTION = 0.01


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
    def __init__(self, x, y, detached_to=None, mass=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('dot.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.x = self.rect.x
        self.y = self.rect.y
        self.x_speed = 0
        self.y_speed = 0
        self.mass = mass

        # link to another point
        self.detached_to = detached_to
        if detached_to:
            self.needed_distance_to_detached_to = distance_between_two_dots(
                detached_to.x,
                detached_to.y,
                self.x,
                self.y,
            )

    def give_force(self, x_vector, y_vector, newtons):
        self.x_speed += round(newtons / self.mass) * x_vector
        self.y_speed += round(newtons / self.mass) * y_vector

    def update(self):
        if self.detached_to:
            distance_to_detached_to = distance_between_two_dots(
                self.detached_to.x,
                self.detached_to.y,
                self.x,
                self.y,
            )
            if self.needed_distance_to_detached_to < distance_to_detached_to:
                # here this dot should be given force towards another dot
                vector = vector_to_another_dot(self.x, self.y, self.detached_to.x, self.detached_to.y)
                self.give_force(vector[0], vector[1], 1)
                self.detached_to.give_force(-vector[0], -vector[1], 1)
            elif self.needed_distance_to_detached_to > distance_to_detached_to:
                # here this dot should be given force away from another dot
                vector = vector_to_another_dot(self.x, self.y, self.detached_to.x, self.detached_to.y)
                self.give_force(vector[0], vector[1], -1)
                self.detached_to.give_force(-vector[0], -vector[1], -1)
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
