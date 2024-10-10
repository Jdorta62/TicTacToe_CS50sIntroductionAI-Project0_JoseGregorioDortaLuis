# Tic-Tac-Toe_CS50sIntroductionAI-Project1_JoseGregorioDortaLuis

## Objective
In this project, you will build an AI for playing Tic-Tac-Toe. The goal is to create an optimal AI that can play the game of Tic-Tac-Toe flawlessly, using a decision-making process based on the **minimax** algorithm. The AI should never lose and will try to either win or draw in every game.

## Key Concepts
- **Minimax Algorithm**: A recursive algorithm used to choose the best move in a game, by simulating all possible future moves of the opponent and the player. It assumes that both players play optimally.
- **Game Tree**: Represents all possible moves and outcomes of the game in a tree-like structure.
- **Maximizer and Minimizer**: In Tic-Tac-Toe, one player (the AI) tries to maximize its chances of winning, while the opponent tries to minimize the AI's chances.

## Steps
1. **Download** the [distribution code](https://cdn.cs50.net/ai/2023/x/projects/0/tictactoe.zip) and extract the data.
2. **Core Files**:
   - `tictactoe.py`: This is where you will implement the game and AI logic.
   - `runner.py`: A script to run the game and interact with your AI.
   
3. **Main Task**: Implement the `minimax` function in `tictactoe.py`:
   - **Initial Setup**: Implement functions to handle game logic like checking the current board state, possible actions, and determining the game outcome.
   - **Minimax**: Implement the minimax algorithm to choose the best move for the AI based on the current game state. The algorithm should evaluate all possible future moves, assume optimal play, and return the best possible action for the AI.
   
4. **Minimax Implementation**:
   - Use recursion to simulate future moves.
   - Maximize the AI’s score while minimizing the opponent’s.
   - Implement terminal state checking to end recursion when the game is over (win, loss, or draw).

## Implementation Details
- You will need to implement the following functions in `tictactoe.py`:
   - `initial_state`: Returns the initial state of the game (an empty 3x3 board).
   - `player`: Returns which player has the next turn (X or O).
   - `actions`: Returns all possible actions (available cells) for the current board.
   - `result`: Returns the resulting board after a move.
   - `winner`: Returns the winner of the game, if there is one.
   - `terminal`: Checks if the game is over (win or draw).
   - `utility`: Returns the utility value of a terminal state (1 if X wins, -1 if O wins, 0 if draw).
   - `minimax`: Implements the minimax algorithm to choose the optimal move for the AI.
   
5. **Optimization**: Ensure that the AI plays optimally by evaluating the best moves quickly. This requires reducing unnecessary checks and pruning the game tree when a winning or losing condition is found.

## Hints
- Carefully implement the game logic to ensure that the AI can evaluate board states correctly.
- When implementing minimax, the AI should maximize its own utility and minimize the opponent’s utility.
- Use recursive logic in minimax to simulate all future outcomes of a game.
- Optimize the algorithm by breaking out of loops when a terminal state is found.

## Testing
- Test the implementation by running `runner.py` to play against the AI.
- You can use `check50` to verify the correctness of your implementation.
- Use `style50` to ensure your code follows the correct style guidelines.

## Submission
- Submit your code using `submit50 ai50/projects/2024/x/tictactoe` after following the setup instructions.

## Additional Resources
- Visit [CS50 AI 2024 Tic-Tac-Toe Project](https://cs50.harvard.edu/ai/2024/projects/0/tictactoe/#tictactoe) for more details.
