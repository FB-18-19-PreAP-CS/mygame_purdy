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

    def start(self):
        done = False
        self.bgmusic.play(-1)
        while not done:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.character.blitme(self.screen)

            self.clock.tick(60)


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
        if self.orientation == 'right':
            screen.blit(self.peng_anim[self.frame],(self.x,self.y))
        elif orientation == 'left':
            # https://stackoverflow.com/questions/45601109/how-do-i-flip-an-image-horizontally-in-pygame
            screen.blit(pygame.transform(self.peng_anim[self.frame],true,false),(self.x,self.y))
    
        

Game().start()