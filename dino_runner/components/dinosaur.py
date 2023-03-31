import pygame
from pygame.sprite import Sprite
from  dino_runner.utils.constants import RUNNING, DUCKING, JUMPING


class Dinosaur(Sprite):

    def __init__(self):
        self.image_run = RUNNING
        self.image_duck = DUCKING
        self.image_jump = JUMPING

        #Incializo la image con la imagen 1 de run
        self.image = self.image_run[0]
        self.dino_rect = self.image.get_rect() #Creo un rectangulo para las colisiones
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
        screen.blit(self.image, (self.dino_rect.x , self.dino_rect.y))
        