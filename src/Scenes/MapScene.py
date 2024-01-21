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
                         [0, 1, 0],
                         [0, 1, 1]]
        # these are starting coords for character when it goes to a new room
        # bottom (1), top (0), left (2), right (3)
        self.starting_positions = ((556, 570), (544, 18), (1132, 312), (-8, 300))
        # position of player in the labirynth
        self.pos_in_maze = [1, 1]

    def set_character_position(self, direction):
        return self.starting_positions[direction]
    
    def move_on_map(self, direction):
        new_pos = self.pos_in_maze
        if direction == 0:
            new_pos[1] -= 1
        if direction == 1:
            new_pos[1] += 1
        if direction == 2:
            new_pos[0] -= 1
        if direction == 3:
            new_pos[0] += 1



class MapScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        '''A scene for map of the game, player will walk around and fight monsters'''

        self.uwu = UwrManager()

        background_img = pygame.image.load(ASSETS_DIR + "/emptyroom.png")
        background_img = pygame.transform.scale(background_img, (1300,730))
        self.add_background_image(background_img)
        
        # setting up a character and things they can interact with
        self.character = Player((550, 300), 150, "player/player.png")

        self.doors = [] # order of these must be the same as starting positions in UwrManager
        # top area
        self.doors.append(Area((600, -50),(100,5),None))
        # bottom area
        self.doors.append(Area((600, 770),(100,100),None))
        # left area
        self.doors.append(Area((-50, 360),(5,100),None))
        # rigt area
        self.doors.append(Area((1320, 360),(5,100),None))

        def enter_room(args):
            print(args['d'])
            self.character.pos = self.uwu.set_character_position(args['d'])

        def go_to_scene(args):
            #gameStateManager.set_state('level', {})
            print('entered')
        self.area = Area((600,700),(100,100),None)
        self.area.on_enter_event = go_to_scene
        #self.character.areas.append(self.area)
        i = 0
        for door in self.doors:
            door.is_door = True
            door.destination = i
            door.on_enter_event = enter_room
            i += 1
            self.character.areas.append(door) 
        self.add_ui_element(self.character)
        
    def on_entry(self, *args):
        '''TODO probalby here will be something to reset the score/formulas'''
        super().on_entry(*args)
        
