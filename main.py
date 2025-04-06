import pygame
import constants


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill("black")
        pygame.display.flip()
        

    print("Starting Asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
    