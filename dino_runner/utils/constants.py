import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUN_DIR =os.path.join(os.path.dirname(__file__), "..", "assets")
# Assets Constants

ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_PLUMA= [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Pluma.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Pluma.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_EXCAVADORA = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Excavadora.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Excavadora.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_PLUMA = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpPluma.png"))
JUMPING_EXCAVADORA = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpExcavadora.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]
DUCKING_EXCAVADORA = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Excavadora.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Excavadora.png")),
]


DUCKING_PLUMA = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Pluma.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Pluma.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
FEATHER = pygame.image.load(os.path.join(IMG_DIR, 'Other/pluma.png'))
EXCAVADORA = pygame.image.load(os.path.join(IMG_DIR, 'Other/excavadora.png'))
SQUARE = pygame.image.load(os.path.join(IMG_DIR, 'Other/square.png'))
RECTANGLE = pygame.image.load(os.path.join(IMG_DIR, 'Other/vegeta.png'))


BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))


HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"

FONT_STYLE = 'freesansbold.ttf'

SHIELD_TYPE = "Shield"

PLUMA_TYPE = "Feather"

EXCAVADORA_TYPE = "Excavator"
