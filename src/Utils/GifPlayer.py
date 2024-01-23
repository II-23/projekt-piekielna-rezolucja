import pygame
import os
from Config.definitnios import ASSETS_DIR
import time

#Displays gifs
#frames_path is path to directory with images, frames should be named such that their lex order is the same as their gif order
#get_surface() method returns surface with current frame
class GifPlayer(pygame.sprite.Sprite):
    def __init__(self, frames_path, frame_update_rate):
        self.frames = [pygame.image.load(os.path.join(frames_path, frame)) for frame in sorted(os.listdir(frames_path))]
        self.previous_step_time = time.time()
        self.FRAME_UPDATE_RATE = frame_update_rate
        self.current_frame = 0
    def process_input(self, events, mouse, *args):
        pass
    def update(self, mouse):
        current_time = time.time()
        time_elapsed = current_time - self.previous_step_time
        if (time_elapsed >= self.FRAME_UPDATE_RATE):
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.previous_step_time = current_time
    def render(self, screen):
        pass
    def get_surface(self):
        return self.frames[self.current_frame]