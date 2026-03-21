import game_logic as gl
import ai

difficulty = int(input("Choose you difficulty level\n1. Easy\n2. Medium\n3. Hard\nResponse: "))

gl.board_init()
gl.display_board()

try:
    while not gl.game_over:
        gl.fetch_token_valid_moves(1, -1)
        gl.display_valid_moves()
        player_can_move = len(gl.valid) > 0

        if player_can_move:
            while True:
                print(f"\nYour turn (Black):")
                try:
                    move_input = input("Enter the position (row columns): ").split()

                    if len(move_input) != 2:
                        print("Please enter both row and column.")
                        continue
                    
                    rw, cl = map(int, move_input)
                    move_made = gl.make_move(rw - 1, cl - 1, 1)

                    if not move_made:
                        print("\nInvalid position! Please choose from the valid moves list.")

                    else:
                        gl.display_board()
                        break

                except ValueError:
                    print("Invalid input. Please enter numbers.")
        else:
            print("\nYou have no valid moves. Passing to AI...")

        # Ai's turn
        gl.fetch_token_valid_moves(-1, 1)
        ai_can_move = len(gl.valid) > 0

        if ai_can_move:
            print("\nAI's turn (White):")
            ai_move = ai.get_best_move(difficulty) 
            
            if ai_move:
                # print(ai_move)
                r, c = ai_move

                # print("Row: ", r, "Col: ", c)
                # gl.display_valid_moves()
                move_made = gl.make_move(r, c, -1)

                if move_made:
                    print(f"AI played at row {r + 1}, col {c + 1}")
                    gl.display_board()

                else:
                    print("\nAI has not made the move. Something went wrong...")

        else:
            print("\nAI has no valid moves. Passing to you...")

        if not player_can_move and not ai_can_move:
            gl.game_over = True

            print("\n" + "="*20)
            print("      GAME OVER")
            print("="*20)
            
            black_score = sum(row.count(1) for row in gl.board)
            white_score = sum(row.count(-1) for row in gl.board)
            
            print(f"Black (You): {black_score}")
            print(f"White (AI): {white_score}")
            
            if black_score > white_score:
                print("\nYou Win!")
            elif white_score > black_score:
                print("\nAI Wins!")
            else:
                print("\nIt's a Tie!")
            break

except Exception as e:
    print(f"\n\nAn unexpected error occurred: {e}")