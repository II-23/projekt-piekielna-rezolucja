import pygame
from main_window import Main_Window
RESOLUTION = (1280, 720)
GRAY_COLOR = (65, 65, 67)

class Volume_slider:
    def __init__(self,pos:tuple,size:tuple,initaial_val,min_val,max_val):
        self.pos=pos
        self.size=size
        self.slider_left_pos=self.pos[0]-(size[0]//2)
        self.slider_right_pos=self.pos[0]+(size[0]//2)
        self.slider_top_pos=self.pos[0]
        self.min_val=min_val
        self.max_val=max_val
        self.initaial_val=(self.slider_right_pos-self.slider_left_pos)*initaial_val

        self.bar_rect=pygame.Rect(self.slider_left_pos,self.slider_top_pos,self.size[0],self.size[1])
        self.button_rect=pygame.Rect(self.slider_left_pos+self.initaial_val-3,self.slider_top_pos,15,self.size[1])

    def render(self,screen):
        pygame.draw.rect(screen,GRAY_COLOR,self.bar_rect)
        pygame.draw.rect(screen,"lightblue",self.button_rect)

# test runs
class tests:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.sliders=[Volume_slider((100,3),(100,10),0.5,0,100)]
    def run(self):
        for i in self.sliders:
            i.render(self.screen)

pygame.init()
screen=pygame.display.set_mode(RESOLUTION)
test=tests(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    test.run()  # 
    pygame.display.flip()  

pygame.quit()