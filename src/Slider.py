import pygame
import numpy as np
from enum import Enum
from main_window import RESOLUTION

pygame.font.init()
pygame.display.init()

BAR_COLOR = (196, 196, 196)
SLIDER_SIZE = (236.16 * RESOLUTION[0]/1920.0, 70.2 * RESOLUTION[1]/1080.0)
SLIDER_COLOR_OFF = (70, 75, 80)
SLIDER_COLOR_OFF_HOVER = (100, 105, 110)
SLIDER_COLOR_ON = (200, 0, 0)
SLIDER_COLOR_ON_HOVER = (230, 0, 0)
TRUE_FALSE_COLOR = (255, 255, 255)

class Status(Enum):
    IDLE = 0
    HOWER = 1

class Slider_Bar(pygame.sprite.Sprite):
    def __init__(self, size):
        self.size = self.width, self.height = size
        loaded_bar = pygame.image.load("./assets/slider_bar.png").convert_alpha()
        self._surface = pygame.transform.scale(loaded_bar, size)
        #self.get_surface().fill(BAR_COLOR)
        self.sliders = []
        self.variable_dict = {}
        self.LEFT_MARGIN = SLIDER_SIZE[0]/10
        self.INTERLINE = SLIDER_SIZE[1]/4
        self.TOP_MARGIN = SLIDER_SIZE[1]/2
        self.SLIDER_OFFSET = SLIDER_SIZE[0]/3.2
        self.parent_rect = None
    def get_surface(self):
        return self._surface
    def set_parent_rect(self, parent_rect):
        self.parent_rect = parent_rect
    def add_slider(self, variable):
        new_slider = Slider(SLIDER_SIZE)
        slider_rect = self.get_surface().blit(new_slider.get_surface(), (self.LEFT_MARGIN + self.SLIDER_OFFSET, (SLIDER_SIZE[1] + self.INTERLINE) * len(self.sliders) + self.TOP_MARGIN))
        new_slider.set_parent_rect(slider_rect)
        self.variable_dict[variable] = len(self.sliders)
        self.sliders.append(new_slider)
    def update(self):
        for slider in self.sliders:
            slider.update()
    def render(self):
        i = 0
        for slider in self.sliders:
            slider.render()
            self.get_surface().blit(slider.get_surface(), (self.LEFT_MARGIN + self.SLIDER_OFFSET, (SLIDER_SIZE[1] + self.INTERLINE) * i + self.TOP_MARGIN))
            i += 1
    def process_input(self, events, mouse):
        for slider in self.sliders:
            slider.process_input(events, (mouse.get_pos()[0] - self.parent_rect[0], mouse.get_pos()[1] - self.parent_rect[1]))
    def update(self, mouse=pygame.mouse):
        rel_coord = (mouse.get_pos()[0] - self.parent_rect[0], mouse.get_pos()[1] - self.parent_rect[1])
        for slider in self.sliders:
            slider.update(rel_coord)


class Slider(pygame.sprite.Sprite):
    def __init__(self, size):
        self.size = self.width, self.height = size
        self._surface = pygame.Surface(size)
        self.state = False
        self.state_positions = [pygame.Rect(i * self.width, 0, 0.4 *self.width, self.height) for i in np.append(np.arange(0, 0.6, 0.1), np.array([0.61]))]
        self.true_position = pygame.Rect(0.2 * self.width, 0.1 * self.height, 0.4*self.width, self.height)
        self.false_position = pygame.Rect(0.6 * self.width, 0.1 * self.height, 0.4*self.width, self.height)
        self.prev_frame = 0
        self.current_frame = 0
        self.status = Status.IDLE
        self.parent_rect = None
        self.true_false_font = pygame.font.Font(None, round(1.3* self.height))
        self.true_sign = self.true_false_font.render("T", True, TRUE_FALSE_COLOR)
        self.false_sign = self.true_false_font.render("F", True, TRUE_FALSE_COLOR)
    def set_parent_rect(self, parent_rect):
        self.parent_rect = parent_rect
    def change_state(self):
        self.state = not self.state
    def get_surface(self):
        return self._surface
    def cursor_over_button(self, pos):
        x, y = (pos[0] - self.parent_rect[0], pos[1] - self.parent_rect[1])
        return 0 <= x < self.width and 0 <= y < self.height
    def process_input(self, events, pos):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.cursor_over_button(pos):
                    self.change_state()
    def update(self, pos):
        if (self.cursor_over_button(pos)):
            self.status = Status.HOWER
        else:
            self.status = Status.IDLE
        self.prev_frame = self.current_frame
        if (self.state and self.current_frame < len(self.state_positions) - 1):
            self.current_frame += 1
        elif (not self.state and self.current_frame > 0):
            self.current_frame -= 1
    def render(self):
        if (self.status == Status.IDLE):
            if not self.state:
                color = SLIDER_COLOR_OFF
            else:
                color = SLIDER_COLOR_ON
        else:
            if not self.state:
                color = SLIDER_COLOR_OFF_HOVER
            else:
                color = SLIDER_COLOR_ON_HOVER
        if (self.state):
            pygame.draw.rect(self.get_surface(), (0, 0, 0), self.false_position)
            self.get_surface().blit(self.true_sign, self.true_position)
        else:
            pygame.draw.rect(self.get_surface(), (0, 0, 0), self.true_position)
            self.get_surface().blit(self.false_sign, self.false_position)
        pygame.draw.rect(self.get_surface(), (0, 0, 0), self.state_positions[self.prev_frame])
        pygame.draw.rect(self.get_surface(), color, self.state_positions[self.current_frame])