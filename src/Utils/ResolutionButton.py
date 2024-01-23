import pygame
import os
from Utils.GifPlayer import GifPlayer
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR

COLOR_PLACEHOLDER = (0,0,0) #Used bcs I wanted to inherit from Button class, but its color feature is useless for me

class ResolutionButton(Button, pygame.sprite.Sprite):
    def __init__(self, position, on_click_event):
        FRAME_PATH = os.path.join(ASSETS_DIR, "resolution_button_frames")
        FRAME_UPDATE_RATE = 0.05
        self.gif_player = GifPlayer(FRAME_PATH, FRAME_UPDATE_RATE)
        self.is_flamed = False
        self.size = self.gif_player.get_surface().get_size()
        self.not_flamed_surface = pygame.image.load(os.path.join(ASSETS_DIR, "resolution_button_without_flames.gif"))
        self.flames_alpha = 0
        Button.__init__(self, position, self.size, on_click_event, COLOR_PLACEHOLDER, COLOR_PLACEHOLDER, COLOR_PLACEHOLDER)
    
    def make_flamed(self):
        self.is_flamed = True

    def make_not_flamed(self):
        self.is_flamed = False

    def update(self, mouse):
        Button.update(self, mouse)
        self.gif_player.update(mouse)

    def render(self, screen):
        screen.blit(self.get_surface(), self.get_rect())

    def get_surface(self):
        return_surface = self.not_flamed_surface.copy().convert_alpha()
        flames = self.gif_player.get_surface()
        if self.is_flamed:
            self.flames_alpha = min(255, self.flames_alpha + 20)
        else:
            self.flames_alpha = max(0, self.flames_alpha - 20)
        flames.set_alpha(self.flames_alpha)
        return_surface.blit(flames, (0,0))
        return return_surface
        return_surface.blit(flame)

    def get_rect(self):
        return pygame.Rect(*self.position, *self.size)

    def get_height(self):
        return self.size[1]

    def get_width(self):
        return self.size[0]