import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,startX,startY):
        pygame.sprite.Sprite.__init__(self)
        self.player_image = pygame.image.load('./images/penguin_walk01.png')
        self.rect = self.player_image.get_rect()
        
        self.x = startX
        self.y = startY - self.player_image.get_size()[1] # make him stand on top of the ground

        self.ground = self.y
        

        self.direction = 'right'
        self.peng_anim = []
        self.frame = 1
        
        for i in range(4):
            self.peng_anim.append(pygame.image.load(f'./images/penguin_walk0{i+1}.png'))
        
        self.on_ground = True # needed if multiple platforms...player could be falling!
        self.is_jumping = False
        self.gravity = .5 # The lower this value, the higher the jump
        self.velocity = 0

    def check_on_ground(self):
        if self.y >= self.ground:
            self.on_ground = True
            self.is_jumping = False
            self.y = self.ground

    def blit(self, screen):
        f = int(self.frame)%4
        self.player_image = self.peng_anim[f]
        if self.direction == 'right':
            screen.blit(self.player_image,(self.x,self.y))
        elif self.direction == 'left':
            screen.blit(pygame.transform.flip(self.player_image),(self.x,self.y))
        self.rect = self.player_image.get_rect()

    def walk(self, direction):
        if direction == 'up':
            self.y -= 3
            self.frame += .25
        elif direction == 'down':
            self.y += 3
            self.frame += .25
        elif direction == 'left':
            self.orientation = 'left'
            self.x -= 3
            self.frame += .25
        elif direction == 'right':
            self.orientation = 'right'
            self.x += 3
            self.frame += .25

    


class JumpGame:
    windowWidth = 640
    windowHeight = 480

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("Jump Demo")
        self.clock = pygame.time.Clock()
        self.player = Player(self.windowWidth//2,self.windowHeight-100)
        

    def draw_ground(self):
        pygame.draw.rect(self.screen,(0,255,0),pygame.rect.Rect(0,self.windowHeight-100,self.windowWidth,100))

    def start(self):
        while True:
            self.draw_ground()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_SPACE] and not self.player.is_jumping and self.player.on_ground:
                # jump!
                self.player.on_ground = False
                self.player.is_jumping = True
                self.player.velocity = 8

            if pressed[pygame.K_LEFT]:
                self.player.walk('left')

            if pressed[pygame.K_RIGHT]:
                self.player.walk('right')
            
            if self.player.is_jumping:
                
                self.player.y -= self.player.velocity
                self.player.velocity -= self.player.gravity 
                self.player.check_on_ground()
            
            self.player.blit(self.screen) # draw the player on the screen
            

            pygame.display.flip()

            self.screen.fill((0,0,0))
            self.clock.tick(60)

JumpGame().start()