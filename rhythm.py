import pygame


## SETUP ##

WIDTH = 400
HEIGHT = 300
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
done = False
inner_r = 1
color = (255,0,0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.circle(screen,color,(WIDTH//2,HEIGHT//2),50)
    pygame.draw.circle(screen,(0,0,255),(WIDTH//2,HEIGHT//2),inner_r)
    
    inner_r = (inner_r +1 )%50
    

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and inner_r == 49:
        color = (0,255,0)
    pygame.display.flip()
    screen.fill((0,0,0))


    clock.tick(60)
    