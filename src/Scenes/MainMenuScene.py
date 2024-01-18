from Scenes.BaseScene import BaseScene, setup_button
from Utils.Slider import Slider_Bar
from Config.definitnios import ASSETS_DIR
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from Config.graphics import RESOLUTION
import pygame
import os

class MainMenuScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        # backgorund for main menu
        logo = PiekielnaRezolucjaLogo((RESOLUTION[0]*0.3, 0))
        piwo_img = pygame.image.load(ASSETS_DIR + "/piwo.png")
        # button for going to da GAME
        self.gameplay_screen_button = setup_button(self.gameStateManager, 'dialog', (100, 100))
        self.gameplay_screen_button.init_text(text='Start Button')
        # adding elements to start scene
        self.add_ui_element(self.gameplay_screen_button)
        self.add_ui_element(logo)
        self.add_background_image(piwo_img)
        
    def on_entry(self):
        print('entering main menu scene')
        return super().on_entry()