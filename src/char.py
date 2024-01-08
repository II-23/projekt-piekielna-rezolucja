import pygame
from Button import Button
class Symbol(pygame.sprite.Sprite):
    def __init__(self, size, num, pos):
        self.state=0
        self.width = size[0]
        self.height = size[1]
        self.x=pos[0]
        self.y=pos[1]
        #assigning image to symbol according to num value. 0 is alternate, -1 is negate. 2nd row is a placeholder for colored icons(hovered)
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
        #ugly way of making a surface. Initializing one in a proper manner was dificult. This is probably fine since image
        #gets cleared immediately but might be worth fixing
        loaded_bar = pygame.image.load("./assets/slider_bar.png").convert_alpha()
        self.surface=pygame.transform.scale(loaded_bar, (self.width*12, self.height)).convert_alpha()
        
        self.content=list
        self.formula_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #reading off list. Each position in list indicates if such element is part of formula. 0 means no variable, 1 means 
        #variable, -1 means negated variable. Code appends alternate symbols aswell
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
        #fill with transparent and blit all of the symbols stored in "tab"
        self.get_surface().fill((0,0,0,0))
        i=0
        for symbol in self.tab:
            symbol.render(screen)
            self.get_surface().blit(symbol.get_surface(), (i*self.width,0))
            i+=1
    def cursor_over_formula(self, pos):
        return self.x<pos[0]<self.x+self.width*12 and self.y<pos[1]<self.y+self.height
    def update(self, mouse=pygame.mouse):
        #This was meant to keep track if formula is hovered. State variable means:
        #0: default 1:hovered 2:clicked(not yet assigned slot) 3:clicked(assigned slot 1) 4:clicked(assigned slot 2)
        #used to cause bug where formulas hovered and clicked would act like not hovered, not clicked.
        #bugs sometimes. Plz review, i have no idea what goes wrong.
        mouse_pos = (mouse.get_pos()[0], mouse.get_pos()[1])
        if self.state==1 and self.cursor_over_formula(mouse_pos)==False and self.clickable:
            for element in self.tab:
                element.state=0
            self.state=0

        if self.state==0 and self.cursor_over_formula(mouse_pos)==True and self.clickable:
            for element in self.tab:
                element.state=1
            self.state=1
        
    def process_input(self, events, mouse, *args):
        #if formula is clicked it checks if it is hovered. If so, it is now clicked. if not, it is now hovered.
        pos=mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.cursor_over_formula(pos) and self.clickable:
                if self.state==1:
                    self.state=2
                else:
                    self.state=1
    def get_surface(self):
        return self.surface
    def get_rect(self):
        return self.formula_rect

class Set_of_formulas(pygame.sprite.Sprite):
    def __init__(self, size, pos, list):
        #once we start fixing layout of stuff on the screen, line below needs to use variables passed from init.
        #for now it acts as placeholder
        self.selected=[Formula((25,25), (500,100), [], 500, False),Formula((25,25), (800,100), [], 500, True)]
        self.button=Button((500,120), (100,20), self.button_clicked, "red", "green", "blue")
        loaded_bar = pygame.image.load("./assets/slider_bar.png").convert_alpha()
        self.surface=pygame.transform.scale(loaded_bar, size).convert_alpha()
        self.set_rect = pygame.Rect(pos[0], pos[1], 500, 500)
        self.selected_index=[1,1]
        self.width=size[0]
        self.height=size[1]
        self.x=pos[0]
        self.y=pos[1]
        self.tab=[]
        #adding formulas given by the generator. Still uses generator prototype.
        for i in range(len(list)):
           self.tab.append(Formula((25,25), (self.x, self.y+i*25), list[i].variables, self.width, True))
    def button_clicked(self, *args):
        #if player selected less than 2 formulas
        if self.selected[0].tab==[] or self.selected[1].tab==[]:
            print("głupota")
        else:
            q1=self.selected[0].content.copy()
            q2=self.selected[1].content.copy()
            q3=[]
            x=len(q1)
            check=-1
            tautology_safeguard=0
            for i in range(x):
                if (q1[i]==1 and q2[i]==-1) or (q1[i]==-1 and q2[i]==1):
                    if check==-1:
                        check=i
                    else:
                        #this triggers if there are two variables that could be resolved by. My code currently doesnt have a way
                        #to store + and - on the same var, it could be 2 in the future if we decide to let the user do it anyway
                        print("głupota")
                        tautology_safeguard=1

            if check==-1:
                #if there is no variable to resolve by
                print("głupota")
            elif tautology_safeguard==0:
                #proceeds to make a new list according to rules.
                for i in range(x):
                    if i==check:
                        q3.append(0)
                    elif q1[i]==0 and q2[i]==0:
                        q3.append(0)
                    elif q1[i]==1 or q2[i]==1:
                        q3.append(1)
                    elif q1[i]==-1 or q2[i]==-1:
                        q3.append(-1)
                #goes through list checking if it isnt empty. if it is, we found proof
                check=0
                for x in q3:
                    if x!=0:
                        check=1
                if check==1:
                    self.tab.append(Formula((25,25), (self.x, self.y+len(self.tab)*25), q3, self.width, True))
                    self.clear_selected(0)
                    self.clear_selected(1)
                    for x in self.tab:
                        x.state=1
                else:
                    print("znaleziono sprzeczność")
    def render(self, screen):
        #fills with transparent and blits formulas
        self.get_surface().fill((0,0,0,0))
        for x in range(len(self.tab)):
            self.tab[x].render(screen)
            self.get_surface().blit(self.tab[x].get_surface(), (0,25*x))

    def update(self, mouse=pygame.mouse):
        #likely cause of bugs with formula state lol.
        #if formula that is indicated to be selected for a slot(selected index) has been unclicked, it clears selected_index and selected
        if self.selected_index[0]!=-1:
            if self.tab[self.selected_index[0]].state!=3:
                self.clear_selected(0)
        if self.selected_index[1]!=-1:
            if self.tab[self.selected_index[1]].state!=4:
                self.clear_selected(1)
        for x in range(len(self.tab)):
            #if something is clicked, checks if either slot is empty. If so, it selects it for a slot. If no, it is unclicked
            if self.tab[x].state==2:
                if self.selected_index[0]==-1:
                    self.tab[x].state=3
                    self.selected_index[0]=x
                    self.selected[0].tab=self.tab[x].tab
                    self.selected[0].content=self.tab[x].content
                elif self.selected_index[1]==-1:
                    self.tab[x].state=4
                    self.selected_index[1]=x
                    self.selected[1].tab=self.tab[x].tab
                    self.selected[1].content=self.tab[x].content
                else:
                     self.tab[x].state=0
        for x in self.tab:
            x.update(mouse)

    def process_input(self, events, mouse, *args):
        for x in self.tab:
            x.process_input(events, mouse, *args)
        pass
    def get_surface(self):
        return self.surface
    def get_rect(self):
        return self.set_rect
    def clear_selected(self, num):
        self.selected_index[num]=-1
        self.selected[num].tab=[]
        self.selected[num].content=[]