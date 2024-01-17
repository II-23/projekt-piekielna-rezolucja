import pygame
RESOLUTION = (1280, 720)
GRAY_COLOR = (65, 65, 67)

class Status:
    IDLE = 0
    HOVER = 1
    CLICKED = 2

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
        self.button_rect=pygame.Rect(self.slider_left_pos+self.initaial_val-6,self.slider_top_pos,10,self.size[1])
        self.status = Status.IDLE
    def move_slider(self, mouse_pos):
        new_x = max(self.slider_left_pos, min(mouse_pos[0], self.slider_right_pos))
        self.button_rect.centerx = new_x

    def cursor_over_button(self, mouse_pos):
        return self.button_rect.collidepoint(mouse_pos)

    def render(self,screen):
        pygame.draw.rect(screen,GRAY_COLOR,self.bar_rect)
        pygame.draw.rect(screen,"lightblue",self.button_rect)

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val = self.button_rect.centerx - self.slider_left_pos
        result_val = (button_val / val_range) * (self.max_val - self.min_val)
        return result_val

    def process_input(self, events, mouse_pos):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.cursor_over_button(mouse_pos):
                    self.status = Status.CLICKED

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.status == Status.CLICKED:
                    pass
                self.status = Status.IDLE

    def update(self, mouse_pos):
        if self.status == Status.CLICKED:
            self.move_slider(mouse_pos)
        elif self.cursor_over_button(mouse_pos):
            self.status = Status.HOVER
        else:
            self.status = Status.IDLE

# test runs
class tests:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.sliders=[Volume_slider((100,5),(100,10),0.5,0,100)]
    def run(self):
        mouse_pos=pygame.mouse.get_pos()
        mouse=pygame.mouse.get_pressed()
        for i in self.sliders:
            if i.bar_rect.collidepoint(mouse_pos) and mouse[0]:
                i.move_slider(mouse_pos)
            print(i.get_value())
            i.render(self.screen)

# pygame.init()
# screen=pygame.display.set_mode(RESOLUTION)
# test=tests(screen)
# running = True
# while running:
#     events = pygame.event.get()
#     mouse_pos = pygame.mouse.get_pos()

#     for event in events:
#         if event.type == pygame.QUIT:
#             running = False

#     # Clear the screen before drawing
#     screen.fill((0, 0, 0))

#     # Process input and update for each slider
#     test.sliders[0].process_input(events, mouse_pos)
#     test.sliders[0].update(mouse_pos)
#     test.run()

#     pygame.display.flip()

# pygame.quit()