from pygame_functions import *

screenSize(1000, 750)
setBackgroundImage("./images/bg-icebergs-1.png")

penguin = makeSprite("./images/penguin_walk01.png")
addSpriteImage(penguin,"./images/penguin_walk02.png")
addSpriteImage(penguin,"./images/penguin_walk03.png")
addSpriteImage(penguin,"./images/penguin_walk04.png")

showSprite(penguin)

ground = 575 # height of ground

xPos = 100
yPos = 575

xSpeed = 0
ySpeed = 0

jumping = False


while True:
    moveSprite(penguin,xPos,yPos,True) # True here makes it base position off of center of the sprite

    if keyPressed("left"):
        xPos -= 3

    if keyPressed("right"):
        xPos += 3

    if keyPressed("up"):
        if not jumping:
            jumping = True
            ySpeed = 8

    yPos -= ySpeed

    if jumping:
        ySpeed -= .5
        if yPos >= ground:
            ySpeed = 0
            yPos = ground
            jumping = False


    
    tick(60)

endWait()