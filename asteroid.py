import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, delta):
        self.position += (self.velocity * delta)

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)

            new_vector1 = self.velocity.rotate(angle)
            new_vector2 = self.velocity.rotate(-angle)

            children_radius = self.radius - ASTEROID_MIN_RADIUS
            child1 = Asteroid(
                self.position.x, self.position.y, children_radius)
            child2 = Asteroid(
                self.position.x, self.position.y, children_radius)

            child1.velocity = new_vector1 * 1.2
            child2.velocity = new_vector2 * 1.2
