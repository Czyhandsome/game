import pyglet


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Define resource path
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

# Load resources and set as center
player_image = pyglet.resource.image("player.png")
center_image(player_image)
bullet_image = pyglet.resource.image("bullet.png")
center_image(bullet_image)
asteroid_image = pyglet.resource.image("asteroid.png")
center_image(asteroid_image)

# Load flame file and set position
engine_image = pyglet.resource.image("engine_flame.png")
engine_image.anchor_x = engine_image.width * 1.5
engine_image.anchor_y = engine_image.height / 2
