"""
if you wanted to run this code as a python module uncomment these and then you can import them all from . (because the interpreter will initialize them before running __main__)
however to build the source code pyinstaller requires absolute paths so you will find that this __init__ file is not being
used. you can remove the code from here if you want but once you do you cannot make imports like the example below.

Example:
some_module.py/
from . import Player

Response:
ImportError: attempted relative import with no known parent package
"""

# from .symbols import (
#     Symbol,
#     X,
#     O,
#     DisplayType,
#     DisplayStyle,
#     EMOJI,
#     TEXT,
# )
from .board import Board
from .player import Player, AIPLayer
from .game import Game
from .sessions import Session
