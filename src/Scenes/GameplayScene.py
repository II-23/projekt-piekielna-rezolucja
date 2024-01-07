# AD     
from Scenes.BaseScene import BaseScene, setup_button
from Slider import Slider_Bar
from char import Symbol, Formula, Set_of_formulas
from generator import *
import pygame

class GameplayScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager, background_color=background_color)
        '''Here you will learn how to add things to your scene. It's simple. Create the object and set its parameters so it fits your needs.
        Then add it to the scene using add_ui_element(). Make sure it has 3 required methods: render(), update(), process_input().
        '''
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
        
        x=generate(max_variable_number, formulas_number, max_len, formula_choice_modifier)
        set=Set_of_formulas((500,500), (500,150), x)
        #for x in set.tab:
        #    self.add_ui_element(x)

        #
        #self.selected=[Formula((25,25), (500,100), [1,1,0], 500, False),Formula((25,25), (800,100), [1,0,2], 500, False)]
        #x=Formula((25,25), (100,100), [], 500)
        #self.add_ui_element(self.selected[0])
        #self.add_ui_element(self.selected[1])
        self.add_ui_element(set)
        self.add_ui_element(set.selected[0])
        self.add_ui_element(set.selected[1])
        self.add_ui_element(set.button)
        #    


        '''for x in set.tab:
            for y in x.tab:
                self.add_ui_element(y)'''
        