import pygame
from settings import *

class Tower(pygame.sprite.Sprite):
    def __init__(self, pos, *groups: pygame.sprite.AbstractGroup, **kwargs) -> None:
        super().__init__(*groups)

        #set image
        self.rect = pygame.Rect(0,0, ENTITY_SIZE, ENTITY_SIZE)
        self.image = pygame.Surface((ENTITY_SIZE, ENTITY_SIZE))
        self.image.fill(RED)
        self.rect.center = pos
        #group
        self.tower_sprites = kwargs['tw_group']
        self.enemy_sprites = kwargs['en_group']
        #dragging
        self.drag = False
        self.drag_vec = pygame.math.Vector2()
        #attack
        self.targeted = None
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 300
        self.create_attack = kwargs['atk_func']

    def dragging(self, pos):
        if self.drag == True :
            old_pos = self.rect.center
            self.rect.center = pos - self.drag_vec
            if self.is_range_over() or self.is_collide_tower():
                self.rect.center = old_pos

    
    def is_range_over(self) -> bool:
        pos_x = self.rect.x
        pos_y = self.rect.y

        if pos_x >= ZONE1_W - ZONE_LANE or pos_x <= ZONE_LANE or pos_y >= ZONE1_W - ZONE_LANE or pos_y <= ZONE_LANE:
            return True
        return False

    def is_collide_tower(self) -> bool:
        for sprite in self.tower_sprites:
            if sprite.drag == False:
                if sprite.rect.colliderect(self.rect):
                    return True
        return False

    def search_enemy(self):
        if self.targeted :
            distance, direction = self.get_distance_and_direction(self.targeted)
            if distance >= 300 :
                self.targeted = None
            elif not self.targeted.alive :
                self.targeted = None
            else:
                return
            
            

        for enemy in self.enemy_sprites:
            distance, direction = self.get_distance_and_direction(enemy)
            if distance < 300 :
                self.targeted = enemy
                return
    
    def get_distance_and_direction(self, target : pygame.sprite.Sprite):
        tw_vec = pygame.math.Vector2(self.rect.center)
        en_vec = pygame.math.Vector2(target.rect.center)

        vec = en_vec - tw_vec
        distance = vec.magnitude()
        if distance > 0:
            direction = vec.normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)
            
    def attack(self):
        if not self.targeted:
            return
        if self.drag:
            return
        
        if self.can_attack:
            self.create_attack(self.rect.center, self.targeted)
            self.can_attack = False
            self.attack_time = pygame.time.get_ticks()

    def cool(self):
        if not self.can_attack :
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time > self.attack_cooldown :
                self.can_attack = True

    def update(self, *args, **kwargs) -> None:
        self.search_enemy()
        self.attack()
        self.cool()
        
        if 'mouse_pos' in kwargs.keys() :
            pos = kwargs['mouse_pos']
            if self.drag == False:
                vec_pos = pygame.math.Vector2(pos)
                self.drag_vec = vec_pos - self.rect.center
            self.dragging(pos)
        
        return super().update(*args, **kwargs)