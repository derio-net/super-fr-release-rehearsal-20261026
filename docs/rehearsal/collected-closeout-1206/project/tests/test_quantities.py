"""Strict, single-pass quantity aggregation."""

import unittest

from quantities import total_units


class TestTotalUnits(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(total_units([]), 0)

    def test_mixed_nonnegative_integers(self):
        self.assertEqual(total_units([2, 0, 3]), 5)

    def test_generator_is_exhausted(self):
        values = (value for value in [2, 0, 3])
        self.assertEqual(total_units(values), 5)
        self.assertEqual(list(values), [])

    def test_arbitrary_large_integers(self):
        large = 10**1000
        self.assertEqual(total_units([large, large, 3]), 2 * large + 3)

    def test_negative_integer_is_rejected(self):
        with self.assertRaises(ValueError):
            total_units([2, -1, 3])

    def test_both_booleans_are_rejected(self):
        for value in (False, True):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    total_units([value])

    def test_floats_are_rejected(self):
        for value in (2.0, -1.0):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    total_units([value])

    def test_strings_are_rejected(self):
        with self.assertRaises(TypeError):
            total_units(["2"])

    def test_int_subclass_is_accepted(self):
        class Units(int):
            pass

        self.assertEqual(total_units([Units(2), Units(3)]), 5)

    def test_int_only_object_is_rejected_without_coercion(self):
        class IntOnly:
            def __int__(self):
                raise AssertionError("must not coerce elements")

        with self.assertRaises(TypeError):
            total_units([IntOnly()])

    def test_iterator_exception_propagates(self):
        error = RuntimeError("iterator failed")

        def values():
            yield 2
            raise error

        with self.assertRaises(RuntimeError) as raised:
            total_units(values())
        self.assertIs(raised.exception, error)
