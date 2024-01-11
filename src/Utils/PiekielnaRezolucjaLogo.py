import pygame
import os
from Config.definitnios import ASSETS_DIR
import time

class PiekielnaRezolucjaLogo(pygame.sprite.Sprite):
    def __init__(self, pos):
        x, y = pos
        self.pos_rect = pygame.Rect(x,y,0,0)
        self.piekielna_rezolucja_frames = [pygame.image.load(os.path.join(ASSETS_DIR, "piekielna_rezolucja_gif", frame)) for frame in sorted(os.listdir(os.path.join(ASSETS_DIR, "piekielna_rezolucja_gif")))]
        self.previous_step_time = time.time()
        self.FRAME_UPDATE_RATE = 0.05
        self.current_frame = 0
    def process_input(self, events, mouse, *args):
        pass
    def update(self, mouse):
        current_time = time.time()
        time_elapsed = current_time - self.previous_step_time
        if (time_elapsed >= self.FRAME_UPDATE_RATE):
            self.current_frame = (self.current_frame + 1) % len(self.piekielna_rezolucja_frames)
            self.previous_step_time = current_time
    def render(self, screen):
        pass
    def get_surface(self):
        print(self.current_frame)
        return self.piekielna_rezolucja_frames[self.current_frame]
    def get_rect(self):
        return self.pos_rect