import pygame

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
        self.room_types = ['street','forrest']
        self.curr_type = 0  

    def start(self):
        done = False
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

    def draw_bg(self):
        if self.curr_type == 0:
            # draw lines on road
            line_x = 0
            for i in range(10):
                pygame.draw.rect(self.screen,(255,255,0), pygame.Rect(line_x,HEIGHT//2,50,25))
                line_x += 100


    


class Penguin:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.orientation = 'right'
        self.peng_anim = []
        self.frame = 0
        for i in range(4):
            self.peng_anim.append(pygame.image.load(f'/home/purdy/PreAPCS/mygame_purdy/images/penguin_walk0{i+1}.png'))

    
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