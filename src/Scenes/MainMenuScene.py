# AD     
from Scenes.BaseScene import BaseScene, setup_button
from volume_slider import Volume_slider
from Utils.Character import Player
from Utils.Slider import Slider_Bar
from Config.definitnios import ASSETS_DIR
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from Config.graphics import RESOLUTION

import pygame
import os

class MainMenuScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager, background_color=background_color)
        # backgorund for main menu
        logo = PiekielnaRezolucjaLogo((RESOLUTION[0]*0.3, 0))
        piwo_img = pygame.image.load(ASSETS_DIR + "/piwo.png")
        # button for going to da GAME
        self.gameplay_screen_button = setup_button(self.gameStateManager, 'level', (100, 100))
        # adding elements to start scene
        self.add_ui_element(self.gameplay_screen_button)
        self.add_background_image(piwo_img)
        
        self.slider = Volume_slider((200, 250), (200, 12), 0.5,0,100,'red','grey',50)
        self.add_ui_element(self.slider)

        self.character = Player((0,0), 100, "player/player.png")
        self.add_ui_element(self.character)

        self.add_ui_element(logo)
        self.add_background_image(piwo_img)

