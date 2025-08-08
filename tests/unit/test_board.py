import unittest
from ..import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_make_move_and_valid_move(self):
        self.assertTrue(self.board.is_valid_move(0,0))
        self.board.make_move(0, 0, "X")
        self.assertFalse(self.board.is_valid_move(0,0))
    
    def test_winner_by_row(self):
        for col in range(3):
            self.board.make_move(0,col, "X")
        self.assertTrue(self.board.is_winner("X"))
    
    def test_is_winner_by_column(self):
        for row in range(3):
            self.board.make_move(row, 1, "0")
        self.assertFalse((self.board.is_winner("O")))
    
    def test_is_winner_by_diagonal_left_to_right(self):
        for i in range(3):
            self.board.make_move(i, i, "X")
        self.assertTrue(self.board.is_winner("X"))
    
    def test_is_winner_by_diagona_right_to_left(self):
        for i in range(3):
            self.board.make_move(i, 2 - i, "O")
        self.assertTrue((self.board.is_winner("O")))
    
    def test_board_is_full_so_tie(self):
        moves = [(row, col) for row in range(3) for col in range(3)]
        for i, (row, col) in enumerate(moves):
            self.board.make_move(row, col, "X" if i%2 == 0 else "O")
        self.assertTrue(self.board.is_full())


if __name__ == "__main__":
    unittest.main()
        