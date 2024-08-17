# -*- coding: utf-8 -*-
"""Provide log symbols for various log levels."""
import platform
import subprocess
from enum import Enum

from colorama import Fore, deinit, init

init(autoreset=True)

_MAIN = {"info": "🔍", "success": "✔️", "warning": "⛔", "error": "❌"}

_FALLBACKS = {"info": "¡", "success": "v", "warning": "!!", "error": "×"}


def is_supported():
    """
    Checks whether the operating system is Windows and if Windows Terminal is installed.

    Returns:
        bool: True if the operating system is Windows and Windows Terminal is installed,
        or if the OS is not Windows (assumed to support Unicode by default).
    """
    if platform.system() == "Windows":
        try:
            subprocess.run(
                ["where", "wt"],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except subprocess.CalledProcessError:
            return False
    return True  # Assume non-Windows systems support Unicode


_SYMBOLS = _MAIN if is_supported() else _FALLBACKS


class LogSymbols(Enum):  # pylint: disable=too-few-public-methods
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

    INFO = Fore.BLUE + _SYMBOLS["info"] + Fore.RESET
    SUCCESS = Fore.GREEN + _SYMBOLS["success"] + Fore.RESET
    WARNING = Fore.YELLOW + _SYMBOLS["warning"] + Fore.RESET
    ERROR = Fore.RED + _SYMBOLS["error"] + Fore.RESET


deinit()
