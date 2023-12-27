from Button import Button
from Slider import Slider, Slider_Bar
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class BaseScene:
    def __init__(self, display, gameStateManager, background_color=WHITE):
        self.display = display
        self.gameStateManager = gameStateManager
        self.ui_elements = []
        self.background_image = None
        self.background_color = background_color
        
    def add_ui_element(self, button):
        self.ui_elements.append(button)
        
    def add_background_image(self, new_image):
        self.background_image = new_image
        
    def process_input(self, events, pressed_keys):
        for element in self.ui_elements:
            element.process_input(events, pygame.mouse, 0)
            
    def update(self, mouse=pygame.mouse):
        for element in self.ui_elements:
            element.update(pygame.mouse)
            
    def render_base_ui(self, screen):
        for element in self.ui_elements:
            element.render(screen)   
            
    def render(self, screen):
        self.display.fill(self.background_color)
        if self.background_image is not None:
            self.display.blit(self.background_image, (self.display.get_width() * 0.5 - 0.5 * self.background_image.get_width(), 0))
        self.render_base_ui(screen)