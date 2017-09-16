# -*- coding: utf-8 -*-
"""Provide log symbols for various log levels."""
from enum import Enum
from colorama import init, Fore
import platform

init(autoreset=True)

_MAIN = {
    'info': 'ℹ',
    'success': '✔',
    'warning': '⚠',
    'error': '✖'
}

_FALLBACKS = {
    'info': 'i',
    'success': '√',
    'warning': '‼',
    'error': '×'
}


def is_supported():
    """Check whether operating system supports main symbols or not.

    Returns
    -------
    boolean
        Whether operating system supports main symbols or not
    """
    os_arch = platform.system() + str(platform.architecture()[0])
    os_name = platform.system() + platform.release()

    print os_name

    if os_arch is not 'Windows32bit':
        return True

    if os_name is 'Windows10':
        return True

    return False

_SYMBOLS = _MAIN if is_supported() else _FALLBACKS


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

    INFO = Fore.BLUE + _SYMBOLS['info']
    SUCCESS = Fore.GREEN + _SYMBOLS['success']
    WARNING = Fore.YELLOW + _SYMBOLS['warning']
    ERROR = Fore.RED + _SYMBOLS['error']
