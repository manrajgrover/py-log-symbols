# -*- coding: utf-8 -*-
from enum import Enum
from colorama import init, Fore
import platform

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


def is_supported():
    os_arch = platform.system() + str(platform.architecture()[0])
    os_name = platform.system() + platform.release()

    print os_name

    if os_arch is not 'Windows32bit':
        return True

    if os_name is 'Windows10':
        return True

    return False

SYMBOLS = MAIN if is_supported() else FALLBACKS


class LogSymbols(Enum):
    INFO = Fore.BLUE + SYMBOLS['info']
    SUCCESS = Fore.GREEN + SYMBOLS['success']
    WARNING = Fore.YELLOW + SYMBOLS['warning']
    ERROR = Fore.RED + SYMBOLS['error']
