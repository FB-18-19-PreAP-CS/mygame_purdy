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
time = 10
timeLabel = makeLabel(f"{time}",40,500,700,"green")
showLabel(timeLabel)
scoreLabel = makeLabel(f"Fish Remaining: {num_fish - score}",24,700,10)
showLabel(scoreLabel)
ground = 575 # height of ground

xPos = 300
yPos = 575

xSpeed = 3
ySpeed = 0

direction = 'right'

jumping = False
frame = 0
nextFrame = clock()
boosted = 0
timeClock = clock()


while True:
    if score == 20:
        winLabel = makeLabel("YOU WIN!",50,400,700,"green")
        hideLabel(timeLabel)
        showLabel(winLabel)
        break
    if clock() - timeClock >= 1000:
        time -= 1
        timeClock = clock()
        if time < 5:
            changeLabel(timeLabel,f"{time}","red")
        else:
            changeLabel(timeLabel,f"{time}","green")
        if time == 0:
            hideLabel(timeLabel)
            loseLabel = makeLabel("YOU LOSE!",50,400,700,"red")
            showLabel(loseLabel)
            break
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
            scrollBackground(xSpeed,0)
            for f in fish:
                moveSprite(f,f.rect[0]+xSpeed,f.rect[1])

        else:
            xPos -= xSpeed

    if keyPressed("space"):
        if boosted ==0 or clock() - boosted > 5000:
            print('here')
            xSpeed = 10
            boosted = clock()
    
    if clock() - boosted > 2000:
        xSpeed = 3

    if keyPressed("right"):
        direction = 'right'
        if not jumping:
            changeSpriteImage(penguin,frame)
        if xPos >= 600:
            xPos = 600
            scrollBackground(-xSpeed,0)
            for f in fish:
                moveSprite(f,f.rect[0]-xSpeed,f.rect[1])
        else:
            xPos += xSpeed

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