from typing import List, Optional
from colorama import Fore, Style

from tictactoe.symbols import ( EMOJI, TEXT, DisplayStyle, Symbols, SymbolDisplay
)

class Board:
    def __init__(self, size, display_style: DisplayStyle = "text"):
        self.size = size
        self.grid: List[List[str]] = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.display_style = display_style
        self.symbols = Symbols.EMOJI if display_style == "emoji" else Symbols.TEXT
        self.emoji_padding = 2
        self.cell_width = 3 if display_style == "text" else 5


    def display(self) -> None:
        print()
        horizontal_sep = "+" + "+".join(["-" * (self.cell_width + 2) for _ in range(self.size)]) + "+"

        for row in self.grid:
            row_str = "|"
            for cell in row:
                symbol = self.colored_symbol(cell)
                if self.display_style == "emoji":
                    padded = f" {symbol.center(self.cell_width)} "
                else:
                    padded = f" {symbol.center(self.cell_width)} "
                row_str += padded + "|"
            print(horizontal_sep)
            print(row_str)
        print(horizontal_sep)
        print()
    
    def colored_symbol(self, symbol: str) -> str:
        if symbol == "X":
                display_char = self.symbols.X
                return display_char if self.display_style == "emoji" else Fore.RED + display_char + Style.RESET_ALL
        
        elif symbol == "O":
            display_char = self.symbols.O
            return display_char if self.display_style == "emoji" else Fore.GREEN + display_char + Style.RESET_ALL
        return " " 
    
    def colored_symbol_v2(self, symbol: str) -> str:
        if self.display_style == self._display_style.emoji:
            if symbol == self._symbol.X:
                return self.display_type.X
            elif symbol == self._symbol.O:
                return self.display_type.O
        
        else:
            if symbol == self._symbol.X:
                return Fore.RED + self._symbol.X + Style.RESET_ALL
            
            elif symbol == self._symbol.O:
                return Fore.GREEN + self._symbol.O + Style.RESET_ALL
        
        return " "
    
    def make_move(self, row: int, col: int, symbol: str):
        self.grid[row][col] = symbol
    
    def is_valid_move(self, row:int, col: int) -> bool:
        return 0 <=row < 3 and 0 <=col < 3 and self.grid[row][col] == ' '
    
    def is_winner(self, symbol: str) -> bool:
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or \
            all(self.grid[j][i] == symbol for j in range(3)):
                return True   
        return(
            all(self.grid[i][i] == symbol for i in range(3)) or
            all(self.grid[i][2 - i] == symbol for i in range(3))
        )
        
    def is_full(self) -> bool:
        return all(cell != ' ' for row in self.grid for cell in row)
    

# def display(self) -> None:
    #     print()
    #     spacer = "     "
    #     divider = spacer.join(["" for _ in range(self.size)])
    #     for i, row in enumerate(self.grid):
    #         line = ""
    #         for j, cell in enumerate(row):
    #             line += f"[  {cell}  ]"
    #             if j < self.size - 1:
    #                 line += "   "
    #         print(line)
    #         if i < self.size - 1:
    #             print(spacer.join(["------" for _ in range(self.size)]))
    #     print()