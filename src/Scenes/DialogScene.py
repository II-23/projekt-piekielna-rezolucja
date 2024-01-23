from Scenes.BaseScene import BaseScene, setup_button, Button
from Utils.Slider import Slider_Bar
from Config.graphics import RESOLUTION
from Config.definitnios import SRC_DIR
from Config.definitnios import ASSETS_DIR
from enum import Enum
from Utils.Image import Image
import pygame
import os

class Side(Enum):
    LEFT = -1
    RIGHT = 1
        
def split_dialog(text, left_name, right_name):
    '''Some sort of function that splits text into two parts for the dialog.
    Probably not the best way to do this but it works. Feel free to make it better if you are bored'''
    left_lines = []
    right_lines = []
    current_line = ""
    side = Side.LEFT
    text = text.splitlines()
    for line in text:
        line = line.strip()
        if line == left_name:
            side = Side.LEFT
            if current_line:
                right_lines.append(current_line)
                current_line = ""
        elif line == right_name:
            side = Side.RIGHT
            if current_line:
                left_lines.append(current_line)
                current_line = ""
        else:
            current_line += line + " "
    if current_line:
        if side == Side.RIGHT:
            right_lines.append(current_line)
        if side == Side.LEFT:
            left_lines.append(current_line)
    return left_lines, right_lines
        
    
class DialogManager():
    '''A dialog manager for all the dialogs in the game. Currently they are 100% cosmetic so there are no options to choose from, just 
        some text that adds a little bit of flavour to the game. Because of that all of the dialogs will be in this scene and when GameStateManager
        will switch to this scene it will set a current dialog to some option. That way we can add easily multiple dialogs to our game.'''
    def __init__(self, dialog_name) -> None:
        self.text = {}
        self.line = 0
        self.current_dialog = dialog_name

    def load_dialog(self, filename, dialog_name):
        path = os.path.join(SRC_DIR, "Scenes", filename)
        with open(path,'r',encoding='UTF-8') as file:
            dialog = file.read()
        text = split_dialog(dialog, 'Left:', 'Right:')
        dialog = []
        for i in range(max(len(text[0]), len(text[1]))):
            for j in range(2):
                  if i < len(text[j]):
                    dialog.append(text[j][i])
        self.text[dialog_name] = dialog
    
    def next_line(self):
        if self.line >= len(self.text[self.current_dialog]):
            self.reset_dialog()
        res = self.text[self.current_dialog][self.line]
        self.line += 1 
        return res
    
    def reset_dialog(self):
        self.line = 0
        
    def set_current_dialog(self, dialog_name):
        self.current_dialog = dialog_name
        
        
class DialogScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        '''Initalizing dialog manager'''
        self.DIALOG_NUMBER = 0
        self.talking_side = Side.LEFT # to remember which side is currently talking
        self.dialog_manager = DialogManager('test_dialog')
        intro_name = 'test_dialog'
        self.dialog_manager.load_dialog('dialog_intro.txt', intro_name)
        
        '''This is a "button" used for displaying the text of the dialog'''
        col = (31, 29, 28)
        tw_size = (750, 250)
        color_text_win=(150, 0, 0)
        color_on_click=(99, 90, 90)
        self.text_window = Button((RESOLUTION[0]/2-tw_size[0]/2 + 25, 460), tw_size, None, col, col, color_on_click)
        self.text_window.init_text(font=None, text_size=32, color=color_text_win, text=self.dialog_manager.next_line())

        bg_path = os.path.join(ASSETS_DIR, 'dialog_scene_bg.png')
        player1_path = os.path.join(ASSETS_DIR, 'player', 'player_dialog.png')
        player2_path = os.path.join(ASSETS_DIR, 'chad_jmi.png')
        bg=Image((0,0), (1280, 720), bg_path)
        player1=Image((300,200),(300,300), player1_path)
        player2=Image((700,50),(300,500), player2_path)

        self.add_ui_element(bg)
        self.add_ui_element(player1)
        self.add_ui_element(player2)

        def next_page_but(args):
            self.text_window.text_next_page()
        self.text_window.on_click_event = next_page_but
        self.add_ui_element(self.text_window)

        '''This is a button that skips to the next line of the dialog, displayed in the text_window'''
        self.next_dialog_line_button = Button((RESOLUTION[0]/2-tw_size[0]/2+750-125+25, 460-50), (125, 50), None, (61, 54, 50), (0,0,0), color_on_click)
        self.next_dialog_line_button.init_text(font=None, color=(color_text_win), text='Next', align_center_h=True, align_center_w=True)
        def next_line_dialog_but(args):
            '''function for next_dialog_line_button that sends a new line of dialog to be displayed to the text_window'''
            self.text_window.update_text(new_text=self.dialog_manager.next_line())
        self.next_dialog_line_button.on_click_event = next_line_dialog_but
        self.add_ui_element(self.next_dialog_line_button)
        
        '''This is a button that redirects to the GameplayScene'''
        #TODO better way to create buttons that go to the next scenes

        self.gp_scene_button = setup_button(gameStateManager, 'map', (1050, 610), sound_on_click="ReverbFart")
        self.gp_scene_button.init_text(font=None, color=(color_text_win), text='Play!', align_center_h=True, align_center_w=True)
        self.add_ui_element(self.gp_scene_button)
        
    def on_entry(self, *args, **kwargs):
        super().on_entry(*args)
        #print('entering dialog scene')
        #print(f'current dialog {args[0]["scene"]}')
        self.dialog_manager.set_current_dialog(args[0]["scene"])
        self.dialog_manager.reset_dialog()
        self.text_window.update_text(new_text=self.dialog_manager.next_line())
    