import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT,SCREEN_WIDTH


class Print_rules:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT//2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH//2
        
    def __init__(self, message, screen):
        self.high_score = 0
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 20)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center=(self.HALF_SCREEN_WIDTH,self.HALF_SCREEN_HEIGHT)

    def update(self,game):
        pygame.display.update()

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def update_message(self, message, POS_X,POS_Y,tupla):  
        self.text = self.font.render(message, True, tupla)
        self.text_rect = self.text.get_rect()
        self.text_rect.center=(POS_X,POS_Y)