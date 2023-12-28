from Button import Button
from Slider import Slider_Bar
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def setup_button(gameStateManager, to_change, position):
    def test2(args):
        gameStateManager.set_state(to_change)
    button2 = Button(position, (200, 100), test2, (0, 0, 0), (70, 70, 70), (200, 200, 200))
    return button2

class BaseScene:
    def __init__(self, display, gameStateManager, background_color=WHITE):
        self.display = display
        self.width = display.get_width()
        self.height = display.get_height()
        self.gameStateManager = gameStateManager
        self.ui_elements = [] # list of all elements of our ui, buttons, sliders, etc. 
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
            if isinstance(element, Slider_Bar):
                screen.blit(element.get_surface(), (screen.get_width() - element.get_surface().get_width(), 0))   
            
    def render(self, screen):
        self.display.fill(self.background_color)
        if self.background_image is not None:
            self.display.blit(self.background_image, (self.display.get_width() * 0.5 - 0.5 * self.background_image.get_width(), 0))
        self.render_base_ui(screen)
        
        
class Start(BaseScene):
    def __init__(self, display, gameStateManager, background_color=WHITE):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager, background_color=background_color)
        
    # def render(self, screen):
    #     self.display.fill('red')
    #     self.render_base_ui(screen)
