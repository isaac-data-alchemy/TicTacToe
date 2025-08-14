from tictactoe.player import Player, AIPLayer
from tictactoe.board import Board
from tictactoe.symbols import Display
from tictactoe.leaderboards import LeaderBoard


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.display = Display()
        style = input(f"Choose symbol display style ({self.display.text} / {self.display.emoji}): ").strip()
        if style not in (self.display.emoji, self.display.text):
            style = self.display.emoji
        self.board = Board(size=3, display_style=style)
        self.player1 = player1
        self.player2 = player2
        self.current_player: Player = self.player1

        self.leaderboards = LeaderBoard(self.player1, self.player2)
        
    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
                
    def play(self):
        self.board.display()
        while True:
            if isinstance(self.current_player, AIPLayer):
                row, col = self.current_player.get_move(self.board)
                print(f"{self.current_player.name}'s move: {row}, {col}")
            else:          
                move = input(f"{self.current_player.name}'s turn ({self.current_player.symbol}, enter row,col (0, 1)): ")
                try:
                    row, col = map(int, move.strip().split(","))
                except Exception:
                    print("Invalid input. Use format row, col (e.g 0,2.)")
                    continue
            if not self.board.is_valid_move(row, col):
                print("Invalid move. Cell occupied or out of bounds.")
                continue
            self.board.make_move(row, col, self.current_player.symbol)
            self.board.display()
            if self.board.is_winner(self.current_player.symbol):
                print(f"🏆 {self.current_player.name} wins!")
                self.leaderboards.register_win(self.current_player.symbol)
                self.switch_player()
                return "win"
            elif self.board.is_full():
                self.leaderboards.draws +=1
                self.switch_player()
                print("🤝 It's a draw!")
                return "draw"            
            self.switch_player()