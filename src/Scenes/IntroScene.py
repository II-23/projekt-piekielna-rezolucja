from Scenes.BaseScene import BaseScene, setup_button
from Utils.Character import Player
from Utils.volume_slider import Volume_slider
from Utils.Slider import Slider_Bar
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from Config.graphics import RESOLUTION

import pygame
import os

class IntroScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        #TODO add some intro here (an image that slowly shows up and then goes black)
        # look at on_entry and on_exit methods in BaseScene.py for more info
  
    def on_entry(self, *args):
        super().on_entry(*args)

