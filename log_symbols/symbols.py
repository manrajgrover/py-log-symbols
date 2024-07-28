"""Provide log symbols for various log levels."""
from enum import Enum

_MAIN = {"info": "🔍", "success": "✔️ ", "warning": "⚠ ", "error": "❌"}


class LogSymbols(Enum):
    """LogSymbol enum class.

    Attributes
    ----------
    ERROR : str
        Colored error symbol
    INFO : str
        Colored info symbol
    SUCCESS : str
        Colored success symbol
    WARNING : str
        Colored warning symbol
    """

    INFO = _MAIN["info"]
    SUCCESS = _MAIN["success"]
    WARNING = _MAIN["warning"]
    ERROR = _MAIN["error"]
