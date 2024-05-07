import pygame
import sys
import math
from Car import Car
import time
from Calc import *

# define constants
height = 1200
width = 1700
fps = 30
running = 1
lastScan = 0
scanDelay = 0.1
allMeasurements = [[-1, -1]]

pygame.init()

screen = pygame.display.set_mode((width, height))
car = Car([width / 2, height / 2], 0)
clock = pygame.time.Clock()


def draw_rectangle(x, y, w, h, color, rotation):
    points = []

    # The distance from the center of the rectangle to
    # one of the corners is the same for each corner.
    radius = math.sqrt((h / 2) ** 2 + (w / 2) ** 2)

    # Get the angle to one of the corners with respect
    # to the x-axis.
    angle = math.atan2(h / 2, w / 2)

    # Transform that angle to reach each corner of the rectangle.
    angles = [angle, -angle + math.pi, angle + math.pi, -angle]

    # Convert rotation from degrees to radians.
    rot_radians = (math.pi / 180) * rotation

    # Calculate the coordinates of each point.
    for angle in angles:
        y_offset = -1 * radius * math.sin(angle + rot_radians)
        x_offset = radius * math.cos(angle + rot_radians)
        points.append((x + x_offset, y + y_offset))

    pygame.draw.polygon(screen, color, points)


# game loop
while running:
    clock.tick(fps)
    # clear the screen every time before drawing new objects
    screen.fill((0, 0, 0))
    # game event loop

    # Quitting Programm
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit(0)

    # movement
    if pygame.key.get_pressed()[pygame.key.key_code("RETURN")]:
        if (lastScan + scanDelay) < time.time():
            car.lidarScanner.scan(car.carPos, -car.rotation)
            allMeasurements = allMeasurements + car.lidarScanner.IntersectionPoints
            lastScan = time.time()

    if pygame.key.get_pressed()[pygame.key.key_code("W")]:
        car.carPos = addVectors(car.carPos, getRotatedVector([5, 0], -car.rotation))

    if pygame.key.get_pressed()[pygame.key.key_code("S")]:
        car.carPos = addVectors(car.carPos, getRotatedVector([-5, 0], -car.rotation))

    if pygame.key.get_pressed()[pygame.key.key_code("A")]:
        car.rotation += math.pi / 40

    if pygame.key.get_pressed()[pygame.key.key_code("D")]:
        car.rotation -= math.pi / 40

    # draw to the Screen

    pygame.draw.circle(screen, (100, 100, 100), (car.carPos[0], car.carPos[1]), 2)
    pygame.draw.line(screen, (255, 255, 255), car.carPos,
                     addVectors(getRotatedVector([30, 0], -car.rotation), car.carPos))
    for Strecke in car.lidarScanner.Map:
        pygame.draw.line(screen, (4, 4, 4), Strecke.A, Strecke.B)
    draw_rectangle(car.carPos[0], car.carPos[1], car.width, car.height, (255, 0, 0), math.degrees(car.rotation))
    for Point1 in allMeasurements:
        pygame.draw.circle(screen, (255, 100, 100), (Point1[0], Point1[1]), 2)
    #for Point2 in car.lidarScanner.IntersectionPoints:
        #pygame.draw.circle(screen, (255, 100, 100), (Point2[0], Point2[1]), 2)
    pygame.display.flip()
pygame.quit()
