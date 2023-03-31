import pygame
from pygame.sprite import Sprite
from  dino_runner.utils.constants import RUNNING, DUCKING, JUMPING


class Dinosaur(Sprite):

    def __init__(self):
        self.image_run = RUNNING[0]
        self.image_duck = DUCKING
        self.image_jumo = JUMPING
        self.dino_rect = self.image_run.get_rect()
        self.dino_rect.x =80
        self.dino_rect.y=310
    
    def update(self, userInput):
        pass

    def run(self):
        pass

    def jump(self):
        pass

    def duck(self):
        pass

    def draw(self, screen):
        screen.blit(self.image_run, (self.dino_rect.x , self.dino_rect.y))
        