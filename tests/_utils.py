"""Utilities for tests.
"""

import re

def strip_ansi(string):
    """Strip ANSI encoding from given string.

    Parameters
    ----------
    string : str
        String from which encoding needs to be removed

    Returns
    -------
    str
        Encoding free string
    """
    pattern = r'(\x1b\[|\x9b)[^@-_]*[@-_]|\x1b[@-_]'
    return re.sub(pattern, '', string, flags=re.I)
