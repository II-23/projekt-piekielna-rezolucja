import pygame
from Utils.Area import Area
from Utils.ImageButton import ImageButton
from Config.definitnios import ASSETS_DIR
import os 

class Trapdoor:
    def __init__(self, position, size, on_enter_event, open_dir, closed_dir) -> None:
        self.active = False
        self.open = False
        self.position = position
        self.size = size
        self.on_enter_event = on_enter_event
        open_path = os.path.join(ASSETS_DIR, open_dir)
        closed_path = os.path.join(ASSETS_DIR, closed_dir)
        self.open_sprite = ImageButton(position, size, open_path, open_path, None)     
        self.closed_sprite = ImageButton(position, size, closed_path, closed_path, None) 

    def process_input(self, events, mouse, *args):
        pass

    def update(self, mouse=pygame.mouse):
        pass

    def render(self, screen):
        if self.active:
            # rendering here
            if self.open:
                self.open_sprite.render(screen)
            else:
                self.closed_sprite.render(screen)