rows = columns = 8

board = []

# Initialize an empty board
def board_init():
    for _ in range(rows):
        new_row = []

        for _ in range(columns):
            new_row.append(0)

        board.append(new_row)

    board[3][3] = board[4][4] = -1
    board[3][4] = board[4][3] = 1

def display_board():
    print('-' * 33)

    for i in range(rows):
        print(f"|", end="")

        for j in range(columns):
            if board[i][j] == 0:        # Empty
                print(f"   |", end="")

            elif board[i][j] == 1:      # Human (Black)
                print(f" B |", end="")

            elif board[i][j] == -1:     # AI (White)
                print(f" W |", end="")

        print()
        print('-' * 33)

# board_init()
# display_board()

valid = []

def top_valid(rn, cn, op):
    if rn > 1:
        if board[rn - 1][cn] == op:
            valid.append([(rn - 2), cn])

def bottom_valid(rn, cn, op):
    if rn < 6:
        if board[rn + 1][cn] == op:
            valid.append([(rn + 2), cn])

def left_valid(rn, cn, op):
    if cn > 1:
        if board[rn][cn - 1] == op:
            valid.append([rn, (cn - 2)])

def right_valid(rn, cn, op):
    if cn < 6:
        if board[rn][cn + 1] == op:
            valid.append([rn, (cn + 2)])

def top_left_valid(rn, cn, op):
    if rn > 1 and cn > 1:
        if board[rn - 1][cn - 1] == op:
            valid.append([(rn - 2), (cn - 2)])

def top_right_valid(rn, cn, op):
    if rn > 1 and cn < 6:
        if board[rn - 1][cn + 1] == op:
            valid.append([(rn - 2), (cn + 2)])

def bottom_left_valid(rn, cn, op):
    if rn < 6 and cn > 2:
        if board[rn + 1][cn - 1] == op:
            valid.append([(rn + 2), (cn - 2)])

def bottom_right_valid(rn, cn, op):
    if rn < 6 and cn < 6:
        if board[rn + 1][cn + 1] == op:
            valid.append([(rn + 2), (cn + 2)])

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
    valid.clear()

    for i in range(rows):
        for j in range(columns):
            if board[i][j] == playing_token:
                generate_valid_moves(i, j, opponent_token)

    print(f"\nValid moves: {valid}")

def make_move(r, c, token):
    if r < 8 and c < 8 and board[r][c] == 0:
        board[r][c] = token

        return True

    return False