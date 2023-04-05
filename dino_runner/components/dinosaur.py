import pygame
from pygame.sprite import Sprite
from  dino_runner.utils.constants import RUNNING, DUCKING, JUMPING


class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    JUMP_SPEED = 8.5
    POS_Y_DUCK = 343

    def __init__(self):
        self.image_run = RUNNING
        self.image_duck = DUCKING
        self.image_jump = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        #Incializo la image con la imagen 1 de run
        self.image = self.image_run[0]
        self.dino_rect = self.image.get_rect() #Creo un rectangulo para las colisiones
        self.dino_rect.x =self.POS_X
        self.dino_rect.y=self.POS_Y
        self.step_index = 0
        
    
    def update(self,userInput):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        
        elif userInput[pygame.K_DOWN]: #and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True

        elif not self.dino_jump:
            self.dino_run = True    
        
            
        if self.step_index >= 10:
            self.step_index = 0


    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index +=1


    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8

        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.POS_Y
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y_DUCK
        self.step_index +=1


    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x , self.dino_rect.y))

    def reset_dinosaur(self):
        self.image_run = RUNNING
        self.image_duck = DUCKING
        self.image_jump = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        #Incializo la image con la imagen 1 de run
        self.image = self.image_run[0]
        self.dino_rect = self.image.get_rect() #Creo un rectangulo para las colisiones
        self.dino_rect.x =self.POS_X
        self.dino_rect.y=self.POS_Y
        self.step_index = 0  