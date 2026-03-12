rows = columns = 8
game_over = False

board = []

def board_init():
    global board, game_over
    board = []

    for _ in range(rows):
        new_row = []

        for _ in range(columns):
            new_row.append(0)

        board.append(new_row)

    board[3][3] = board[4][4] = -1
    board[3][4] = board[4][3] = 1

    game_over = False

def display_board():
    print('-' * 33)

    for i in range(rows):
        print(f"|", end="")
        
        for j in range(columns):
            if board[i][j] == 0:
                print(f"   |", end="")

            elif board[i][j] == 1: 
                print(f" B |", end="")

            elif board[i][j] == -1:   
                print(f" W |", end="")

        print()
        print('-' * 33)

valid = []

def top_valid(rn, cn, op):
    if rn > 1:
        x = rn - 1
        y = cn

        while x >= 0 and board[x][y] == op:
            x -= 1

        if x >= 0 and board[x][y] == 0 and x < rn - 1:
            valid.append([x + 1, y + 1])

def bottom_valid(rn, cn, op):
    if rn < 6:
        x = rn + 1
        y = cn

        while x < 8 and board[x][y] == op:
            x += 1

        if x < 8 and board[x][y] == 0 and x > rn + 1:
            valid.append([x + 1, y + 1])

def left_valid(rn, cn, op):
    if cn > 1:
        x = rn
        y = cn - 1
        
        while y >= 0 and board[x][y] == op:
            y -= 1

        if y >= 0 and board[x][y] == 0 and y < cn - 1:
            valid.append([x + 1, y + 1])

def right_valid(rn, cn, op):
    if cn < 6:
        x = rn
        y = cn + 1

        while y < 8 and board[x][y] == op:
            y += 1

        if y < 8 and board[x][y] == 0 and y > cn + 1:
            valid.append([x + 1, y + 1])

def top_left_valid(rn, cn, op):
    if rn > 1 and cn > 1:
        x = rn - 1
        y = cn - 1
        
        while x >= 0 and y >= 0 and board[x][y] == op:
            x -= 1
            y -= 1

        if x >= 0 and y >= 0 and board[x][y] == 0 and x < rn - 1:
            valid.append([x + 1, y + 1])

def top_right_valid(rn, cn, op):
    if rn > 1 and cn < 6:
        x = rn - 1
        y = cn + 1

        while x >= 0 and y < 8 and board[x][y] == op:
            x -= 1
            y += 1

        if x >= 0 and y < 8 and board[x][y] == 0 and x < rn - 1:
            valid.append([x + 1, y + 1])

def bottom_left_valid(rn, cn, op):
    if rn < 6 and cn > 1:
        x = rn + 1
        y = cn - 1

        while x < 8 and y >= 0 and board[x][y] == op:
            x += 1
            y -= 1

        if x < 8 and y >= 0 and board[x][y] == 0 and x > rn + 1:
            valid.append([x + 1, y + 1])

def bottom_right_valid(rn, cn, op):
    if rn < 6 and cn < 6:
        x = rn + 1
        y = cn + 1

        while x < 8 and y < 8 and board[x][y] == op:
            x += 1
            y += 1

        if x < 8 and y < 8 and board[x][y] == 0 and x > rn + 1:
            valid.append([x + 1, y + 1])

def generate_valid_moves(rownum, colnum, opponent):
    top_valid(rownum, colnum, opponent)
    bottom_valid(rownum, colnum, opponent)

    left_valid(rownum, colnum, opponent)
    right_valid(rownum, colnum, opponent)

    top_left_valid(rownum, colnum, opponent)
    top_right_valid(rownum, colnum, opponent)
    
    bottom_left_valid(rownum, colnum, opponent)
    bottom_right_valid(rownum, colnum, opponent)

def display_valid_moves(playing_token, opponent_token):
    global game_over
    valid.clear()

    for i in range(rows):
        for j in range(columns):
            if board[i][j] == playing_token:
                generate_valid_moves(i, j, opponent_token)
    
    unique_valid = []

    for move in valid:
        if move not in unique_valid:
            unique_valid.append(move)
            
    valid[:] = unique_valid
    
    print(f"\nValid moves: {valid}")

    if not valid:
        pass 

def flip_top(rw, col, tkn, opponent):
    if rw > 1:
        x = rw - 1

        while x >= 0 and board[x][col] == opponent:
            x -= 1

        if x >= 0 and board[x][col] == tkn and x < rw - 1:
            for i in range(x + 1, rw):
                board[i][col] = tkn

def flip_bottom(rw, col, tkn, opponent):
    if rw < 6:
        x = rw + 1

        while x < 8 and board[x][col] == opponent:
            x += 1

        if x < 8 and board[x][col] == tkn and x > rw + 1:
            for i in range(rw + 1, x):
                board[i][col] = tkn

def flip_right(rw, col, tkn, opponent):
    if col < 6:
        y = col + 1

        while y < 8 and board[rw][y] == opponent:
            y += 1

        if y < 8 and board[rw][y] == tkn and y > col + 1:
            for i in range(col + 1, y):
                board[rw][i] = tkn

def flip_left(rw, col, tkn, opponent):
    if col > 1:
        y = col - 1

        while y >= 0 and board[rw][y] == opponent:
            y -= 1

        if y >= 0 and board[rw][y] == tkn and y < col - 1:
            for i in range(y + 1, col):
                board[rw][i] = tkn

def flip_left_top(rw, col, tkn, opponent):
    if rw > 1 and col > 1:
        x, y = rw - 1, col - 1

        while x >= 0 and y >= 0 and board[x][y] == opponent:
            x, y = x - 1, y - 1

        if x >= 0 and y >= 0 and board[x][y] == tkn and x < rw - 1:
            curr_x, curr_y = x + 1, y + 1

            while curr_x < rw:
                board[curr_x][curr_y] = tkn

                curr_x += 1
                curr_y += 1

def flip_right_top(rw, col, tkn, opponent):
    if rw > 1 and col < 7:
        x, y = rw - 1, col + 1

        while x >= 0 and y < 8 and board[x][y] == opponent:
            x, y = x - 1, y + 1

        if x >= 0 and y < 8 and board[x][y] == tkn and x < rw - 1:
            curr_x, curr_y = x + 1, y - 1

            while curr_x < rw:
                board[curr_x][curr_y] = tkn

                curr_x += 1
                curr_y -= 1

def flip_bottom_left(rw, col, tkn, opponent):
    if rw < 6 and col > 1:
        x, y = rw + 1, col - 1
        
        while x < 8 and y >= 0 and board[x][y] == opponent:
            x, y = x + 1, y - 1

        if x < 8 and y >= 0 and board[x][y] == tkn and x > rw + 1:
            curr_x, curr_y = x - 1, y + 1

            while curr_x > rw:
                board[curr_x][curr_y] = tkn
            
                curr_x -= 1
                curr_y -= 1

def flip_bottom_right(rw, col, tkn, opponent):
    if rw < 6 and col < 6:
        x, y = rw + 1, col + 1

        while x < 8 and y < 8 and board[x][y] == opponent:
            x, y = x + 1, y + 1

        if x < 8 and y < 8 and board[x][y] == tkn and x > rw + 1:
            curr_x, curr_y = x - 1, y - 1

            while curr_x > rw:
                board[curr_x][curr_y] = tkn

                curr_x -= 1
                curr_y -= 1

def flip_pieces(fr, fc, ftkn):
    opp = -ftkn

    flip_top(fr, fc, ftkn, opp)
    flip_bottom(fr, fc, ftkn, opp)

    flip_right(fr, fc, ftkn, opp)
    flip_left(fr, fc, ftkn, opp)

    flip_left_top(fr, fc, ftkn, opp)
    flip_right_top(fr, fc, ftkn, opp)

    flip_bottom_left(fr, fc, ftkn, opp)
    flip_bottom_right(fr, fc, ftkn, opp)

def make_move(r, c, token):
    if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == 0:
        for move in valid:
            if [r + 1, c + 1] == move:
                board[r][c] = token
                flip_pieces(r, c, token)
                
                return True
    return False