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

class MainMenuScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        # backgorund for settings
        piwo_img = pygame.image.load(ASSETS_DIR + "/piwo.png")