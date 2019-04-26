from pygame_functions import *
from random import randint


setAutoUpdate(False)

screenSize(1000, 750)
pygame.display.set_caption("Ice Fishing") # has to go after screenSize
setBackgroundImage(["./images/bg-icebergs-1.png","./images/bg-icebergs-1.png"])
num_fish = 20
fish = []
for i in range(num_fish):
    fish.append(makeSprite("./images/fish.png"))

for f in fish:
    moveSprite(f,randint(-1000,1000),500,True)
    showSprite(f)
    
jumpSound = makeSound("./sounds/jump.wav")
bgMusic = makeMusic("./sounds/main_theme.ogg")
playMusic()
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

score = 0
scoreLabel = makeLabel(f"Fish Remaining: {num_fish - score}",24,700,10)
showLabel(scoreLabel)
ground = 575 # height of ground

xPos = 300
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
        if xPos <= 300:

            xPos = 300
            scrollBackground(3,0)
            for f in fish:
                moveSprite(f,f.rect[0]+3,f.rect[1])

        else:
            xPos -= 3

    if keyPressed("right"):
        direction = 'right'
        if not jumping:
            changeSpriteImage(penguin,frame)
        if xPos >= 600:
            xPos = 600
            scrollBackground(-3,0)
            for f in fish:
                moveSprite(f,f.rect[0]-3,f.rect[1])
        else:
            xPos += 3

    if keyPressed("up"):
        if direction == 'right':
            changeSpriteImage(penguin,6)
        elif direction == 'left':
            changeSpriteImage(penguin,6)
            transformSprite(penguin,0,1,hflip=True)
        if not jumping:
            playSound(jumpSound)
            jumping = True
            ySpeed = 10

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

    for f in fish:
        if touching(penguin,f):
            killSprite(f)
            fish.remove(f)
            score += 1
        
    

    changeLabel(scoreLabel,f"Fish Remaining: {num_fish - score}")

    tick(60)
    updateDisplay()

endWait()