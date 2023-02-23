import pygame

pygame.init()

display = pygame.display.set_mode((1080, 764))
pygame.display.set_caption("Simple Space")
icon = pygame.image.load("pic.png")
pygame.display.set_icon(icon)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill((20, 45, 84))
    pygame.display.update()