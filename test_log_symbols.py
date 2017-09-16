# -*- coding: utf-8 -*-
"""This module tests LogSymbol enum."""
import re
import unittest

from log_symbols import LogSymbols


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
    pattern = '(\x1b\[|\x9b)[^@-_]*[@-_]|\x1b[@-_]'
    return re.sub(pattern, '', string, flags=re.I)


class TestLogSymbols(unittest.TestCase):
    """Test LogSymbols enum for attribute values."""

    def test_symbols(self):
        """Test the symbols in LogSymbol enum."""
        self.assertTrue(
            strip_ansi(LogSymbols.SUCCESS.value) in ('✔', '√')
        )


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogSymbols)
    unittest.TextTestRunner(verbosity=2).run(suite)