import pygame
from Utils.Area import Area
from Utils.ImageButton import ImageButton
from Config.definitnios import ASSETS_DIR
import os 

class Enemy:
    def __init__(self, position, size, on_enter_event, image_dir, dead_dir) -> None:
        self.active = False
        self.position = position
        self.size = size
        self.health = 1
        self.alive = True
        self.on_enter_event = on_enter_event
        image_path = os.path.join(ASSETS_DIR, image_dir)
        dead_image_path = os.path.join(ASSETS_DIR, dead_dir)
        self.sprite = ImageButton(position, size, image_path, image_path, None)     
        self.dead_sprite = ImageButton(position, size, dead_image_path, dead_image_path, None)        

    def process_input(self, events, mouse, *args):
        pass

    def update(self, mouse=pygame.mouse):
        pass

    def render(self, screen):
        if self.active:
            # rendering here
            if self.health > 0:
                self.sprite.render(screen)
            else:
                self.dead_sprite.render(screen)