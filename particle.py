import pygame
from settings import *

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, target, *groups) -> None:
        super().__init__(*groups)
        self.target = target

        self.image = pygame.Surface([20,20], pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        pygame.draw.circle(self.image, RED, [10,10], 10)

    
    def move(self):
        distance, direction = self.get_direction()
        
        self.rect.centerx += direction.x * 10
        self.rect.centery += direction.y * 10

    def check_alive(self):
        if not self.target.alive :
            self.kill()

    def get_direction(self):
        en_vec = pygame.math.Vector2(self.target.rect.center)
        my_vec = pygame.math.Vector2(self.rect.center)

        vec = en_vec - my_vec

        distance = vec.magnitude()
        if distance > 0:
            direction = vec.normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)
    
    def check_hit(self):
        if self.rect.colliderect(self.target):
            self.target.get_damage(10)
            self.kill()

    def update(self, *args, **kwargs) -> None:
        self.check_alive()
        self.move()
        self.check_hit()
        return super().update(*args, **kwargs)
