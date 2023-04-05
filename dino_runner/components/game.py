import pygame

from dino_runner.utils.constants import BG,FONT_STYLE ,ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.print import Print_message

class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.menu = Menu('Press any key to start...', self.screen)
        self.print_message= Print_message('Press any key to restart...',self.screen)
        self.runnig = False
        self.death_count = 0
        self.score = 0
        self.high_score = 0

    def execute(self):
        self.runnig = True
        while self.runnig:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
        

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.player.reset_dinosaur()
        self.score = 0
        self.game_speed = self.GAME_SPEED
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        userInput = pygame.key.get_pressed()
        self.player.update(userInput)
        self.cloud.update(self.game_speed)#########
        self.obstacle_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))  #RGB(0,0,0)
        self.draw_background()
        self.player.draw(self.screen)
        self.cloud.draw(self.screen) # llamo al metodo player de dinosaur para dibujarlo 
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()
        


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed #hace avanzar el fondo

    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT//2
        half_screen_width = SCREEN_WIDTH//2
        self.menu.reset_screen_color(self.screen)

        if self.death_count ==0:
            self.menu.draw(self.screen)
        else:
            self.menu.update_message('Game over. Press any key to restart...')
            #High score print
            self.print_message.update_message(f'Your score: {self.score}',550,370)# print(message, pos_x,pos_y)
            self.print_message.draw(self.screen)
            self.print_message.update_message(f'Highest score: {self.high_score}',550,410)
            self.print_message.draw(self.screen)
            self.print_message.update_message(f'Total deaths: {self.death_count}',550,450)
            self.print_message.draw(self.screen)
            self.menu.draw(self.screen)
        self.screen.blit(ICON,(half_screen_width-50,half_screen_height-140))
        self.print_message.update(self)
        self.menu.update(self)


    def update_score(self):
        self.score +=1
        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 2
        if self.score > self.high_score:
            self.high_score = self.score
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'score: {self.score}', True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center=(1000,50)
        self.screen.blit(text, text_rect)

