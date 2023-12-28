import pygame
from pygame.locals import *
import numpy
import math
from gamestatemanager import GameStateManager
from Scenes.BaseScene import * # this also imports slider stuff
from Scenes.GameplayScene import GameplayScene
from Scenes.MainMenuScene import MainMenuScene

RESOLUTION = (1280, 720)
GRAY_COLOR = (65, 65, 67)
SLIDER_SIZE = (220, 70)

def setup_button(gameStateManager, to_change, position):
    def test2(args):
        gameStateManager.set_state(to_change)
    button2 = Button(position, (200, 100), test2, (0, 0, 0), (70, 70, 70), (200, 200, 200))
    return button2

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
        # Here we create scenes for our game. The input part is handled in __input__() of each of these scenes,
        # so this space here, in main_window, can stay clean. If you want to create your own scene check out 
        # .py files of these scenes (and BaseScene) here and take inspirations.  
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
        self.on_init()
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
    app = Main_Window(RESOLUTION)
    app.on_execute()