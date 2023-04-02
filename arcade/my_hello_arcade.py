import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "My paint"

RED = arcade.color.RED
ORANGE_RED = arcade.color.ORANGE_RED
YELLOW_ORANGE = arcade.color.YELLOW_ORANGE


def draw_paint(screen__width, screen__height):
    count = 0
    center_x = 50
    center_y = 25
    width = 100
    height = 50
    direction = 0
    while True:
        if (count == 0):
            count = 1
            arcade.draw_rectangle_filled(
                center_x, center_y, width, height, RED)
        elif (count == 1):
            count = 2
            arcade.draw_rectangle_filled(
                center_x, center_y, width, height, ORANGE_RED)
        elif (count == 2):
            count = 0
            arcade.draw_rectangle_filled(
                center_x, center_y, width, height, YELLOW_ORANGE)

        if (direction == 0):
            center_y += 50

        if (direction == 1):
            center_y -= 50

        if (center_x >= screen__width+100):
            break

        if (center_y > screen__height+25 or center_y <= -25):
            if direction == 0:
                direction = 1
            elif direction == 1:
                direction = 0
            center_x += 100


if __name__ == "__main__":

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()

    draw_paint(SCREEN_HEIGHT, SCREEN_WIDTH)

    arcade.finish_render()
    arcade.run()
