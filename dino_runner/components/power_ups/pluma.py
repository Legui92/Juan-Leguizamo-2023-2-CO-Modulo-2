from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import FEATHER,PLUMA_TYPE

class Feather(PowerUp):
    def __init__(self):
        super().__init__(FEATHER, PLUMA_TYPE)