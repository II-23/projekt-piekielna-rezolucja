from Scenes.BaseScene import BaseScene, setup_button
from Utils.Character import Player
from Utils.Area import Area
from Utils.volume_slider import Volume_slider
from Utils.Slider import Slider_Bar
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from Config.graphics import RESOLUTION
from soundtrackmanager import SoundtrackManager

import pygame
import os

class SettingsScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        # backgorund for settings
        piwo_img = pygame.image.load(ASSETS_DIR + "/piwo.png")
        self.add_background_image(piwo_img)
        # positions for easy placing of new things
        #settings_pos = [i]
        help_text_color = (166, 54, 54)
        self.slider_text = Button((340, 180), (600, 50), None, help_text_color, help_text_color, help_text_color)
        self.slider_text.init_text(None, 36, (0,0,0), "Volume: ", False, True)
        self.slider = Volume_slider((650, 180+25-10), (200, 20), 0.5,0,100,'red','grey',50)
        self.slider.observer_functions.append(SoundtrackManager.setVolume)
        self.add_ui_element(self.slider_text)
        self.add_ui_element(self.slider)

        self.back_to_menu_button = setup_button(gameStateManager, 'start', (1060, 600))
        self.back_to_menu_button.init_text(text="return to menu", align_center_h=True, align_center_w=True)
        self.add_ui_element(self.back_to_menu_button)