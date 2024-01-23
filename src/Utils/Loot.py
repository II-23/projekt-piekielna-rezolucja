import pygame
from Utils.Area import Area
from Utils.ImageButton import ImageButton
from Utils.Image import Image
from Config.definitnios import ASSETS_DIR
import os
from random import randint

LOOT_POINTS = 1000
loot_spirtes_path = [os.path.join(ASSETS_DIR, "loot_img", x) for x in os.listdir(os.path.join(ASSETS_DIR, "loot_img"))]

class Loot:
    def __init__(self, position, size, on_enter_event, image_dir) -> None:
        self.position = position
        self.size = size
        self.active = True
        self.on_enter_event = on_enter_event
        self.image_dir = image_dir
        self.sprite = Image(position, size, self.image_dir)

    def process_input(self, events, mouse, *args):
        pass

    def update(self, mouse=pygame.mouse):
        pass

    def render(self, screen):
        if self.active:
              self.sprite.render(screen)
    def set_active(self, value):
        self.active = value