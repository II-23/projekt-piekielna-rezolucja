import pygame
from pygame.locals import *
import numpy
import math
from Slider import *

GRAY_COLOR = (65, 65, 67)
SLIDER_SIZE = (220, 70)

class Main_Window:
    def __init__(self, resolution):
        self.running = True
        self._display_surface = None
        self.size = self.width, self.height = resolution
        self.FramesPerSec = pygame.time.Clock()
        self.FPS = 60
        self.paper_sheet = pygame.image.load("./assets/papersheet.jpg")
        self.paper_sheet = pygame.transform.rotate(self.paper_sheet, 90)
        paper_height = self.paper_sheet.get_height()
        self.paper_sheet = pygame.transform.scale_by(self.paper_sheet, self.height/paper_height)
        self.slider_bar = Slider_Bar((0.2 * self.width, 0.65 * self.height))
        self.slider_bar.add_slider("dupa")
        self.slider_bar.add_slider("dupa")
        self.slider_bar.add_slider("dupa")
        self.slider_bar.add_slider("dupa")
    def on_init(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode(self.size)
        self._display_surface.fill(GRAY_COLOR)
        self._display_surface.blit(self.paper_sheet, (self.width * 0.5 - 0.5 * self.paper_sheet.get_width(), 0))
        self.slider_bar_rect = self._display_surface.blit(self.slider_bar.get_surface(), (self.width - self.slider_bar.get_surface().get_width(), 0))
        self.slider_bar.set_parent_rect(self.slider_bar_rect)
    def on_event(self, event):
        button_clicks = []
        match event.type:
            case pygame.QUIT:
                self.running = False
    def on_loop(self):
        self.slider_bar.update()
    def on_render(self):
        self.slider_bar.render()
        self._display_surface.blit(self.slider_bar.get_surface(), (self.width - self.slider_bar.get_surface().get_width(), 0))
        pygame.display.update()
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        self.on_init()
        while (self.running):
            events = pygame.event.get()
            for event in events:
                self.on_event(event)
            self.slider_bar.process_input(events, pygame.mouse)
            self.on_loop()
            self.on_render()
            self.FramesPerSec.tick(self.FPS)
        self.on_cleanup()

if __name__ == "__main__":
    app = Main_Window((1920, 1080))
    app.on_execute()