from tictactoe.player import Player, AIPLayer
from tictactoe.game import Game
from tictactoe.symbols import Symbols


class Session:
    def __init__(self):
        self.start()
    
    def start(self) -> None:
        self._symbol = Symbols()
        print("\n🎮 Starting New Tic Tac Toe Session")
        mode = input("Choose mode: \n1 = Human vs Human, \n2 = Human vs AI, \n3 = AI vs AI: \n").strip()

        if mode == "1":
            p1 = Player(input(f"Enter name for Player 1 ({self._symbol.TEXT.X}): "), self._symbol.TEXT.X)
            p2 = Player(input(f"Enter name for Player 2 ({self._symbol.TEXT.O}): "), self._symbol.TEXT.X)
        elif mode == "2":
            p1 = Player(input(f"Enter name for Player 1 ({self._symbol.TEXT.X}): "), self._symbol.TEXT.X)
            difficulty = input("Select AI difficulty (easy, medium, hard): ").lower()
            p2 = AIPLayer(input(f"Enter name for Player 2 ({self._symbol.TEXT.O}): "), self._symbol.TEXT.O, difficulty=difficulty)
        elif mode == "3":
            difficulty1 = input("Select AI difficulty (easy, medium, hard): ").lower()
            difficulty2 = input("Select AI difficulty (easy, medium, hard): ").lower()
            p1 = AIPLayer(input(f"Enter name for Player 1 ({self._symbol.TEXT.X}): "), self._symbol.TEXT.X, difficulty=difficulty1)
            p2 = AIPLayer(input(f"Enter name for Player 2 ({self._symbol.TEXT.O}): "), self._symbol.TEXT.O, difficulty=difficulty2)
        else:
            print("Invalid option.  Defaulting to Human vs AI (hard)")
            p1 = Player("You", symbol=self._symbol.TEXT.X)
            p2 = AIPLayer("Bot", symbol=self._symbol.TEXT.O, difficulty="hard")

        self.player1 = p1
        self.player2 = p2
        self.run()
    
    def run(self) -> None:
        while True:
            game = Game(self.player1, self.player2)
            result = game.play()
            self.display_scores()
            choice = input("Play again? (y = rematch, r = restart, q = quit): ").lower()
            if choice == 'y':
                continue
            elif choice == 'r':
                print("🔁 Restarting session and clearing scores...\n")
                self.start()
                break
            elif choice == 'q':
                print("👋 Thanks for playing!")
                break
            else:
                print("Invalid option. Exiting")
    
    def display_scores(self) -> None:
        print(f"\n🏅 Scores: {self.player1.name}: {self.player1.score}, {self.player2.name}: {self.player2.score}\n \n🤝Draws: {self.player1.draws}")

