import math


def getRotatedUnitVector(a):
    einheitsVector: list[int] = [1, 0]
    Vector = [
        math.cos(a) * einheitsVector[0] - math.sin(a * einheitsVector[1]),
        math.sin(a) * einheitsVector[0] + math.cos(a) * einheitsVector[1]]
    return Vector


def getRotatedVector(vector, a):
    startVector: list[int] = vector
    Vector = [
        math.cos(a) * startVector[0] - math.sin(a * startVector[1]),
        math.sin(a) * startVector[0] + math.cos(a) * startVector[1]]
    return Vector


def addVectors(a, b):
    Vector = [a[0] + b[0], a[1] + b[1]]
    return Vector

def normalize(vector):
    len = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])
    return [vector[0] / len,vector[1] / len]