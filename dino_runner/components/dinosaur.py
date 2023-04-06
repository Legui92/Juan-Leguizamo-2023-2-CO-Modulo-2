import pygame
from pygame.sprite import Sprite
from  dino_runner.utils.constants import RUNNING,DEFAULT_TYPE, DUCKING, JUMPING, SHIELD_TYPE, RUNNING_SHIELD,DUCKING_SHIELD,JUMPING_SHIELD


RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    JUMP_SPEED = 8.5
    POS_Y_DUCK = 343

    def __init__(self):
        self.type = DEFAULT_TYPE
        # self.image_run = RUN_IMG[self.type][0]################################
        # self.image_duck = DUCK_IMG[self.type][0]
        # self.image_jump = JUMP_IMG[self.type]
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        #Incializo la image con la imagen 1 de run
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect() #Creo un rectangulo para las colisiones
        self.dino_rect.x =self.POS_X
        self.dino_rect.y=self.POS_Y
        self.step_index = 0
        self.has_power_up = False
        self.power_time_up = 0
        
    
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
        self.image = RUN_IMG[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y
        self.step_index +=1


    def jump(self):
        self.image = JUMP_IMG[self.type]###################
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8

        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.POS_Y
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.POS_X
        self.dino_rect.y = self.POS_Y_DUCK
        self.step_index +=1


    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x , self.dino_rect.y))

    def reset_dinosaur(self):
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        #Incializo la image con la imagen 1 de run
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect() #Creo un rectangulo para las colisiones
        self.dino_rect.x =self.POS_X
        self.dino_rect.y=self.POS_Y
        self.step_index = 0  