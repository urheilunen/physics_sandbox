import pygame


class Point(pygame.sprite.Sprite):
    def __init__(self, x, y, mass=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('dot.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.x_speed = 0
        self.y_speed = 0
        self.mass = mass

    def give_force(self, x_vector, y_vector, newtons):
        self.x_speed += round(newtons / self.mass) * x_vector
        self.y_speed += round(newtons / self.mass) * y_vector

    def update(self):
        if self.x_speed < 0:
            self.x_speed += 1
        if self.x_speed > 0:
            self.x_speed -= 1
        if self.y_speed < 0:
            self.y_speed += 1
        if self.y_speed > 0:
            self.y_speed -= 1
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.rect.x = round(self.rect.x)
        self.rect.y = round(self.rect.y)

