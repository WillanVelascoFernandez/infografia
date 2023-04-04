import arcade
import math
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Lineas con bresenham"


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.px = SCREEN_WIDTH / 2
        self.py = SCREEN_HEIGHT / 2
        self.movement = 5
        self.points = []
        # self.radio_colision = 5
        self.score = 0

    def on_key_press(self, symbol: int, modifiers: int):
        """Metodopara detectar teclas que han sido presionadas"""
        """El punto se movera con las teclas de direccion
            symbol: tecla presionada
            modifiers: modificadores presionados
        """
        if symbol == arcade.key.UP:
            print("arriba")
            self.py += self.movement
        if symbol == arcade.key.DOWN:
            print("abajo")
            self.py -= self.movement
        if symbol == arcade.key.LEFT:
            print("izquierda")
            self.px -= self.movement
        if symbol == arcade.key.RIGHT:
            print("derecha")
            self.px += self.movement

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """Metodo para detectar clics del mouse
        En la posicion del click, se dibujara un nuevo punto
        Argumentos
        x: coordenada x del clic
        y: coordenada y del click
        button: boton del mouse presionado
        modifiers: teclas modificadoras presionadas (shift, ctrl, alt, etc)
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(f"Agregando punto a ({x}, {y})")
            self.points.append((x, y))

    def on_update(self, delta_time: float):
        """ Metodo para actualizar onjetos de la app"""
        # print(f"{1/delta_time}")
        colision = self.player_is_on_food()
        if self.player_is_on_food() != -1:
            print(
                f"Ñam, Ñam, Score: {self.score}")
            self.points.pop(colision)
            self.score += 1

    def player_is_on_food(self):
        """Funcion que detecta si eljugador ha colisionado con un punto
        Devuelve el indice del punto en la lista self.points si existe una colision
        Si no existela colision, devuelve el valor de -1
        self.points= = [
        0:    (3, 4)
        1:    (6, 7)
        2:    (18, 20)
        ]
        jugador colisiona con punto (6, 7): retornar 1
        jugador no colisiona con ningun punto: retornar -1
        """

        for i, point in enumerate(self.points):
            # Calcula la distancia euclidiana entre el punto del jugador y el punto en la lista
            # distance = math.sqrt((point[0] - self.px) ** 2 + (point[1] - self.py) ** 2)

            if abs(self.px - point[0]) <= 5 and abs(self.py - point[1]) <= 5:

                return i

        return -1

    def on_draw(self):
        """Metodo para dibujar en la pantalla"""
        arcade.start_render()
        arcade.draw_point(self.px, self.py, arcade.color.RED, 5)
        if self.points:
            arcade.draw_points(self.points, arcade.color.GREEN, 5)

        arcade.draw_text("Come todos los puntos verdes!",
                         0,
                         670,
                         arcade.color.YELLOW,
                         15,
                         width=SCREEN_WIDTH,
                         align="center"
                         )
        arcade.draw_text(f"Score: {self.score}",
                         0,
                         35,
                         arcade.color.YELLOW,
                         15,
                         width=SCREEN_WIDTH,
                         align="right"
                         )


if __name__ == "__main__":
    app = App()
    arcade.run()
