import random
import math
from PIL import Image
import numpy as np
import skimage as ski 


class Particle:
    def __init__(self):
        self.turn = 0
        self.position = [random.randint(0, 500), random.randint(0, 500)]

        self.color = random.choice([
            [86, 71, 86],
            [80, 124, 186],
            [90, 204, 160],
            [229, 247, 210]
        ])
        self.direction = random.choice([
            "UP",
            "DOWN",
            "LEFT",
            "RIGHT"
        ])

    def change_direction(self):
        self.direction = random.choice([
            "UP",
            "DOWN",
            "LEFT",
            "RIGHT"
        ])

#cat = ski.data.chelsea()
size = (500, 500)

img = 255 * np.ones((size[0],size[1],3), np.uint8)

particles = [Particle() for _ in range(500)]

for _ in range(1000):
    for particle in particles:
        particle.turn += 1
        if particle.direction == "UP":
            particle.position[1] -= 1
        elif particle.direction == "DOWN":
            particle.position[1] += 1
        elif particle.direction == "LEFT":
            particle.position[0] -= 1 
        elif particle.direction == "RIGHT":
            particle.position[0] += 1

        if particle.turn % 2 == 0:
            particle.change_direction()

        if particle.position[0] < 500 and particle.position[1] >= 0:
            if particle.position[1] < 500 and particle.position[1] >= 0:
                img[particle.position[0], particle.position[1]] = particle.color

Image.fromarray(img).save("file.jpg");
