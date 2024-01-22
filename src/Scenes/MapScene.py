from Scenes.BaseScene import BaseScene, setup_button
from Utils.Character import Player
from Utils.Area import Area
from Utils.ImageButton import ImageButton
from Formulas.FormulaGenerator import *
from Config.definitnios import ASSETS_DIR
from Utils.ResolutionButton import ResolutionButton
from Scenes.GameplayScene import GameplayScene
import pygame
from Utils.game_over import Game_over_window
from Utils.clock import Clock
from Utils.Enemy import Enemy
import copy
import os

GRAY_COLOR = (65, 65, 67)

class Room():
    def __init__(self, pos: tuple, enemy_action) -> None:
        self.position_on_map = pos
        self.enemy_action = enemy_action
        p = 'closed_door.png'
        image_path = os.path.join(ASSETS_DIR, p)
        # bottom (0), top (1), left (2), right (3)
        self.door_exists = [False, False, False, False]
        self.doors = []
        # bottom door
        self.doors.append(ImageButton((564, 689), (715-560, 200), image_path, image_path, None))
        # top door 
        self.doors.append(ImageButton((545, -150), (700-543, 200), image_path, image_path, None))
        # left door
        self.doors.append(ImageButton((16-200, 190), (200, 472-190+4), image_path, image_path, None))
        # right door 
        self.doors.append(ImageButton((1252, 188), (200, 475-188+4), image_path, image_path, None))
        self.entities = []

    def add_enemy(self, position, size):
        self.entities.append(Enemy(position, size, self.enemy_action, 'ghost.png'))

    def change_enemy_activity(self, active):
        for enemy in self.entities:
            enemy.active = active

class UwrManager:
    def __init__(self, enemy_action) -> None:
        '''This is map of the game, 1 means that there is a room, 0 that there is no room'''
        # setting up a character and things they can interact with
        self.character = Player([550, 300]  , 150, "player/player.png")
        mapa = [[0, 1, 0],
                [0, 1, 1],
                [0, 1, 1]]
        self.game_map = copy.deepcopy(mapa) # map with numbers
        self.map_w = len(self.game_map[0])
        self.map_h = len(self.game_map)
        self.rooms = copy.deepcopy(mapa) # map with references to rooms
        # i = y, j = x
        for i in range(self.map_h):
            for j in range(self.map_w):
                if self.game_map[i][j] == 1:
                    room = Room((j, i), enemy_action)
                    # bottom (0), top (1), left (2), right (3)
                    room.door_exists[0] = False if i + 1 >= 3 else False if self.game_map[i + 1][j] == 0 else True 
                    room.door_exists[1] = False if i - 1 < 0 else False if self.game_map[i - 1][j] == 0  else True 
                    room.door_exists[2] = False if j - 1 < 0 else False if self.game_map[i][j - 1] == 0 else True 
                    room.door_exists[3] = False if j + 1 >= 3 else False if self.game_map[i][j + 1] == 0 else True 
                    self.rooms[i][j] = room

        # these are starting coords for character when it goes to a new room
        # bottom (1), top (0), left (2), right (3)
        self.starting_positions = ((556, 570), (544, 18), (1132, 312), (-8, 300))
        # position of player in the labirynth
        self.pos_in_maze = [1, 0]
        self.current_room = self.rooms[self.pos_in_maze[1]][self.pos_in_maze[0]]
        #self.current_room.add_enemy((200,200), (100,100))
        self.current_room.change_enemy_activity(True)

    def set_character_position(self, direction):
        return self.starting_positions[direction]
    
    def add_enemy_to_room(self, room_pos, enemy_pos):
        self.rooms[room_pos[1]][room_pos[0]].add_enemy(enemy_pos, (100,100))

    def move_on_map(self, direction):
        '''Used to move character to a new room'''
        new_pos = self.pos_in_maze.copy()
        if direction == 0:
            new_pos[1] -= 1
        if direction == 1:
            new_pos[1] += 1
        if direction == 2:
            new_pos[0] -= 1
        if direction == 3:
            new_pos[0] += 1

        if 0 <= new_pos[1] < self.map_h and 0 <= new_pos[0] < self.map_w: #checks if we didn't go outside of map
            if self.game_map[new_pos[1]][new_pos[0]] == 1:
                self.current_room.change_enemy_activity(False)
                self.pos_in_maze = new_pos
                self.current_room = self.rooms[self.pos_in_maze[1]][self.pos_in_maze[0]]
                self.current_room.change_enemy_activity(True)
                return True
            else:
                return False
        else:
            return False
        
    def process_input(self, events, mouse, *args):
        pass

    def update(self, mouse=pygame.mouse):
        # colissions
        #for entity in self.current_room.entities:
        for i in range(len(self.current_room.entities)):
            entity = self.current_room.entities[i]
            if self.character.check_collision(self.character.pos, (self.character.size, self.character.size),
                                              entity.position, entity.size) and entity.active:
                entity.on_enter_event({'e': entity, 'p': self.character}) # event of enemy

            # checking health of enemies
            if entity.health <= 0:
                self.current_room.entities.pop(i)

        if self.character.health <= 0:
            self.character.on_death_event({})

    def render(self, screen):
        # render entities on a map (enemies)
        for entity in self.current_room.entities:
            entity.render(screen)
        # render doors
        for i in range(4):
            if not self.current_room.door_exists[i]:
                self.current_room.doors[i].render(screen)

class MapScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        '''A scene for map of the game, player will walk around and fight monsters'''
        def go_to_scene(args): # function that goes to level scene
            gameStateManager.set_state('level', args)
            self.uwu.character.pos_before_collision = (self.uwu.character.pos[0]-self.uwu.character.velocity[0]*self.uwu.character.speed,
                                                       self.uwu.character.pos[1]-self.uwu.character.velocity[1]*self.uwu.character.speed)
            self.uwu.character.pos = self.uwu.character.pos_before_collision
            level = GameplayScene(self.display, self.gameStateManager, background_color=GRAY_COLOR, enemy=args['e'], player=args['p'])
            gameStateManager.states['level'] = level
            self.pause = True

        def on_death(args):
            gameStateManager.set_state('start', args)
        
        # a class to manage the map of the game
        self.uwu = UwrManager(go_to_scene)
        self.uwu.character.on_death_event = on_death
        #adding enemies to the map
        self.uwu.add_enemy_to_room((1, 1), (200, 200))
        self.uwu.add_enemy_to_room((1, 0), (500, 200))
        self.uwu.add_enemy_to_room((1, 2), (200, 400))
        self.uwu.current_room.change_enemy_activity(True) # set activity of current room to True
        
        background_img = pygame.image.load(ASSETS_DIR + "/emptyroom.png")
        background_img = pygame.transform.scale(background_img, (1300,730))
        self.add_background_image(background_img)
        
        '''These are areas for doors, used for checking if player touched them. They are unique and stored 
        in character class'''
        self.doors = [] # order of these must be the same as starting positions in UwrManager
        # top area
        self.doors.append(Area((600, -50),(100,5),None))
        # bottom area
        self.doors.append(Area((600, 770),(100,100),None))
        # left area
        self.doors.append(Area((-50, 360),(10, 100),None))
        # rigt area
        self.doors.append(Area((1320, 360),(10,100),None))

        def enter_room(args):
            if self.uwu.move_on_map(args['d']):
                self.uwu.character.pos = self.uwu.set_character_position(args['d'])
        
        self.area = Area((600,700),(100,100),None)
        self.area.on_enter_event = go_to_scene
        #self.character.areas.append(self.area)
        i = 0
        for door in self.doors:
            door.is_door = True
            door.destination = i
            door.on_enter_event = enter_room
            i += 1
            self.uwu.character.areas.append(door) 
            #door.size = (door.size[0]-5, door.size[1])
            self.uwu.character.obstacles.append(door)
        self.add_ui_element(self.uwu.character)
        self.add_ui_element(self.uwu)
        
    def on_entry(self, *args, prev_state):
        '''TODO probalby here will be something to reset player position'''
        self.uwu.character.reset()
        if prev_state == 'level':
            self.uwu.character.pos = self.uwu.character.pos_before_collision
        else:
            self.uwu.character.health = 1
            #TODO create impostors
            self.uwu.character.pos = (550, 300)
        super().on_entry(*args)#