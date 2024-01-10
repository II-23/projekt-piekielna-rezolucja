from Scenes.BaseScene import BaseScene, setup_button, Button
from Slider import Slider_Bar
import pygame

RESOLUTION = (1280, 720)

class GameplayIntroScene(BaseScene):
    def __init__(self, display, gameStateManager, background_color=(255, 255, 255)):
        BaseScene.__init__(self, display=display, gameStateManager=gameStateManager, background_color=background_color)
        
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
        
        def foo(args):
            print('clicky')
        col = (255, 135, 135)
        tw_size = (800, 250)
        self.text_window = Button((RESOLUTION[0]/2-tw_size[0]/2, 460), tw_size, foo, col, col, col)
        self.text_window.init_text(font=None, text_size=32, color=(42, 62, 115), text=intro_text)
        self.add_ui_element(self.text_window)