#Aleksandra Ponikowska

import pygame
import numpy as np
import os
from Config.definitnios import ASSETS_DIR

RESOLUTION = (1280, 720)
GRAY_COLOR = (65, 65, 67)

class Player:
    def __init__(self, pos:tuple, size):
        self.pos = np.array(pos)
        self.size = size
        self.velocity = np.array([0,0])
        self.speed = 6
        self.obstacles = []
        self.obstacles.append(((100,100), (100, 100)))

    def render(self,screen):

        rect= pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)
        image_path = os.path.join(ASSETS_DIR, "player/idle.png")
        image = pygame.image.load(image_path)

        screen.blit(image, rect)

        for pos, size in self.obstacles:
            rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
            pygame.draw.rect(screen,(100,100,100),rect)
            
    def check_collision(self, pos1, size1, pos2, size2):
        x1, y1 = pos1
        w1, h1 = size1
        x2, y2 = pos2
        w2, h2 = size2
        
        if x1 < x2 + w2 and x1 + w1 > x2:
            if y1 < y2 + h2 and y1 + h1 > y2:
                return True
        return False


    def process_input(self, events,mouse, *args):

        for event in events:
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.velocity[1] += -1  
                elif event.key == pygame.K_s:
                    self.velocity[1] += 1   
                elif event.key == pygame.K_a:
                    self.velocity[0] += -1  
                elif event.key == pygame.K_d:
                    self.velocity[0] += 1   

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.velocity[1] -= -1  
                elif event.key == pygame.K_s:
                    self.velocity[1] -= 1   
                elif event.key == pygame.K_a:
                    self.velocity[0] -= -1  
                elif event.key == pygame.K_d:
                    self.velocity[0] -= 1  

        collision = False
        dummy_pos = self.pos + self.velocity * self.speed

        for pos2, size2 in self.obstacles:
            if self.check_collision(dummy_pos, (self.size, self.size), pos2, size2):
                collision = True
        #print(self.velocity)
        if not collision:
            self.pos += self.velocity * self.speed
    
    def update(self, mouse):
        pass


