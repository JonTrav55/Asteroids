import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y,shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shots_group = shots_group

        self.rotation = 0

    def rotate(self,dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.shots_group.add(new_shot)
        print(f"Shot created! Position: {new_shot.position}, Velocity: {new_shot.velocity}")
        print(f"Total shots: {len(self.shots_group)}")

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()


        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white", self.triangle(), 2)