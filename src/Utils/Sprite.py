import pygame

class Sprite:
    def __init__(self,image_path,pos:tuple,visible=True,scale=None,trans=None):
        self.image=pygame.image.load(image_path)
        if scale is not None:
            self.image = pygame.transform.scale_by(self.image, scale)
        self.pos=pos
        self.vis=visible
        self.trans=trans
        if trans is not None:
            self.image.set_alpha(trans)

    def draw(self,screen):
        if self.vis==True:
            screen.blit(self.image, self.pos)
    def update(self, dx, dy, hide=False):
        self.pos = (dx, dy)
        if hide==True:
            self.vis = False
    def get_pos(self):
        return self.pos
    
# # test
# RESOLUTION = (1280, 720)
# pygame.init()
# screen = pygame.display.set_mode(RESOLUTION)
# sprite = Sprite("image_path", (0, 0),True)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pos=sprite.get_pos()
#     sprite.update(pos[0],pos[1])  # This will move the sprite and hide it

#     screen.fill((0, 0, 0))
#     sprite.draw(screen)
#     pygame.display.flip()

# pygame.quit()