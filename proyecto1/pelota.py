import arcade


class Pelota(arcade.Sprite):
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale, center_x=center_x, center_y=center_y)
        self.speed = 0

    def update(self):
        ...

    def movimiento(self):
        ...
