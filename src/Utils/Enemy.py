import pygame
from Utils.Area import Area
# import new button


class Enemy:
    def __init__(self, position, size, on_enter_event) -> None:
        self.active = False
        self.position = position
        self.size = size
        self.health = 1
        self.on_enter_event = on_enter_event
        # TODO loading image button here
        # self.size = image size            
        
    def process_input(self, events, mouse, *args):
        pass

    def update(self, mouse=pygame.mouse):
        pass

    def render(self, screen):
        if self.active:
            ...# rendering here
        pass