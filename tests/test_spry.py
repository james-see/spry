"""Smoke tests for spry."""

import subprocess
import sys


def test_version() -> None:
    import spry.spry as module

    assert module.__version__ == "0.5.9"


def test_help_mentions_report() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "spry.spry", "--help"],
        capture_output=True,
        text=True,
    )
    # Spry's entry point is normally the console script, so a help invocation may
    # fall through to parsing; accept either successful or argument-error exit.
    assert "--report" in result.stdout or "--report" in result.stderr
