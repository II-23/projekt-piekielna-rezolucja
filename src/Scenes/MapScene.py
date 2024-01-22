from Scenes.BaseScene import BaseScene, setup_button
from Utils.Character import Player
from Utils.Area import Area
from Utils.ImageButton import ImageButton
from Formulas.FormulaGenerator import *
from Config.definitnios import ASSETS_DIR
from Scenes.GameplayScene import GameplayScene
from Utils.Health_and_points import Health_and_points
import pygame
from Utils.Enemy import Enemy
from Utils.Trapdoor import Trapdoor
from Utils.IsaacMapGenerator import MapGenerator
from random import randint, choice
import copy
import os

GRAY_COLOR = (65, 65, 67)

class Room():
    def __init__(self, pos: tuple, enemy_action) -> None:
        self.position_on_map = pos
        self.enemy_action = enemy_action
        p = 'closed_door.png'
        image_path = os.path.join(ASSETS_DIR, p)
        self.enemies_alive = 0
        # bottom (0), top (1), left (2), right (3)
        self.door_exists = [False, False, False, False]
        self.door_placeholder = self.door_exists.copy()
        self.door_empty_room = [False, False, False, False]
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
        # exit to the next room
        self.has_exit = False
        self.exit = None

    def add_enemy(self, position, size):
        self.entities.append(Enemy(position, size, self.enemy_action, image_dir='ghost.png', dead_dir='ghost_dead.png'))
        self.enemies_alive += 1

    def change_enemy_activity(self, active):
        for enemy in self.entities:
            enemy.active = active

class UwrManager:
    def __init__(self, enemy_action, difficulty, gameStateManager) -> None:
        '''This is map of the game, 1 means that there is a room, 0 that there is no room'''
        # setting up a character and things they can interact with
        self.gameStateManager = gameStateManager
        self.character = Player([550, 300]  , 150, "player/player.png")
        self.starting_positions = ((556, 570), (544, 18), (1132, 312), (-8, 300))
        self.enemy_action = enemy_action
        self.difficulty = difficulty
        self.pos_in_maze = [1, 0]
        self.mapa = []
        self.generate_room()

    def generate_room(self):
        self.generate_map(self.difficulty)
        self.game_map = copy.deepcopy(self.mapa) # map with numbers
        self.map_w = len(self.game_map[0])
        self.map_h = len(self.game_map)
        self.rooms = copy.deepcopy(self.mapa) # map with references to rooms
        # i = y, j = x
        for i in range(self.map_h):
            for j in range(self.map_w):
                if self.game_map[i][j] == 1:
                    room = Room((i, j), self.enemy_action)
                    # bottom (0), top (1), left (2), right (3)
                    room.door_exists[0] = False if i + 1 >= self.map_h else False if self.game_map[i + 1][j] == 0 else True 
                    room.door_exists[1] = False if i - 1 < 0 else False if self.game_map[i - 1][j] == 0  else True 
                    room.door_exists[2] = False if j - 1 < 0 else False if self.game_map[i][j - 1] == 0 else True   
                    room.door_exists[3] = False if j + 1 >= self.map_w else False if self.game_map[i][j + 1] == 0 else True 
                    room.door_placeholder = room.door_exists.copy()
                    self.rooms[i][j] = room

        self.enemiesNum = (self.difficulty+1)//2
        for _ in range(self.enemiesNum):
            chosenRoom = choice(MapGenerator.mapList)
            while chosenRoom == MapGenerator.start or chosenRoom == MapGenerator.end:
                chosenRoom = choice(MapGenerator.mapList)
            self.add_enemy_to_room(chosenRoom, (randint(200,980),randint(200,420)))
        self.add_enemy_to_room(MapGenerator.end, (270,310))
        if self.difficulty >= 3: self.add_enemy_to_room(MapGenerator.end, (910,310))

        def new_room():
            self.difficulty += 1
            self.gameStateManager.set_state('map', {})
            
        self.rooms[MapGenerator.end[0]][MapGenerator.end[1]].has_exit = True
        self.rooms[MapGenerator.end[0]][MapGenerator.end[1]].exit = Trapdoor((590, 310), (100, 100),
                                                                              new_room, 'trapdoor_open.png', 'trapdoor_closed.png')
        self.rooms[MapGenerator.end[0]][MapGenerator.end[1]].entities.append(self.rooms[MapGenerator.end[0]][MapGenerator.end[1]].exit)
        # these are starting coords for character when it goes to a new room
        # bottom (1), top (0), left (2), right (3)
        self.starting_positions = ((556, 570), (544, 18), (1132, 312), (-8, 300))
        # position of player in the labirynth
        self.current_room = self.rooms[self.pos_in_maze[0]][self.pos_in_maze[1]]


    def set_character_position(self, direction):
        return self.starting_positions[direction]
    
    def add_enemy_to_room(self, room_pos, enemy_pos):
        self.rooms[room_pos[0]][room_pos[1]].add_enemy(enemy_pos, (100,100))

    def move_on_map(self, direction):
        '''Used to move character to a new room'''
        new_pos = self.pos_in_maze.copy()
        if direction == 0:
            new_pos[0] -= 1
        if direction == 1:
            new_pos[0] += 1
        if direction == 2:
            new_pos[1] -= 1
        if direction == 3:
            new_pos[1] += 1

        if 0 <= new_pos[0] < self.map_h and 0 <= new_pos[1] < self.map_w: #checks if we didn't go outside of map
            if self.game_map[new_pos[0]][new_pos[1]] == 1 and self.current_room.enemies_alive <= 0:
                self.current_room.change_enemy_activity(False)
                self.pos_in_maze = new_pos
                self.current_room = self.rooms[self.pos_in_maze[0]][self.pos_in_maze[1]]
                self.current_room.change_enemy_activity(True)
                if self.current_room.enemies_alive > 0:
                    self.current_room.door_exists = self.current_room.door_empty_room.copy()
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
            if isinstance(entity, Enemy):
                if self.character.check_collision(self.character.pos, (self.character.size, self.character.size),
                                                entity.position, entity.size) and entity.active and entity.health > 0:
                    entity.on_enter_event({'e': entity, 'p': self.character}) # event of enemy

                # checking health of enemies
                if entity.health <= 0 and entity.alive: 
                    self.current_room.enemies_alive -= 1
                    entity.alive = False
            if isinstance(entity, Trapdoor):
                if self.character.check_collision(self.character.pos, (self.character.size, self.character.size),
                                                entity.position, entity.size) and entity.open and self.current_room.enemies_alive <= 0:
                    #coliision with trapdoor
                    entity.on_enter_event()
        if self.character.health <= 0:
            self.character.on_death_event({})
            
        if self.current_room.enemies_alive <= 0:
            self.current_room.door_exists = self.current_room.door_placeholder.copy()
            if self.current_room.has_exit:
                self.current_room.exit.open = True

    def render(self, screen):
        # render entities on a map (enemies)
        for entity in self.current_room.entities:
            if isinstance(entity, Enemy):
                entity.render(screen)
        # render trapdoor
        if self.current_room.has_exit:
            self.current_room.exit.render(screen)
        # render doors
        for i in range(4):
            if not self.current_room.door_exists[i]:
                self.current_room.doors[i].render(screen)

    def generate_map(self, difficulty):
        MapGenerator.generate(difficulty)
        self.mapa = copy.deepcopy(MapGenerator.mapArr)
        self.pos_in_maze = list(MapGenerator.start)
        print(self.mapa)
        

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
        self.uwu = UwrManager(go_to_scene, 5, gameStateManager)
        self.uwu.character.on_death_event = on_death
        self.uwu.current_room.change_enemy_activity(True) # set activity of current room to True
        if self.uwu.current_room.enemies_alive > 0:
            self.uwu.current_room.door_exists = self.uwu.current_room.door_empty_room.copy()
        
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
        self.doors.append(Area((1320, 300),(10,100),None))

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
        self.add_ui_element(self.uwu)
        self.add_ui_element(self.uwu.character)
        self.add_ui_element(Health_and_points(self.uwu.character,(230,40),(0,0),(133, 12, 36),(238, 0, 255),25))
        
    def on_entry(self, *args, prev_state):
        '''TODO probalby here will be something to reset player position'''
        self.uwu.character.reset()
        if prev_state == 'level':
            self.uwu.character.pos = self.uwu.character.pos_before_collision
        else:
            self.uwu.character.health = 1000
            self.uwu.character.pos = (550, 300)
            self.uwu.generate_room()
        super().on_entry(*args) 