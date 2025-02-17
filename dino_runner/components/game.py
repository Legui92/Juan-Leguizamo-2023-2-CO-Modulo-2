import pygame

from dino_runner.utils.constants import BG,DEFAULT_TYPE,FONT_STYLE ,ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SQUARE,RECTANGLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.print import Print_message
from dino_runner.components.print_rules import Print_rules
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    GAME_SPEED = 20
    TIME_PER_DAY = 500

    def __init__(self):
        self.half_screen_height = SCREEN_HEIGHT//2
        self.half_screen_width = SCREEN_WIDTH//2
        pygame.mixer.init()
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.background_dark = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.cloud = Cloud()
        self.menu = Menu('Press any key to start...', self.screen)
        self.print_message= Print_message('Press any key to restart...',self.screen)
        self.runnig = False
        self.print_rules=Print_rules('message',self.screen)
        self.death_count = 0
        self.score = 0
        self.coins = 0
        self.high_score = 0
        self.power_up_manager = PowerUpManager()
        self.time=0

    def execute(self):
        self.runnig = True
        while self.runnig:
            if not self.playing:              
                self.show_menu()
                self.time =0
                self.player.type = DEFAULT_TYPE
                self.player.has_power_up = False
                self.background_dark=False
        pygame.display.quit()
        pygame.quit()
        

    def run(self):
        self.reset_game()
        # Game loop: events - update - draw
        pygame.mixer.music.load("dino_runner/assets/Other/fumarato.ogg")
        #pygame.mixer.music.load("dino_runner/assets/Other/js4e.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.playing = True


        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.mixer.music.stop()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        userInput = pygame.key.get_pressed()
        self.player.update(userInput)
        self.cloud.update(self.game_speed)#########
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))  #RGB(0,0,0)
        self.draw_background()
        self.player.draw(self.screen)
        self.cloud.draw(self.screen) # llamo al metodo player de dinosaur para dibujarlo 
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        pygame.display.update()
        

    def draw_background(self):
        image_width = BG.get_width()
        self.time +=1
        if self.time >= self.TIME_PER_DAY:
            self.time = 0
            self.background_dark = False if self.background_dark else True

        if self.background_dark:   
            self.screen.fill((0,0,0))   
        else:
            self.screen.fill((255,255,255))

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
            self.screen.blit(RECTANGLE,(-7,410))
            self.print_rules.update_message(f'Power-ups:(Shield,Feather,Excavator) ',550,370,(255,0,0)) # print(message, pos_x,pos_y)
            self.print_rules.draw(self.screen)
            self.print_rules.update_message(f'SHIELD your are immune for # seconds ',250,450,(0,0,0)) # print(message, pos_x,pos_y)
            self.print_rules.draw(self.screen)
            self.print_rules.update_message(f'FEATHER you win a jump boost  for # seconds ',250,500,(0,0,0)) # print(message, pos_x,pos_y)
            self.print_rules.draw(self.screen)
            self.print_rules.update_message(f'EXCAVATOR DRILL press Ctrl to use for # seconds ',260,550,(0,0,0)) # print(message, pos_x,pos_y)
            self.print_rules.draw(self.screen)
            self.print_rules.update_message(f'If you pick 10 coins the next power-up',850,480,(0,0,255)) # print(message, pos_x,pos_y)
            self.print_rules.draw(self.screen)
            self.print_rules.update_message(f'lasts longer',850,510,(0,0,255)) # print(message, pos_x,pos_y)
            self.print_rules.draw(self.screen)

        else:
            #self.menu.update_message('Game over. Press K_P0 to go to the shop or other key to restart...')
            self.menu.update_message('Game over. Press any key to restart...')
            #High score print
            self.print_message.update_message(f'Your score: {self.score}',550,370,(0,0,0)) # print(message, pos_x,pos_y)
            self.print_message.draw(self.screen)
            self.print_message.update_message(f'Highest score: {self.high_score}',550,410,(0,0,0))
            self.print_message.draw(self.screen)
            self.print_message.update_message(f'Total deaths: {self.death_count}',550,450,(0,0,0))
            self.menu.draw(self.screen)
            self.print_message.draw(self.screen)
        self.screen.blit(ICON,(half_screen_width-50,half_screen_height-140))
        self.print_message.update(self)
        self.print_rules.update(self)
        self.menu.update(self)


    def update_score(self):
        self.score +=1
        if self.score % 100 == 0 and self.game_speed < 500:
            self.game_speed += 2
        if self.score > self.high_score:
            self.high_score = self.score
        if self.coins > 10:
            #ponerle power up
            self.coins = 0
        
            
    
    def draw_score(self):
        if self.time >=self.TIME_PER_DAY:
            self.background_dark = False if self.background_dark else True
            #NIGHT
        if self.background_dark:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render(f'score: {self.score}', True,(255,255,255))
            text_rect = text.get_rect()
            text_rect.center=(1000,50)
            self.print_message.update_message(f'high score: {self.high_score}',970,85,(255,255,255)) 
            self.print_message.draw(self.screen)
            self.print_message.update_message(f'coins: {self.coins}',1010,120,(255,255,255))
            self.print_message.draw(self.screen)
            self.screen.blit(text, text_rect)

        else:
            #DAY
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render(f'score: {self.score}', True,(0,0,0))
            text_rect = text.get_rect()
            text_rect.center=(1000,50)
            self.print_message.update_message(f'high score: {self.high_score}',970,85,(0,0,0)) # print(message, pos_x,pos_y)
            self.print_message.draw(self.screen)
            self.print_message.update_message(f'coins: {self.coins}',1010,120,(0,0,0))
            self.print_message.draw(self.screen)
            self.screen.blit(text, text_rect)
            
            


    def reset_game(self):
        self.player.reset_dinosaur()
        self.power_up_manager.reset()
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.time=0
        self.game_speed = self.GAME_SPEED


    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up-pygame.time.get_ticks())/1000,2)

            if time_to_show >=0:
                if self.time >=self.TIME_PER_DAY:
                    self.background_dark = False if self.background_dark else True
                if self.background_dark:
                    #Night
                    self.print_message.update_message(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 550,50,(255,255,255))
                    self.print_message.draw(self.screen)
                    
                else:
                    #Day
                    self.print_message.update_message(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 550,50,(0,0,0))
                    self.print_message.draw(self.screen)
                    

            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE    

    def go_shop(self):
        self.top_screen = self.half_screen_width + 200 
        self.screen.fill((255,255,255))    
        if self.death_count ==0:
            self.menu.draw(self.screen)
        else:
            self.print_message.update_message(f'Welcome to the shop',self.half_screen_width,self.top_screen,(0,0,0))
            self.print_message.draw(self.screen)
            self.print_message.update_message(f'You have {self.coins} coins',self.half_screen_width,self.top_screen+100,(0,0,0))
            self.print_message.draw(self.screen)
        self.print_message.update(self)
        self.menu.update(self)
    