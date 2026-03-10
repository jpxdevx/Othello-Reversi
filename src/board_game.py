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

def board():
    # Borders
    top    = Entity(model='cube', scale=(grid + border*2, border, 1), position=(0,  offset, 0), color=color.black)
    bottom = Entity(model='cube', scale=(grid + border*2, border, 1), position=(0, -offset, 0), color=color.black)
    left   = Entity(model='cube', scale=(border, grid, 1),position=(-offset, 0, 0), color=color.black)
    right  = Entity(model='cube', scale=(border, grid, 1),position=( offset, 0, 0), color=color.black)

    # Main board
    Entity(model='cube', scale=(grid, grid, 0.2), position=(0, 0, 0), color=rgb(0, 128, 0))
    thick_lines = 0
    # Vertical and horizontal lines
    for i in range(-4, 5):
        thick_lines += 1
        if thick_lines == 3 or thick_lines == 7:  # thicker lines at 3 and 6
            Entity(model='cube', scale=(line_thickness*1.5, grid, 0.1), position=(i * tile, 0, -0.11), color=color.black)
        else:
            Entity(model='cube', scale=(line_thickness, grid, 0.1), position=(i * tile, 0, -0.11), color=color.black)
    thick_lines = 0
    for i in range(-4, 5):
        thick_lines += 1
        if thick_lines == 3 or thick_lines == 7:  # thicker lines at 3 and 6
            Entity(model='cube', scale=(grid, line_thickness*1.5, 0.1), position=(0, i * tile, -0.11), color=color.black)
        else:
             Entity(model='cube', scale=(grid, line_thickness, 0.1), position=(0, i * tile, -0.11), color=color.black)

    # Dots
    dot_positions = [(-2*tile, 2*tile), (-2*tile, -2*tile), (2*tile, 2*tile), (2*tile, -2*tile)]
    for pos in dot_positions:
        Entity(model=Cylinder(resolution = 64), scale=(0.3,0.2,0.3), position=(pos[0], pos[1], -0.2), color=color.black).rotation_x = 90  
    
    #center pieces --> permanent
    Entity(model=Cylinder(resolution = 64), scale=(0.9,0.3,0.9), position=(0.5,0.5,-0.3), color=color.black).rotation_x = 90
    Entity(model=Cylinder(resolution = 64), scale=(0.9,0.3,0.9), position=(-0.5,-0.5,-0.3), color=color.black).rotation_x = 90
    Entity(model=Cylinder(resolution = 64), scale=(0.9,0.3,0.9), position=(0.5,-0.5,-0.3), color=color.gray).rotation_x = 90
    Entity(model=Cylinder(resolution = 64), scale=(0.9,0.3,0.9), position=(-0.5,0.5,-0.3), color=color.gray).rotation_x = 90

    


def draw_piece(x, y, color):
    Entity(model=Cylinder(resolution = 64), scale=(0.9,0.3,0.9), position=(x*tile, y*tile, -0.3), color=color).rotation_x = 90 
  
def main():
    show_menu = True
    if show_menu:
        show_menu = menu.main_menu(show_menu)
    else:
        board()
    camera.position = (0, -15, -15)
    camera.rotation = (-45, 0, 0)
    camera.fov = 45
    app.run() 

if __name__ == "__main__":
    main()