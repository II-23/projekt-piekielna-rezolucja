from Scenes.BaseScene import BaseScene, setup_button
from Utils.Slider import Slider_Bar
from Formulas.Formula import Symbol, Formula
from Formulas.FormulaSet import Set_of_formulas
from Formulas.FormulaGenerator import *
from Config.definitnios import ASSETS_DIR
from Utils.ResolutionButton import ResolutionButton
import pygame
from Utils.game_over import Game_over_window
from Utils.clock import Clock
from soundtrackmanager import SoundtrackManager

class GameplayScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255), enemy=0, player=0):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        '''Here you will learn how to add things to your scene. It's simple. Create the object and set its parameters so it fits your needs.
        Then add it to the scene using add_ui_element(). Make sure it has 3 required methods: render(), update(), process_input().
        '''
        self.enemy = enemy
        self.player = player
        self.won = [False]
        paper_sheet = pygame.image.load(ASSETS_DIR + "/papersheet.jpg")
        paper_sheet = pygame.transform.rotate(paper_sheet, 90)
        paper_height = paper_sheet.get_height()
        paper_sheet = pygame.transform.scale_by(paper_sheet, self.display.get_height()/paper_height)
        self.add_background_image(paper_sheet)
        print('generacja')
        abc = good_generate()
        #
        formula_generator = Generator(5, 6)   
        formula_generator.fill(5, 6)
        formulas=abc.formulas
        #


        self.formula_set=Set_of_formulas((500,500), (500,150), formulas, self.won)

        self.add_ui_element(self.formula_set)
        self.add_ui_element(self.formula_set.selected[0])
        self.add_ui_element(self.formula_set.selected[1])
        self.add_ui_element(self.formula_set.button)
        self.scorescreen=Game_over_window((500,500),(200,200),1, self.formula_set)
        self.add_ui_element(self.scorescreen)
        self.clock=Clock((100,100), (300,300), 60)
        self.add_ui_element(self.clock)
        #

        # creating the slider_bar
        indicies_of_variables = self.formula_set.get_variable_set()
        self.slider_bar = Slider_Bar((0.18 * self.width, self.height), indicies_of_variables)
        self.slider_bar_rect = self.display.blit(self.slider_bar.get_surface(), (self.width - self.slider_bar.get_surface().get_width(), 0))
        self.slider_bar.set_parent_rect(self.slider_bar_rect)
        self.add_ui_element(self.slider_bar)
        # creating button to go to start scene
        # def test2(args):
        #     gameStateManager.set_state('map', args)
        # button2 = Button(position, (200, 100), test2, (0, 0, 0), (70, 70, 70), (200, 200, 200), **kwargs)
        self.start_screen_button = setup_button(self.gameStateManager, 'map', (100, 300))
        self.add_ui_element(self.start_screen_button)
        self.soundtrackmanager = SoundtrackManager
        
    def on_entry(self, *args, **kwargs):
        '''TODO probalby here will be something to reset the score/formulas'''
        # #
        # formula_generator = Generator(5, 6)   
        # formula_generator.fill(5, 6)
        # formulas=abc.formulas
        # #
        # self.formula_set=Set_of_formulas((500,500), (500,150), formulas)
        # self.scorescreen=Game_over_window((500,500),(200,200),1, self.formula_set)
        # self.clock=Clock((100,100), (300,300), 60)
        
        super().on_entry(*args)
        self.soundtrackmanager.playMusic("GameplayMusic")
    
    def on_exit(self, *args, **kwargs):
        super().on_exit(*args)
        print(self.won[0])
        if self.won[0]:
            self.enemy.health -= 1
            self.player.points += 1000
        else:
            self.player.health -= 1 
        self.soundtrackmanager.stopMusic()

    def update(self, mouse=pygame.mouse):
        super().update(mouse)
        if (self.slider_bar.evalutation_requested):
            self.formula_set.evaluate(self.slider_bar.get_valuation())
            self.slider_bar.evalutation_requested = False

    def process_input(self, events, pressed_keys):
        super().process_input(events, pressed_keys)
        KEYS = {pygame.K_q: 'q'} 
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in KEYS:
                    self.won[0] = True # CHEATING