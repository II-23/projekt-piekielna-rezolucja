from Scenes.BaseScene import BaseScene, setup_button, Button
from Utils.Slider import Slider_Bar
from Config.graphics import RESOLUTION
from enum import Enum
import pygame

class Side(Enum):
    LEFT = -1
    RIGHT = 1

#RESOLUTION = (1280, 720)

# class Actor:
#     '''This is a class for the npcs that talk during cutscenes'''
#     def __init__(self):
#         self.dialog = []
#         self.active = False
        
def split_dialog(text, left_name, right_name):
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

# class DialogManager():
#     def __init__(self, left_npc, right_npc):
#         self.left_actor = left_npc
#         self.right_actor = right_npc
#         self.side_talking = Side.LEFT
#         self.left_dialog = self.left_actor.dialog.copy()
#         self.right_dialog = self.right_actor.dialog.copy()

#     def reset_dialog(self):
#         self.side_talking = Side.LEFT
#         self.left_dialog = self.left_actor.dialog.copy()
#         self.right_dialog = self.right_actor.dialog.copy()

#     def switch_actor_talking(self):
#         self.side_talking = Side(self.side_talking.value*(-1))
        
#     def say_line(self):
#         if not self.right_dialog and not self.left_dialog:
#             self.reset_dialog()
#         text = self.left_dialog.pop(0) if self.side_talking == Side.LEFT and self.left_dialog else (self.right_dialog.pop(0) if self.right_dialog else '...')
#         print(text)
#         self.switch_actor_talking()
        
    
class DialogManager():
    def __init__(self, dialog_name) -> None:
        self.text = {}
        self.line = 0
        self.current_dialog = dialog_name

    def load_dialog(self, filename, dialog_name):
        path = 'src/Scenes/'+filename
        with open(path,'r') as file:
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
        
        '''A dialog manager for all the dialogs in the game. Currently they are 100% cosmetic so there are no options to choose from, just 
        some text that adds a little bit of flavour to the game. Because of that all of the dialogs will be in this scene and when GameStateManager
        will switch to this scene it will set a current dialog to some option. That way we can add easily multiple dialogs to our game.'''
        self.DIALOG_NUMBER = 0
        self.talking_side = Side.LEFT # to remember which side is currently talking
        self.dialog_manager = DialogManager('test_dialog')
        intro_name = 'test_dialog'
        self.dialog_manager.load_dialog('dialog_intro.txt', intro_name)
        
        '''This is a "button" used for displaying the text of the dialog'''
        col = (255, 135, 135)
        tw_size = (750, 250)
        self.text_window = Button((RESOLUTION[0]/2-tw_size[0]/2 + 25, 460), tw_size, None, col, col, (255,160,160))
        self.text_window.init_text(font=None, text_size=32, color=(42, 62, 115), text=self.dialog_manager.next_line())
        def foo(args):
            self.text_window.text_next_page()
        self.text_window.on_click_event = foo
        self.add_ui_element(self.text_window)
        '''This is a button that skips to the next line of the dialog, displayed in the text_window'''
        self.next_dialog_line_button = Button((RESOLUTION[0]/2-tw_size[0]/2+750-125+25, 460-50), (125, 50), None, (200, 150, 150), (255, 135, 135), (255,180,180))
        self.next_dialog_line_button.init_text(font=None, color=(255, 77, 131), text='Next')
        def bar(args):
            '''function for next_dialog_line_button that sends a new line of dialog to be displayed to the text_window'''
            self.text_window.update_text(new_text=self.dialog_manager.next_line())
        self.next_dialog_line_button.on_click_event = bar
        self.add_ui_element(self.next_dialog_line_button)
        
        '''This is a button that redirects to the GameplayScene'''
        #TODO better way to create buttons that go to the next scenes
        self.gp_scene_button = setup_button(gameStateManager, 'level', (1050, 610))
        self.gp_scene_button.init_text(font=None, color=(255, 77, 131), text='Play!')
        self.add_ui_element(self.gp_scene_button)
        
    def on_entry(self, *args):
        print('entering dialog scene')
        print(f'current dialog {args[0]["scene"]}')
        self.dialog_manager.set_current_dialog(args[0]["scene"])
        self.dialog_manager.reset_dialog()
        self.text_window.update_text(new_text=self.dialog_manager.next_line())
    