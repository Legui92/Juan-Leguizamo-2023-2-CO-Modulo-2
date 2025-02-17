import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.pluma import Feather
from dino_runner.components.power_ups.excavadora import Excavadora


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(150,250)
        self.duration = random.randint(3,5)

    def generate_power_up(self):
        #possible_power_ups =[Pluma()]
        possible_power_ups =[Shield(), Feather(),Excavadora()]
        power_up = random.choice(possible_power_ups)
        self.when_appears += random.randint(150,250)
        self.power_ups.append(power_up)

    def update(self, game):
        if len(self.power_ups) == 0 and self.when_appears == game.score:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed,self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                if game.coins == 10:
                    self.duration += random.randint(1,4)
                game.coins +=1
                power_up.start_time=pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration* 1000)
                self.power_ups.remove(power_up)
                self.duration = random.randint(3,5)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset(self,):
        self.power_ups = []
        self.when_appears = random.randint(150, 250)