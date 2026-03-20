from ursina import *
import board_game,rules_display,creators_display

button_holder, cloud1, cloud2, cloud3 = None, None, None, None

def update():
    if button_holder:
        button_holder.rotation_z = math.sin(time.time() * 1.2) * 3
    
    if cloud1:
        cloud1.x += 0.001
        cloud2.x += 0.0007
        cloud3.x += 0.0005

        if cloud1.x > 1.2: cloud1.x = -1.2
        if cloud2.x > 1.2: cloud2.x = -1.2
        if cloud3.x > 1.2: cloud3.x = -1.2


def clear_scene():
    global button_holder, cloud1, cloud2, cloud3
    button_holder, cloud1, cloud2, cloud3 = None, None, None, None
    for e in scene.entities[:]:
        if e is not camera and not isinstance(e, EditorCamera):
            destroy(e)

def back_to_menu():
        clear_scene()
        main_menu()



def main_menu():
    
    global button_holder,cloud1, cloud2, cloud3

    def start_game():
        clear_scene()
        board_game.board()
    def view_rules():
        clear_scene()
        rules_display.view_rules()
    def view_creators():
        clear_scene()
        creators_display.view_creators()
        
    button_holder = Entity(model = "quad",parent=camera.ui,scale=(1,0.9),texture = "textures/board2.0.png", position=(0, 0.06, 0))
    background = Entity(model = "quad",parent=camera.ui,scale=(2, 1),texture = "textures/menu_background.png", color=color.white, position=(0, 0, 2))
    play = Button(text="PLAY",font='VeraMono.ttf',texture="textures/play_button.png", parent=button_holder,text_color=color.white,position=(0.01, 0.1, -0.1), scale=(0.4, 0.2),color=color.white, highlight_color=color.brown,highlight_text_color=color.red,text_size=1.5,text_origin=(0,0), on_click = start_game)
    rules = Button(text="RULES",font='VeraMono.ttf',texture="textures/rules_button.png", parent=button_holder,text_color=color.white,position=(0.01, -0.05, -0.1), scale=(0.4, 0.2),color=color.white, highlight_color=color.brown,highlight_text_color=color.red,text_size=1.5,text_origin=(0,0.05), on_click = view_rules)
    creators = Button(text="CREATORS",font='VeraMono.ttf',texture="textures/credits_button.png", parent=button_holder,text_color=color.white,position=(0.01, -0.2, -0.1), scale=(0.4, 0.2),color=color.white, highlight_color=color.brown,highlight_text_color=color.red,text_size=1.5,text_origin=(0,0.05), on_click = view_creators)

    cloud1 = Entity(model="cube", parent=camera.ui, scale=(0.5, 0.3), texture="textures/cloud1.png", position=(-0.6, 0.3, 1))
    cloud2 = Entity(model="cube", parent=camera.ui, scale=(0.4, 0.25), texture="textures/cloud2.png", position=(0.5, 0.2, 1))
    cloud3 = Entity(model="cube", parent=camera.ui, scale=(0.6, 0.35), texture="textures/cloud3.png", position=(-0.3, 0.1, 1))




