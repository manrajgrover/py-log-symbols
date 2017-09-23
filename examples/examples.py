from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from log_symbols.symbols import LogSymbols
    
for symbol in LogSymbols:
    print symbol.value, symbol.name.lower()
