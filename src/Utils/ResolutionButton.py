import pygame
import os
from Utils.GifPlayer import GifPlayer
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR

COLOR_PLACEHOLDER = (0,0,0) #Used bcs I wanted to inherit from Button class, but its color feature is useless for me

class ResolutionButton(Button, pygame.sprite.Sprite):
    def __init__(self, position, size, on_click_event):
        Button.__init__(self, position, size, on_click_event, COLOR_PLACEHOLDER, COLOR_PLACEHOLDER, COLOR_PLACEHOLDER)
        FRAME_PATH = os.path.join(ASSETS_DIR, "resolution_button_frames")
        FRAME_UPDATE_RATE = 0.05
        self.gif_player = GifPlayer(FRAME_PATH, FRAME_UPDATE_RATE)
        self.is_visible = False
    
    def make_visible(self):
        self.is_visible = True

    def make_not_visible(self):
        self.is_visible = False

    def render(self, screen):
        if (self.is_visible):
            screen.blit(self.get_surface(), self.get_rect())

    def get_surface(self):
        return self.gif_player.get_surface()
    
    def get_rect(self):
        return pygame.Rect(*self.position, *self.size)
