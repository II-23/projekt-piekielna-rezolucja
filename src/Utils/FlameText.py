import pygame
import os
from Utils.GifPlayer import GifPlayer
from Config.definitnios import ASSETS_DIR

class FlameText:
    def __init__(self, pos, path_to_gif_frames, **kwargs):
        x, y = pos
        self.ends_credits = False
        if ('ends_credits' in kwargs):
            self.ends_credits = kwargs['ends_credits']
        self.pos_rect = pygame.Rect(x, y, 0, 0)
        self.gif_path = path_to_gif_frames
        self.frame_update_rate = 0.05
        self.logo_gif_player = GifPlayer(self.gif_path, self.frame_update_rate)
    def get_surface(self):
        return self.logo_gif_player.get_surface()
    def get_rect(self):
        return self.pos_rect
    def process_input(self, events, mouse, *args):
        pass
    def update(self, mouse):
        self.logo_gif_player.update(mouse)
    def render(self, screen):
        screen.blit(self.get_surface(), self.get_rect())