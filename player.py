import pygame
from circleshape import CircleShape
from constants import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 5)

    def rotate(self, delta):
        self.rotation += PLAYER_TURN_SPEED * delta

    def update(self, delta):
        self.shoot_cooldown -= delta

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta)
        if keys[pygame.K_d]:
            self.rotate(delta)
        if keys[pygame.K_s]:
            self.move(-delta)
        if keys[pygame.K_w]:
            self.move(delta)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, delta):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta

    def shoot(self):
        if self.shoot_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(
                self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
