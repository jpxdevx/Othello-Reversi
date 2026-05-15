# Technical Design Document: Othello AI

## Architecture Overview
The project is split into three main modules to separate concerns:
1. **Game Logic (`game_logic.py`)**: The "Engine." Handles board state, move validation, and flipping mechanics.
2. **AI Engine (`ai.py`)**: The "Brain." Implements decision-making algorithms based on difficulty.
3. **Interfaces**: 
   - `main.py`: Command-line interface for testing.
   - `board_game.py`: 3D GUI powered by the Ursina Engine.

## Core Algorithms

### 1. Radial Flip Logic (The "Lighthouse" Algorithm)
Instead of scanning the whole board, the game uses a radial search from the placement coordinates $(x, y)$. It scans in 8 directions:
- **Cardinal:** Up, Down, Left, Right
- **Diagonal:** Top-Left, Top-Right, Bottom-Left, Bottom-Right

**Boundary Math:** To prevent index errors, boundaries are strictly set at $[1, 7]$. A flip is only triggered if the scan finds an opponent token followed by a "capping" player token within these bounds.

### 2. AI Strategy: Minimax Algorithm
The AI evaluates potential moves by simulating future board states. 
- **Easy:** Randomly selects from valid moves.
- **Medium/Hard:** Uses a Minimax depth search to maximize the player's score.
  
$$Score = \sum (\text{Player Tokens}) - \sum (\text{Opponent Tokens})$$

## Known Challenges & Solutions
- **Global State Collision:** During AI simulation, the global `valid_moves` list was being overwritten. This was resolved by re-fetching valid moves in the main loop immediately before a move is finalized to ensure "Reality" matches the current board state.

- **Passive Sandwich Rule:** The engine is designed to only flip tokens directly outflanked by the *current* move. Subsequent "accidental" sandwiches are not flipped, adhering to official Othello rules.