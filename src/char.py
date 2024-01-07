import pygame
class Symbol(pygame.sprite.Sprite):
    def __init__(self, size, num, pos):
        self.state=0
        self.width = size[0]
        self.height = size[1]
        self.x=pos[0]
        self.y=pos[1]
        match num:
            case 1:
                self.symbol = [pygame.image.load("./assets/one.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
            case 2:
                self.symbol = [pygame.image.load("./assets/2.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
            case 3:
                self.symbol = [pygame.image.load("./assets/three.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
            case 4:
                self.symbol = [pygame.image.load("./assets/4.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
            case 5:
                self.symbol = [pygame.image.load("./assets/five.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
            case 6:
                self.symbol = [pygame.image.load("./assets/6.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
            case 7:
                self.symbol = [pygame.image.load("./assets/seven.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
            case 8:
                self.symbol = [pygame.image.load("./assets/eight.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
            case 0:
                self.symbol = [pygame.image.load("./assets/alternate.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
            case -1:
                self.symbol = [pygame.image.load("./assets/minus-sign.png").convert_alpha(), pygame.image.load("./assets/minus-sign.png").convert_alpha()]
        
        self.surface = pygame.transform.scale(self.symbol[0], (self.width, self.height))
        self.symbol_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def render(self, screen):
        if self.state==0:
            self.surface = pygame.transform.scale(self.symbol[0], (self.width, self.height))
        if self.state==1:
            self.surface = pygame.transform.scale(self.symbol[1], (self.width, self.height))
        if self.state==2:
            self.surface = pygame.transform.scale(self.symbol[1], (self.width, self.height))
        
    def update(self, mouse_pos):
        pass
    def process_input(self, raz, dwa, trzy):
        pass
    def get_surface(self):
        return self.surface
    def get_rect(self):
        return self.symbol_rect
    

class Formula(pygame.sprite.Sprite):
    def __init__(self, size, pos, list, width, clickable):
        self.clickable=clickable
        self.state=0
        self.width=size[0]
        self.height=size[1]
        self.x=pos[0]
        self.y=pos[1]
        self.max_width=width
        self.tab=[]
        #
        #self.surface=pygame.Surface((200,200))
        
        loaded_bar = pygame.image.load("./assets/slider_bar.png").convert_alpha()
        self.surface=pygame.transform.scale(loaded_bar, (self.width*12, self.height)).convert_alpha()
        

        self.formula_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        #
        counter=0
        for i in range(len(list)):
            if list[i]==1:
                if len(self.tab)>0:
                    self.tab.append(Symbol((self.width, self.height), 0, (pos[0]+counter*self.width, pos[1])))
                    counter+=1
                self.tab.append(Symbol((self.width, self.height), i+1, (pos[0]+counter*self.width, pos[1])))
                counter=counter+1
            if list[i]==-1:
                if len(self.tab)>0:
                    self.tab.append(Symbol((self.width, self.height), 0, (pos[0]+counter*self.width, pos[1])))
                    counter+=1
                self.tab.append(Symbol((self.width, self.height), -1, (pos[0]+counter*self.width, pos[1])))
                counter=counter+1
                self.tab.append(Symbol((self.width, self.height), i+1, (pos[0]+counter*self.width, pos[1])))
                counter=counter+1
    def render(self, screen):
        self.get_surface().fill((0,0,0,0))
        i=0
        for symbol in self.tab:
            symbol.render(screen)
            self.get_surface().blit(symbol.get_surface(), (i*self.width,0))
            i+=1
    def cursor_over_formula(self, pos):
        return self.x<pos[0]<self.x+self.width*12 and self.y<pos[1]<self.y+self.height
    def update(self, mouse=pygame.mouse):
        mouse_pos = (mouse.get_pos()[0], mouse.get_pos()[1])
        if self.state==0 and self.cursor_over_formula(mouse_pos)==True and self.clickable:
            for element in self.tab:
                element.state=1
            self.state=1
        if self.state==1 and self.cursor_over_formula(mouse_pos)==False and self.clickable:
            for element in self.tab:
                element.state=0
            self.state=0
    def process_input(self, events, mouse, *args):
        pos=mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.cursor_over_formula(pos) and self.clickable:
                if self.state==1:
                    self.state=2
                else:
                    self.state=1
        pass
    def get_surface(self):
        return self.surface
    def get_rect(self):
        return self.formula_rect

class Set_of_formulas(pygame.sprite.Sprite):
    def __init__(self, size, pos, list):
        self.selected=[Formula((25,25), (500,100), [1,1,0], 500, False),Formula((25,25), (800,100), [1,0,2], 500, False)]
        self.selected_index=[1,1]
        self.width=size[0]
        self.height=size[1]
        self.x=pos[0]
        self.y=pos[1]
        self.tab=[]
        counter=0
        for i in range(len(list)):
           self.tab.append(Formula((25,25), (self.x, self.y+i*25), list[i][1], self.width, True))
    def render(self, screen):
        pass
    def update(self, mouse=pygame.mouse):
        if self.selected_index[0]!=-1:
            if self.tab[self.selected_index[0]].state!=3:
                self.selected_index[0]=-1
                self.selected[0].tab=[]
                
        if self.selected_index[1]!=-1:
            if self.tab[self.selected_index[1]].state!=4:
                self.selected_index[1]=-1
                self.selected[1].tab=[]
        for x in range(len(self.tab)):
            
            if self.tab[x].state==2:
                if self.selected_index[0]==-1:
                    self.tab[x].state=3
                    self.selected_index[0]=x
                    self.selected[0].tab=self.tab[x].tab
                elif self.selected_index[1]==-1:
                    self.tab[x].state=4
                    self.selected_index[1]=x
                    self.selected[1].tab=self.tab[x].tab
                else:
                     self.tab[x].state=1
            

    def process_input(self, events, mouse, *args):
        pass