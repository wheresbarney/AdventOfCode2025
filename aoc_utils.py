#!/usr/bin/env python3
"""Utility functions for Advent of Code solutions."""

from pathlib import Path


def load_real_input(caller_file):
    """
    Auto-detect day number from caller filename and load real input data.

    Args:
        caller_file: Pass __file__ from the calling script

    Returns:
        Contents of the corresponding data file as a string

    Example:
        # In day1.py:
        from aoc_utils import load_real_input
        real_input = load_real_input(__file__)
    """
    day = Path(caller_file).stem.replace('day', '')
    data_file = Path(caller_file).parent / "data" / f"day{day}.txt"

    if not data_file.exists():
        raise FileNotFoundError(
            f"Real input not found: {data_file}\n"
            f"Create the file or keep using inline sample data for testing."
        )

    return data_file.read_text().strip()
