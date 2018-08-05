import math
import random
from typing import List

from pyglet.sprite import Sprite

from version1.game.resources import *
from version2.game.PhysicalObject import PhysicalObject


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def asteroids(num_asteroids, player_location, batch=None) -> List[Sprite]:
    """
    Initialize a number of randomly located asteroids
    :param num_asteroids
    :param player_location:
    :param batch:
    """
    _asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_location
        while distance((asteroid_x, asteroid_y), player_location) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = PhysicalObject(img=asteroid_image,
                                      x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        # Init the velocity
        new_asteroid.velocity_x = random.random() * 40
        new_asteroid.velocity_y = random.random() * 40
        _asteroids.append(new_asteroid)
    return _asteroids


def player_lives(num_icons, batch=None):
    """
    Show player lives
    :param num_icons
    :param batch
    """
    _lives = []
    for i in range(num_icons):
        new_sprite = Sprite(img=player_image,
                            x=785 - i * 30, y=585,
                            batch=batch)
        new_sprite.scale = 0.5
        _lives.append(new_sprite)
    return _lives


def new_bullet(name, rotation, width, x, y, velocity_x, velocity_y, speed, batch):
    """
    Create a new bullet
    :param velocity_x:
    :param velocity_y:
    :param name:
    :param rotation:
    :param width:
    :param x:
    :param y:
    :param speed:
    :param batch:
    :return:
    """
    angle_radians = -math.radians(rotation)
    ship_radius = width
    bullet_x = x + math.cos(angle_radians) * ship_radius
    bullet_y = y + math.sin(angle_radians) * ship_radius
    from version2.game.Bullet import Bullet
    _new_bullet = Bullet(bullet_x, bullet_y, batch=batch)
    _new_bullet.name = name
    _new_bullet.speed = speed
    bullet_vx = (
            velocity_x +
            math.cos(angle_radians) * _new_bullet.speed
    )
    bullet_vy = (
            velocity_y +
            math.sin(angle_radians) * _new_bullet.speed
    )
    _new_bullet.velocity_x = bullet_vx
    _new_bullet.velocity_y = bullet_vy
    return _new_bullet
