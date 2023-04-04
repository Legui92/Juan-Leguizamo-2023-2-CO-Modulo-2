import pygame,random
from pygame.sprite import Sprite
from  dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image,self.type) #de la clase padre llamar al constructor
        pos_y = [250, 300, 150] #250 mitad(agacha o salta para pasar), 300 baja(saltar para pasar), 150 alta(agachar o correr)
        eleccion = random.choice(pos_y)
        self.rect.y = eleccion
        self.step_index = 0

    def draw(self, screen):
        if self.step_index >=10:
            self.step_index =0
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        screen.blit(self.image, (self.rect.x,self.rect.y))
        self.step_index +=1

