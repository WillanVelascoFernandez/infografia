import arcade
from pared import Pared
from pelota import Pelota
from player import Player

# definicion de constantes
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pin Pon"


class TransformWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pared_arriba = None
        self.pared_abajo = None
        self.pared_izquierda = None
        self.pared_derecha = None
        self.pelota = None
        self.player1 = None
        self.player2 = None
        self.keys_pressed = set()

    def setup(self):
        self.pared_arriba = Pared(50, SCREEN_HEIGHT-80,
                                  SCREEN_WIDTH-50, SCREEN_HEIGHT-80)
        self.pared_abajo = Pared(50, 50, SCREEN_WIDTH-50, 50)

        self.pared_izquierda = Pared(
            50, 50, 50, SCREEN_HEIGHT-80, arcade.color.BLUE)
        self.pared_derecha = Pared(SCREEN_WIDTH-50, 50,
                                   SCREEN_WIDTH-50, SCREEN_HEIGHT-80, arcade.color.BLUE)
        self.pelota = Pelota(SCREEN_WIDTH/2,
                             ((SCREEN_HEIGHT-80)+50)/2, 15, 5)
        self.player1 = Player(80, ((SCREEN_HEIGHT-80)+50)/2, 30, 100)
        self.player2 = Player(
            SCREEN_WIDTH-80, ((SCREEN_HEIGHT-80)+50)/2, 30, 100)

    def on_draw(self):
        arcade.start_render()
        self.pared_arriba.draw()
        self.pared_abajo.draw()
        self.pared_izquierda.draw()
        self.pared_derecha.draw()
        self.pelota.draw()
        self.player1.draw()
        self.player2.draw()
        arcade.draw_text(f"{self.player1.score}/{self.player2.score}",
                         0,
                         SCREEN_HEIGHT-40,
                         arcade.color.YELLOW,
                         15,
                         width=SCREEN_WIDTH,
                         align="center"
                         )
        arcade.finish_render()

    def update(self, delta_time):

        if arcade.key.W in self.keys_pressed:
            self.player1.center_y += self.player1.movement
        elif arcade.key.S in self.keys_pressed:
            self.player1.center_y -= self.player1.movement
        if arcade.key.UP in self.keys_pressed:
            self.player2.center_y += self.player2.movement
        elif arcade.key.DOWN in self.keys_pressed:
            self.player2.center_y -= self.player2.movement

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)


def main():

    app = TransformWindow()
    app.setup()
    arcade.run()


if __name__ == "__main__":
    main()
