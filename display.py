import pygame
from pygame.locals import *

# creates user display
class Display:

    def __init__(self):
        """ initialize pygame and creates game title"""
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('SpaceVentureZ')
    
        '''Sets the speed of the game in the run_game function'''
        self.game_speed = 60 
        ''' Following are Display variables need for creation of display canvas'''
        self.background_color = (0, 0, 0)
        self.width = 600
        self.height = 600
        self.font = pygame.font.SysFont('times new roman', 30)

        self.display = pygame.display.set_mode((self.width, self.height))

        '''variables that handles user mouse click on any display'''
        self.user_click = False

    '''Prints out text on the screen based on location x , y'''
    @staticmethod
    def add_text(text, font, color_, display, x, y):
        display.blit(font.render(text, True, color_), (x, y))
    '''Adds an image on the display screen'''
    @staticmethod
    def add_image(image, scale_w, scale_h, display, x, y):
        display.blit(pygame.transform.scale(image, (scale_w, scale_h)), (x, y))

    '''Display's game menu '''
    def menu(self):
        self.display = pygame.display.set_mode((600, 600))

        start = True
        while start:
            self.display.fill((0, 0, 0))

            '''gets user mouse click coordinates '''
            x, y = pygame.mouse.get_pos()

            '''Load's image'''
            game_Logo = pygame.image.load('game_images/SpaceVentureZ.png').convert()
            start_game = pygame.image.load('game_images/startButton.png').convert()
            options = pygame.image.load('game_images/optionButton.png').convert()
            
            '''Gets the rect from the images loaded and sets the position on display'''
            start_game_b = start_game.get_rect()
            start_game_b.x, start_game_b.y , start_game_b.w, start_game_b.h = (175, 200, 250, 85)
            options_b = options.get_rect()
            options_b.x, options_b.y, options_b.w, options_b.h = (175, 285, 250, 85)


            '''pygame event handling, exit and user mouse click handling'''
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    start = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.user_click = True
                        if start_game_b.collidepoint(x, y):
                            if self.user_click:
                                self.user_click = False
                                self.run_game()
                        if options_b.collidepoint(x, y):
                            if self.user_click:
                                self.user_click = False
                                self.options()
            pygame.display.update()
            self.clock.tick(60)

    def run_game(self):
        self.display = pygame.display.set_mode((self.width,self.height))

        start = True
        while start:
            self.display.fill((0, 0, 0))
            self.add_text('Game Page', self.font, (255, 0, 0), self.display, 100, 0)

            '''pygame event handling, exit and user mouse click handling'''
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    start = False
                 ''' Decided to press the escape button to leave the game'''
                 if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.menu()

            '''Run and Update game display'''
            self.run()
            pygame.display.update()
            self.clock.tick(60)

    ''' Dsiplay's Options Page'''
    def options(self):
        self.display = pygame.display.set_mode((600, 600))
        start = True
        while start:
            self.display.fill((0, 0, 0))
            self.add_text('Options Page', self.font, (255, 0, 0), self.display, 100, 0)

            # mouse coordinates
            x, y = pygame.mouse.get_pos()

            '''Creates Buttons and draw's them on the display'''
            menu = pygame.Rect(0, 0, 80, 40)

            pygame.draw.rect(self.display, (192, 192, 192), menu)
            self.add_text('Menu', self.font, (255, 255, 255), self.display, 0, 5)

            '''pygame event handling, exit and user mouse click handling'''
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    start = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.user_click = True
                        if menu.collidepoint(x, y):
                            if self.user_click:
                                self.user_click = False
                                self.menu()
            pygame.display.update()
            self.clock.tick(60)

    '''added run here to be overwritten in the main.py'''
    def run(self):
        pass

'''
NOTE: options and menu are incomplete
was unable to condense code into smaller helper functions
'''

