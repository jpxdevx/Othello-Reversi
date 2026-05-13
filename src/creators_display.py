from ursina import *
import menu
def view_creators():

    menu.play_menu_music()
    creators_container = Entity(parent=camera.ui)
    Entity(parent=creators_container, model="quad", scale=(1.8, 1), texture="textures/creator_background.jpg", position=(0, 0, 1))

    Text("About Us", parent=creators_container, position=(-0.1, 0.38, 0),scale=2.2, color=color.orange, font='VeraMono.ttf')
    Entity(parent=creators_container, model="quad", scale=(0.65, 0.005),color=color.orange, position=(0, 0.33, 0))

    image_box1 = Entity(texture="textures/John.jpeg",model="quad",parent=creators_container,position=(-0.3,0.05,0),scale=(0.4,0.45),color=color.white)
    image_box2 = Entity(texture="textures/Koushik.jpeg",model="quad",parent=creators_container,position=(0.3,0.05,0),scale=(0.4,0.45),color=color.white)
    name1 = "John Paul Fernandes"
    name2 = "Koushik Sharma"
    Text(name1,color=color.rgb(255,255,255),parent=creators_container,position=(-0.45,-0.2,0),font='VeraMono.ttf')
    Text(name2,color=color.rgb(255,255,255),parent=creators_container,position=(0.2,-0.2,0),font='VeraMono.ttf')
    back_button = Button(texture="textures/back.png", parent=camera.ui, position=(-0.8, 0.44, -0.1), scale=(0.07, 0.07), color=color.white, text_size=2.4, on_click=menu.back_to_menu)