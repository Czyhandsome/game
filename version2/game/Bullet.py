import pyglet

from version2.game.PhysicalObject import PhysicalObject
from version2.game.resources import bullet_image


class Bullet(PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(bullet_image, *args, **kwargs)

        # Name
        self.name = 'Bullet'

        # Bullet speed
        self.speed = 700

        # Schedule to die
        pyglet.clock.schedule_once(self.__disappear, 0.5)

    def __disappear(self, dt):
        """Set that a bullet dies"""
        self.die()
