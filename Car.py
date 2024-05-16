from LidarScanner import LidarScanner
import math
import Calc


class Car:
    carPos = [0, 0]  # gets overwritten in constructor
    carSpeed = [0, 0]
    carAccel = [0, 0]

    rotation = 0.0  # gets overwritten in constructor

    width = 40
    height = 40
    lidarScanner = LidarScanner(math.radians(1), math.radians(180), 75.0)

    def __init__(self, carPos, rotation):
        self.carPos = carPos
        self.rotation = rotation

    def updatePos(self, dt):
        frictionFactor = 0.01
        frictionAbs = Calc.getDist(self.carSpeed)
        if frictionAbs != 0:
            frictionVector = Calc.normalize(self.carSpeed)
            self.carAccel = Calc.addVectors(self.carAccel, Calc.multVec(frictionVector, -frictionAbs**2 * frictionFactor))
        self.carSpeed = Calc.addVectors(self.carSpeed, Calc.multVec(self.carAccel, dt / 1000))
        self.carPos = Calc.addVectors(self.carPos, Calc.multVec(self.carSpeed, dt / 1000))
        print(dt)
