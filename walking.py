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
        self.font = pygame.font.SysFont("arial",24)

    def gen_fish(self):
        for i in range(3):
            self.fish.add(Fish())

    def start(self):
        done = False
        self.gen_fish()
        self.bgmusic.play(-1)
        while not done:
            self.screen.fill((0,0,0))
            score_text = self.font.render(f"Hunger: {self.character.hunger}",True,(255,255,255))
            self.screen.blit(score_text,(0,0))
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
                if self.character.rect.colliderect(f):
                    self.character.hunger -= 50
                    self.fish.remove(f)

            for f in self.fish:
                f.blitme(self.screen)
            self.character.blitme(self.screen)

            

            pygame.display.flip()

            self.check_edge()

            self.clock.tick(60)

    ## Check if penguin has reached the edge of the screen
    ## TODO: Add animation in each direction
    def check_edge(self):
        if self.character.rect.x > WIDTH:
            next_clock = pygame.time.Clock()
            frame_count = 0
            line_x = 0
            while True:
                frame_count += 1
                self.screen.fill((0,0,0))
                
                for i in range(10):
                    pygame.draw.rect(self.screen,(255,255,0), pygame.Rect(line_x,150,50,25))
                    line_x += 100
                
                self.character.rect.x -= 3
                line_x = frame_count * -3
                self.character.blitme(self.screen)
                next_clock.tick(120)
                if self.character.rect.x == 0:
                    break

                
                pygame.display.flip()
                for f in self.fish:
                    self.fish.remove(f)

                self.gen_fish()

        elif self.character.rect.x <= 0:
            next_clock = pygame.time.Clock()
            frame_count = 0
            line_x = 0
            while True:
                frame_count += 1
                self.screen.fill((0,0,0))
                
                for i in range(10):
                    pygame.draw.rect(self.screen,(255,255,0), pygame.Rect(line_x,150,50,25))
                    line_x += 100
                
                self.character.rect.x += 3
                line_x = frame_count * 3
                self.character.blitme(self.screen)
                next_clock.tick(120)
                if self.character.rect.x <= WIDTH:
                    break

                pygame.display.flip()

        elif self.character.rect.y <=0:
             self.character.rect.y = 0

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

        self.image = pygame.image.load('./images/fish.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(self.image.get_size()[0],WIDTH-self.image.get_size()[0])
        self.rect.y = randint(0,HEIGHT-self.image.get_size()[1])

    
    def blitme(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))


class Penguin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.orientation = 'right'
        self.peng_anim = []
        self.frame = 0
        
        for i in range(4):
            self.peng_anim.append(pygame.image.load(f'./images/penguin_walk0{i+1}.png'))
        self.rect = self.peng_anim[0].get_rect()
        self.rect.x = 30
        self.rect.y = 30
        self.hunger = 100
        #print(self.rect)


    def blitme(self,screen):
        f = int(self.frame)%4
        if self.orientation == 'right':
            screen.blit(self.peng_anim[f],(self.rect.x,self.rect.y))
        elif self.orientation == 'left':
            # https://stackoverflow.com/questions/45601109/how-do-i-flip-an-image-horizontally-in-pygame
            screen.blit(pygame.transform.flip(self.peng_anim[f],True,False),(self.rect.x,self.rect.y))

    def walk(self, direction):
        self.hunger += 1
        if direction == 'up':
            self.rect.y -= 3
            self.frame += .25
        elif direction == 'down':
            self.rect.y += 3
            self.frame += .25
        elif direction == 'left':
            self.orientation = 'left'
            self.rect.x -= 3
            self.frame += .25
        elif direction == 'right':
            self.orientation = 'right'
            self.rect.x += 3
            self.frame += .25



    
        

Game().start()