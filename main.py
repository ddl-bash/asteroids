import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        print("Game over!")