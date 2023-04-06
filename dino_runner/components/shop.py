import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT,SCREEN_WIDTH


class Shop:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT//2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH//2

    def __init__(self, message, screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center=(self.HALF_SCREEN_WIDTH,self.HALF_SCREEN_HEIGHT)

    def update(self,game):
        pygame.display.update()

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def reset_screen_color(self,screen):
        screen.fill((255,255,255))

    

    def update_message(self, message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center=(self.HALF_SCREEN_WIDTH,self.HALF_SCREEN_HEIGHT)
