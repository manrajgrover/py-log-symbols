# -*- coding: utf-8 -*-
from enum import Enum
from colorama import init, Fore

init(autoreset=True)

MAIN = {
    'info': 'ℹ',
    'success': '✔',
    'warning': '⚠',
    'error': '✖'
}

FALLBACKS = {
    'info': 'i',
    'success': '√',
    'warning': '‼',
    'error': '×'
}

SYMBOLS = MAIN


class LogSymbols(Enum):
    INFO = Fore.BLUE + SYMBOLS['info']
    SUCCESS = Fore.GREEN + SYMBOLS['success']
    WARNING = Fore.YELLOW + SYMBOLS['warning']
    ERROR = Fore.RED + SYMBOLS['error']
