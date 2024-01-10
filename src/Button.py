# Author : Krzysztof Olejnik
from enum import Enum
import pygame

class Status(Enum):
    IDLE = 0
    HOWER = 1
    CLICKED = 2,  

class Button():
    def __init__(self, position, size, on_click_event, idle_color, hower_color, click_color):
        self.position = position
        self.size = size
        self.idle_color = idle_color
        self.hower_color = hower_color
        self.click_color = click_color
        self.on_click_event = on_click_event
        self.status = Status.IDLE
        # text
        self.text = None
        self.text_str = None
        self.text_color = None
        self.font = None
        self.text_margin = 0.1
        self.text_printing_format = None
        
    def init_text(self, font=None, text_size=32, color=(0, 255, 0), text='2137'): 
        #print(f'doing the init:))')
        self.text_str = text
        self.text_color = color
        self.font = pygame.font.Font(font, text_size)
        self.text_printing_format = self.wrap_text(self.text_str)
        print(self.text_printing_format)
        #print(f'TYPE FONT: {self.font}')
        self.text = self.font.render(self.text_str, True, self.text_color)   
    
    def cursor_over_button(self, mouse):
        mouse_pos = mouse.get_pos()
        return self.position[0] <= mouse_pos[0] <= self.position[0] + self.size[0] and \
        self.position[1] <= mouse_pos[1] <= self.position[1] + self.size[1]

    def render(self, screen):
        color = self.idle_color
        if self.status == Status.HOWER:
            color = self.hower_color
        elif self.status == Status.CLICKED:
            color = self.click_color
        
        pygame.draw.rect(screen, color, pygame.Rect(*self.position, *self.size))
        if self.text is not None:
            #y_offset = 0
            t_y = self.position[1]+self.size[1]*self.text_margin
            for line in self.text_printing_format:
                fw, fh = self.font.size(line)
                text_line = self.font.render(line, True, self.text_color)
                screen.blit(text_line, (self.position[0]*(1+self.text_margin), t_y))
                t_y += fh 

    def process_input(self, events, mouse, *args):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.cursor_over_button(mouse):
                    self.status = Status.CLICKED
                else:
                    self.status = Status.IDLE

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.status == Status.CLICKED:
                    self.trigger_event(*args)

                if self.cursor_over_button(mouse):
                    self.status = Status.HOWER
                else:
                    self.status = Status.IDLE

    def update(self, mouse=pygame.mouse):
        if self.status == Status.CLICKED:
            return
        if not self.cursor_over_button(mouse):
            self.status = Status.IDLE
        else:
            self.status = Status.HOWER

    def trigger_event(self, *args):
        self.on_click_event(*args)
        
    def update_text(self, new_text, color=None):
        self.text_str = new_text
        self.text = self.font.render(new_text, True, color if color else self.text_color)
        
    def wrap_text(self, text_to_wrap):
        words = text_to_wrap.split()
        allowed_width = self.size[0]*(1-self.text_margin*2)
        lines = []
        while len(words) > 0:
            new_line = []
            while len(words) > 0:
                new_line.append(words.pop(0))
                print(f'TYPE FONT: {self.font}')
                fw, fh = self.font.size(' '.join(new_line + words[:1]))
                if fw > allowed_width:
                    break
            line = ' '.join(new_line)
            lines.append(line)
        return lines
            
