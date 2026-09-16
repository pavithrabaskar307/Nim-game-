import sys
import os

# Add the src folder to the Python path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "src")
))

from main import calculate_nim_sum, find_best_move


def test_nim_sum_zero():
    """Test a losing position."""
    assert calculate_nim_sum([1, 2, 3]) == 0


def test_nim_sum_nonzero():
    """Test a winning position."""
    assert calculate_nim_sum([3, 4, 5]) == 2


def test_best_move_exists():
    """Test that an optimal move is found."""
    assert find_best_move([3, 4, 5]) is not None


def test_best_move_makes_zero_nim_sum():
    """Test that the selected move makes Nim-sum zero."""
    piles = [3, 4, 5]
    move = find_best_move(piles)

    pile_index, objects_removed = move
    new_piles = piles.copy()
    new_piles[pile_index] -= objects_removed

    assert calculate_nim_sum(new_piles) == 0


def test_losing_position():
    """Test that no winning move exists for a zero Nim-sum position."""
    assert find_best_move([1, 2, 3]) is None
