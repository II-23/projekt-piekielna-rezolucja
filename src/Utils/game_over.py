import pygame
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR

class Game_over_window:
    def __init__(self, pos, size, result, formula_set):
        victory = pygame.image.load(ASSETS_DIR + "/victory.png").convert_alpha()
        self.victory_surface=pygame.transform.scale(victory, (300,100)).convert_alpha()
        loss = pygame.image.load(ASSETS_DIR + "/loss.jpg").convert_alpha()
        self.loss_surface=pygame.transform.scale(loss, (300,100)).convert_alpha()
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
            self.surface.fill((0,0,0,0))
            self.get_surface().blit(self.victory_surface, (100,0))
        if self.formula_set.state==2:
            self.surface.fill((0,0,0,0))
            self.get_surface().blit(self.loss_surface, (100,0))
        if self.formula_set.state==0:
            self.get_surface().fill((0,0,0,0))
        
    def update(self, mouse_pos):
        pass
    def process_input(self, raz, dwa, trzy):
        pass