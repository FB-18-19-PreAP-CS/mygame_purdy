from pygame_functions import *

setAutoUpdate(False)

screenSize(1000, 750)
setBackgroundImage(["./images/bg-icebergs-1.png","./images/bg-icebergs-1.png"])

penguin = makeSprite("./images/penguin_walk01.png")
addSpriteImage(penguin,"./images/penguin_walk02.png")
addSpriteImage(penguin,"./images/penguin_walk03.png")
addSpriteImage(penguin,"./images/penguin_walk04.png")
addSpriteImage(penguin,"./images/penguin_jump01.png")
addSpriteImage(penguin,"./images/penguin_jump02.png")
addSpriteImage(penguin,"./images/penguin_jump03.png")

showSprite(penguin)

instructions = makeLabel("Catch all the fish!",40,325,10)
showLabel(instructions)


ground = 575 # height of ground

xPos = 100
yPos = 575

xSpeed = 0
ySpeed = 0

direction = 'right'

jumping = False
frame = 0
nextFrame = clock()

while True:

    if clock() > nextFrame:
        frame = (frame+1)%4
        nextFrame += 80

    moveSprite(penguin,xPos,yPos,True) # True here makes it base position off of center of the sprite

    if keyPressed("left"):
        direction = 'left'
        if not jumping:
            changeSpriteImage(penguin,frame)
        transformSprite(penguin,0,1,hflip=True)
        xPos -= 3

    if keyPressed("right"):
        direction = 'right'
        if not jumping:
            changeSpriteImage(penguin,frame)
        xPos += 3

    if keyPressed("up"):
        if direction == 'right':
            changeSpriteImage(penguin,6)
        elif direction == 'left':
            changeSpriteImage(penguin,6)
            transformSprite(penguin,0,1,hflip=True)
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
            changeSpriteImage(penguin,frame)
            if direction == 'left':
                transformSprite(penguin,0,1,hflip=True)


    
    tick(60)
    updateDisplay()

endWait()