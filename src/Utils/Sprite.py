import pygame
class Status:
    IDLE = 0
    CLICKED = 1

class Sprite:
    def __init__(self,image_path,pos:tuple,visible=True,scale=None,trans=None):
        self.image=pygame.image.load(image_path)
        if scale is not None:
            self.image = pygame.transform.scale_by(self.image, scale)
        self.pos=pos
        self.vis=visible
        self.trans=trans
        self.status=Status.IDLE
        if trans is not None:
            self.image.set_alpha(trans)

    def render(self,screen):
        if self.vis==True:
            screen.blit(self.image, self.pos)

    def update(self, dx, dy, hide=False):
        self.pos = (dx, dy)
        if hide==True:
            self.vis = False

    def get_pos(self):
        return self.pos

    def cursor_over_sprite(self, mouse):
        mouse_pos=pygame.mouse.get_pos()
        sprite_rect = self.image.get_rect(topleft=self.pos)
        return sprite_rect.collidepoint(mouse_pos)

    def process_input(self, events, mouse,*args):
        mouse_pos=pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.cursor_over_sprite(mouse_pos):
                    self.status=Status.CLICKED
                else:
                    self.status=Status.IDLE
    
# test
# RESOLUTION = (1280, 720)
# pygame.init()
# screen = pygame.display.set_mode(RESOLUTION)
# sprite = Sprite("image_path", (0, 0),True)
# running = True
# while running:
#     events=pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             running = False
#     pos=sprite.get_pos()
#     sprite.update(pos[0],pos[1])  

#     screen.fill((0, 0, 0))
#     sprite.process_input(events,pygame.mouse)
#     sprite.render(screen)
#     pygame.display.flip()

# pygame.quit()