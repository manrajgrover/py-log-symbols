# -*- coding: utf-8 -*-
"""Provide log symbols for various log levels."""
import platform

from enum import Enum

_MAIN = {
    'info': 'ℹ',
    'success': '✔',
    'warning': '⚠',
    'error': '✖'
}

_FALLBACKS = {
    'info': '¡',
    'success': 'v',
    'warning': '!!',
    'error': '×'
}


def is_supported():
    """Check whether operating system supports main symbols or not.

    Returns
    -------
    boolean
        Whether operating system supports main symbols or not
    """

    os_arch = platform.system()

    if os_arch != 'Windows':
        return True

    return False


_SYMBOLS = _MAIN if is_supported() else _FALLBACKS


def _ansi_code(code):
    return '\033[' + str(code) + 'm'

_RED = _ansi_code(31)
_GREEN = _ansi_code(32)
_YELLOW = _ansi_code(33)
_BLUE = _ansi_code(34)
_RESET = _ansi_code(39)


class LogSymbols(Enum): # pylint: disable=too-few-public-methods
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

    INFO = _BLUE + _SYMBOLS['info'] + _RESET
    SUCCESS = _GREEN + _SYMBOLS['success'] + _RESET
    WARNING = _YELLOW + _SYMBOLS['warning'] + _RESET
    ERROR = _RED + _SYMBOLS['error'] + _RESET
