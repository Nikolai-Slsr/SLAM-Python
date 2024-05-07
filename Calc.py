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
    return [vector[0] / len, vector[1] / len]


def arrayMatch(Array1, Array2):
    Score = 0
    if Array1.length() == Array2.length():
        for index in range(0, Array1.length()):
            max_diff = max(abs(Array1[index]), abs(Array2[index]))
            if max_diff == 0:
                Score += 1.0
            else:
                Score += 1.0 - (abs(Array1[index] - Array2[index]) / max_diff)
        return Score / Array1.length()
    else:
        return -1
