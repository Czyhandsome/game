import pyglet
from pip._vendor.urllib3.connectionpool import xrange

from version2.game import load
# Main game window
from version2.game.Player import Player

game_window = pyglet.window.Window(800, 600)

# Batch draw
main_batch = pyglet.graphics.Batch()

# Score label
score = 0
score_label = pyglet.text.Label(text="Score: 0",
                                x=10, y=575, batch=main_batch)


# Update score
def update_score(dt):
    global score
    score += 10
    score_label.text = "Score: {0}".format(score)


# Level label
level_label = pyglet.text.Label(text="My Amazon Game",
                                x=400, y=575, anchor_x='center', batch=main_batch)

# The player ship
player_ship = Player(x=400, y=300, batch=main_batch)

# Asteroids
asteroids = load.asteroids(3, player_ship.position, main_batch)

# All game objects
game_objects = [player_ship] + asteroids

# Number of asteroids
num_asteroids = 3
# Max number of asteroids
max_num_asteroids = 10


# Update all objects
def update(dt):
    # Collision detect
    for i in xrange(len(game_objects)):
        for j in xrange(i + 1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            if not obj_1.is_dead() and not obj_2.is_dead():
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    # Added game objects
    to_add = []

    # Update game_objects
    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []

    # Remove dead objects
    for to_remove in [obj for obj in game_objects if obj.is_dead()]:
        to_remove.delete()
        game_objects.remove(to_remove)
        if to_remove.name == 'Asteroid':
            # update_score(dt)
            global num_asteroids
            num_asteroids -= 1
        elif to_remove.name == 'Player Bullet':
            player_ship.remove_shoot()
        print(to_remove.name)

    # Add object
    game_objects.extend(to_add)


# 更新小行星
def update_asteroids(dt):
    # Add asteroid
    global num_asteroids
    if num_asteroids < max_num_asteroids:
        game_objects.extend(load.asteroids(1, player_ship.position, main_batch))
        num_asteroids += 1
    for p_object in game_objects:
        if p_object is not None and not p_object.is_dead() and p_object.name == 'Asteroid':
            p_object.speed_up(dt)


@game_window.event
def on_draw():
    # ----- Draw things here ----- #
    # Clear game window
    game_window.clear()

    # Batch draw
    main_batch.draw()


def auto_update_score(dt):
    if not player_ship.is_dead():
        update_score(dt)


if __name__ == '__main__':
    # Schedule the movement of all objects
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    # Schedule creation of asteroids
    pyglet.clock.schedule_interval(update_asteroids, 1)
    # Add 10 points every second
    pyglet.clock.schedule_interval(auto_update_score, 0.1)
    # Push player_ship into event stack
    game_window.push_handlers(player_ship.key_handler)
    game_window.push_handlers(player_ship)
    pyglet.app.run()
