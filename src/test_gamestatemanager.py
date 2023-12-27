import pygame
from gamestatemanager import *
from Button import Button
from BaseScene import *
pygame.init()

GRAY_COLOR = (65, 65, 67)

# Set up display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")
paper_sheet = pygame.image.load("./assets/papersheet.jpg")
paper_sheet = pygame.transform.rotate(paper_sheet, 90)
paper_height = paper_sheet.get_height()
paper_sheet = pygame.transform.scale_by(paper_sheet, height/paper_height)

piwo_img = pygame.image.load("./assets/piwo.png")

screen.fill(GRAY_COLOR)
screen.blit(paper_sheet, (width * 0.5 - 0.5 * paper_sheet.get_width(), 0))

running = True
clock = pygame.time.Clock()

# creating scenes and scene manager
gameStateManager = GameStateManager('start')
start = Start(screen, gameStateManager, background_color=GRAY_COLOR)
level = BaseScene(screen, gameStateManager)

# setting up buttons
def test(args):
    gameStateManager.set_state('level')

def test2(args):
    gameStateManager.set_state('start')

button = Button((100, 100), (200, 100), test, (0, 0, 0), (70, 70, 70), (200, 200, 200))
button2 = Button((100, 300), (200, 100), test2, (0, 0, 0), (70, 70, 70), (200, 200, 200))

start.add_ui_element(button)
start.add_background_image(paper_sheet)
level.add_ui_element(button2)
level.add_background_image(piwo_img)
# after we create out states we add them to this dictionary 
states = {'start':start, 'level':level}

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