"""
PS: This Tictactoe actually implements tictactoe the way I learned to play it in Nigeria
and you will find these assumptions in the way that code is written.

X is always Player 1 and X is the default.
O is the default Player 2. 
This principle is the reason the Leaderboard class because the register_win method is making 
pretty bold assumptions about who is player 1 and player 2....
"""
import os

from tictactoe.player import Player, AIPLayer
from tictactoe.game import Game
from tictactoe.symbols import Symbols


class Session:
    def __init__(self):
        self.start()

    def start(self) -> None:
        self._symbol = Symbols()
        print("\n🎮 Starting New Tic Tac Toe Session")
        mode = input(
            "Choose mode: \n\n1 : Human vs Human, \n\n2 : Human vs AI, \n\n3 : AI vs AI: \n\n"
        ).strip()

        if mode == "1":
            p1 = Player(
                input(f"Enter name for Player 1 ({self._symbol.TEXT.X}): "),
                self._symbol.TEXT.X,
            )
            p2 = Player(
                input(f"Enter name for Player 2 ({self._symbol.TEXT.O}): "),
                self._symbol.TEXT.O,
            )
        elif mode == "2":
            p1 = Player(
                input(f"Enter name for Player 1 ({self._symbol.TEXT.X}): "),
                self._symbol.TEXT.X,
            )
            difficulty = input("Select AI difficulty: 1 (easy), 2 (medium), 3 (hard): ")
            difficulty = int(difficulty)
            p2 = AIPLayer(
                input(f"Enter name for Player 2 ({self._symbol.TEXT.O}): "),
                self._symbol.TEXT.O,
                difficulty=difficulty,
            )
        elif mode == "3":
            difficulty1 = input("Select AI difficulty: 1 (easy), 2 (medium), 3 (hard): ")
            difficulty2 = input("Select AI difficulty: 1 (easy), 2 (medium), 3 (hard): ")
            
            difficulty1 = int(difficulty1)

            difficulty2 = int(difficulty2)
            p1 = AIPLayer(
                input(f"Enter name for Player 1 ({self._symbol.TEXT.X}): "),
                self._symbol.TEXT.X,
                difficulty=difficulty1,
            )
            p2 = AIPLayer(
                input(f"Enter name for Player 2 ({self._symbol.TEXT.O}): "),
                self._symbol.TEXT.O,
                difficulty=difficulty2,
            )
        else:
            print("Invalid option.  Defaulting to Human vs AI (hard)")
            p1 = Player("You", symbol=self._symbol.TEXT.X)
            p2 = AIPLayer("Bot", symbol=self._symbol.TEXT.O, difficulty=3)

        self.player1 = p1
        self.player2 = p2
        self.run()

    def run(self) -> None:
        self.game = Game(self.player1, self.player2)
        while True:
            result = self.game.play()
            self.display_scores()
            choice = input("Play again? (y = rematch, r = restart, q = quit): ").lower()
            if choice == "y":
                # This is a phony way of persisting the leaderboard data whenever you rematch the game.
                leaderboard = self.game.leaderboards
                self.game = Game(self.player1, self.player2)
                self.game.leaderboards = leaderboard
                self.clear_screen()
                continue
            elif choice == "r":
                print("🔁 Restarting session and clearing scores...\n")
                self.clear_screen()
                self.start()
                break
            elif choice == "q":
                print("👋 Thanks for playing!")
                break
            else:
                print("Invalid option. Rematching the game")
                self.clear_screen()
                leaderboard = self.game.leaderboards
                self.game = Game(self.player1, self.player2)
                self.game.leaderboards = leaderboard
                continue
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_scores(self) -> None:
        """Display game scores in a clean, formatted layout."""
        print("\n" + "=" * 50)
        print("🏅LEADERBOARDS")
        print("=" * 50)

        # Player 1
        print(
            f"👤 {self.game.leaderboards.p1_name:<20}({self.game.leaderboards.p1}) Wins: {self.game.leaderboards.p1_wins:>3} | Losses: {self.game.leaderboards.p1_loss:>3}"
        )

        # Player 2 stats
        print(
            f"👤 {self.game.leaderboards.p2_name:<20}({self.game.leaderboards.p2}) Wins: {self.game.leaderboards.p2_wins:>3} | Losses: {self.game.leaderboards.p2_loss:>3}"
        )

        # Draws
        print(f"🤝 {'Draws':<20} {self.game.leaderboards.draws:>3}")

        print("=" * 50)

        # Calculate total games
        total_games = self.game.leaderboards.total
        print(f"📊 Total Games Played: {total_games}")
        print("=" * 50 + "\n")
