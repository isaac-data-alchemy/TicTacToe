import random
from typing import Tuple, Literal
import time

from tictactoe.board import Board

class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol
        self.score: int = 0
        self.draws: int = 0

class AIPLayer(Player):
    DELAY = 3
    def __init__(self, name: str, symbol: Literal["O"], difficulty: str = "hard"):
        super().__init__(name, symbol)
        self.difficulty = difficulty.lower()
    
    def get_move(self, board: Board) -> Tuple[int, int]:
        if self.difficulty == "easy":
            return self.random_move(board)
        elif self.difficulty == "medium":
            return self.random_move(board) if random.random() < 0.5 else self.best_move(board)
        else:
            return self.best_move(board)
        
    def random_move(self, board: Board) -> Tuple[int, int]:
        valid_moves = [(r, c) for r in range(3) for c in range(3) if board.is_valid_move(r, c)]
        time.sleep(self.DELAY)
        return random.choice(valid_moves)
    
    def best_move(self, board: Board) -> Tuple[int, int]:
        _, move = self.minimax(board, self.symbol, True)
        time.sleep(self.DELAY)
        print("move score: ", _)
        return move

    def minimax(self, board: Board, player_symbol: str, is_maximizing: bool) -> Tuple[float, Tuple[int, int]]:
        opponent_symbol = "X" if self.symbol == "O" else "O"
        if board.is_winner(self.symbol):
            return 1, (-1,-1)
        elif board.is_winner(opponent_symbol):
            return -1, (-1,-1)
        elif board.is_full():
            return 0, (-1,-1)
        
        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = (-1,-1)

        for r in range(3):
            for c in range(3):
                if board.is_valid_move(r,c):
                    board.make_move(r,c, player_symbol)
                    score, _ = self.minimax(board, opponent_symbol if is_maximizing else self.symbol, not is_maximizing)
                    board.make_move(r,c, " ")

                    if is_maximizing:
                        if score > best_score:
                            best_score = score
                            best_move = (r,c)
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = (r, c)

        return best_score, best_move
