import pyglet

from version2.game.PhysicalObject import PhysicalObject
from version2.game.resources import bullet_image


class Bullet(PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(bullet_image, *args, **kwargs)

        # Bullet speed
        self.speed = 700

        # Schedule to die
        pyglet.clock.schedule_once(self.die, 0.5)

    def die(self, dt):
        """Set that a bullet dies"""
        self.dead = True
