import arcade


WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

arcade.draw_circle_filled(50, 50, 30, arcade.color.BLUE_GREEN)
arcade.draw_triangle_filled(75, 23, 45, 1, 5, 8, arcade.color.BLUE_BELL)
# End drawing
arcade.finish_render()
arcade.run()

