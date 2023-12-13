# Author : Krzysztof Olejnik
from enum import Enum
import pygame

class Status(Enum):
    IDLE = 0
    HOWER = 1
    CLICKED = 2

class Button():
    def __init__(self, position, size, on_click_event, idle_color, hower_color, click_color):

        self.position = position
        self.size = size
        self.idle_color = idle_color
        self.hower_color = hower_color
        self.click_color = click_color
        self.on_click_event = on_click_event
        self.status = Status.IDLE

    def cursor_over_button(self, mouse):
        mouse_pos = mouse.get_pos()
        return self.position[0] <= mouse_pos[0] <= self.position[0] + self.size[0] and \
        self.position[1] <= mouse_pos[1] <= self.position[1] + self.size[1]

    def render(self, screen):
        color = self.idle_color
        if self.status == Status.HOWER:
            color = self.hower_color
        elif self.status == Status.CLICKED:
            color = self.click_color
        
        pygame.draw.rect(screen, color, pygame.Rect(*self.position, *self.size))

    def process_input(self, events, mouse, *args):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.cursor_over_button(mouse):
                    self.status = Status.CLICKED
                else:
                    self.status = Status.IDLE

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.status == Status.CLICKED:
                    self.trigger_event(*args)

                if self.cursor_over_button(mouse):
                    self.status = Status.HOWER
                else:
                    self.status = Status.IDLE

    def update(self, mouse=pygame.mouse):
        if self.status == Status.CLICKED:
            return
        if not self.cursor_over_button(mouse):
            self.status = Status.IDLE
        else:
            self.status = Status.HOWER

    def trigger_event(self, *args):
        self.on_click_event(*args)
