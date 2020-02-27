from data import Point, vector_to_another_dot


class Car:
    def __init__(self, x_center, y_center):
        size = 20
        self.corners = []
        self.corners.append(Point(x_center-size, y_center-size*2))
        self.corners.append(Point(x_center+size, y_center-size*2, self.corners[0]))
        self.corners.append(Point(x_center-size, y_center+size*2, self.corners[0], self.corners[1]))
        self.corners.append(Point(x_center+size, y_center+size*2, self.corners[0], self.corners[1], self.corners[2]))

    def update(self, sc):
        for corner in self.corners:
            corner.update()
            sc.blit(corner.image, corner.rect)

    def throttle(self, force=1):
        vector = vector_to_another_dot(self.corners[2].x, self.corners[2].y, self.corners[1].x, self.corners[1].y)
        self.corners[2].give_force(vector[0], vector[1], force)
        vector = vector_to_another_dot(self.corners[3].x, self.corners[3].y, self.corners[0].x, self.corners[0].y)
        self.corners[3].give_force(vector[0], vector[1], force)

    def turn(self, is_right):
        force = 0.5
        if is_right:
            vector = vector_to_another_dot(self.corners[0].x, self.corners[0].y, self.corners[1].x, self.corners[1].y)
        else:
            vector = vector_to_another_dot(self.corners[1].x, self.corners[1].y, self.corners[0].x, self.corners[0].y)
        self.corners[0].give_force(vector[0], vector[1], force)
        self.corners[1].give_force(vector[0], vector[1], force)
