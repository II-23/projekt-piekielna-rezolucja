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

class UwrManager:
    def __init__(self) -> None:
        '''This is map of the game, 1 means that there is a room, 0 that there is no room'''
        self.game_map = [[1, 1, 1],
                         [0, 1, 0]
                         [1, 1, 1]]
        # these are starting coords for character when it goes to a new room
        # upper, lower, left, right
        self.starting_positions = ((560, 500), (544, 102), (76, 300), (1060, 288))
        # position of player in the labirynth
        self.pos_in_maze = [1, 1]


class MapScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        '''A scene for map of the game, player will walk around and fight monsters'''

        background_img = pygame.image.load(ASSETS_DIR + "/emptyroom.png")
        background_img = pygame.transform.scale(background_img, (1300,730))
        self.add_background_image(background_img)
        
        # setting up a character and things they can interact with
        self.character = Player((550, 300), 150, "player/player.png")

        self.doors = []
        # top area
        self.doors.append(Area((600, 0),(100,5),None))
        # bottom area
        self.doors.append(Area((600,700),(100,100),None))
        # left area
        self.doors.append(Area((0, 360),(5,100),None))
        # rigt area
        self.doors.append(Area((1278, 360),(5,100),None))

        def go_to_scene(args):
            #gameStateManager.set_state('level', {})
            print('entered')
        self.area = Area((600,700),(100,100),None)
        self.area.on_enter_event = go_to_scene
        self.character.areas.append(self.area)
        for door in self.doors:
            door.on_enter_event = go_to_scene
            self.character.areas.append(door) 
        self.add_ui_element(self.character)
        
    def on_entry(self, *args):
        '''TODO probalby here will be something to reset the score/formulas'''
        super().on_entry(*args)
        
