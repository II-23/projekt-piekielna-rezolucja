from Utils.Character import Player
import pygame

class Health_and_points:
    def __init__(self,player,size:tuple,pos:tuple,col_bar,col_text,size_text,difficulty=None):
        self.player=player
        self.health=self.player.health
        self.points=self.player.points
        self.difficulty=difficulty
        self.pos=pos
        self.size=size
        self.col_bar=col_bar
        self.col_text=col_text
        self.size_text=size_text
        self.button_rect=pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        if difficulty==None :
            self.text=f'Health:{self.health} Points{self.points}'

    def set_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty
        self.update_text()

    def update_text(self):
        if self.difficulty is None:
            self.text = f'Health: {self.health} Points: {self.points}'
        else:
            self.text = f'Health: {self.health} Points: {self.points} Difficulty: {self.difficulty}'

    def render(self,screen):
        pygame.draw.rect(screen, self.col_bar, self.button_rect)
        font = pygame.font.Font(None, self.size_text)  
        text_surface = font.render(self.text, True, self.col_text)  
        text_rect = text_surface.get_rect()
        text_rect.center = self.button_rect.center
        screen.blit(text_surface, text_rect)

    def process_input(self,events,mouse,*args):
        pass

    def update(self,screen):
        self.health = self.player.health
        self.points = self.player.points
        self.update_text()

