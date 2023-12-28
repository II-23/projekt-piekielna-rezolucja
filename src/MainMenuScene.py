from BaseScene import BaseScene, setup_button
from Slider import Slider_Bar
import pygame

class MainMenuScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager, background_color=background_color)
        #backgorund for start
        piwo_img = pygame.image.load("./assets/piwo.png")
        # creating buttons
        self.gameplay_screen_button = setup_button(self.gameStateManager, 'level', (100, 100))
        # adding elements to start scene
        self.add_ui_element(self.gameplay_screen_button)
        self.add_background_image(piwo_img)