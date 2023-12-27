from Button import Button
from BaseScene import *
import pygame

class Start(BaseScene):
    def __init__(self, display, gameStateManager, background_color=WHITE):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager, background_color=background_color)
        
    # def render(self, screen):
    #     self.display.fill('red')
    #     self.render_base_ui(screen)
        
class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
        
    def get_state(self):
        return self.currentState
    
    def set_state(self, state):
        self.currentState=state
