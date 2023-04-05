import pygame,random
from pygame.sprite import Sprite
from  dino_runner.utils.constants import CLOUD

from dino_runner.utils.constants import SCREEN_WIDTH

class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.x = SCREEN_WIDTH
        self.y = random.randint(50,150)
        self.width = self.image.get_width()
    
    
    def update(self, game_speed):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500,3000) # + random para que no salga sinronizada con un obstacle
            self.y = random.randint(50,100)

    def draw(self,screen):
        screen.blit(self.image, (self.x,self.y))
