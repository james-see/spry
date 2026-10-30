"""Smoke tests for spry."""

import spry.spry


def test_version() -> None:
    assert spry.spry.__version__ == "0.5.8"
