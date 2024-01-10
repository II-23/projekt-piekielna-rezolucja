import pygame
from pygame.locals import *
import numpy
import math
from gamestatemanager import GameStateManager
from Scenes.BaseScene import * # this also imports slider stuff
from Scenes.GameplayScene import GameplayScene
from Scenes.MainMenuScene import MainMenuScene
from Utils.Slider import *
from Formulas.Formula import *
from Formulas.FormulaSet import *
from Config.definitnios import ASSETS_DIR

GAME_TITLE = "Piekielna rezolucja 3"
GAME_LOGO = pygame.image.load(ASSETS_DIR + "/placeholder_logo.png")
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
    def on_event(self, event):
        button_clicks = []
        match event.type:
            case pygame.QUIT:
                self.running = False
                
    def on_loop(self):
        self.states[self.gameStateManager.get_state()].update(pygame.mouse)
        
    def on_render(self):
        self.states[self.gameStateManager.get_state()].render(self._display_surface)
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