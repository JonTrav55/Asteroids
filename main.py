import pygame
import constants
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    while True:
        dt = clock.tick(60) / 1000
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


    print("Starting Asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
    