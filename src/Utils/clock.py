import pygame
import math
import os
from Config.definitnios import ASSETS_DIR


PI=math.pi
class Clock(pygame.sprite.Sprite):
    def __init__(self, size, pos, time):
        self.timer=clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.timer_interval = 100
        self.timer_event = pygame.USEREVENT
        pygame.time.set_timer(self.timer_event , self.timer_interval)
        self.time_total=time*1000
        self.time_left=time*1000
        self.pos = pos
        #self.surface=pygame.Surface((2000,2000))
        #self.rect=pygame.Rect(size[0],size[1],pos[0],pos[1])
        self.size=size[0]
        self.runnning = True
        
    def frame(self, name, size):
        sprite_path = f"clock/clock_{int(name)}.png"
        path = os.path.join(ASSETS_DIR, sprite_path)
        img = pygame.image.load( path )
        #print(path)
        img = pygame.transform.scale(img, (size, size))
        return img
    
    def framee(self, name, size):
        sprite_path = f"clock/clock_{int(name)}.png"
        path = os.path.join(ASSETS_DIR, sprite_path)
        img = pygame.image.load( path )
        #print(path)
        size *= 1.3
        img = pygame.transform.scale(img, (size * 1.7, size))
        return img

    def render(self, screen):
        """
        current_color=(int(self.time_left/self.time_total*255), int(self.time_left/self.time_total*255), int(self.time_left/self.time_total*255))
        self.get_surface().fill((0,0,0))
        for x in range(self.size):
            for y in range(self.size):
                if math.sqrt((x-self.size/2)**2+(y-self.size/2)**2)<=self.size/2:
                    if math.sqrt((x-self.size/2)**2+(y-self.size/2)**2)>=self.size/2*90/100:
                        self.get_surface().set_at((x+self.pos[0], y+self.pos[1]), (1,1,1))
                    else:
                        percentage=max(0, self.time_left/self.time_total*100)
                        color=(255*(1-percentage/100),255*percentage/100,0)
                        angle = math.atan2(y-self.size/2,x-self.size/2) + PI/2
                        if angle < 0 : angle += 2*PI
                        if 2*PI-angle <= 2*PI*percentage/100:
                            self.get_surface().set_at((x+self.pos[0], y+self.pos[1]), (color))
                        else:
                            self.get_surface().set_at((x+self.pos[0], y+self.pos[1]), (1,1,1))
                        # if percentage>75:
                        #     #if not -1*PI/2*(percentage-75)/100>math.atan2(y-self.size/2,x-self.size/2)>-1*PI/2:
                        #     if not -1*PI/2<math.atan2(y-self.size/2,x-self.size/2)<-1*PI/2*(percentage-75)/25:
                        #         self.get_surface().set_at((x, y), (color))
                        #     else:
                        #         self.get_surface().set_at((x, y), (1,1,1))
                        # elif percentage>25:
                        #     if not -1*PI/2<math.atan2(y-self.size/2,x-self.size/2)<PI*(percentage-75)/50*-1:
                        #         self.get_surface().set_at((x, y), (color))
                        #     else:
                        #         self.get_surface().set_at((x, y), (1,1,1))
                        # else:
                        #     if (not -1*PI/2<math.atan2(y-self.size/2,x-self.size/2)) and not math.atan2(y-self.size/2,x-self.size/2)<-1*PI/2-PI/2*percentage/25:
                        #         self.get_surface().set_at((x, y), (color))
                        #     else:
                        #         self.get_surface().set_at((x, y), (1,1,1))
                    else:
                        self.get_surface().set_at((x, y), (100,100,100))
        self.get_surface().set_colorkey((0, 0, 0))
        """

        rect = pygame.Rect(self.pos[0]-90, self.pos[1]-10, self.size, self.size)

        image = self.framee(-1, self.size)
        screen.blit(image, rect)

        rect = pygame.Rect(self.pos[0]+20, self.pos[1]+10, self.size, self.size)


        percentage= 100 - max(0, self.time_left/self.time_total*100)
        image = self.frame(percentage, self.size)

        

        screen.blit(image, rect)


        

        #screen.blit()

    def update(self, mouse=pygame.mouse):
        pass

    def process_input(self, events, mouse, *args):

        if self.runnning:
            for event in events:
                if event.type == self.timer_event:
                    self.time_left-=self.timer_interval
            self.time_left = max(0, self.time_left)
                    #print(self.time_left)
              
    def get_surface(self):
        return self.surface
    
    def get_rect(self):
        return self.rect
    
    def stop_clock(self):
        self.runnning = False
    
    def substract_time(self, value):
        self.time_left -= value

    def check_time_up(self):
        return self.time_left == 0