import pygame  # noqa: I001

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroidfield import AsteroidField  # noqa: F401
from asteroid import Asteroid



def main():
    pygame.init()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    player = Player(x, y)  # noqa: F841
    AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        print(len(updatable))
        print(dt)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
