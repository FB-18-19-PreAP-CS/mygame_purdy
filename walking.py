import pygame
from random import randint

WIDTH = 400
HEIGHT = 300

class Game:
    def __init__(self):
        pygame.mixer.pre_init(48000,-16,2,2048)
        pygame.mixer.init()
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Walking Simulator")
        self.clock = pygame.time.Clock()
        self.bgmusic = pygame.mixer.Sound('/home/purdy/PreAPCS/mygame_purdy/sounds/main_theme.ogg')
        self.character = Penguin()
        self.fish = pygame.sprite.Group()
        self.room_types = ['street','forrest']
        self.curr_type = 0  

    def start(self):
        done = False
        for i in range(3):
            self.fish.add(Fish())
        self.bgmusic.play(-1)
        while not done:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                self.character.walk('up')
        
            if pressed[pygame.K_DOWN]:
                self.character.walk('down')
            if pressed[pygame.K_LEFT]:
                self.character.walk('left')
            if pressed[pygame.K_RIGHT]:
                self.character.walk('right')


            

            self.draw_bg()
            #self.fish.draw(self.screen)
            for f in self.fish:
                # hit = pygame.sprite.collide_rect(self.character, f)
                # if hit:
                #     self.fish.remove(f)
                #     self.fish.append(Fish())
                f.blitme(self.screen)


            # for f in pygame.sprite.spritecollide(self.character,self.fish,1):    
            #     f.kill()

            self.character.blitme(self.screen)
            pygame.display.flip()

            self.check_edge()

            self.clock.tick(60)

    ## Check if penguin has reached the edge of the screen
    ## TODO: Add animation in each direction
    def check_edge(self):
        if self.character.x > WIDTH:
            next_clock = pygame.time.Clock()
            frame_count = 0
            line_x = 0
            while True:
                frame_count += 1
                self.screen.fill((0,0,0))
                
                for i in range(10):
                    pygame.draw.rect(self.screen,(255,255,0), pygame.Rect(line_x,150,50,25))
                    line_x += 100
                
                self.character.x -= 3
                line_x = frame_count * -3
                self.character.blitme(self.screen)
                next_clock.tick(120)
                if self.character.x == 0:
                    break

                pygame.display.flip()

        elif self.character.x <= 0:
            next_clock = pygame.time.Clock()
            frame_count = 0
            line_x = 0
            while True:
                frame_count += 1
                self.screen.fill((0,0,0))
                
                for i in range(10):
                    pygame.draw.rect(self.screen,(255,255,0), pygame.Rect(line_x,150,50,25))
                    line_x += 100
                
                self.character.x += 3
                line_x = frame_count * 3
                self.character.blitme(self.screen)
                next_clock.tick(120)
                if self.character.x <= WIDTH:
                    break

                pygame.display.flip()

        elif self.character.y <=0:
             self.character.y = 0

        # elif self.character.y >= HEIGHT - self.character.peng_anim[0].get_size():
        #     self.character.y = HEIGHT
    


    def draw_bg(self):
        if self.curr_type == 0:
            # draw lines on road
            line_x = 0
            for i in range(10):
                pygame.draw.rect(self.screen,(255,255,0), pygame.Rect(line_x,HEIGHT//2,50,25))
                line_x += 100


class Fish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = randint(0,WIDTH)
        self.y = randint(0,HEIGHT)
        self.image = pygame.image.load('/home/purdy/PreAPCS/mygame_purdy/images/fish.png')
        self.rect = self.image.get_rect()
        #print(self.rect)
    
    def blitme(self, screen):
        screen.blit(self.image,(self.x,self.y))


class Penguin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 30
        self.y = 30
        self.orientation = 'right'
        self.peng_anim = []
        self.frame = 0
        
        for i in range(4):
            self.peng_anim.append(pygame.image.load(f'/home/purdy/PreAPCS/mygame_purdy/images/penguin_walk0{i+1}.png'))
        self.rect = self.peng_anim[0].get_rect()
        #print(self.rect)

    
    def is_collided_with(self, sprite):
        return self.rect.colliderect()

    def blitme(self,screen):
        f = int(self.frame)%4
        if self.orientation == 'right':
            screen.blit(self.peng_anim[f],(self.x,self.y))
        elif self.orientation == 'left':
            # https://stackoverflow.com/questions/45601109/how-do-i-flip-an-image-horizontally-in-pygame
            screen.blit(pygame.transform.flip(self.peng_anim[f],True,False),(self.x,self.y))

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



    
        

Game().start()