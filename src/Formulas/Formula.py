import pygame
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR
from enum import Enum
import os

non_hover_symbol_list = [ASSETS_DIR + "/variables/non_hover/" + variable_asset for variable_asset in os.listdir(ASSETS_DIR + "/variables/non_hover")]

class Symbol_Type(Enum):
    ALTERNATIVE = 1
    NEGATION = 2
    VARIABLE = 3

#If type is Symbol_Type.VARIABLE, then kwarg variable_index must be specified
class Symbol(pygame.sprite.Sprite):
    def __init__(self, size, type, pos, **kwargs):
        self.state=0
        self.width = size[0]
        self.height = size[1]
        self.x=pos[0]
        self.y=pos[1]
        #assigning image to symbol according to num value. 0 is alternate, -1 is negate. 2nd row is a placeholder for colored icons(hovered)
        match type:
            case Symbol_Type.ALTERNATIVE:
                self.symbol = [pygame.image.load(ASSETS_DIR + "/alternate.png").convert_alpha(), pygame.image.load(ASSETS_DIR + "/minus-sign.png").convert_alpha()]
            case Symbol_Type.NEGATION:
                self.symbol = [pygame.image.load(ASSETS_DIR + "/minus-sign.png").convert_alpha(), pygame.image.load(ASSETS_DIR + "/minus-sign.png").convert_alpha()]
            case Symbol_Type.VARIABLE:
                self.symbol = [pygame.image.load(non_hover_symbol_list[kwargs['variable_index']]).convert_alpha(), pygame.image.load(ASSETS_DIR + "/minus-sign.png").convert_alpha()]
        
        self.surface = pygame.transform.scale(self.symbol[0], (self.width, self.height))
        self.symbol_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def render(self, screen):
        if self.state==0:
            self.surface = pygame.transform.scale(self.symbol[0], (self.width, self.height))
        if self.state==1:
            self.surface = pygame.transform.scale(self.symbol[1], (self.width, self.height))
        if self.state==2:
            self.surface = pygame.transform.scale(self.symbol[1], (self.width, self.height))
        
    def update(self, mouse_pos):
        pass
    def process_input(self, raz, dwa, trzy):
        pass
    def get_surface(self):
        return self.surface
    def get_rect(self):
        return self.symbol_rect
    

class Formula(pygame.sprite.Sprite):
    def __init__(self, size, pos, list_of_formulas, width, clickable):
        self.clickable=clickable
        self.state=0
        self.width=size[0]
        self.height=size[1]
        self.x=pos[0]
        self.y=pos[1]
        self.max_width=width
        self.tab=[]
        self.surface = pygame.surface.Surface((self.width*12, self.height)).convert_alpha()
        
        self.content=list_of_formulas
        self.formula_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #reading off list. Each position in list indicates if such element is part of formula. 0 means no variable, 1 means 
        #variable, -1 means negated variable. Code appends alternate symbols aswell
        counter=0
        for i in range(len(list_of_formulas)):
            if list_of_formulas[i]==1:
                if len(self.tab)>0:
                    self.tab.append(Symbol((self.width, self.height), Symbol_Type.ALTERNATIVE, (pos[0]+counter*self.width, pos[1])))
                    counter+=1
                self.tab.append(Symbol((self.width, self.height), Symbol_Type.VARIABLE, (pos[0]+counter*self.width, pos[1]), variable_index=i))
                counter=counter+1
            if list_of_formulas[i]==-1:
                if len(self.tab)>0:
                    self.tab.append(Symbol((self.width, self.height), Symbol_Type.ALTERNATIVE, (pos[0]+counter*self.width, pos[1])))
                    counter+=1
                self.tab.append(Symbol((self.width, self.height), Symbol_Type.NEGATION, (pos[0]+counter*self.width, pos[1])))
                counter=counter+1
                self.tab.append(Symbol((self.width, self.height), Symbol_Type.VARIABLE, (pos[0]+counter*self.width, pos[1]), variable_index=i))
                counter=counter+1
    def render(self, screen):
        #fill with transparent and blit all of the symbols stored in "tab"
        self.get_surface().fill((0,0,0,0))
        i=0
        for symbol in self.tab:
            symbol.render(screen)
            self.get_surface().blit(symbol.get_surface(), (i*self.width,0))
            i+=1
    def cursor_over_formula(self, pos):
        return self.x<pos[0]<self.x+self.width*12 and self.y<pos[1]<self.y+self.height
    def update(self, mouse=pygame.mouse):
        #This was meant to keep track if formula is hovered. State variable means:
        #0: default 1:hovered 2:clicked(not yet assigned slot) 3:clicked(assigned slot 1) 4:clicked(assigned slot 2)
        #used to cause bug where formulas hovered and clicked would act like not hovered, not clicked.
        #bugs sometimes. Plz review, i have no idea what goes wrong.
        mouse_pos = (mouse.get_pos()[0], mouse.get_pos()[1])
        if self.state==1 and self.cursor_over_formula(mouse_pos)==False and self.clickable:
            for element in self.tab:
                element.state=0
            self.state=0

        if self.state==0 and self.cursor_over_formula(mouse_pos)==True and self.clickable:
            for element in self.tab:
                element.state=1
            self.state=1
        
    def process_input(self, events, mouse, *args):
        #if formula is clicked it checks if it is hovered. If so, it is now clicked. if not, it is now hovered.
        pos=mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.cursor_over_formula(pos) and self.clickable:
                if self.state==1:
                    self.state=2
                else:
                    self.state=1
    def get_surface(self):
        return self.surface
    def get_rect(self):
        return self.formula_rect
