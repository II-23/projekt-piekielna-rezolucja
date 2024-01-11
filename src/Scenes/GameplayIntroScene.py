from Scenes.BaseScene import BaseScene, setup_button, Button
from Slider import Slider_Bar
from enum import Enum
import pygame

class Side(Enum):
    LEFT = -1
    RIGHT = 1

RESOLUTION = (1280, 720)

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
        test = Side(1)
        #print(test)
        #print(f'side: {Side(-1)}')
        #print(f'side: {Side(1)}')
        
        #print(self.left_npc.dialog)
        #print(self.right_npc.dialog)
        intro_text = 'Jak to jest być skrybą, dobrze? \
        A, wie pan, moim zdaniem to nie ma tak, że dobrze, albo że niedobrze.\
        Gdybym miał powiedzieć, co cenię w życiu najbardziej, powiedziałbym, że ludzi.\
        Ludzi, którzy podali mi pomocną dłoń, kiedy sobie nie radziłem, kiedy byłem sam,\
        i co ciekawe, to właśnie przypadkowe spotkania wpływają na nasze życie.\
        Chodzi o to, że kiedy wyznaje się pewne wartości, nawet pozornie uniwersalne,\
        bywa, że nie znajduje się zrozumienia, które by tak rzec, które pomaga się nam rozwijać.\
        Ja miałem szczęście, by tak rzec, ponieważ je znalazłem, i dziękuję życiu!\
        Dziękuję mu; życie to śpiew, życie to taniec, życie to miłość!\
        Wielu ludzi pyta mnie o to samo: ale jak ty to robisz, skąd czerpiesz tę radość? A ja odpowiadam, że to proste!\
        To umiłowanie życia. To właśnie ono sprawia, że dzisiaj na przykład buduję maszyny, a jutro - kto wie? Dlaczego by nie - oddam się pracy społecznej i będę, ot, choćby, sadzić... doć— m-marchew... '
        
        col = (255, 135, 135)
        tw_size = (800, 250)
        self.text_window = Button((RESOLUTION[0]/2-tw_size[0]/2, 460), tw_size, None, col, col, (255,160,160))
        self.text_window.init_text(font=None, text_size=32, color=(42, 62, 115), text=intro_text)
        def foo(args):
            self.text_window.text_next_page()
            self.dialog_manager.say_line()
            #print('next page!')
        self.text_window.on_click_event = foo
        self.add_ui_element(self.text_window)
        
        self.gp_scene_button = setup_button(gameStateManager, 'level', (1050, 610))
        self.gp_scene_button.init_text(font=None, color=(255, 77, 131), text='Play!')
        self.add_ui_element(self.gp_scene_button)