import pygame
import os
from Utils.GifPlayer import GifPlayer
from Config.definitnios import ASSETS_DIR

class PiekielnaRezolucjaLogo:
    def __init__(self, pos):
        x, y = pos
        self.pos_rect = pygame.Rect(x, y, 0, 0)
        self.gif_path = os.path.join(ASSETS_DIR, "piekielna_rezolucja_gif")
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
        pass