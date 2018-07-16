import pyglet

from version1.game import resources, load

# Main game window
game_window = pyglet.window.Window(800, 600)

# Score label
score_label = pyglet.text.Label(text="Score: 0",
                                x=10, y=575)
# Level label
level_label = pyglet.text.Label(text="My Amazon Game",
                                x=400, y=575, anchor_x='center')

# The player ship
player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)

# Asteroids
asteroids = load.asteroids(3, player_ship.position)


@game_window.event
def on_draw():
    # ----- Draw things here ----- #
    # Clear game and draw labels
    game_window.clear()
    level_label.draw()
    score_label.draw()

    # draw player ship
    player_ship.draw()

    # Draw asteroids
    for asteroid in asteroids:
        asteroid.draw()


if __name__ == '__main__':
    pyglet.app.run()
