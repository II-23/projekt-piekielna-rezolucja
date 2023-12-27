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
            button.process_input(events, pygame.mouse, 0)
            
    def update(self, mouse=pygame.mouse):
        for button in self.buttons:
            button.update(pygame.mouse)
            
    def render_base_ui(self, screen):
        for button in self.buttons:
            button.render(screen)   
            
    def render(self, screen):
        self.display.fill('blue')
        self.render_base_ui(screen)