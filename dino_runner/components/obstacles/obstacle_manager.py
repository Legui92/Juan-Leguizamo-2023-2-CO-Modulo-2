import pygame,random
from dino_runner.components.obstacles.smallCactus import SmallCactus
from dino_runner.components.obstacles.largeCactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS , BIRD
from dino_runner.utils.constants import LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def generate_obstacle(self):
        obstacle = [SmallCactus(SMALL_CACTUS),LargeCactus(LARGE_CACTUS),Bird(BIRD)]
        randomObstacle=random.choice(obstacle)
        return randomObstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print("Collision")
                pygame.time.delay(1000)
                game.death_count +=1
                game.playing = False
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles =[]
    
