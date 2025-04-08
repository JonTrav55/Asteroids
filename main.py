import sys
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = updatable, drawable, shots_group

    

    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, shots_group)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    

    # Main game loop
    while True:
        # Calculate delta time
        dt = clock.tick(60) / 1000
        
        updatable.update(dt)
        shots_group.update(dt)

        for shot in shots_group:
            shot.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        for entity in drawable:
            entity.draw(screen)
            if isinstance(entity, Asteroid) and entity.collides_with(player):
                print("Game over!")
                sys.exit()

        for asteroid in drawable:
            if isinstance(asteroid, Asteroid):
                for bullet in shots_group:
                    if asteroid.collides_with(bullet):
                        print("Asteroid hit!")
                        bullet.kill()
                        asteroid.split()
                        


        pygame.display.flip()
        screen.fill("black") 

    #what does this do?
if __name__ == "__main__":
    main()
    