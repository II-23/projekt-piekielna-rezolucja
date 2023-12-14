import pygame
from enum import Enum

BAR_COLOR = (196, 196, 196)
SLIDER_SIZE = (220, 70)
SLIDER_COLOR_OFF = (70, 75, 80)
SLIDER_COLOR_OFF_HOVER = (100, 105, 110)
SLIDER_COLOR_ON = (200, 0, 0)
SLIDER_COLOR_ON_HOVER = (230, 0, 0)

class Status(Enum):
    IDLE = 0
    HOWER = 1

class Slider_Bar(pygame.sprite.Sprite):
    def __init__(self, size):
        self.size = self.width, self.height = size
        self._surface = pygame.Surface(size)
        self.get_surface().fill(BAR_COLOR)
        self.sliders = []
        self.LEFT_MARGIN = 0.1 * self.width
        self.INTERLINE = 0.05 * self.height
        self.TOP_MARGIN = 0.1 * self.height
        self.parent_rect = None
    def get_surface(self):
        return self._surface
    def set_parent_rect(self, parent_rect):
        self.parent_rect = parent_rect
    def add_slider(self, variable):
        new_slider = Slider((0.82 * self.width, 0.1 * self.height))
        slider_rect = self.get_surface().blit(new_slider.get_surface(), (self.LEFT_MARGIN, (SLIDER_SIZE[1] + self.INTERLINE) * len(self.sliders) + self.TOP_MARGIN))
        new_slider.set_parent_rect(slider_rect)
        self.sliders.append(new_slider)
    def update(self):
        for slider in self.sliders:
            slider.update()
    def render(self):
        i = 0
        for slider in self.sliders:
            slider.render()
            self.get_surface().blit(slider.get_surface(), (self.LEFT_MARGIN, (SLIDER_SIZE[1] + self.INTERLINE) * i + self.TOP_MARGIN))
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
        self.state_positions = [pygame.Rect(0, 0, 0.4 * self.width, self.height), pygame.Rect(0.6 * self.width, 0, 0.4 * self.width, self.height)]
        self.cur_pos = self.state_positions[0]
        self.status = Status.IDLE
        self.parent_rect = None
        pygame.draw.rect(self.get_surface(), (70, 75, 80), self.cur_pos)
    def set_parent_rect(self, parent_rect):
        self.parent_rect = parent_rect
    def change_state(self):
        self.state = not self.state
    def get_surface(self):
        return self._surface
    def cursor_over_button(self, pos):
        rel_coord = (pos[0] - self.parent_rect[0], pos[1] - self.parent_rect[1])
        if self.state:
            return self.state_positions[1].collidepoint(rel_coord)
        else:
            return self.state_positions[0].collidepoint(rel_coord)
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
            pygame.draw.rect(self.get_surface(), (0, 0, 0), self.state_positions[0])
            pygame.draw.rect(self.get_surface(), color, self.state_positions[1])
        else:
            pygame.draw.rect(self.get_surface(), (0, 0, 0), self.state_positions[1])
            pygame.draw.rect(self.get_surface(), color, self.state_positions[0])