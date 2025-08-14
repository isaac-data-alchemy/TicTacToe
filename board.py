# from tictactoe.symbols import ( EMOJI, TEXT, DisplayStyle, Symbols, SymbolDisplay
# )

# class Board:
#     def __init__(self, size, display_style: DisplayStyle = "text"):
#         self.size = size
#         self.grid: List[List[str]] = [[' ' for _ in range(self.size)] for _ in range(self.size)]
#         self.display_style = display_style
#         self.symbols = Symbols.EMOJI if display_style == "emoji" else Symbols.TEXT
#         self.cell_content_width = 3 if display_style == "text" else 2
#         self.total_cell_width = self.cell_content_width + 2


#     def display(self) -> None:
#         print()
#         horizontal_sep = "+" + ("_" * self.total_cell_width + "+") * self.size

#         for row in self.grid:
#             print(horizontal_sep)
#             row_str = "|"
#             for cell in row:
#                 symbol = self.colored_symbol(cell)
#                 if self.display_style == "emoji":
#                     padded = f" {symbol} "
#                 else:
#                     padded = f" {symbol.center(self.cell_content_width)} "
#                 row_str += padded + "|"
#             print(row_str)
#         print(horizontal_sep)
#         print()
    
#     def colored_symbol(self, symbol: str) -> str:
#         if symbol == "X":
#                 display_char = self.symbols.X
#                 return display_char if self.display_style == "emoji" else Fore.RED + display_char + Style.RESET_ALL
        
#         elif symbol == "O":
#             display_char = self.symbols.O
#             return display_char if self.display_style == "emoji" else Fore.GREEN + display_char + Style.RESET_ALL
#         return " " 
    
#     def colored_symbol_v2(self, symbol: str) -> str:
#         if self.display_style == self._display_style.emoji:
#             if symbol == self._symbol.X:
#                 return self.display_type.X
#             elif symbol == self._symbol.O:
#                 return self.display_type.O
        
#         else:
#             if symbol == self._symbol.X:
#                 return Fore.RED + self._symbol.X + Style.RESET_ALL
            
#             elif symbol == self._symbol.O:
#                 return Fore.GREEN + self._symbol.O + Style.RESET_ALL
        
#         return " "
    
#     def make_move(self, row: int, col: int, symbol: str):
#         self.grid[row][col] = symbol
    
#     def is_valid_move(self, row:int, col: int) -> bool:
#         return 0 <=row < 3 and 0 <=col < 3 and self.grid[row][col] == ' '
    
#     def is_winner(self, symbol: str) -> bool:
#         for i in range(3):
#             if all(self.grid[i][j] == symbol for j in range(3)) or \
#             all(self.grid[j][i] == symbol for j in range(3)):
#                 return True   
#         return(
#             all(self.grid[i][i] == symbol for i in range(3)) or
#             all(self.grid[i][2 - i] == symbol for i in range(3))
#         )
        
#     def is_full(self) -> bool:
#         return all(cell != ' ' for row in self.grid for cell in row)

from typing import List
from colorama import Fore, Style

# Assuming you have these definitions elsewhere
# from tictactoe.symbols import Symbols
from typing import List
from colorama import Fore, Style
from wcwidth import wcwidth  # <-- The key to a robust solution

class Board:
    def __init__(self, size, display_style: str = "text"):
        self.size = size
        self.grid: List[List[str]] = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.display_style = display_style
        
        if self.display_style == "emoji":
            self.symbols = {'X': '❌', 'O': '⭕', ' ': ' '}
        else:
            self.symbols = {'X': 'X', 'O': 'O', ' ': ' '}
            
        # Define a single, consistent target width for the content of all cells.
        # This will hold content like "  X  " or " ❌  ".
        self.TARGET_CELL_WIDTH = 5

    def _get_formatted_cell(self, cell_value: str) -> str:
        """
        Creates a perfectly centered cell string.
        """
        symbol = self.symbols[cell_value]
        symbol_width = wcwidth(symbol)
        if symbol_width < 0: symbol_width = 1

        # THIS CALCULATION MUST use the shared width variable
        padding_needed = self.TARGET_CELL_WIDTH - symbol_width
        
        left_padding = padding_needed // 2
        right_padding = padding_needed - left_padding
        
        left_spaces = ' ' * left_padding
        right_spaces = ' ' * right_padding

        if self.display_style == "text":
            if cell_value == 'X':
                symbol = Fore.RED + symbol + Style.RESET_ALL
            elif cell_value == 'O':
                symbol = Fore.GREEN + symbol + Style.RESET_ALL

        return f"{left_spaces}{symbol}{right_spaces}"

    def display(self) -> None:
        """
        Displays the board.
        """
        # THIS SEPARATOR MUST use the same shared width variable
        horizontal_sep = f"+{'-' * self.TARGET_CELL_WIDTH}+" * self.size

        print()
        for row in self.grid:
            print(horizontal_sep)
            row_str = "|"
            for cell_value in row:
                row_str += self._get_formatted_cell(cell_value) + "|"
            print(row_str)
        print(horizontal_sep)
        print()
        
    def make_move(self, row: int, col: int, symbol: str):
        self.grid[row][col] = symbol
    def is_valid_move(self, row:int, col: int) -> bool:
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == ' '
    def is_winner(self, symbol: str) -> bool:
        for i in range(self.size):
            if all(self.grid[i][j] == symbol for j in range(self.size)) or \
               all(self.grid[j][i] == symbol for j in range(self.size)):
                return True
        if all(self.grid[i][i] == symbol for i in range(self.size)) or \
           all(self.grid[i][self.size - 1 - i] == symbol for i in range(self.size)):
            return True
        return False
    def is_full(self) -> bool:
        return all(cell != ' ' for row in self.grid for cell in row)