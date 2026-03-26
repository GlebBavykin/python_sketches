import pytest
import math
from design_patterns.structural.adapter import RoundHole, RoundPeg, SquarePeg, SquarePegAdapter

"""
    Peg-in-Hole Assembly Tests
"""

RADIUS = 12.5
HEIGHT = 50.0
WIDTH = RADIUS / (math.sqrt(2) / 2)  # Ширина колышка совпадает с радиусом отверстия


@pytest.fixture(scope="class")
def hole() -> RoundHole:
    """
    RoundHole instance
    """
    return RoundHole(RADIUS, HEIGHT)


@pytest.mark.parametrize(
    "peg, is_compatible",
    [
        (RoundPeg(RADIUS - 0.5, HEIGHT - 10), True),
        (RoundPeg(RADIUS + 0.5, HEIGHT - 10), False),
        (RoundPeg(RADIUS - 0.5, HEIGHT + 10), False),
    ],
)
def test_round_compatibility(hole: RoundHole, peg: RoundPeg, is_compatible: bool):
    """
    Test whether a peg is compatible with a round hole
    """
    assert hole.fits(peg) == is_compatible


@pytest.mark.parametrize(
    "peg, is_compatible",
    [
        (SquarePeg(RADIUS - 0.5, HEIGHT - 10), True),
        (SquarePeg(RADIUS + 0.5, HEIGHT - 10), False),
        (SquarePeg(RADIUS - 0.5, HEIGHT + 10), False),
    ],
)
def test_round_incompatibility(hole: RoundHole, peg: SquarePeg, is_compatible: bool):
    """
    Test whether a peg is incompatible with a round hole
    """
    with pytest.raises(AttributeError):
        assert hole.fits(peg) == is_compatible


@pytest.mark.parametrize(
    "peg, is_compatible",
    [
        (SquarePeg(WIDTH - 0.5, HEIGHT - 10), True),
        (SquarePeg(WIDTH + 0.5, HEIGHT - 10), False),
        (SquarePeg(WIDTH - 0.5, HEIGHT + 10), False),
    ],
)
def test_round_compatibility_with_adapter(hole: RoundHole, peg: SquarePeg, is_compatible: bool):
    """
    Test whether adapter is compatible with a round hole
    """
    assert hole.fits(SquarePegAdapter(peg)) == is_compatible
