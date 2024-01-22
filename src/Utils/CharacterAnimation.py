#Aleksandra Ponikowska

import pygame
from PIL import Image, ImageOps
import os
from Config.definitnios import ASSETS_DIR
from Utils.Area import Area

RESOLUTION = (1280, 720)
GRAY_COLOR = (65, 65, 67)

NEXT_FRAME = {"a1":"a2",
              "a2":"a1",
              "b1":"b2",
              "b2":"b1",
              "c1":"c2",
              "c2":"c1",
              "d1":"d2",
              "d2":"d1",
              "e1":"e2",
              "e2":"e3", 
              "e3":"e1", 
              "f":"f"}

def frame(name, size):
    sprite_path = f"player/animation/{name}.png"
    path = os.path.join(ASSETS_DIR, sprite_path)
    img = pygame.image.load( path )
    img = pygame.transform.scale(img, (size*5*1.1, size*5))
    return img

class CharacterAnimation:
    def __init__(self, pos, size):

        self.pos = pos
        self.size = size
        self.frame = "f"

        self.clock = 0
        self.it = 0

    def render(self,screen):

        rect = pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)
        image = frame(self.frame, self.size)
        (193, 181, 179)
        screen.blit(image, rect)
        pygame.draw.rect(screen, (193, 181, 179), (self.pos[0]+20, self.pos[1]+340, self.size*5, self.size*0.5))

    def process_input(self, events, mouse, *args):
        pass
        #for event in events:
        #    event
            # meow
    
    def update(self, mouse):
        self.clock += 1
        self.clock %= 10
        if self.clock == 0:
            if self.it:
                self.frame = NEXT_FRAME[self.frame]
                self.it -= 1
            else:
                self.frame = "f"
    
    def animate(name, it):
        self.frame = name
        self.it = it




