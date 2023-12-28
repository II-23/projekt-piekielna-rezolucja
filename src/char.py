import pygame
class Symbol(pygame.sprite.Sprite):
    def __init__(self, size, num, pos):
        self.width = size[0]
        self.height = size[1]
        self.x=pos[0]
        self.y=pos[1]
        match num:
            case 1:
                symbol = pygame.image.load("./assets/one.png").convert_alpha()
            case 2:
                symbol = pygame.image.load("./assets/2.png").convert_alpha()
            case 3:
                symbol = pygame.image.load("./assets/three.png").convert_alpha()
            case 4:
                symbol = pygame.image.load("./assets/4.png").convert_alpha()
            case 5:
                symbol = pygame.image.load("./assets/five.png").convert_alpha()
            case 6:
                symbol = pygame.image.load("./assets/6.png").convert_alpha()
            case 7:
                symbol = pygame.image.load("./assets/seven.png").convert_alpha()
            case 8:
                symbol = pygame.image.load("./assets/eight.png").convert_alpha()
            case 0:
                symbol = pygame.image.load("./assets/alternate.png").convert_alpha()
            case -1:
                symbol = pygame.image.load("./assets/minus-sign.png").convert_alpha()
        
        self.surface = pygame.transform.scale(symbol, (self.width, self.height))
        self.symbol_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    #def draw_symbol(self):
        #self.surface.blit(symbol, self.symbol_rect)
        #print("dupa")
    def get_surface(self):
        return self.surface
    def get_rect(self):
        return self.symbol_rect

class Formula(pygame.sprite.Sprite):
    def __init__(self, size, pos, list, width):
        self.width=size[0]
        self.height=size[1]
        self.x=pos[0]
        self.y=pos[1]
        self.max_width=width
        self.tab=[]
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

class Set_of_formulas(pygame.sprite.Sprite):
    def __init__(self, size, pos, list):
        self.width=size[0]
        self.height=size[1]
        self.x=pos[0]
        self.y=pos[1]
        self.tab=[]
        counter=0
        for i in range(len(list)):
           self.tab.append(Formula((25,25), (self.x, self.y+i*25), list[i][1], self.width))