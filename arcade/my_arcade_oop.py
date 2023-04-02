from my_hello_arcade import draw_paint
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 825
SCREEN_TITLE = "My Arcade Class"


class Hola(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        arcade.start_render()
        draw_paint(SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.finish_render()


if __name__ == "__main__":

    app = Hola()
    app.run()
