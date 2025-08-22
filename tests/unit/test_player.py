import unittest

from .. import Player


class TestPlayer(unittest.TestCase):
    def test_player_gets_creation(self):
        player = Player("Heather", "X")
        self.assertEqual(player.name, "Heather")
        self.assertEqual(player.symbol, "X")
        self.assertEqual(player.score, 0)


if __name__ == "__main__":
    unittest.main()
