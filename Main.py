import pygame
import math
from Car import Car

# define constants
height = 1000
width = 1000
fps = 60
running = 1

pygame.init()
screen = pygame.display.set_mode((width, height))
car = Car([width / 2, height / 2], 45)
clock = pygame.time.Clock()


def draw_rectangle(x, y, width, height, color, rotation):
    points = []

    # The distance from the center of the rectangle to
    # one of the corners is the same for each corner.
    radius = math.sqrt((height / 2) ** 2 + (width / 2) ** 2)

    # Get the angle to one of the corners with respect
    # to the x-axis.
    angle = math.atan2(height / 2, width / 2)

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Quitting...")


    # movement
    def rotatedVector():
        cos = math.cos(car.rotation)
        sin = math.sin(car.rotation)
        return [cos - sin, sin + cos]


    if pygame.key.get_pressed()[pygame.key.key_code("W")]:
        car.carPos[1] += -2

    if pygame.key.get_pressed()[pygame.key.key_code("S")]:
        car.carPos[1] += 2

    if pygame.key.get_pressed()[pygame.key.key_code("A")]:
        car.carPos[0] += -2

    if pygame.key.get_pressed()[pygame.key.key_code("D")]:
        car.carPos[0] += 2

    if pygame.key.get_pressed()[pygame.key.key_code("Q")]:
        car.rotation += 2

    if pygame.key.get_pressed()[pygame.key.key_code("E")]:
        car.rotation -= 2

    draw_rectangle(car.carPos[0], car.carPos[1], car.width, car.height, (255, 0, 0), car.rotation)
    pygame.draw.circle(screen, (100, 100, 100), (car.carPos[0], car.carPos[1]), 2)
    print(car.rotation)
    pygame.display.flip()
pygame.quit()
