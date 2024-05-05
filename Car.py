from LidarScanner import LidarScanner
import math

class Car:
    carPos = [0, 0]  # gets overwritten in constructor

    rotation = 0.0  # gets overwritten in constructor

    width = 40
    height = 40
    lidarScanner = LidarScanner(math.pi / 32, math.pi , 75.0)

    def __init__(self, carPos, rotation):
        self.carPos = carPos
        self.rotation = rotation

