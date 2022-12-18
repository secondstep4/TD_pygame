import pygame
from settings import *
from zone import Zone
from enemy import Enemy
from tower import Tower
from particle import Particle

class Level:
    def __init__(self) -> None:
        #get display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.tower_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        #set field
        self.set_field()

        #input event
        self.mouse_down = False
        self.key_down = False

        #tower
        self.dragging_tower : Tower = None

        #spawn enemy
        self.can_spawn = True
        self.spawn_time = None
        self.spawn_duration = 400

    def set_field(self) -> None:
        self.zone1 = Zone((0,0), pygame.Surface((ZONE1_W, ZONE1_W)), WHITE, self.visible_sprites)
        self.zone2 = Zone((Z3_off,Z3_off), pygame.Surface((ZONE2_W, ZONE2_W)), GRAY, self.visible_sprites)
        self.zone3 = Zone((ZONE1_W, 0), pygame.Surface((ZONE3_W, HEIGHT)), C1_BLUE, self.visible_sprites)

    def spawn_enemy(self):
        if self.can_spawn:
            self.can_spawn = False
            self.spawn_time = pygame.time.get_ticks()
            Enemy(ZONE_LANE_HALF,ZONE_LANE_HALF, self.visible_sprites, self.enemy_sprites)

    def cool(self):
        if not self.can_spawn:
            current_time = pygame.time.get_ticks()
            if current_time - self.spawn_time > self.spawn_duration:
                self.can_spawn = True
        
    def input(self) -> None:
        if pygame.mouse.get_pressed() == (1,0,0) and not self.mouse_down: #left clicked
            self.mouse_down = True
            pos = pygame.mouse.get_pos()
            for sprite in self.tower_sprites:
                if sprite.rect.collidepoint(pos) and not self.dragging_tower:
                    self.dragging_tower = sprite
                    self.dragging_tower.update(mouse_pos = pygame.mouse.get_pos())
                    self.dragging_tower.drag = True
        elif pygame.mouse.get_pressed() == (0,0,0) and self.mouse_down:
            self.mouse_down = False
            if self.dragging_tower:
                self.dragging_tower.drag = False
                self.dragging_tower = None
        else:
            if self.dragging_tower :
                self.dragging_tower.update(mouse_pos = pygame.mouse.get_pos())

        if pygame.mouse.get_pressed() == (0,0,0):
            self.mouse_down = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.key_down:
            self.key_down = True
            Tower((ZONE1_W//2,ZONE1_W//2), self.visible_sprites, self.tower_sprites, 
                tw_group = self.tower_sprites, en_group = self.enemy_sprites, atk_func = self.create_attack)
        if not keys[pygame.K_SPACE] and self.key_down:
            self.key_down = False
    
    def create_attack(self, pos, target):
        Particle(pos, target, self.visible_sprites)

    def run(self) -> None:
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.input()

        self.spawn_enemy()
        self.cool()

