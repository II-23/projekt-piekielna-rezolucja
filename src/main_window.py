import pygame
from pygame.locals import *
import numpy
import math

GRAY_COLOR = (65, 65, 67)

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
    def on_init(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode(self.size)
        self._display_surface.fill(GRAY_COLOR)
        self._display_surface.blit(self.paper_sheet, (self.width * 0.5 - 0.5 * self.paper_sheet.get_width(), 0))
    def on_event(self, event):
        match event.type:
            case pygame.QUIT:
                self.running = False
    def on_loop(self):
        pass
    def on_render(self):
        pygame.display.update()
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        self.on_init()
        while (self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.FramesPerSec.tick(self.FPS)
        self.on_cleanup()

if __name__ == "__main__":
    app = Main_Window((1920, 1080))
    app.on_execute()