from Scenes.BaseScene import BaseScene, setup_button, Button
from Utils.Slider import Slider_Bar
from Config.graphics import RESOLUTION
from enum import Enum
import pygame

class Side(Enum):
    LEFT = -1
    RIGHT = 1

#RESOLUTION = (1280, 720)

class Actor:
    '''This is a class for the npcs that talk during cutscenes'''
    def __init__(self):
        self.dialog = []
        self.active = False
        
def split_dialog(text):
    left_lines = []
    right_lines = []
    left = []
    right = []
    side = Side.LEFT
    text = text.splitlines()
    for line in text:
        line = line.strip()
        if line == 'Left:':
            side = Side.LEFT
            if right:
                right_lines.append(right)
                right = []
        elif line == 'Right:':
            side = Side.RIGHT
            if left:
                left_lines.append(left)
                left = []
        else:
            #print(f'appending {line} to {side}')
            if side == Side.RIGHT:
                right.append(line)
            if side == Side.LEFT:
                left.append(line)
    if left:
        left_lines.append(left)
    if right:
        right_lines.append(right)
                
    return left_lines, right_lines

class DialogManager():
    def __init__(self, left_npc, right_npc):
        self.left_actor = left_npc
        self.right_actor = right_npc
        self.side_talking = Side.LEFT
        self.left_dialog = self.left_actor.dialog.copy()
        self.right_dialog = self.right_actor.dialog.copy()

    def reset_dialog(self):
        self.side_talking = Side.LEFT
        self.left_dialog = self.left_actor.dialog.copy()
        self.right_dialog = self.right_actor.dialog.copy()

    def switch_actor_talking(self):
        self.side_talking = Side(self.side_talking.value*(-1))
        
    def say_line(self):
        if not self.right_dialog and not self.left_dialog:
            self.reset_dialog()
        text = self.left_dialog.pop(0) if self.side_talking == Side.LEFT and self.left_dialog else (self.right_dialog.pop(0) if self.right_dialog else '...')
        print(text)
        self.switch_actor_talking()
        
    
class DialogScene():
    def __init__(self) -> None:
        self.text = {}
        self.line = 1

    def load_dialog(self, filename, dialog_name):
        path = 'src/Scenes/'+filename
        with open(path,'r') as file:
            dialog = file.read()
        text = split_dialog(dialog)
        dialog = []
        for i in range(max(len(text[0]), len(text[1]))):
            for j in range(2):
                  if i < len(text[j]):
                    dialog.append(text[j][i])
        self.text[dialog_name] = dialog
        #print(dialog)
    
    def next_line(self, dialog_name):
        if self.line >= len(self.text[dialog_name]):
            self.line = 0
        res = self.text[dialog_name][self.line]
        print(res)
        self.line += 1 
        return res[0]

class GameplayIntroScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        
        self.talking_side = Side.LEFT # to remember which side is currently talking
        self.left_npc = Actor()
        self.right_npc = Actor()
        with open('src/Scenes/dialog_intro.txt','r') as file:
            dialog = file.read()
        self.left_npc.dialog, self.right_npc.dialog = split_dialog(dialog)
        self.dialog_manager = DialogManager(self.left_npc, self.right_npc)
        #self.dialog_manager.switch_actor_talking()
        self.test_scene = DialogScene()
        intro_name = 'test_dialog'
        self.test_scene.load_dialog('dialog_intro.txt', intro_name)
        
        col = (255, 135, 135)
        tw_size = (750, 250)
        self.text_window = Button((RESOLUTION[0]/2-tw_size[0]/2 + 25, 460), tw_size, None, col, col, (255,160,160))
        self.text_window.init_text(font=None, text_size=32, color=(42, 62, 115), text=self.test_scene.next_line(intro_name))
        def foo(args):
            self.text_window.text_next_page()
            self.dialog_manager.say_line()
            #print('next page!')
        self.text_window.on_click_event = foo
        self.add_ui_element(self.text_window)
        self.next_dialog_line_button = Button((RESOLUTION[0]/2-tw_size[0]/2+750-125+25, 460-50), (125, 50), None, (200, 150, 150), (255, 135, 135), (255,180,180))
        self.next_dialog_line_button.init_text(font=None, color=(255, 77, 131), text='Next')
        def bar(args):
            self.text_window.update_text(new_text=self.test_scene.next_line(intro_name))
        self.next_dialog_line_button.on_click_event = bar
        self.add_ui_element(self.next_dialog_line_button)
        
        self.gp_scene_button = setup_button(gameStateManager, 'level', (1050, 610))
        self.gp_scene_button.init_text(font=None, color=(255, 77, 131), text='Play!')
        self.add_ui_element(self.gp_scene_button)