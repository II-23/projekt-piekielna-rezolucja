import pygame
from Utility.Button import Button
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")

running = True
clock = pygame.time.Clock()

def test(args):
    print(69)

def test2(args):
    print(args)

button = Button((100, 100), (200, 100), test, (0, 0, 0), (70, 70, 70), (200, 200, 200))
button2 = Button((100, 300), (200, 100), test2, (0, 0, 0), (70, 70, 70), (200, 200, 200))

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    button.process_input(events, pygame.mouse, 0)
    button.update(pygame.mouse)
    button.render(screen)   

    button2.process_input(events, pygame.mouse, pygame.mouse.get_pos())
    button2.update(pygame.mouse)
    button2.render(screen)   

    pygame.display.flip()

    clock.tick(60)

pygame.quit()