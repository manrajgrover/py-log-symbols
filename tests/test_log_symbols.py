# -*- coding: utf-8 -*-
"""This module tests LogSymbol enum."""
import re
import unittest

from log_symbols import LogSymbols

from tests._utils import strip_ansi


class TestLogSymbols(unittest.TestCase):
    """Test LogSymbols enum for attribute values."""

    def test_symbols(self):
        """Test the symbols in LogSymbol enum."""
        self.assertTrue(
            strip_ansi(LogSymbols.SUCCESS.value) in ('✔', 'v')
        )

        self.assertTrue(
            strip_ansi(LogSymbols.INFO.value) in ('ℹ', '¡')
        )

        self.assertTrue(
            strip_ansi(LogSymbols.WARNING.value) in ('⚠', '!!')
        )

        self.assertTrue(
            strip_ansi(LogSymbols.ERROR.value) in ('✖', '×')
        )


if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestLogSymbols)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
