from Scenes.BaseScene import BaseScene, setup_button
from Slider import Slider_Bar
import pygame

class GameplayScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager, background_color=background_color)
        paper_sheet = pygame.image.load("./assets/papersheet.jpg")
        paper_sheet = pygame.transform.rotate(paper_sheet, 90)
        paper_height = paper_sheet.get_height()
        paper_sheet = pygame.transform.scale_by(paper_sheet, self.display.get_height()/paper_height)
        self.add_background_image(paper_sheet)
        # creating the slider_bar
        self.slider_bar = Slider_Bar((0.18 * self.width, self.height))
        self.slider_bar_rect = self.display.blit(self.slider_bar.get_surface(), (self.width - self.slider_bar.get_surface().get_width(), 0))
        self.slider_bar.set_parent_rect(self.slider_bar_rect)
        self.slider_bar.add_slider("p")
        self.slider_bar.add_slider("q")
        self.slider_bar.add_slider("r")
        self.slider_bar.add_slider("k")
        self.slider_bar.add_slider("s")
        self.slider_bar.add_slider("h")
        self.slider_bar.add_slider("u")
        self.slider_bar.add_slider("w")
        self.add_ui_element(self.slider_bar)
        # creating button to go to start scene
        self.start_screen_button = setup_button(self.gameStateManager, 'start', (100, 300))
        self.add_ui_element(self.start_screen_button)
        
    