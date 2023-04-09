import arcade


class Player:
    def __init__(self, center_x, center_y, width, height, color=arcade.color.GREEN):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.tilt_angle = 0
        self.color = color
        self.score = 0
        self.movement = 5

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color, self.tilt_angle)
