import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    delta = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable_object in updatable:
            updatable_object.update(delta)

        for asteroid_object in asteroids:
            if asteroid_object.check_collision(player):
                sys.exit("Game over!")

            for shot_object in shots:
                if asteroid_object.check_collision(shot_object):
                    asteroid_object.kill()

        screen.fill('black')

        for drawable_objects in drawable:
            drawable_objects.draw(screen)

        pygame.display.flip()

        time_passed = clock.tick(60)
        delta = time_passed / 1000


if __name__ == "__main__":
    main()
