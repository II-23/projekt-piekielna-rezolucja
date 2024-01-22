import pygame
from Utils.Area import Area
from Utils.ImageButton import ImageButton
from Config.definitnios import ASSETS_DIR
import os
from random import randint

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
            if roll != 1001:
                rollcolor = randint(1, 7)
                image_path = os.path.join(ASSETS_DIR, 'amogi', f"ghost{rollcolor}.png")
                dead_image_path = os.path.join(ASSETS_DIR, 'amogi', f"ghost{rollcolor}_dead.png")
            else:
                image_path = os.path.join(ASSETS_DIR, 'amogi', f"amogus_gif.gif")
                dead_image_path = os.path.join(ASSETS_DIR, 'amogi', f"ghost{rollcolor}_dead.png")
        else:
            image_path = os.path.join(ASSETS_DIR, image_dir)
            dead_image_path = os.path.join(ASSETS_DIR, dead_image_path)
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