import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()
font = pygame.font.SysFont('sans', 20)
running=True
YELLOW=(255,250,205)
RED=(250,0,0)

def gameintro():
    treasure=pygame.image.load('treasure.png')
    screen.blit(treasure,(1280/6,10))


while running:
    clock.tick(60)
    gameintro()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()



