from dataclasses import dataclass
from typing import Literal
import typing as t

EMOJI = t.NewType("EMOJI", str)
TEXT = t.NewType("TEXT", str)
DisplayStyle = Literal["emoji", "text"]


@dataclass(frozen=True)
class SymbolDisplay:
    X: str
    O: str


class Symbols:
    EMOJI = SymbolDisplay(X="❌", O="⭕")
    TEXT = SymbolDisplay(X="X", O="O")


@dataclass(frozen=True)
class Display:
    emoji: EMOJI = "emoji"
    text: TEXT = "text"
