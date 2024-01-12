# AD     
from Scenes.BaseScene import BaseScene, setup_button
from Utils.Slider import Slider_Bar
from Formulas.Formula import Symbol, Formula
from Formulas.FormulaSet import Set_of_formulas
from Formulas.FormulaGenerator import *
from Config.definitnios import ASSETS_DIR
import pygame
from Utils.game_over import Game_over_window
from Utils.clock import Clock

class GameplayScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager, background_color=background_color)
        '''Here you will learn how to add things to your scene. It's simple. Create the object and set its parameters so it fits your needs.
        Then add it to the scene using add_ui_element(). Make sure it has 3 required methods: render(), update(), process_input().
        '''
        paper_sheet = pygame.image.load(ASSETS_DIR + "/papersheet.jpg")
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
        
        #
        formula_generator = Generator(5, 6)   
        formula_generator.fill(5, 6)
        formulas=abc.formulas
        #

        formula_set=Set_of_formulas((500,500), (500,150), formulas)
        self.add_ui_element(formula_set)
        self.add_ui_element(formula_set.selected[0])
        self.add_ui_element(formula_set.selected[1])
        self.add_ui_element(formula_set.button)
        scorescreen=Game_over_window((500,500),(200,200),1, formula_set)
        self.add_ui_element(scorescreen)
        clock=Clock((100,100), (300,300), 60)
        self.add_ui_element(clock)
        #    
