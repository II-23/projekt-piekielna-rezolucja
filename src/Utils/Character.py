#Aleksandra Ponikowska

import pygame
import numpy as np
from PIL import Image, ImageOps
import os
from Config.definitnios import ASSETS_DIR
from Utils.Area import Area
from Utils.Loot import LOOT_POINTS
from soundtrackmanager import SoundtrackManager

RESOLUTION = (1280, 720)
GRAY_COLOR = (65, 65, 67)
KEYS = {pygame.K_w : 'w', 
        pygame.K_s : 's',
        pygame.K_a : 'a',
        pygame.K_d : 'd',
        pygame.K_LSHIFT : 'shift',
        pygame.K_LCTRL : 'ctrl'}

def save_as(dict, image, path, name):
    new_path = os.path.join(os.path.dirname(path), name + ".png")
    image.save(new_path)
    dict[name] = new_path

class Player:
    def __init__(self, pos, size, sprite_path):
        self.pos = np.array(pos)
        self.starting_pos = pos
        self.pos_before_collision = pos
        self.size = size
        self.velocity = np.array([0,0])
        self.speed = 6
        self.state = "s"
        self.ded = False

        #STATYSTYKI
        self.health = 3
        self.points = 0
        self.on_death_event = None

        self.animation = False
        self.f = 1

        self.active = False # Determines whether character is going to interact with areas

        self.areas = []
        self.obstacles = []

        # left border
        self.obstacles.append(((0,0), (50, 200)))
        self.obstacles.append(((0,470), (50, 200)))

        # right border
        self.obstacles.append(((1230,0), (50, 200)))
        self.obstacles.append(((1230,470), (50, 200)))

        # top border
        self.obstacles.append(((0,0), (520, 30)))
        self.obstacles.append(((735,0), (2000, 30)))

        # bottom border
        self.obstacles.append(((0,670), (530, 30)))
        self.obstacles.append(((752,670), (2000, 30)))

        self.frames = {}
        self.pressed = {v : False for k, v in KEYS.items()}

        #nie wiem

        image_path = os.path.join(ASSETS_DIR, sprite_path)
        image = Image.open(image_path)
        image = image.resize((size*3, size))
        
        for i, x in enumerate(["s","w","a"]):
            im = image.crop((i*size,0,(i+1)*size,size))
            save_as(self.frames, im, image_path, x)

        # A
        im = ImageOps.mirror(im)
        save_as(self.frames, im, image_path, "d")

        for name in ["w","s","a","d"]:
            new_path = os.path.join(os.path.dirname(image_path), name + ".png")
            im = Image.open(new_path)

            im1 = im.rotate(5)
            save_as(self.frames, im1, image_path, name + "1")

            im2 = im.rotate(-5)
            save_as(self.frames, im2, image_path, name + "2")


    def pickup_loot(self):
        self.points += LOOT_POINTS
        SoundtrackManager.playSound("PickupSound")

    def render(self,screen):

        rect = pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)

        if self.animation:
            self.f += 0.1
            lizma = int(((self.f)%2)+1)
            image = pygame.image.load( self.frames[self.state + str(lizma)] )
        else:
            image = pygame.image.load( self.frames[self.state] )

        screen.blit(image, rect)

        if False:
            for pos, size in self.obstacles:
                rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
                pygame.draw.rect(screen,(100,100,100),rect)

            for x in self.areas:
                x.render(screen)
            
    def check_collision(self, pos1, size1, pos2, size2):
        x1, y1 = pos1
        w1, h1 = size1
        x2, y2 = pos2
        w2, h2 = size2
        
        if x1 < x2 + w2 and x1 + w1 > x2:
            if y1 < y2 + h2 and y1 + h1 > y2:
                return True
        return False

    def reset(self):
        self.pos = self.starting_pos
        self.velocity[0] = 0
        self.velocity[1] = 0
        self.active = False
        for k, v in self.pressed.items():
            self.pressed[k] = False

    def process_input(self, events, mouse, *args):
        if not self.ded:
            self.fake_process_input(events, mouse, args)

    def fake_process_input(self, events, mouse, *args):
        '''This is run only if the character is still alive'''
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in KEYS and KEYS[event.key] in self.pressed:
                    self.pressed[KEYS[event.key]] = True
            
            if event.type == pygame.KEYUP:
                if event.key in KEYS and KEYS[event.key] in self.pressed:
                    self.pressed[KEYS[event.key]] = False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_w:
            #         self.velocity[1] += -1
            #     elif event.key == pygame.K_s:
            #         self.velocity[1] += 1   
            #     elif event.key == pygame.K_a:
            #         self.velocity[0] += -1  
            #     elif event.key == pygame.K_d:
            #         self.velocity[0] += 1   
                    
            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_w:
            #         self.velocity[1] -= -1
            #     elif event.key == pygame.K_s:
            #         self.velocity[1] -= 1
            #     elif event.key == pygame.K_a:
            #         self.velocity[0] -= -1  
            #     elif event.key == pygame.K_d:
            #         self.velocity[0] -= 1 

        self.velocity = np.array([0,0])     
        multiplyer = 1
        if self.pressed['shift'] or self.pressed['ctrl']: multiplyer = 2
        if self.pressed['w']: self.velocity[1] += -1 * multiplyer
        if self.pressed['s']: self.velocity[1] += 1 * multiplyer
        if self.pressed['a']: self.velocity[0] += -1 * multiplyer
        if self.pressed['d']: self.velocity[0] += 1 * multiplyer

        if self.velocity[1] == -1 or self.velocity[1] == -2:
            self.state = "w"
        if self.velocity[1] == 1 or self.velocity[1] == 2:
            self.state = "s"
        if self.velocity[0] == -1 or self.velocity[0] == -2:
            self.state = "a"
        if self.velocity[0] == 1 or self.velocity[0] == 2:
            self.state = "d"

        if self.velocity[0] == 0 and self.velocity[1] == 0:
            self.animation = False
            self.state = "s"
        else:
            self.animation = True

        # Move X
        collision = False
        dummy_pos = (self.pos[0] + self.velocity[0] * self.speed, self.pos[1])

        for x in self.areas:
            if self.check_collision(dummy_pos, (self.size, self.size), x.pos, x.size):
                if self.active:
                    x.process_input(events,mouse, *args)
                    self.velocity[0] = 0
                    self.velocity[1] = 0
                    self.active = False
                collision = True

        for obstacle in self.obstacles:
            if isinstance(obstacle, tuple):
                pos2, size2 = obstacle
                if self.check_collision(dummy_pos, (self.size, self.size), pos2, size2):
                    collision = True
            elif isinstance(obstacle, Area):
                if self.check_collision(dummy_pos, (self.size, self.size), obstacle.pos, obstacle.size):
                    collision = True
                    
        if not collision:
            self.pos = list(self.pos)
            self.pos[0] += self.velocity[0] * self.speed
            self.pos = tuple(self.pos)

            #self.pos[0] += self.velocity[0] * self.speed

        # Move Y
        collision = False
        dummy_pos = (self.pos[0], self.pos[1] + self.velocity[1] * self.speed)

        for x in self.areas:
            if self.check_collision(dummy_pos, (self.size, self.size), x.pos, x.size):
                if self.active:
                    x.process_input(events,mouse, *args)
                    self.velocity[0] = 0
                    self.velocity[1] = 0
                    self.active = False
                collision = True

        for obstacle in self.obstacles:
            if isinstance(obstacle, tuple):
                pos2, size2 = obstacle
                if self.check_collision(dummy_pos, (self.size, self.size), pos2, size2):
                    collision = True
            elif isinstance(obstacle, Area):
                if self.check_collision(dummy_pos, (self.size, self.size), obstacle.pos, obstacle.size):
                    collision = True
            
        if not collision:
            self.pos = list(self.pos)
            self.pos[1] += self.velocity[1] * self.speed
            self.pos = tuple(self.pos)

            #self.pos[1] += self.velocity[1] * self.speed

        collision = False

        

        if not collision:
            self.active = True

        
    
    def update(self, mouse):
        pass


