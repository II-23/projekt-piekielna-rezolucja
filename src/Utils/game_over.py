import pygame
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR
from Formulas.FormulaSet import Set_Of_Formulas_State

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
        if self.formula_set.state != Set_Of_Formulas_State.DEFAULT:
            if self.formula_set.state == Set_Of_Formulas_State.OUT_OF_TIME:
                message="skończył się czas"
            if self.formula_set.state == Set_Of_Formulas_State.OUT_OF_SPACE:
                message="skończyło się miejsce"
            if self.formula_set.state == Set_Of_Formulas_State.WRONG_EVALUATION:
                message="niepoprawne wartościowanie"
            if self.formula_set.state == Set_Of_Formulas_State.FOUND_EVALUATION:
                message="znaleziono wartościowanie"
            if self.formula_set.state == Set_Of_Formulas_State.FOUND_PROOF:
                message="znaleziono dowód"
            font = pygame.font.Font('freesansbold.ttf', 32)
            color = (0, 255, 0)
            transparent = (1, 1, 1)
            text = font.render(message, True, color, transparent)
            text.set_colorkey((1,1,1))
        if self.formula_set.state==Set_Of_Formulas_State.FOUND_EVALUATION or self.formula_set.state==Set_Of_Formulas_State.FOUND_PROOF:
            self.surface.fill((0,0,0,0))
            self.get_surface().blit(self.victory_surface, (100,0))
            self.get_surface().blit(text, (100,100))
        if self.formula_set.state==Set_Of_Formulas_State.OUT_OF_SPACE or self.formula_set.state==Set_Of_Formulas_State.OUT_OF_TIME or self.formula_set.state==Set_Of_Formulas_State.WRONG_EVALUATION:
            self.surface.fill((0,0,0,0))
            self.get_surface().blit(self.loss_surface, (100,0))
            self.get_surface().blit(text, (100,100))
        if self.formula_set.state==self.formula_set.state==Set_Of_Formulas_State.DEFAULT:
            self.get_surface().fill((0,0,0,0))
        
    def update(self, mouse_pos):
        pass
    def process_input(self, raz, dwa, trzy):
        pass