import math

from pyglet.sprite import Sprite
from pyglet.window import key

from version2.game.PhysicalObject import PhysicalObject
from version2.game.resources import player_image, engine_image


class Player(PhysicalObject):
    """
    Player class
    """

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=player_image, *args, **kwargs)

        # Name
        self.name = 'Player'

        # Bullets
        self._num_bullets = 0

        # Thrust & rotate speed
        self.thrust = 20000.0
        self.rotate_speed = 200.0

        # Flame image
        self.engine_sprite = Sprite(img=engine_image, *args, **kwargs)
        self.engine_sprite.visible = False

        # Obtain key state handler
        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        """
        Override super update method
        :param dt:
        :return:
        """
        super(Player, self).update(dt)
        # ----- Rotate ----- #
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        # ----- Forward or backward ----- #
        if self.key_handler[key.UP]:
            self.__run(dt)
        elif self.key_handler[key.DOWN]:
            self.__run(-dt)
        else:
            self.__stop()

        # ----- Speed up and slow down ----- #
        if self.key_handler[key.J]:
            self.__speed_up()
        if self.key_handler[key.K]:
            self.__slow_down()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self._do_shoot_bullet()

    def _do_shoot_bullet(self):
        if self.can_shoot():
            self.shoot_bullet(700)
            self.add_shoot()

    def __run(self, dt):
        """
        Speed up
        """
        # 正方向定义不同，加负号
        angle_radians = -math.radians(self.rotation)
        force_x = math.cos(angle_radians) * self.thrust * dt
        force_y = math.sin(angle_radians) * self.thrust * dt
        self.velocity_x = force_x
        self.velocity_y = force_y
        # Ignite engine flame
        self.__ignite_engine_flame()

    def __stop(self):
        self.velocity_x = 0
        self.velocity_y = 0
        # Ignite engine flame
        self.__stop_engine_flame()

    def __speed_up(self):
        self.thrust += 4000

    def __slow_down(self):
        """
        Slow down
        """
        self.thrust -= 4000
        if self.thrust <= 2000:
            self.thrust = 2000

    def __ignite_engine_flame(self):
        self.engine_sprite.visible = True
        self.engine_sprite.rotation = self.rotation
        self.engine_sprite.x = self.x
        self.engine_sprite.y = self.y

    def __stop_engine_flame(self):
        self.engine_sprite.visible = False

    def can_shoot(self):
        return self._num_bullets <= 1

    def add_shoot(self):
        self._num_bullets += 1

    def remove_shoot(self):
        self._num_bullets -= 1

    def delete(self):
        """
        Operations when destroyed
        :return:
        """
        self.engine_sprite.delete()
        super(Player, self).delete()
