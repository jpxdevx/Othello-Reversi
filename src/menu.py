import board_game
from ursina import *

def main_menu():
    button_holder = Entity(model="quad",scale = (0.8, 0.6),color = color.rgba(255, 255, 255),texture = "textures/menu_box_texture.png",parent = camera.ui)
    def start_game():
        destroy(button_holder)
        board_game.board()
    start = Button(text="Start", parent=button_holder,text_color=color.black,position=(0, 0.3, -0.1), scale=(0.5, 0.2), color=color.orange, highlight_color=color.red,text_size=2.4, on_click = start_game)

