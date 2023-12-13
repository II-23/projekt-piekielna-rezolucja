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

gameStateManager = GameStateManager('start')
start = Start(screen, gameStateManager)
level = BaseScene(screen, gameStateManager)

states = {'start':start, 'level':level}

def test(args):
    gameStateManager.set_state('level')

def test2(args):
    gameStateManager.set_state('start')

button = Button((100, 100), (200, 100), test, (0, 0, 0), (70, 70, 70), (200, 200, 200))
button2 = Button((100, 300), (200, 100), test2, (0, 0, 0), (70, 70, 70), (200, 200, 200))

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    states[gameStateManager.get_state()].render()

    button.process_input(events, pygame.mouse)
    button.update(pygame.mouse)
    button.render(screen)   

    button2.process_input(events, pygame.mouse, pygame.mouse.get_pos())
    button2.update(pygame.mouse)
    button2.render(screen)   
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()