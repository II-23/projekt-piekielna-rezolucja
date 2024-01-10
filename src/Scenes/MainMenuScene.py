# AD     
from Scenes.BaseScene import BaseScene, setup_button
from Utils.Slider import Slider_Bar
from Config.definitnios import ASSETS_DIR
import pygame

class MainMenuScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager, background_color=background_color)
        # backgorund for main menu
        piwo_img = pygame.image.load(ASSETS_DIR + "/piwo.png")
        # button for going to da GAME
        self.gameplay_screen_button = setup_button(self.gameStateManager, 'level', (100, 100))
        # adding elements to start scene
        self.add_ui_element(self.gameplay_screen_button)
        self.add_background_image(piwo_img)