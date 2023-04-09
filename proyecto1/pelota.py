import arcade


class Pelota:
    def __init__(self, center_x, center_y, radius, border_width, color=arcade.color.WHITE):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.border_width = border_width
        self.tilt_angle = 0
        self.num_segments = -1
        self.color = color

    def draw(self):
        arcade.draw_circle_outline(self.center_x, self.center_y, self.radius,
                                   self.color, self.border_width, self.tilt_angle, self.num_segments)
