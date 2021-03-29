#!/usr/bin/python3
"""Unittest for the class TestConsole"""

import unittest
import pep8
import console

HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_console(self):
        """Test that console.py correspond to PEP8"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['console.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_pep8_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_console.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None, "console.py needs a docstring")
        st = "console.py needs a docstring"
        self.assertTrue(len(console.__doc__) >= 1, st)

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        st = "HBNBCommand class needs a docstring"
        self.assertIsNot(HBNBCommand.__doc__, None, st)
        self.assertTrue(len(HBNBCommand.__doc__) >= 1, st)

if __name__ == '__main__':
    unittest.main()
