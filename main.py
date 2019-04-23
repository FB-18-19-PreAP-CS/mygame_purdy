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


    def start(self):
        done = False
        self.bgmusic.play(-1)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


Game().start()