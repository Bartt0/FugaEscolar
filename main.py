import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

    
screen.fill("purple")


pygame.display.flip()

clock.tick(1)  

pygame.quit()