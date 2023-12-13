import pygame
from gamestatemanager import *
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

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    states[gameStateManager.get_state()].render()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()