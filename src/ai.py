import game_logic as gl
import random
import copy

# Heuristics
CORNER_WEIGHT = 100
EDGE_WEIGHT = 10  
PIECE_WEIGHT = 1

def evaluate_board():
    score = 0
  
    corners = [(0,0), (0,7), (7,0), (7,7)]

    for r, c in corners:
        if gl.board[r][c] == 1: 
            score -= CORNER_WEIGHT
            
        elif gl.board[r][c] == -1: 
            score += CORNER_WEIGHT
    
    black = sum(row.count(1) for row in gl.board)
    white = sum(row.count(-1) for row in gl.board)

    score += (white - black) * PIECE_WEIGHT

    return score

def get_all_valid_moves(player):
    gl.fetch_token_valid_moves(player, -player)
    return [m[:] for m in gl.valid]

    return [m[:] for m in gl.valid]

def minimax(depth, alpha, beta, maximizing):
    current_player = -1 if maximizing else 1

    valid_moves = get_all_valid_moves(current_player)
    
    if depth == 0 or not valid_moves:
        return evaluate_board()
    
    original_board = copy.deepcopy(gl.board)
    
    if maximizing:
        max_eval = float('-inf')

        for move in valid_moves:
            r, c = move[0]-1, move[1]-1
            gl.make_move(r, c, -1)

            eval_score = minimax(depth-1, alpha, beta, False)

            gl.board = copy.deepcopy(original_board)
            
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)

            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = float('inf')

        for move in valid_moves:
            r, c = move[0]-1, move[1]-1
            gl.make_move(r, c, 1)

            eval_score = minimax(depth-1, alpha, beta, True)

            gl.board = copy.deepcopy(original_board)
            
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)

            if beta <= alpha:
                break

        return min_eval

def get_best_move(difficulty):
    valid_moves = get_all_valid_moves(-1)
    
    if not valid_moves:
        return None
    
    if difficulty == 1:
        if random.random() < 0.5:
            move = random.choice(valid_moves)
            return (move[0]-1, move[1]-1)

        depth = 2

    elif difficulty == 2:
        depth = 3

    else:
        depth = 4
    
    best_score = float('-inf')
    best_move = None
    original_board = copy.deepcopy(gl.board)

    for move in valid_moves:
        r, c = move[0]-1, move[1]-1
        gl.make_move(r, c, -1)

        board_score = minimax(depth-1, float('-inf'), float('inf'), False)

        gl.board = copy.deepcopy(original_board)
        
        if board_score > best_score:
            best_score = board_score
            best_move = (r, c)
            
    gl.fetch_token_valid_moves(-1, 1)
    
    return best_move