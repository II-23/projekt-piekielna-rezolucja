import pygame
from Utils.Button import Button
from Formulas.Formula import *
from Config.definitnios import ASSETS_DIR
from Formulas.Formula import Formula_State
from Utils.ResolutionButton import ResolutionButton
from Config.graphics import RESOLUTION
from soundtrackmanager import SoundtrackManager
from Config.definitnios import VARIABLES

LINE_HEIGHT = 32

class Set_of_formulas(pygame.sprite.Sprite):
    def __init__(self, size, pos, list_of_formulas, game_result, max_variable_number):
        #once we start fixing layout of stuff on the screen, line below needs to use variables passed from init.
        #for now it acts as placeholder
        #self.selected=[Formula((25,25), (500,100), [], 500, False),Formula((25,25), (800,100), [], 500, True)]
        self.selected=[Formula((25,25), (4000,0), [], 500, False),Formula((25,25), (4000,0), [], 500, True)]

        self.button = Button((500,120), (100,20), self.button_clicked, "red", "green", "blue")
        self.button = ResolutionButton((0.133* RESOLUTION[0],0), self.button_clicked)
        loaded_bar = pygame.image.load(ASSETS_DIR + "/slider_bar.png").convert_alpha()
        self.surface=pygame.transform.scale(loaded_bar, size).convert_alpha()
        self.set_rect = pygame.Rect(pos[0], pos[1], 500, 500)
        self.max_variable_number = max_variable_number

        self.selected_index=[1,1]
        self.width=size[0]
        self.height=size[1]
        self.x=pos[0]
        self.y=pos[1]
        self.formulas=[]
        self.state=0
        self.variables = set()
        #adding formulas given by the generator. Still uses generator prototype.
        for i in range(len(list_of_formulas)):
           self.formulas.append(Formula((25,25), (self.x, self.y+i*LINE_HEIGHT), list_of_formulas[i].variables, self.width, True))
        for formula in self.formulas:
            self.variables = self.variables.union(formula.get_variable_set())
        
        self.game_state = game_result
        self.subscribers = {} # GAMEPLAYSCENE ONLY

    def subscribe(self, obj, event):
        if not event in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(obj) # GAMEPLAYSCENE ONLY

    def WrongValuationEventTrigger(self):
        for obj in self.subscribers["WrongValuation"]:
            obj.WrongValuationEvent()

    def HappyEventTrigger(self):
        for obj in self.subscribers["Happy"]:
            obj.HappyEvent()

    def WritingEventTrigger(self):
        for obj in self.subscribers["Writing"]:
            obj.WritingEvent()
    
    def get_variable_set(self):
        return self.variables
    def button_clicked(self, *args):
        if self.state: return
        print('ads')
        #if player selected less than 2 formulas
        if self.selected[0].symbols==[] or self.selected[1].symbols==[]:
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
                    """ DODAĆ ANIMACJE PISANIA """
                    self.WritingEventTrigger()
                    SoundtrackManager.playSound("WritingEffect")
                    self.formulas.append(Formula((25,25), (self.x, self.y+len(self.formulas)*LINE_HEIGHT), q3, self.width, True))
                    self.clear_selected(0)
                    self.clear_selected(1)
                    for x in self.formulas:
                        x.state=Formula_State.HOVER
                else:
                    """ DODAĆ ANIMACJĘ RADOŚCI """
                    self.HappyEventTrigger()
                    print("znaleziono sprzeczność")
                    self.game_state[0] = True
                    SoundtrackManager.stopMusic()
                    SoundtrackManager.playSound("MarioLevelComplete")
                    self.state=1
    def render(self, screen):
        #fills with transparent and blits formulas
        self.get_surface().fill((0,0,0,0))
        for x in range(len(self.formulas)):
            self.formulas[x].render(screen)
            self.get_surface().blit(self.formulas[x].get_surface(), (0,LINE_HEIGHT*x))



    def update(self, mouse=pygame.mouse):
        self.selected[0].state=Formula_State.CLICKED_NOT_ASSIGNED
        self.selected[1].state=Formula_State.CLICKED_NOT_ASSIGNED
        #likely cause of bugs with formula state lol.
        #if formula that is indicated to be selected for a slot(selected index) has been unclicked, it clears selected_index and selected
        if self.selected_index[0]!=-1:
            if self.formulas[self.selected_index[0]].state!=Formula_State.CLICKED_SLOT_1:
                self.clear_selected(0)
        if self.selected_index[1]!=-1:
            if self.formulas[self.selected_index[1]].state!=Formula_State.CLICKED_SLOT_2:
                self.clear_selected(1)
        for x in range(len(self.formulas)):
            #if something is clicked, checks if either slot is empty. If so, it selects it for a slot. If no, it is unclicked
            if self.formulas[x].state==Formula_State.CLICKED_NOT_ASSIGNED:
                if self.selected_index[0]==-1:
                    self.formulas[x].state = Formula_State.CLICKED_SLOT_1
                    self.selected_index[0]=x
                    self.selected[0].symbols=self.formulas[x].symbols
                    self.selected[0].content=self.formulas[x].content
                elif self.selected_index[1]==-1:
                    self.formulas[x].state=Formula_State.CLICKED_SLOT_2
                    self.selected_index[1]=x
                    self.selected[1].symbols=self.formulas[x].symbols
                    self.selected[1].content=self.formulas[x].content
                else:
                     self.formulas[x].state=Formula_State.DEFAULT
        if (self.selected_index[0] != -1 and self.selected_index[1] != -1):
            self.button.make_flamed()
        else:
            self.button.make_not_flamed()
        for x in self.formulas:
            x.update(mouse)

    def process_input(self, events, mouse, *args):
        if self.state: return
        for x in self.formulas:
            x.process_input(events, mouse, *args)
        pass
    def get_surface(self):
        return self.surface
    def get_rect(self):
        return self.set_rect
    def clear_selected(self, num):
        self.selected_index[num]=-1
        self.selected[num].symbols=[]
        self.selected[num].content=[]
    def evaluate(self, valuation_dict):
        if self.state: return
        print(f'[Log][Formula set]: requested evaluation at {valuation_dict}')
        variable_names = sorted([VARIABLES[i] for i in range(self.max_variable_number)])
        valuation_katafiasz_normal_form = [0 if x not in valuation_dict else 1 if valuation_dict[x] else -1 for x in variable_names]
        global_satisfied = True
        for formula in self.formulas:
            formula_katafiasz_normal_form = formula.content
            satisfied = False
            for i in range(len(valuation_katafiasz_normal_form)):
                if (valuation_katafiasz_normal_form[i] != 0 and valuation_katafiasz_normal_form[i] == formula_katafiasz_normal_form[i]):
                    satisfied = True
                    break
            global_satisfied = global_satisfied and satisfied
        if (global_satisfied):
            """ DODAĆ ANIMACJĘ RADOŚCI """
            self.HappyEventTrigger()
            print(f"[Log][Formula set]: valuation is correct")
            self.game_state[0] = True
            print(self.game_state)
            SoundtrackManager.stopMusic()
            SoundtrackManager.playSound("MarioLevelComplete")
            self.state = 1
        else:
            self.WrongValuationEventTrigger()
            print(f"[Log][Formula set]: valuation is incorrect")