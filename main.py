import sys
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable
    AsteroidField.containers = updatable
    

    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    

    # Main game loop
    while True:
        # Calculate delta time
        dt = clock.tick(60) / 1000
        
        updatable.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        for entity in drawable:
            entity.draw(screen)
            if isinstance(entity, Asteroid) and entity.collides_with(player):
                print("Game over!")
                sys.exit()


        
        
        pygame.display.flip()
        screen.fill("black")

    #does nothing?
    print("Starting Asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

    #what does this do?
if __name__ == "__main__":
    main()
    