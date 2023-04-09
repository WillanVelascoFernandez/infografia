import arcade


class Pared:
    def __init__(self, start_x, start_y, end_x, end_y, color=arcade.color.RED):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.color = color
        self.line_width = 4

    def draw(self):
        arcade.draw_line(self.start_x, self.start_y,
                         self.end_x, self.end_y, self.color, self.line_width)
