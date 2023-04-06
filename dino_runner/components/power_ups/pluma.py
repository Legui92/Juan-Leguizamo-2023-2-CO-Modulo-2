from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import PLUMA,PLUMA_TYPE

class Pluma(PowerUp):
    def __init__(self):
        super().__init__(PLUMA, PLUMA_TYPE)