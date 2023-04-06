import pygame,random
from dino_runner.components.obstacles.smallCactus import SmallCactus
from dino_runner.components.obstacles.largeCactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS,BIRD,SHIELD_TYPE,LARGE_CACTUS, PLUMA_TYPE,EXCAVADORA_TYPE



class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.death_sound= pygame.mixer.Sound("dino_runner/assets/Other/fortnite.mp3")
    
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
                if game.player.type == SHIELD_TYPE:
                    self.obstacles.remove(obstacle)
                elif game.player.type == PLUMA_TYPE:
                    pass
                elif game.player.type == EXCAVADORA_TYPE:
                    game.playing = False
                    game.death_count +=1
                    self.death_sound.play()                                  
                else:
                    pygame.time.delay(1000)
                    game.death_count +=1
                    game.playing = False
                    self.death_sound.play()
                    break
                    


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles =[]
    
