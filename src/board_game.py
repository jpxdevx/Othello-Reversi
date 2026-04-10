from ursina import *
import menu,game_logic,ai
app = Ursina()
difficulty = 1
DirectionalLight(rotation=(45, -45), shadows=True)
AmbientLight(color=color.rgba(80, 80, 80, 0.5))
border = 0.2
grid = 8.0
half = grid / 2   # 4.0
offset = half + border / 2  # 4.1
tile = grid / 8   #1 for 64 tiles
line_thickness = 0.05
tile_buttons = {}
pieces = {}
player_turn = True
total_delay = 0

def update():
    menu.update()

def to_board_coords(x, y):
    col = x + 4
    row = 3 - y
    return row, col

def to_3d_coords(row, col):
    x = col - 4
    y = 3 - row
    return x, y

def invalid():
    invalid = "Invalid position!"
    des = Text(invalid, parent=camera.ui, position=(0, 0.4), origin=(0, 0), color=color.red, scale=2,font='VeraMono.ttf')
    des.animate('color', color.rgba(1, 0, 0, 0), duration=2)
    destroy(des, delay=2)

def no_moves():
    no_moves = "No Valid Moves Available!"
    des = Text(no_moves, parent=camera.ui, position=(0, 0.4), origin=(0, 0), color=color.red, scale=2,font='VeraMono.ttf')
    des.animate('color', color.rgba(1, 0, 0, 0), duration=2)
    destroy(des, delay=2)

def board():

    game_logic.board_init()
    game_logic.fetch_token_valid_moves(1, -1)

    def show_game_over():
        black_score = sum(row.count(1) for row in game_logic.board)
        white_score = sum(row.count(-1) for row in game_logic.board)
        display = Button(disabled=True,position=(0,0,-1.5),scale=(0.3,0.2))
        if black_score > white_score:
            result = f"You Win!\n{Entity(model="circle",parent=display,color=color.black, position=(-0.25,0,-2),scale=(0.2,0.2))}   {Entity(model="circle",parent=display,color=color.white,position=(0.25,0,-2),scale=(0.2,0.2))}\n{black_score} - {white_score}"
            col = color.green
        elif white_score > black_score:
            result = f"AI Wins!\n{Entity(model="circle",parent=display,color=color.black,position=(-0.25,0,-2),scale=(0.2,0.2))}   {Entity(model = "circle",parent=display,color=color.white,position=(0.25,0,-2),scale=(0.2,0.2))}\n{black_score} - {white_score}"
            col = color.red
        else:
            result = f"Tie!\n{Entity(model = "circle",parent=display,color=color.black,position=(-0.25,0,-2),scale=(0.2,0.2))}   {Entity(model = "circle",parent=display,color=color.white,position=(0.25,0,-2),scale=(0.2,0.2))}\n{black_score} - {white_score}"
            col = color.yellow

        
        Text(result, parent=camera.ui, position=(0, 0,-2),origin=(0, 0), color=col, scale=2, font='VeraMono.ttf')

    #AI to play
    def AI_turn():
        global player_turn, total_delay
        player_turn = False
        game_logic.fetch_token_valid_moves(-1,1)
        if not game_logic.valid:
            no_moves()
            game_logic.fetch_token_valid_moves(1,-1)
            if not game_logic.valid:
                # player has no moves either
                game_logic.game_over = True
                show_game_over()
            else:
                player_turn = True
            return
        
        old_board = [r[:] for r in game_logic.board]
        ai_move = ai.get_best_move(difficulty)

        if ai_move:
            r,c = ai_move
            game_logic.make_move(r,c,-1)

            #for 3d board
            ux,uy = to_3d_coords(r,c)
            place_piece(ux,uy,color.gray)
            flip_pieces(old_board,(ux,uy))
        #i want to add a delay before the player's turn
        player_turn = True
        #checking for players move 
        game_logic.fetch_token_valid_moves(1, -1)
        if not game_logic.valid:
            no_moves()
            #AI has no moves either
            game_logic.fetch_token_valid_moves(-1, 1)
            if not game_logic.valid:
                game_logic.game_over = True
                show_game_over()
            else:
                player_turn = False
                invoke(AI_turn,delay=0.5)

    def handle_player_move(x, y):

        global player_turn, total_delay

        if game_logic.game_over or player_turn == False:
            return
        #handle the players move
        row,col = to_board_coords(x, y)
        old_board = [row[:] for row in game_logic.board]
        move_made = game_logic.make_move(row, col, 1)

        if not move_made:
            invalid()
            return
        player_turn = False
        place_piece(x, y, color.black)
        animation_dur = flip_pieces(old_board, (x, y))

        game_logic.fetch_token_valid_moves(-1, 1)

        if not game_logic.valid:
            no_moves()

            #check if player also has no moves
            game_logic.fetch_token_valid_moves(1, -1)

            if not game_logic.valid:
                game_logic.game_over = True
                show_game_over()
            return
        
        #adding a 0.8 sec pause for the Ai to start
        total_delay = animation_dur + 0.8
        invoke(AI_turn,delay = total_delay)

    def animate_flip(entity, to_black, delay=0):
        #animate flip
        if not hasattr(entity, 'flip_count'):
            entity.flip_count = 0
        entity.flip_count += 1
        z_correction = -0.15 if entity.flip_count % 2 == 0 else 0.15
        target = entity.rotation_x + 180 
        old_pos = entity.z + z_correction
        entity.animate('rotation_x', target, duration=0.4, delay=delay, curve=curve.in_out_sine)
        entity.is_black = to_black
        entity.animate('z',old_pos, duration=0.4, delay=delay)
        

    def flip_pieces(old_board,placed):
        #for the pieces that needs flipping
        flip_count = 0
        for r in range(8):
            for c in range(8):
                if game_logic.board[r][c] != old_board[r][c]:
                    x, y = to_3d_coords(r, c)
                    if (x,y) == placed:
                        continue
                    if (x, y) in pieces:
                        to_black = game_logic.board[r][c] == 1
                        
                        animate_flip(pieces[(x, y)], to_black , delay=flip_count * 0.15)
                        flip_count += 1
        
        if flip_count == 0:
            return 0
        
        #last piece starts flipping at (flip_count - 1) * 0.15
        #it takes 0.4 seconds to finish its rotation       
        total_time = ((flip_count - 1)* 0.15) + 0.4
        return total_time


    def place_piece(x, y, starting_color):
        pivot = Entity(parent=board_container,position=((x + 0.5)*tile, (y + 0.5)*tile, -0.3))
        p = Entity(parent=pivot,scale=(0.85, 0.3, 0.85),rotation_x=90)  
        p.origin = (0,0,0)
        #top half and bottom half - swap colors based on starting color
        if starting_color == color.black:
            top_col = color.black
            bot_col = color.rgb(230,230,230)
        else:
            top_col = color.rgb(230,230,230)
            bot_col = color.black

        top = Entity(parent=p, model=Cylinder(resolution=64), scale=(1, 0.5, 1), color=top_col,y=-0.25)
        bot = Entity(parent=p, model=Cylinder(resolution=64), scale=(1, 0.5, 1), color=bot_col,y=0.25)
    
        p.top = top
        p.bot = bot
        p.is_black = (starting_color == color.black)
        
        pieces[(x, y)] = pivot
        if (x, y) in tile_buttons:
            tile_buttons[(x, y)].enabled = False
    
    
    back_button = Button(text="Back", parent=camera.ui, position=(-0.45, 0.4, -0.1), scale=(0.1, 0.05), color=color.orange, highlight_color=color.red, text_size=2.4, on_click=menu.back_to_menu)
    # Borders
    board_container = Entity()
    top    = Entity(parent = board_container,model='cube', scale=(grid + border*2, border, 1), position=(0,  offset, 0),texture="textures/board_texture.jpg", texture_scale=(grid + border*2, border))
    bottom = Entity(parent = board_container,model='cube', scale=(grid + border*2, border, 1), position=(0, -offset, 0),texture="textures/board_texture.jpg", texture_scale=(grid + border*2, border))
    left   = Entity(parent = board_container,model='cube', scale=(border, grid, 1),position=(-offset, 0, 0),texture="textures/board_texture.jpg", texture_scale=(border, grid))
    right  = Entity(parent = board_container,model='cube', scale=(border, grid, 1),position=( offset, 0, 0),texture="textures/board_texture.jpg", texture_scale=(border, grid))

    # Main board
    Entity(parent = board_container,model='cube', scale=(grid, grid, 0.2), position=(0, 0, 0), color="#1F6040")
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
    center_pieces = [((0, 0),color.black), ((0, -1),color.gray), ((-1, 0),color.gray), ((-1, -1),color.black)]
    for pos, col in center_pieces:
        place_piece(pos[0], pos[1], col)

    #buttons for the posibilities of placing pieces
    for x in range(-4, 4):
        for y in range(-4, 4):
            if (x, y) in [(-1,-1),(-1,0),(0,-1),(0,0)]:
                continue
        
            cx, cy = x, y
            btn = Button(parent=board_container,model=Cylinder(resolution=64),scale=(0.85, 0.3, 0.85),position=((x + 0.5)*tile, (y + 0.5)*tile, -0.3),color=color.clear,highlight_color=color.light_gray,rotation_x = 90,on_click=lambda cx=cx, cy=cy: handle_player_move(cx, cy))
        
            tile_buttons[(x, y)] = btn

    
def main():
    EditorCamera()
    camera.position = (0, -20, 10)
    camera.rotation = (-45, 0, 0)
    camera.fov = 35
    menu.main_menu()

    app.run() 


if __name__ == "__main__":
    main()