import numpy

import Calc
from Strecke import Strecke
import math
import pygame
from Calc import *


class LidarScanner:
    angleResolution = math.pi / 32

    FOV = math.pi / 2

    maxRange = 75.0

    Distances = []

    Points = [[1, 1]]

    IntersectionPoints = [[1, 1]]

    Map = [Strecke([400, 800], [800, 800]),
           Strecke([800, 800], [800, 400]),
           Strecke([800, 400], [400, 400]),
           Strecke([400, 400], [400, 800]),
           Strecke([100, 99], [1100, 700])]

    def __init__(self, angleResolution, FOV, maxRange):
        self.angleResolution = angleResolution
        self.FOV = FOV
        self.maxRange = maxRange

    def intersectionPoint(self, x1, y1, x2, y2, x3, y3, x4, y4):
        """ Return the point where the lines through (x1,y1)-(x2,y2)
            and (x3,y3)-(x4,y4) cross.  This may not be on-screen  """
        # Use determinant method, as per
        # Ref: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        try:
            Px = ((((x1 * y2) - (y1 * x2)) * (x3 - x4)) - ((x1 - x2) * ((x3 * y4) - (y3 * x4)))) / (
                    ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
            Py = ((((x1 * y2) - (y1 * x2)) * (y3 - y4)) - ((y1 - y2) * ((x3 * y4) - (y3 * x4)))) / (
                    ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
            return Px, Py
        except:
            print("parallel")
            return 0, 0

    def getDistance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    def scan(self, carPos, rotation):
        self.Points.clear()
        self.Distances.clear()
        self.IntersectionPoints.clear()
        # global SX
        for i in range(0, int(self.FOV / self.angleResolution)):
            CurrentIntersections = [[1, 1]]
            CurrentIntersections.clear()
            a = (-self.FOV / 2) + (i * self.angleResolution)
            Vector = getRotatedVector([10000, 0], a + rotation)
            Point = addVectors(Vector, carPos)
            self.Points.append(Point)
            for Strecke in self.Map:
                SX, SY = self.intersectionPoint(carPos[0], carPos[1], Point[0], Point[1], Strecke.A[0], Strecke.A[1],
                                                Strecke.B[0], Strecke.B[1])
                ConvexA = [0, 0]
                ConvexB = [0, 0]
                if Strecke.A[0] < Strecke.B[0]:
                    ConvexA[0] = Strecke.A[0] - 1
                    ConvexB[0] = Strecke.B[0] + 1
                else:
                    ConvexA[0] = Strecke.B[0] - 1
                    ConvexB[0] = Strecke.A[0] + 1
                if Strecke.A[1] < Strecke.B[1]:
                    ConvexA[1] = Strecke.A[1] - 1
                    ConvexB[1] = Strecke.B[1] + 1
                else:
                    ConvexA[1] = Strecke.B[1] - 1
                    ConvexB[1] = Strecke.A[1] + 1
                isOnLine = SX > ConvexA[0] and SX < ConvexB[0] and SY > ConvexA[1] and SY < ConvexB[1]
                if isOnLine:
                    self.Distances.append(self.getDistance(carPos[0], carPos[1], SX, SY))

                    if round(numpy.dot(Calc.normalize(Vector), Calc.normalize([carPos[0] - SX, carPos[1] - SY])),
                             6) != 1:
                        CurrentIntersections.append([SX, SY])
            if len(CurrentIntersections) > 0:
                minPoint = CurrentIntersections[0]
                for Point in CurrentIntersections:
                    if (self.getDistance(carPos[0], carPos[1], Point[0], Point[1]) < self.getDistance(carPos[0],
                                                                                                      carPos[1],
                                                                                                      minPoint[0],
                                                                                                      minPoint[1])):
                        minPoint[0] = Point[0]
                        minPoint[1] = Point[1]
                self.IntersectionPoints.append(minPoint)
        return self.Distances
        #print(self.Distances)
