import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_image = pygame.image.load('./images/penguin_walk01.png')
        self.rect = self.player_image.get_rect()

        self.x = WIDTH // 2
        self.y = HEIGHT - 100  # room for the ground to show

        self.direction = 'right'
        self.on_ground = True
        self.is_jumping = False
        self.gravity = 1.2
        self.velocity = 0

        self.rect.center = (self.x, self.y)

class JumpGame:
    windowWidth = 640
    windowHeight = 480

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("Jump Demo")
        self.clock = pygame.time.Clock()
        self.player = Player()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_SPACE]:
                # jump!
                player.is_jumping = True
                player.velocity = 8