from Button import Button
import pygame

class BaseScene:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = []
        
    def add_button(self, button):
        self.buttons.append(button)
        
    def process_input(self, events, pressed_keys):
        for button in self.buttons:
            button.process_input(events, pygame.mouse)
            
    def update(self, mouse=pygame.mouse):
        for button in self.buttons:
            button.update(pygame.mouse)
            
    def render_base_ui(self, screen):
        for button in self.buttons:
            button.render(screen)   
            
    def render(self, screen):
        self.display.fill('blue')
        self.render_base_ui(screen)

class Start(BaseScene):
    def __init__(self, display, gameStateManager):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager)
        
    def render(self, screen):
        self.display.fill('red')
        self.render_base_ui(screen)
        
class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
        
    def get_state(self):
        return self.currentState
    
    def set_state(self, state):
        self.currentState=state
