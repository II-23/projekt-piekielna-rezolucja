from Scenes.BaseScene import BaseScene, setup_button
from Utils.Character import Player
from Utils.Area import Area
from Utils.Slider import Slider_Bar
from Formulas.Formula import Symbol, Formula
from Formulas.FormulaSet import Set_of_formulas
from Formulas.FormulaGenerator import *
from Config.definitnios import ASSETS_DIR
from Utils.ResolutionButton import ResolutionButton
import pygame
from Utils.game_over import Game_over_window
from Utils.clock import Clock

class MapScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        '''A scene for map of the game, player will walk around and fight monsters'''

        background_img = pygame.image.load(ASSETS_DIR + "/emptyroom.png")
        background_img = pygame.transform.scale(background_img, (1300,730))
        self.add_background_image(background_img)
        
        # setting up a character and things they can interact with
        self.character = Player((550, 300), 150, "player/player.png")
        def go_to_scene(args):
            gameStateManager.set_state('level', {})
        self.area = Area((600,700),(100,100),None)
        self.area.on_enter_event = go_to_scene
        self.character.areas.append(self.area)

        self.add_ui_element(self.character)
        
    def on_entry(self, *args):
        '''TODO probalby here will be something to reset the score/formulas'''
        super().on_entry(*args)
        
