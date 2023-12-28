import pygame
from pygame.locals import *
import numpy
import math
from gamestatemanager import GameStateManager
from Scenes.BaseScene import * # this also imports slider stuff
from Scenes.GameplayScene import GameplayScene
from Scenes.MainMenuScene import MainMenuScene
from Slider import *
from char import *
from generator import *

GAME_TITLE = "Piekielna rezolucja 3"
GAME_LOGO = pygame.image.load("./assets/placeholder_logo.png")
RESOLUTION = (1280, 720)
GRAY_COLOR = (65, 65, 67)
SLIDER_SIZE = (220, 70)

class Main_Window:
    def __init__(self, resolution):
        self.size = self.width, self.height = resolution
        pygame.init()
        self._display_surface = pygame.display.set_mode(self.size)
        self.running = True
        self.FramesPerSec = pygame.time.Clock()
        self.FPS = 60
        # setting up manager for game states (in other words: scenes)
        self.gameStateManager = GameStateManager('start') # this is the default scene
        # Here we create scenes for our game. The init part is handled in __init__() of each of these scenes,
        # so this space here, in main_window, can stay clean. If you want to create your own scene or add some
        # buttons/sliders/whatever check out .py files of these scenes (and BaseScene) here and take inspirations.  
        self.start = MainMenuScene(self._display_surface, self.gameStateManager, background_color=GRAY_COLOR)
        self.level = GameplayScene(self._display_surface, self.gameStateManager, background_color=GRAY_COLOR)
        self.states = {'start':self.start, 'level':self.level}
        
        self.paper_sheet = pygame.image.load("./assets/papersheet.jpg")
        self.paper_sheet = pygame.transform.rotate(self.paper_sheet, 90)
        paper_height = self.paper_sheet.get_height()
        self.paper_sheet = pygame.transform.scale_by(self.paper_sheet, self.height/paper_height)
        self.slider_bar = Slider_Bar((0.18 * self.width, self.height))
        #tutaj
        #self.symbol=Symbol((25,25), 7, (500,300))
        #self.formula=Formula((25,25), (500, 400), [-1,-1,1], 50000)
        #self.set=Set_of_formulas((500,500), (500,300), [[3,[-1,-1,1]],[3,[-1,-1,1]]])
        x=generate(max_variable_number, formulas_number, max_len, formula_choice_modifier)
        self.set=Set_of_formulas((500,500), (500,300), x)
        self.slider_bar.add_slider("p")
        self.slider_bar.add_slider("q")
        self.slider_bar.add_slider("r")
        self.slider_bar.add_slider("k")
        self.slider_bar.add_slider("s")
        self.slider_bar.add_slider("h")
        self.slider_bar.add_slider("u")
        self.slider_bar.add_slider("w") 
    def on_init(self):
        self._display_surface.fill(GRAY_COLOR)
        self._display_surface.blit(self.paper_sheet, (self.width * 0.5 - 0.5 * self.paper_sheet.get_width(), 0))
        self.slider_bar_rect = self._display_surface.blit(self.slider_bar.get_surface(), (self.width - self.slider_bar.get_surface().get_width(), 0))
        self.slider_bar.set_parent_rect(self.slider_bar_rect)
    def on_event(self, event):
        button_clicks = []
        match event.type:
            case pygame.QUIT:
                self.running = False
                
    def on_loop(self):
        self.states[self.gameStateManager.get_state()].update(pygame.mouse)
        
    def on_render(self):
        self.states[self.gameStateManager.get_state()].render(self._display_surface)
        for x in self.set.tab:
            for y in x.tab:
                self._display_surface.blit(y.get_surface(), y.get_rect())
        pygame.display.update()
        
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        while (self.running):
            events = pygame.event.get()
            for event in events:
                self.on_event(event)
            self.states[self.gameStateManager.get_state()].process_input(events, pygame.mouse)
            self.on_loop()
            self.on_render()
            self.FramesPerSec.tick(self.FPS)
        self.on_cleanup()

if __name__ == "__main__":
    
    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_icon(GAME_LOGO)
    app = Main_Window(RESOLUTION)
    app.on_execute()