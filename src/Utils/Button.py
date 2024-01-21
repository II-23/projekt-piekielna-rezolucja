# Author : Krzysztof Olejnik
from enum import Enum
import pygame
from soundtrackmanager import SoundtrackManager

class Status(Enum):
    IDLE = 0
    HOWER = 1
    CLICKED = 2,  

class Button():
    def __init__(self, position, size, on_click_event, idle_color, hower_color, click_color, **kwargs):
        self.position = position
        self.size = size
        self.idle_color = idle_color
        self.hower_color = hower_color
        self.click_color = click_color
        self.on_click_event = on_click_event
        self.status = Status.IDLE
        self.sound_on_click = None
        if ('sound_on_click' in kwargs):
            self.sound_on_click = kwargs['sound_on_click']
        # text variables
        self.text = None # This is the pygame text, kinda used like a flag to check if the button has any text
        self.text_str = None # This is the string format of the text
        self.text_printing_format = None # And this is formatted text (after using wrap_text) in form of a list 
        self.text_color = None
        self.font = None
        self.text_margin = 0.1 # How much free space is going to be around the text
        '''If the text is a little bit larger than the text window it gets split into pages in wrap_text().
        Page is the current page (index of the list with pages), and max_page is... the maximum page that can be accesed'''
        self.page = 0
        self.max_page = 0
        
    def init_text(self, font=None, text_size=32, color=(0, 255, 0), text='2137', align_center_w=False, align_center_h=False): 
        '''Initalizes text. It is exluded from init() so that we can still create buttons without text,
        if someone wants to.'''
        self.font = pygame.font.Font(font, text_size)
        self.align_center_w = align_center_w
        self.align_center_h = align_center_h
        self.update_text(text,color)
    
    def cursor_over_button(self, mouse, offset = (0,0)):
        mouse_pos = (mouse.get_pos()[0] + offset[0], mouse.get_pos()[1] + offset[1])
        return self.position[0] <= mouse_pos[0] <= self.position[0] + self.size[0] and \
        self.position[1] <= mouse_pos[1] <= self.position[1] + self.size[1]

    def render_text(self, screen):
        '''I'm not 100% positive that this is the correct way to display a text in pygame.
        Let me know if I should change something - Adam Dziwi'''
        if self.text is not None:
            if not self.align_center_h and not self.align_center_w:
                t_y = self.position[1]+self.size[1]*self.text_margin
                for line in self.text_printing_format[self.page]:
                    fw, fh = self.font.size(line)
                    text_line = self.font.render(line, True, self.text_color)
                    screen.blit(text_line, (self.position[0]+self.text_margin*self.size[0], t_y))
                    t_y += fh
            else:
                text_line = self.font.render(self.text_str, True, self.text_color)
                fw, fh = self.font.size(self.text_str)
                pos = [self.position[0]+self.text_margin*self.size[0],
                       self.position[1]+self.text_margin*self.size[1]]
                if self.align_center_w:
                    pos[0] = self.position[0] + self.size[0]/2 - fw/2
                if self.align_center_h:
                    pos[1] = self.position[1] + self.size[1]/2 - fh/2
                screen.blit(text_line, tuple(pos))

    def render(self, screen):
        color = self.idle_color
        if self.status == Status.HOWER:
            color = self.hower_color
        elif self.status == Status.CLICKED:
            color = self.click_color
        pygame.draw.rect(screen, color, pygame.Rect(*self.position, *self.size))
        self.render_text(screen)

    def process_input(self, events, mouse, *args):
        offset = (0, 0)
        if (len(args) >= 2):
            offset = (args[0], args[1])
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.cursor_over_button(mouse, offset):
                    self.status = Status.CLICKED
                else:
                    self.status = Status.IDLE

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.status == Status.CLICKED:
                    self.trigger_event(*args)
                    if (self.sound_on_click != None):
                        SoundtrackManager.playSound(self.sound_on_click)

                if self.cursor_over_button(mouse, offset):
                    self.status = Status.HOWER
                else:
                    self.status = Status.IDLE

    def update(self, mouse=pygame.mouse, offset = (0,0)):
        if self.status == Status.CLICKED:
            return
        if not self.cursor_over_button(mouse, offset):
            self.status = Status.IDLE
        else:
            self.status = Status.HOWER

    def trigger_event(self, *args):
        if self.on_click_event:
            self.on_click_event(*args)
        
    def update_text(self, new_text, color=None):
        self.text_str = new_text
        self.text_color = color if color else self.text_color
        self.text_printing_format = self.wrap_text(self.text_str)
        self.max_page = len(self.text_printing_format)-1
        self.page = 0
        self.text = self.font.render(self.text_str, True, self.text_color)
        
    def wrap_text(self, text_to_wrap):
        '''Method used to slice a long dialog into parts so each fits perfectly into the button.
        Text is split into smaller parts that are put into a list (self.text_printing_format). I was 
        inpired by some kind soul on StackOverflow with this beauty. '''
        words = text_to_wrap.split() # first we split text into words
        allowed_width = self.size[0]*(1-self.text_margin*2)
        allowed_height = self.size[1]*(1-self.text_margin*2)
        pages = []
        current_page = []
        fw, fh = self.font.size(' '.join('test'))
        current_text_height = 0
        while len(words) > 0: # then we go over the whole list of words
            new_line = []
            while len(words) > 0:
                new_line.append(words.pop(0)) # add a word to a new line
                fw, fh = self.font.size(' '.join(new_line + words[:1])) # calculate lenght of a line with the next word
                if fw > allowed_width: # if it's too long stop, we have a new line of text for our button!
                    break
            line = ' '.join(new_line)
            current_text_height += fh
            current_page.append(line) # we add our new line to a current page
            if current_text_height + fh > allowed_height: 
                '''if current page height plus height of one new line excedes our limit we 
                add current page to the "library" and create another new, empty one'''
                current_text_height = 0
                pages.append(current_page)
                current_page = []
        pages.append(current_page)
        return pages
    
    def text_next_page(self):
        self.page += 1
        if self.page > self.max_page:
            self.page = 0
            
