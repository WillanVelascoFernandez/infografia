from my_hello_arcade import draw_paint
import arcade


class Hola(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY)
        self.width = width
        self.height = height

    def on_draw(self):
        arcade.start_render()
        draw_paint(self.width, self.height)
        arcade.finish_render()


if __name__ == "__main__":
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "My Arcade Class"
    app = Hola(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.run()
