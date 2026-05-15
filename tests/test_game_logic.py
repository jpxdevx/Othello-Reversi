import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import game_logic as gl # type: ignore

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        gl.board_init()

# Verify if initial pieces are correct
    def test_initial_setup(self):
        self.assertEqual(gl.board[3][3], -1)
        self.assertEqual(gl.board[4][4], -1)
        self.assertEqual(gl.board[3][4], 1)
        self.assertEqual(gl.board[4][3], 1)

# Check valid moves generation
    def test_valid_move_logic(self):
        gl.fetch_token_valid_moves(1, -1) # Black's turn
        expected_moves = [[3, 4], [4, 3], [5, 6], [6,5]]

        for move in expected_moves:
            self.assertIn(move, gl.valid)

    def test_edge_boundary_flip(self):
        gl.board[1][4] = -1 # White at Row 2, Col 5
        gl.board[2][4] = 1  # Black at Row 3, Col 5
        gl.fetch_token_valid_moves(1, -1)
        
        gl.make_move(0, 4, 1)
        
        self.assertEqual(gl.board[1][4], 1, "Edge flip failed!")

if __name__ == '__main__':
    unittest.main()