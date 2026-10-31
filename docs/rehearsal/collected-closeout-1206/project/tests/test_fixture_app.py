"""Baseline behavior; the two proposed task modules do not exist yet."""

import contextlib
import io
import unittest

import fixture_app


class FixtureAppTests(unittest.TestCase):
    def test_default_prints_application_name(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = fixture_app.main([])
        self.assertEqual(result, 0)
        self.assertEqual(output.getvalue(), "collected-closeout-fixture\n")

    def test_version_prints_fixture_version(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = fixture_app.main(["--version"])
        self.assertEqual(result, 0)
        self.assertEqual(output.getvalue(), "1\n")

    def test_unknown_argument_is_rejected(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                fixture_app.main(["--unknown"])
        self.assertEqual(raised.exception.code, 2)
