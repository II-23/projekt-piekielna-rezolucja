import pygame
import os
from Utils.GifPlayer import GifPlayer
from Utils.Button import Button, Status
from Config.definitnios import ASSETS_DIR

COLOR_PLACEHOLDER = (0,0,0) #Used bcs I wanted to inherit from Button class, but its color feature is useless for me

class ImageButton(Button, pygame.sprite.Sprite):
    def __init__(self, position, size, image_dir, image_dir_hover, on_click_event, **kwargs):
        self.background = pygame.image.load(image_dir)
        self.background = pygame.transform.scale(self.background, size)
        self.hover_background = pygame.image.load(image_dir_hover)
        self.hover_background = pygame.transform.scale(self.hover_background, size)
        self.size = size
        self.active = True
        Button.__init__(self, position, self.size, on_click_event, COLOR_PLACEHOLDER, COLOR_PLACEHOLDER, COLOR_PLACEHOLDER, **kwargs)
    
    def update(self, mouse, offset = (0,0)):
        Button.update(self, mouse, offset)

    def process_input(self, events, mouse, *args):
        if self.active:
            super().process_input(events, mouse, args)

    def render(self, screen):
        if self.active:
            if (self.status == Status.HOWER):
                screen.blit(self.hover_background, self.get_rect())
            else:
                screen.blit(self.background, self.get_rect())
            Button.render_text(self, screen)

    def get_rect(self):
        return pygame.Rect(*self.position, *self.size)

    def get_height(self):
        return self.size[1]

    def get_width(self):
        return self.size[0]