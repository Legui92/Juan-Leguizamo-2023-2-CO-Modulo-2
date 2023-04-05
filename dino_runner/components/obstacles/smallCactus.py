import random

from dino_runner.components.obstacles.obstacle import Obstacle


class SmallCactus(Obstacle):
    CACTUS = {
        "LARGE":(),
        "SMALL": (),
    }
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image,self.type) #de la clase padre llamar al constructor
        self.rect.y = 325
        