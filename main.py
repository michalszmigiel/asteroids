import pygame
from constants import *
from player import *


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    clock = pygame.time.Clock()
    delta = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable_object in updatable:
            updatable_object.update(delta)

        screen.fill('black')

        for drawable_objects in drawable:
            drawable_objects.draw(screen)

        pygame.display.flip()

        time_passed = clock.tick(60)
        delta = time_passed / 1000


if __name__ == "__main__":
    main()
