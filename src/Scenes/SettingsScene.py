from Scenes.BaseScene import BaseScene, setup_button
from Utils.Character import Player
from Utils.Area import Area
from Utils.volume_slider import Volume_slider
from Utils.Slider import Slider_Bar
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from Config.graphics import RESOLUTION

import pygame
import os

class SettingsScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        # backgorund for settings
        piwo_img = pygame.image.load(ASSETS_DIR + "/piwo.png")
        self.add_background_image(piwo_img)

        self.slider = Volume_slider((200, 250), (200, 12), 0.5,0,100,'red','grey',50)
        self.add_ui_element(self.slider)

        self.back_to_menu_button = setup_button(gameStateManager, 'start', (800, 600))
        self.back_to_menu_button.init_text(text="return to menu")
        self.add_ui_element(self.back_to_menu_button)