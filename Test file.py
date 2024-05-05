import math

a = math.pi*4

rotation = 0

einheitsVector = [1, 0]

Vector = [
    math.cos(a + math.radians(rotation)) * einheitsVector[0] - math.sin(a + math.radians(rotation) * einheitsVector[1]),
    math.sin(a + math.radians(rotation)) * einheitsVector[0] + math.cos(a + math.radians(rotation)) * einheitsVector[1]]
print(Vector)