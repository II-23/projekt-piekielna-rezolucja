import pygame
from Utils.Area import Area
from Utils.ImageButton import ImageButton
from Config.definitnios import ASSETS_DIR
import os
from random import randint
from Utils.GifPlayer import GifPlayer

class Enemy:
    def __init__(self, position, size, on_enter_event, image_dir, dead_dir) -> None:
        self.active = False
        self.position = position
        self.size = size
        self.health = 1
        self.alive = True
        self.on_enter_event = on_enter_event
        if image_dir == 'ghost.png':
            roll = randint(1, 1000)
            rollcolor = randint(1, 6)
            if roll != 1000:
                image_path = os.path.join(ASSETS_DIR, 'amogi', f"ghost{rollcolor}.png")
                dead_image_path = os.path.join(ASSETS_DIR, 'amogi', f"ghost{rollcolor}_dead.png")
                self.sprite = ImageButton(position, size, image_path, image_path, None)     
                self.dead_sprite = ImageButton(position, size, dead_image_path, dead_image_path, None) 
            else:
                image_path = os.path.join(ASSETS_DIR, 'amogi', "amogisecret")
                dead_image_path = os.path.join(ASSETS_DIR, 'amogi', f"ghost7_dead.png")
                self.sprite = EnemyGif(pygame.Rect(*self.position, *self.size), GifPlayer(image_path, 0.08))    
                self.dead_sprite = ImageButton(position, size, dead_image_path, dead_image_path, None) 
        else:
            image_path = os.path.join(ASSETS_DIR, image_dir)
            dead_image_path = os.path.join(ASSETS_DIR, dead_image_path)
            self.sprite = ImageButton(position, size, image_path, image_path, None)     
            self.dead_sprite = ImageButton(position, size, dead_image_path, dead_image_path, None)        

    def process_input(self, events, mouse, *args):
        pass

    def update(self, mouse=pygame.mouse):
        if isinstance(self.sprite, EnemyGif):
            self.sprite.surface.update(mouse)

    def render(self, screen):
        if self.active:
            # rendering here
            if self.health > 0:
                self.sprite.render(screen)
            else:
                self.dead_sprite.render(screen)

class EnemyGif:
    def __init__(self, rect, surface):
        self.surface = surface
        self.rect = rect

    def render(self, screen):
        screen.blit(self.surface.get_surface(), self.rect)
