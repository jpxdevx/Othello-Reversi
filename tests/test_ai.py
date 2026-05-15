import unittest

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import ai # type: ignore
import game_logic as gl #type: ignore

class TestAI(unittest.TestCase):
    def setUp(self):
        gl.board_init()

# AI should choose from the valid move only
    def test_ai_makes_legal_move(self):
        gl.fetch_token_valid_moves(-1, 1)
        move = ai.get_best_move(1)

        [x, y] = move
        move = [x + 1, y + 1]
        
        # None return check
        self.assertIsNotNone(move, "AI returned None when moves were available.")
        self.assertIn(move, gl.valid, f"AI tried to play {move}, which is ILLEGAL.")

# AI return no moves when board is full
    def test_ai_handles_no_moves(self):
        # Fill board with black
        gl.board = [[1 for _ in range(8)] for _ in range(8)]

        gl.fetch_token_valid_moves(-1, 1)
        move = ai.get_best_move(1)

        self.assertIsNone(move, "AI should return None when no moves are possible.")

if __name__ == '__main__':
    unittest.main()