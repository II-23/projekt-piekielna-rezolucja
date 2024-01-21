import pygame
import os
from Utils.GifPlayer import GifPlayer
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR

COLOR_PLACEHOLDER = (0,0,0) #Used bcs I wanted to inherit from Button class, but its color feature is useless for me

class EvaluateButton(Button, pygame.sprite.Sprite):
    def __init__(self, position, on_click_event):
        self.background = pygame.image.load(os.path.join(ASSETS_DIR, "evaluate_button.png"))
        Button.__init__(self, position, self.size, on_click_event, COLOR_PLACEHOLDER, COLOR_PLACEHOLDER, COLOR_PLACEHOLDER)
        Button.init_text(self, text="SPRAWDŹ")
    
    def update(self, mouse):
        Button.update(self, mouse)
        self.gif_player.update(mouse)

    def render(self, screen):
        screen.blit(self.get_surface(), self.get_rect())
        Button.render_text(self, screen)

    def get_surface(self):
        return self.background

    def get_rect(self):
        return pygame.Rect(*self.position, *self.size)

    def get_height(self):
        return self.size[1]

    def get_width(self):
        return self.size[0]