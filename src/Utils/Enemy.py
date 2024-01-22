import pygame
from Utils.Area import Area
from Utils.ImageButton import ImageButton
from Config.definitnios import ASSETS_DIR
import os 

class Enemy:
    def __init__(self, position, size, on_enter_event, image_dir) -> None:
        self.active = False
        self.position = position
        self.size = size
        self.health = 1
        self.on_enter_event = on_enter_event
        image_path = os.path.join(ASSETS_DIR, image_dir)
        self.sprite = ImageButton(position, size, image_path, image_path, None)           

    def process_input(self, events, mouse, *args):
        pass

    def update(self, mouse=pygame.mouse):
        pass

    def render(self, screen):
        if self.active:
            # rendering here
            self.sprite.render(screen)
        pass