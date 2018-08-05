import math
import random

from pyglet.sprite import Sprite, pyglet

from version2.game import load
from version2.game.util import distance


class PhysicalObject(Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        # Name property
        self.name = 'Asteroid'

        # Dead property
        self.__dead = False

        # Added objects
        self.new_objects = []

        # Velocity
        self.thrust = 40
        self.angle_radians = random.randint(0, 360)
        self.velocity_x = 0
        self.velocity_y = 0

        if self.name == 'Asteroid' and not self.is_dead():
            # Shoot bullet
            # pyglet.clock.schedule_interval(self._inner_shoot, 1)
            # Die
            pyglet.clock.schedule_once(self._self_destroy, 10)

    def _inner_shoot(self, dt):
        if self.name == 'Asteroid':
            self.shoot_bullet(100)

    def shoot_bullet(self, speed):
        if self.image:
            new_bullet = load.new_bullet(self.name + " Bullet",
                                         self.rotation,
                                         self.image.width / 2,
                                         self.x,
                                         self.y,
                                         self.velocity_x,
                                         self.velocity_y,
                                         speed,
                                         self.batch)
            self.new_objects.append(new_bullet)

    def _self_destroy(self, dt):
        self.die()

    def update(self, dt):
        """Update the object's position"""
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.check_bounds()

    def speed_up(self, dt):
        if self.thrust <= 2000:
            self.thrust += 40
        self._set_velocity(dt)

    def _set_velocity(self, dt):
        force_x = math.cos(self.angle_radians) * self.thrust * dt
        force_y = math.sin(self.angle_radians) * self.thrust * dt
        self.velocity_x = force_x
        self.velocity_y = force_y

    def collides_with(self, other_object: 'PhysicalObject'):
        """
        Detect if collides with other object
        :param other_object:
        :return:
        """
        collision_distance = self.image.width / 2 + other_object.image.width / 2
        actual_distance = distance(
            self.position, other_object.position)
        return actual_distance <= collision_distance

    def handle_collision_with(self, other_object: 'PhysicalObject'):
        """
        Things to do when collides with other object
        :param other_object:
        :return:
        """
        if not (self.is_dead() or other_object.is_dead()):
            if self.name != other_object.name:
                if self.name == 'Asteroid Bullet' and other_object.name == 'Player':
                    other_object.die()
                elif self.name == 'Player Bullet' and other_object.name == 'Asteroid':
                    other_object.die()
                elif self.name == 'Player' and \
                        (other_object.name == 'Asteroid' or other_object.name == 'Asteroid Bullet'):
                    self.die()
                elif self.name == 'Asteroid':
                    if other_object.name == 'Player Bullet':
                        self.die()
                    elif other_object.name == 'Player':
                        other_object.die()

    def die(self):
        self.__dead = True

    def is_dead(self):
        return self.__dead

    def check_bounds(self):
        """
        Check if the object reaches the bounds.
        If it does, move it the the opposite site
        of the window.
        """
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y
