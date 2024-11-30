# PyChess

## Description
This is a Python-based Chess game where you can play in two modes:  
- **Player vs Player**: Two human players can play against each other.  
- **Player vs AI**: A human player can play against an AI opponent powered by the Minimax algorithm with Alpha-Beta Pruning.

## Features
- Graphical chessboard with intuitive piece movement.
- Valid move highlighting for better gameplay experience.
- Correct implementation of special moves like castling, en passant, and pawn promotion.
- Detection of check, checkmate, and stalemate conditions.
- Ability to undo moves and restart the game.

## Technologies Used
- **Python**: Core programming language.
- **Pygame**: Used for graphical interface and user interaction.
- **Minimax Algorithm**: Implements AI decision-making.
- **Alpha-Beta Pruning**: Optimizes the Minimax search for efficiency.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chess-ai-project.git
   cd chess-ai-project

2. Install the required dependencies:
   ```bash
   pip install game
   
3. Run the game:
   ```bash
   python main.py
   
## How to Play
- **Player vs Player**: Both players alternate turns by clicking on pieces and selecting valid moves.
- **Player vs AI**: Player 1 plays against the AI, which calculates its moves using the Minimax algorithm.

## Game Controls
- **Left Click**: Select and move pieces.
- **Right Click**: Deselect the current piece.
- **Esc**: Return to the main menu.
- **R**: Restart the game.
- **Z**: Undo the last move.

## Project Structure
chess/
- images/               # Chess piece images and board assets
- chessAI.py            # AI decision-making logic
- chessEngine.py        # Core game logic and rules
- Chessmain.py          # Alternative entry point for the game
- main.py               # Main game loop and event handling

## Future Enhancements (maybe)
- Add different AI difficulty levels.
- Implement a save/load game feature.
- Add sound effects for moves and captures.

## License
This project is licensed under the MIT License. See the **LICENSE** file for details.
## Contact
For inquiries or contributions, contact **Prince Parmar** at **parmar774623@gmail.com**.
  
