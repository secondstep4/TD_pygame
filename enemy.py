import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, left, top, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        
        #set temperature image
        self.rect = pygame.Rect(left, top, ENTITY_SIZE, ENTITY_SIZE)
        self.image = pygame.Surface((ENTITY_SIZE,ENTITY_SIZE))
        self.image.fill(RED)
    
        #next waypoint (def = 0)
        self.target = 0

        #set hitbox for waypoint
        self.hitbox = pygame.Rect(left, top, ENTITY_SIZE/3, ENTITY_SIZE/3)

        #set movement
        self.direction = pygame.math.Vector2(0,1)
        self.speed = 4.0

        #spec
        self.alive = True
        self.hp = 100

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * self.speed
        self.hitbox.y += self.direction.y * self.speed
        self.rect.center = self.hitbox.center

    def check_waypoint(self):
        if self.hitbox.collidepoint(
            WAY_POINT[self.target]['x'], 
            WAY_POINT[self.target]['y']):
            self.target += 1

        if self.target >= WAY_POINT.__len__():
            self.target = 0
        waypoint_vec = pygame.math.Vector2(WAY_POINT[self.target]['x'], WAY_POINT[self.target]['y'])
        self.direction = waypoint_vec - self.rect.center

    def get_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
            self.kill()


    def update(self, *args, **kwargs) -> None:
        self.move()
        self.check_waypoint()
        return super().update(*args, **kwargs)
