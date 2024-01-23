"""Tests"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Tests for the calc module."""

    def test_add_numbers(self):
        """Tests the addition functionality."""

        result = calc.add(5, 6)
        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        """Tests the subtraction functionality."""

        difference = calc.subtract(10, 15)
        self.assertEqual(difference, 5)
