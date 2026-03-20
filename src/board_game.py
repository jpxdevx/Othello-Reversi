from ursina import *
import menu
app = Ursina()

DirectionalLight(rotation=(45, -45), shadows=True)
AmbientLight(color=color.rgba(80, 80, 80, 0.5))
border = 0.2
grid = 8.0
half = grid / 2   # 4.0
offset = half + border / 2  # 4.1
tile = grid / 8   #1 for 64 tiles
line_thickness = 0.05
tile_buttons = {}

def update():
    menu.update()

def board():
    
    back_button = Button(text="Back", parent=camera.ui, position=(-0.45, 0.4, -0.1), scale=(0.1, 0.05), color=color.orange, highlight_color=color.red, text_size=2.4, on_click=menu.back_to_menu)
    # Borders
    board_container = Entity()
    top    = Entity(parent = board_container,model='cube', scale=(grid + border*2, border, 1), position=(0,  offset, 0),texture="textures/board_texture.jpg", texture_scale=(grid + border*2, border))
    bottom = Entity(parent = board_container,model='cube', scale=(grid + border*2, border, 1), position=(0, -offset, 0),texture="textures/board_texture.jpg", texture_scale=(grid + border*2, border))
    left   = Entity(parent = board_container,model='cube', scale=(border, grid, 1),position=(-offset, 0, 0),texture="textures/board_texture.jpg", texture_scale=(border, grid))
    right  = Entity(parent = board_container,model='cube', scale=(border, grid, 1),position=( offset, 0, 0),texture="textures/board_texture.jpg", texture_scale=(border, grid))

    # Main board
    Entity(parent = board_container,model='cube', scale=(grid, grid, 0.2), position=(0, 0, 0), color=rgb(0, 128, 0))
    thick_lines = 0
    # Vertical and horizontal lines
    for i in range(-4, 5):
        thick_lines += 1
        if thick_lines == 3 or thick_lines == 7:  # thicker lines at 3 and 6
            Entity(parent = board_container,model='cube', scale=(line_thickness*1.5, grid, 0.1), position=(i * tile, 0, -0.11), color=color.black)
        else:
            Entity(parent = board_container,model='cube', scale=(line_thickness, grid, 0.1), position=(i * tile, 0, -0.11), color=color.black)
    thick_lines = 0
    for i in range(-4, 5):
        thick_lines += 1
        if thick_lines == 3 or thick_lines == 7:  # thicker lines at 3 and 6
            Entity(parent = board_container,model='cube', scale=(grid, line_thickness*1.5, 0.1), position=(0, i * tile, -0.11), color=color.black)
        else:
             Entity(parent = board_container,model='cube', scale=(grid, line_thickness, 0.1), position=(0, i * tile, -0.11), color=color.black)

    # Dots
    dot_positions = [(-2*tile, 2*tile), (-2*tile, -2*tile), (2*tile, 2*tile), (2*tile, -2*tile)]
    for pos in dot_positions:
        Entity(parent = board_container,model=Cylinder(resolution = 64), scale=(0.3,0.2,0.3), position=(pos[0], pos[1], -0.2), color=color.black).rotation_x = 90  
    
    #center pieces --> permanent
    Entity(parent = board_container,model=Cylinder(resolution = 64), scale=(0.85,0.3,0.85), position=(0.5,0.5,-0.3), color=color.black).rotation_x = 90
    Entity(parent = board_container,model=Cylinder(resolution = 64), scale=(0.85,0.3,0.85), position=(-0.5,-0.5,-0.3), color=color.black).rotation_x = 90
    Entity(parent = board_container,model=Cylinder(resolution = 64), scale=(0.85,0.3,0.85), position=(0.5,-0.5,-0.3), color=color.gray).rotation_x = 90
    Entity(parent = board_container,model=Cylinder(resolution = 64), scale=(0.8,0.3,0.85), position=(-0.5,0.5,-0.3), color=color.gray).rotation_x = 90


    #buttons for the posibilities of placing pieces
    for x in range(-4, 4):
        for y in range(-4, 4):
            if (x, y) in [(-1,-1),(-1,0),(0,-1),(0,0)]:
                continue
        
            cx, cy = x, y
            btn = Button(parent=board_container,model=Cylinder(resolution=64),scale=(0.85, 0.3, 0.85),position=((x + 0.5)*tile, (y + 0.5)*tile, -0.3),color=color.clear,highlight_color=color.light_gray,rotation_x = 90,on_click=lambda cx=cx, cy=cy: draw_piece(cx, cy, color.black))
        
            tile_buttons[(x, y)] = btn


    def draw_piece(x, y, color):
        if (x, y) in tile_buttons:
            tile_buttons[(x, y)].enabled = False
        Entity(parent = board_container,model=Cylinder(resolution = 64), scale=(0.85,0.3,0.85), position=((x + 0.5)*tile, (y + 0.5)*tile, -0.3), color=color).rotation_x = 90 
    
  
def main():
    EditorCamera()
    camera.position = (0, -20, 10)
    camera.rotation = (-45, 0, 0)
    camera.fov = 35
    menu.main_menu()

    app.run() 


if __name__ == "__main__":
    main()