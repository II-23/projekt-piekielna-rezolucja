from Scenes.BaseScene import BaseScene, setup_button
from Utils.Character import Player
from Utils.CharacterAnimation import CharacterAnimation
from Utils.Area import Area
from Utils.volume_slider import Volume_slider
from Utils.Slider import Slider_Bar
from Utils.Button import Button
from Config.definitnios import ASSETS_DIR
from Utils.PiekielnaRezolucjaLogo import PiekielnaRezolucjaLogo
from Config.graphics import RESOLUTION
from soundtrackmanager import SoundtrackManager
from Utils.Health_and_points import Health_and_points
from datasavemanager import DataSaveManager
import pygame
from Utils.clock import Clock

import os

class MainMenuScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        # backgorund for main menu
        logo = PiekielnaRezolucjaLogo((RESOLUTION[0]*0.3, 0))
        background_img = pygame.image.load(ASSETS_DIR + "/background.png")
        background_img = pygame.transform.scale(background_img, (1300,730))
        
        '''button for going to da GAME
        Here I create the function for the button manually because I want to pass the additional arguments to it,
        (Probably will add better way to do this) that is the dialog that will be loaded when changed to dialog scene.'''
        self.gameplay_screen_button = Button((100, 100), (200, 100), None, (0, 0, 0), (70, 70, 70), (200, 200, 200))
        def go_to_scene(args):
            gameStateManager.set_state('dialog', {'scene':'test_dialog'})
            #gameStateManager.states[gameStateManager.get_state()].on_entry({'scene':'test_dialog'})
        # self.gameplay_screen_button.on_click_event = go_to_scene
        # self.gameplay_screen_button.init_text(text='Start Button')
        # adding elements to start scene
        # self.add_ui_element(self.gameplay_screen_button)
        
        self.add_ui_element(logo)
        self.add_background_image(background_img)

        # setting up a character and things they can interact with
        self.character = Player((550, 300), 150, "player/player.png")
        
        self.area_intro = Area((600,700),(100,100),None)
        self.area_intro.on_enter_event = go_to_scene
        self.character.areas.append(self.area_intro)


        def go_to_settings(*args):
            gameStateManager.set_state('settings', {})
        self.area_settings = Area((0, 360),(5,100),None)
        self.area_settings.on_enter_event = go_to_settings
        self.character.areas.append(self.area_settings)

        def go_to_credits(*args):
            gameStateManager.set_state('credits', {})
        self.area_credits = Area((self.width, 360), (5,100), None)
        self.area_credits.on_enter_event = go_to_credits
        self.character.areas.append(self.area_credits)

        high_score_color = (0,0,0)
        self.high_score_text = Button((400, 140), (400,30), None, high_score_color, high_score_color, high_score_color)
        self.high_score_text.init_text(text_size=42, color=(75, 46, 223), text=f"Highscore: {DataSaveManager.get('Highscore')}")
        self.high_score_text.invisible = True
        self.add_ui_element(self.high_score_text)
        self.add_ui_element(self.character) 
  
    def on_entry(self, *args, **kwargs):
        self.character.reset()
        self.high_score_text.init_text(text_size=42, color=(75, 46, 223), text=f"Highscore: {DataSaveManager.get('Highscore')}")
        if (kwargs['prev_state'] != 'settings'):
            SoundtrackManager.playMusic("MainMenuTheme", loops=-1)
        super().on_entry(*args)

    def on_exity(self, *args, **kwargs):
        SoundtrackManager.stopMusic()
        super().on_exit(*args)