from Strecke import Strecke


class LidarScanner:
    angleResolution = 0.5

    FOV = 270.0

    maxRange = 75.0

    Map = [Strecke([-20, 20], [20, 20]),
           Strecke([20, 20], [20, -20]),
           Strecke([20, -20], [-20, -20]),
           Strecke([-20, -20], [-20, 20])]

    def __init__(self, angleResolution, FOV, maxRange):
        self.angleResolution = angleResolution
        self.FOV = FOV
        self.maxRange = maxRange
