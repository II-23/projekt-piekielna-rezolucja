# Aleksandra Ponikowska

import pygame

class Area():
    def __init__(self, pos, size, on_enter_event):
        self.pos = pos
        self.size = size
        self.on_enter_event = on_enter_event
        
    def render(self, screen):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        pygame.draw.rect(screen,(255,0,100), rect)

    def process_input(self, events, mouse, *args):
        self.trigger_event(*args)

    def update(self, mouse=pygame.mouse):
        pass

    def trigger_event(self, *args):
        self.on_enter_event(*args)
        