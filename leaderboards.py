from typing import Union
from dataclasses import dataclass

from tictactoe.player import Player, AIPLayer
 
class LeaderBoard:
    def __init__(self, player_one: Player, player_two: Union[Player, AIPLayer]):
        self.p1 = player_one.symbol
        self.p2 = player_two.symbol
        self.p1_wins = 0
        self.p2_wins = 0
        self.p1_loss = 0
        self.p2_loss = 0
        self.draws = 0

    @property
    def total(self) -> int:
        return self.p1_wins + self.p2_wins + self.draws
    
    def register_win(self, symbol: str):
        if symbol == "X":
            self.p1_wins +=1
            self.p2_loss +=1
        elif symbol == "O":
            self.p2_wins +=1
            self.p1_loss +=1
    
    