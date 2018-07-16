import math
import random
from typing import List

from pyglet.sprite import Sprite

from version1.game.resources import asteroid_image


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def asteroids(num_asteroids, player_location) -> List[Sprite]:
    """
    Initialize a number of randomly located asteroids
    :param num_asteroids
    :param player_location:
    """
    _asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_location
        while distance((asteroid_x, asteroid_y), player_location) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = Sprite(img=asteroid_image,
                              x=asteroid_x, y=asteroid_y)
        new_asteroid.rotation = random.randint(0, 360)
        _asteroids.append(new_asteroid)
    return _asteroids
