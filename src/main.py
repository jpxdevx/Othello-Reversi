import game_logic as gl

import random

gl.board_init()
gl.display_board()

try:
    while True:
        while True:
            # User's turn

            gl.display_valid_moves(1, -1)

            print(f"\nYour turn:")
            rw, cl = map(int, input("Enter the position (row, columns): ").split())
            move_made = gl.make_move(rw - 1, cl - 1, 1)

            if not move_made:
                print("\nInvalid position!")

            else:
                gl.display_board()
                break

        while True:
            print(f"\nAI's turn:")
            # AI's turn
            rw = random.randint(0, 8)
            cl = random.randint(0, 8)
            move_made = gl.make_move(rw - 1, cl - 1, -1)

            if not move_made:
                print("\nInvalid position!")
                continue

            else:
                gl.display_board()
                break

except ValueError:
    print(f"\n\nSomething went wrong...")