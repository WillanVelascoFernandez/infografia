import random
import arcade
from pared import Pared
from pelota import Pelota
from player import Player

# definicion de constantes
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ping Pong Retro"


class TransformWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.sprites = None
        self.paredes = None
        self.pelotas = None
        self.goals = None
        self.players = None
        self.keys_pressed = set()

    def setup(self):
        self.sprites = arcade.SpriteList()
        self.pelotas = arcade.SpriteList()
        self.paredes = arcade.SpriteList()
        self.goals = arcade.SpriteList()
        self.players = arcade.SpriteList()

        pared_arriba = Pared(SCREEN_WIDTH-100, 5, arcade.color.RED,
                             (SCREEN_WIDTH/2), (SCREEN_HEIGHT - 80))
        self.paredes.append(pared_arriba)
        self.sprites.append(pared_arriba)

        pared_abajo = Pared(SCREEN_WIDTH-100, 5,
                            arcade.color.RED, (SCREEN_WIDTH/2), (50))
        self.paredes.append(pared_abajo)
        self.sprites.append(pared_abajo)

        goal_izquierda = Pared(
            5, (SCREEN_HEIGHT-80-50), arcade.color.BLUE, (50), (((SCREEN_HEIGHT-80)+50)/2))
        self.goals.append(goal_izquierda)
        self.sprites.append(goal_izquierda)

        goal_derecha = Pared(5, (SCREEN_HEIGHT-80-50), arcade.color.BLUE,
                             (SCREEN_WIDTH-50), (((SCREEN_HEIGHT-80)+50)/2))
        self.goals.append(goal_derecha)
        self.sprites.append(goal_derecha)

        pelota = Pelota("sprites/disco.png", 0.08, SCREEN_WIDTH/2,
                        ((SCREEN_HEIGHT-80)+50)/2)
        self.pelotas.append(pelota)
        self.sprites.append(pelota)

        player1 = Player(30, 100, arcade.color.GREEN,
                         80, (((SCREEN_HEIGHT-80)+50)/2))
        self.players.append(player1)
        self.sprites.append(player1)

        player2 = Player(30, 100, arcade.color.GREEN,
                         (SCREEN_WIDTH-80), (((SCREEN_HEIGHT-80)+50)/2))
        self.players.append(player2)
        self.sprites.append(player2)

        # self.player1 = Player(80, ((SCREEN_HEIGHT-80)+50)/2, 30, 100)
        # self.player2 = Player(
        #     SCREEN_WIDTH-80, ((SCREEN_HEIGHT-80)+50)/2, 30, 100)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"{0}/{0}",
                         0,
                         SCREEN_HEIGHT-40,
                         arcade.color.YELLOW,
                         15,
                         width=SCREEN_WIDTH,
                         align="center"
                         )
        self.sprites.draw()
        arcade.finish_render()

    def update(self, delta_time):
        self.sprites.update()

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
