import pygame

class Image(pygame.sprite.Sprite):
    def __init__(self, position, size, image_dir):
        self.background = pygame.transform.scale(pygame.image.load(image_dir),size)
        self.size = size
        self.position = position
        self.pos_rect = pygame.Rect(position[0], position[1], 0, 0)

    def render(self, screen):
        screen.blit(self.background, self.get_rect())

    def get_rect(self):
        return self.pos_rect

    def get_height(self):
        return self.size[1]

    def get_width(self):
        return self.size[0]
     
    def process_input(self, mouse, *args):
        pass

    def update(self, mouse):
        pass
