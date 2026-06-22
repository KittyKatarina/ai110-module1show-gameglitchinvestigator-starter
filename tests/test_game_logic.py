import pytest
from logic_utils import check_guess


class TestCheckGuessWin:
    """Test cases for winning guesses."""

    def test_winning_guess_middle_range(self):
        """When guess equals secret in middle range, return Win with correct message."""
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_winning_guess_low_range(self):
        """When guess equals secret at low end of range, return Win."""
        outcome, message = check_guess(1, 1)
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_winning_guess_high_range(self):
        """When guess equals secret at high end of range, return Win."""
        outcome, message = check_guess(100, 100)
        assert outcome == "Win"
        assert message == "🎉 Correct!"


class TestCheckGuessTooHigh:
    """Test cases for guesses that are too high."""

    def test_guess_too_high_standard(self):
        """When guess > secret, return Too High outcome."""
        outcome, message = check_guess(60, 50)
        assert outcome == "Too High"
        assert message == "📉 Go LOWER!"

    def test_guess_too_high_off_by_one(self):
        """When guess is only 1 more than secret, return Too High."""
        outcome, message = check_guess(51, 50)
        assert outcome == "Too High"
        assert message == "📉 Go LOWER!"

    def test_guess_too_high_large_difference(self):
        """When guess is much larger than secret, return Too High."""
        outcome, message = check_guess(100, 10)
        assert outcome == "Too High"
        assert message == "📉 Go LOWER!"

    def test_guess_too_high_at_max(self):
        """When guess is at max (100) and secret is lower, return Too High."""
        outcome, message = check_guess(100, 75)
        assert outcome == "Too High"
        assert message == "📉 Go LOWER!"


class TestCheckGuessTooLow:
    """Test cases for guesses that are too low."""

    def test_guess_too_low_standard(self):
        """When guess < secret, return Too Low outcome."""
        outcome, message = check_guess(40, 50)
        assert outcome == "Too Low"
        assert message == "📈 Go HIGHER!"

    def test_guess_too_low_off_by_one(self):
        """When guess is only 1 less than secret, return Too Low."""
        outcome, message = check_guess(49, 50)
        assert outcome == "Too Low"
        assert message == "📈 Go HIGHER!"

    def test_guess_too_low_large_difference(self):
        """When guess is much smaller than secret, return Too Low."""
        outcome, message = check_guess(1, 100)
        assert outcome == "Too Low"
        assert message == "📈 Go HIGHER!"

    def test_guess_too_low_at_min(self):
        """When guess is at min (1) and secret is higher, return Too Low."""
        outcome, message = check_guess(1, 50)
        assert outcome == "Too Low"
        assert message == "📈 Go HIGHER!"


class TestCheckGuessEdgeCases:
    """Test cases for edge cases including out of bounds and negative inputs."""

    def test_guess_negative_number_too_low(self):
        """When guess is negative and less than secret, return Too Low."""
        outcome, message = check_guess(-10, 50)
        assert outcome == "Too Low"
        assert message == "📈 Go HIGHER!"

    def test_guess_out_of_bounds_upwards(self):
        """When guess exceeds max range (100), return Too High."""
        outcome, message = check_guess(150, 50)
        assert outcome == "Too High"
        assert message == "📉 Go LOWER!"

    def test_guess_far_out_of_bounds_upwards(self):
        """When guess is far beyond max range, return Too High."""
        outcome, message = check_guess(1000, 50)
        assert outcome == "Too High"
        assert message == "📉 Go LOWER!"

    def test_guess_decimal_rounds_down_too_high(self):
        """When guess is decimal that rounds down and is still too high."""
        outcome, message = check_guess(75.9, 50)
        assert outcome == "Too High"
        assert message == "📉 Go LOWER!"

    def test_guess_decimal_rounds_down_too_low(self):
        """When guess is decimal that rounds down and is too low."""
        outcome, message = check_guess(40.5, 50)
        assert outcome == "Too Low"
        assert message == "📈 Go HIGHER!"

    def test_guess_decimal_equals_secret_after_conversion(self):
        """No decimal rounding when guessing secret number as decimal."""
        outcome, message = check_guess(50.3, 50)
        assert outcome == "Too High"
        assert message == "📉 Go LOWER!"

    def test_guess_decimal_just_below_secret(self):
        """When decimal guess is just below secret after rounding."""
        outcome, message = check_guess(49.9, 50)
        assert outcome == "Too Low"
        assert message == "📈 Go HIGHER!"

