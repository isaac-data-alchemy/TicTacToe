from typing import Union
from dataclasses import dataclass

from tictactoe.player import Player, AIPLayer

@dataclass
class LeaderBoard:
    wins: int
    losses: int
    draws: int


class LeaderBoard:
    def __init__(self, player_one: Player, player_two: Union[Player, AIPLayer]):
        self.p1 = player_one.symbol
        self.p2 = player_two.symbol
        self.p1_wins = 0
        self.p2_wins = 0
        self.p1_loss = 0
        self.p2_loss = 0
        self.draws = 0
    
    def __str__(self):
        return f"{self.p1.symbol}:{self.p1_wins} {self.p2.symbol}: {self.p2_wins}"
    
    # @property
    # def draws(self):
    #     return self.draws
    
    # @draws.setter
    # def draws(self, val):
    #     return self.draws 

    
    def register_win(self, symbol: str):
        if symbol == "X":
            self.p1_wins +=1
            self.p2_loss +=1
        elif symbol == "O":
            self.p2_wins +=1
            self.p1_loss +=1
    
    