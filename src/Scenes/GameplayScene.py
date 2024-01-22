from Scenes.BaseScene import BaseScene, setup_button
from Utils.Slider import Slider_Bar
from Utils.ImageButton import ImageButton
from Formulas.Formula import Symbol, Formula
from Formulas.FormulaSet import Set_of_formulas
from Formulas.FormulaGenerator import *
from Config.definitnios import ASSETS_DIR
from Utils.ResolutionButton import ResolutionButton
from Utils.CharacterAnimation import CharacterAnimation
import pygame
from Utils.game_over import Game_over_window
from Utils.clock import Clock
from soundtrackmanager import SoundtrackManager
<<<<<<< HEAD
import os
=======
from Formulas.FormulaGenerator import DifficultyLevels
>>>>>>> 3cd6825 (Added some difficulty levels)

class GameplayScene(BaseScene):
    def __init__(self, display, gameStateManager, difficulty_level = DifficultyLevels.HARD, background_color=(255, 255, 255), enemy=0, player=0):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        '''Here you will learn how to add things to your scene. It's simple. Create the object and set its parameters so it fits your needs.
        Then add it to the scene using add_ui_element(). Make sure it has 3 required methods: render(), update(), process_input().
        '''
        self.enemy = enemy
        self.player = player
        self.won = [False]
        self.time_finished = None
        self.time_is_up = False
        paper_sheet = pygame.image.load(ASSETS_DIR + "/papersheet.jpg")
        paper_sheet = pygame.image.load(ASSETS_DIR + "/background_gameplay.png")
        #paper_sheet = pygame.transform.rotate(paper_sheet, 90)
        paper_height = paper_sheet.get_height()
        paper_sheet = pygame.transform.scale_by(paper_sheet, self.display.get_height()/paper_height)
        self.add_background_image(paper_sheet)
<<<<<<< HEAD
        print('generacja')
<<<<<<< HEAD
        abc = good_generate(difficulty_level)
=======

        abc = good_generate(2)
>>>>>>> main
=======
        abc = good_generate(DifficultyLevels.MEDIUM)
>>>>>>> 3cd6825 (Added some difficulty levels)
        #
        formulas=abc.formulas
        #
        max_variables_number = abc.get_variables_number()


        #self.formula_set=Set_of_formulas((500,500), (500,150), formulas)

        self.formula_set=Set_of_formulas((500,500), (200,125), formulas, self.won, max_variables_number)
        self.formula_set.subscribe(self, "WrongValuation")


        self.add_ui_element(self.formula_set)
        self.add_ui_element(self.formula_set.selected[0])
        self.add_ui_element(self.formula_set.selected[1])
        self.add_ui_element(self.formula_set.button)
        self.scorescreen=Game_over_window((500,500),(200,200),1, self.formula_set)
        self.add_ui_element(self.scorescreen)
        self.clock=Clock((200,200), (700,440), 60)
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
        
        def test2(args):
            gameStateManager.set_state("map", args)

        self.start_screen_button = setup_button(self.gameStateManager, "map", (100, 300))
        img = os.path.join(ASSETS_DIR, "back_to_menu.png")
        img_hover = os.path.join(ASSETS_DIR, "back_to_menu_hover.png")

        self.start_screen_button = ImageButton((0,0),(100,700),img, img_hover, test2)
        self.add_ui_element(self.start_screen_button)
        self.soundtrackmanager = SoundtrackManager

        # character animation :3
        self.anim = CharacterAnimation((580, 25), 80)
        self.add_ui_element(self.anim)

    def WrongValuationEvent(self): # DODANA PRZEZ KRZYCHA
        print("Zła waluacja")
        self.clock.substract_time(self.clock.time_total//10)
        
    def on_entry(self, *args, **kwargs):
        '''TODO probalby here will be something to reset the score/formulas'''
        super().on_entry(*args)
        self.soundtrackmanager.playMusic("GameplayMusic")
    
    def on_exit(self, *args, **kwargs):
        super().on_exit(*args)
        print(self.won[0])
        if self.won[0]:
            self.enemy.health -= 1
            self.player.points += 1000 + self.time_finished
        else:
            self.player.health -= 1 
        self.soundtrackmanager.stopMusic()

    def update(self, mouse=pygame.mouse):
        super().update(mouse)
        if self.won[0]:
            self.clock.stop_clock()
            self.time_finished = self.clock.time_left

        if self.clock.check_time_up() and not self.time_is_up:
            self.won[0] = False
            self.time_is_up = True
            self.start_screen_button.on_click_event({})

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