import pygame
pygame.init()

class BaseScene:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def process_input(self, events, pressed_keys):
        pass
    def update(self):
        pass
    def render(self):
        self.display.fill('blue')

class Start(BaseScene):
    def __init__(self, display, gameStateManager):
        BaseScene.__init__(self,display=display,gameStateManager=gameStateManager)
    def render(self):
        self.display.fill('red')
        
class GameStateManager:
    def __init__(self, currentState):
        self.currentState=currentState
    def get_state(self):
        return self.currentState
    def set_stat(self, state):
        self.currentState=state

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")

running = True
clock = pygame.time.Clock()

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()