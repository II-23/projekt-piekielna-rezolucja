import pygame
from gamestatemanager import *
from Button import Button
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")

running = True
clock = pygame.time.Clock()

# creating scenes and scene manager
gameStateManager = GameStateManager('start')
start = Start(screen, gameStateManager)
level = BaseScene(screen, gameStateManager)

states = {'start':start, 'level':level}

# setting up buttons
def test(args):
    gameStateManager.set_state('level')

def test2(args):
    gameStateManager.set_state('start')

button = Button((100, 100), (200, 100), test, (0, 0, 0), (70, 70, 70), (200, 200, 200))
button2 = Button((100, 300), (200, 100), test2, (0, 0, 0), (70, 70, 70), (200, 200, 200))

start.add_button(button)
level.add_button(button2)

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    states[gameStateManager.get_state()].process_input(events, pygame.mouse)
    states[gameStateManager.get_state()].update(pygame.mouse)
    states[gameStateManager.get_state()].render(screen)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()