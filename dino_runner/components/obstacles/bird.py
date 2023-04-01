import pygame,random
from pygame.sprite import Sprite
from  dino_runner.utils.constants import BIRD

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Sprite):

    def __init__(self):
        self.image_bird = BIRD
        self.image = self.image_bird[0]
        self.bird_rect = self.image.get_rect() #creo un rectangulo para el pajaro
        self.bird_rect.x =800
        self.bird_rect.y=100
        self.step_index = 0
        self.bird_move = True
    
    def update(self):
        if self.bird_move:
            self.move()

        if self.step_index >= 10:
            self.step_index = 0

    def move(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = 800
        self.bird_rect.y = 100
        self.step_index +=1

    def draw(self, screen):
        screen.blit(self.image, (self.bird_rect.x , self.bird_rect.y))