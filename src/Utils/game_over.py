import pygame
from Utils.Button import Button

class Game_over_window:
    def __init__(self, pos, size, result, formula_set):
        self.surface=pygame.Surface(size)
        self.surface = self.surface.convert_alpha()
        self.rect=pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.result=result
        self.formula_set=formula_set
    def get_surface(self):
        return self.surface
    def get_rect(self):
        return self.rect
    def render(self, screen):
        if self.formula_set.state==1:
            self.surface.fill((100,0,0))
        if self.formula_set.state==0:
            self.get_surface().fill((0,0,0,0))
        
    def update(self, mouse_pos):
        pass
    def process_input(self, raz, dwa, trzy):
        pass