import pygame


## SETUP ##

WIDTH = 400
HEIGHT = 300
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
done = False
inner_r = 1
colors = [(255,0,0),(0,255,0)]
color = 0
button_pressed = False
still_pressed = False
while not done:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            done = True
        

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and button_pressed:
        #     still_pressed = True

        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        #     button_pressed = True

        # elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
        #     button_pressed = False
        #     still_pressed = False

    pygame.draw.circle(screen,colors[color],(WIDTH//2,HEIGHT//2),50)
    pygame.draw.circle(screen,(0,0,255),(WIDTH//2,HEIGHT//2),inner_r)
    
    
    
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_DOWN] and not button_pressed:
        print('pressed')
        button_pressed = True
        if inner_r >=45: # closer to 50 is harder
            color = (color + 1) % 2

    if button_pressed and not pressed[pygame.K_DOWN]:
        print('released')
        button_pressed = False

    inner_r = (inner_r +1 )%50
    
    pygame.display.flip()
    screen.fill((0,0,0))


    clock.tick(60)
    