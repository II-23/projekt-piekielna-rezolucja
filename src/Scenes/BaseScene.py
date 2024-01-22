from Utils.Button import Button
from Utils.Slider import Slider_Bar
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from Formulas.Formula import Symbol, Formula
from Formulas.FormulaSet import Set_of_formulas
import pygame
from Utils.game_over import Game_over_window
from Utils.clock import Clock
from Config.graphics import RESOLUTION

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def setup_button(gameStateManager, to_change, position, **kwargs):
    '''This is a function that is used for creating a button that will switch current scene.'''
    def test2(args):
        gameStateManager.set_state(to_change, args)
    button2 = Button(position, (200, 100), test2, (0, 0, 0), (70, 70, 70), (200, 200, 200), **kwargs)
    return button2

class BaseScene:
    ''' This is a template for all scenes in this game. It has 3 crucial methods: render(), update(), process_input()
    They are vital for this shit working, so if you want to override them, please put them in your stupid class.
    __init__() of BaseScene should be the first thing that is executed in init of each new scene.
    If you want to see how to add stuff to your scene (buttons, sliders etc.) go to the GameplayScene.py
    '''
    def __init__(self, display, gameStateManager, background_color=WHITE):
        self.display = display
        self.pause = False
        self.width = display.get_width()
        self.height = display.get_height()
        self.gameStateManager = gameStateManager
        self.ui_elements = [] # list of all elements of our ui, buttons, sliders, etc. 
        self.background_image = None
        self.background_color = background_color
        self.screen_saver = pygame.Surface(RESOLUTION)
        self.screen_saver_alpha = 255
        self.screen_saver.set_alpha(self.screen_saver_alpha)                
        self.screen_saver.fill((0,0,0))
        self.transition_tick = 15
        self.lower_opacity = False
        self.up_opacity = False
          
        
    def on_entry(self, *args, **kwargs):
        '''This is the method that is executed when GameStateManager changes to a scene. For example you can use it 
        to reset gameplay, generate new formulas etc. Override it in each scene, with your own code, if you want to use it.'''
        self.lower_opacity = True
        self.pause = True
    
    def on_exit(self, **kwargs):
        '''This is a method that is executed when leaving a scene'''
        self.up_opacity = True
        self.pause = True
  
    # These two are just for adding stuff to the scene
    def add_ui_element(self, button):
        self.ui_elements.append(button)
        
    def add_background_image(self, new_image):
        self.background_image = new_image
         
    def process_input(self, events, pressed_keys):
        if not self.pause:
            for element in self.ui_elements:
                element.process_input(events, pygame.mouse, 0)
            
    def update(self, mouse=pygame.mouse):
        for element in self.ui_elements:
            element.update(pygame.mouse)
            
    def render_base_ui(self, screen):
        for element in self.ui_elements:
            element.render(screen)
            '''!!!IMPORTANT!!!
               !!!UwAGA KURWA!!!
            If your class that displays something needs some blit(), put it here just like this one
            If you need to give it some more parameters or something'''
            if isinstance(element, Slider_Bar):
                screen.blit(element.get_surface(), (screen.get_width() - element.get_surface().get_width(), 0))  
            if isinstance(element, Symbol):
                screen.blit(element.get_surface(), element.get_rect())   
            if isinstance(element, Formula):
                screen.blit(element.get_surface(), element.get_rect())   
            if isinstance(element, Set_of_formulas):
                screen.blit(element.get_surface(), element.get_rect())   
            if isinstance(element, PiekielnaRezolucjaLogo):
                screen.blit(element.get_surface(), element.get_rect())   
            if isinstance(element, Game_over_window):
                screen.blit(element.get_surface(), element.get_rect())   
            #if isinstance(element, Clock):
            #    screen.blit(element.get_surface(), element.get_rect())   
                
        
    def render(self, screen):
        self.display.fill(self.background_color)
        if self.background_image is not None:
            self.display.blit(self.background_image, (self.display.get_width() * 0.5 - 0.5 * self.background_image.get_width(), 0))
        self.render_base_ui(screen)
        
        '''When entering a scene the screen will start to become less black'''
        if self.lower_opacity:
            opacity = self.screen_saver_alpha - self.transition_tick
            if opacity <= 0:
                opacity = 0
                self.lower_opacity = False
                self.pause = False
            self.screen_saver_alpha = opacity
        '''And when exiting a scene it will go dark'''    
        if self.up_opacity:
            opacity = self.screen_saver_alpha + self.transition_tick
            if opacity >= 255:
                opacity = 255
                self.up_opacity = False
                self.pause = False
            self.screen_saver_alpha = opacity
            
        self.screen_saver.set_alpha(self.screen_saver_alpha)
        screen.blit(self.screen_saver, (0,0))