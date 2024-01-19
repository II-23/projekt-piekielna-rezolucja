from Scenes.BaseScene import BaseScene, setup_button
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
        # backgorund for main menu
        logo = PiekielnaRezolucjaLogo((RESOLUTION[0]*0.3, 0))
        piwo_img = pygame.image.load(ASSETS_DIR + "/piwo.png")
        '''button for going to da GAME
        Here I create the function for the button manually because I want to pass the additional arguments to it,
        (Probably will add better way to do this) that is the dialog that will be loaded when changed to dialog scene.'''
        self.gameplay_screen_button = Button((100, 100), (200, 100), None, (0, 0, 0), (70, 70, 70), (200, 200, 200))
        def go_to_scene(args):
            gameStateManager.set_state('dialog')
            gameStateManager.states[gameStateManager.get_state()].on_entry({'scene':'test_dialog'})
        self.gameplay_screen_button.on_click_event = go_to_scene
        self.gameplay_screen_button.init_text(text='Start Button')
        # adding elements to start scene
        self.add_ui_element(self.gameplay_screen_button)
        self.add_ui_element(logo)
        self.add_background_image(piwo_img)
        
    def on_entry(self, *args):
        print('entering main menu scene')