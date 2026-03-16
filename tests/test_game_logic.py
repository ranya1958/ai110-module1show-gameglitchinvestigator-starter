from logic_utils import check_guess


def _outcome(result):
    """Normalize check_guess return value to outcome string.

    `check_guess` may return either an outcome string or a (outcome, message) tuple.
    This helper extracts the outcome for assertions.
    """
    return result[0] if isinstance(result, tuple) else result


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    assert _outcome(check_guess(50, 50)) == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    assert _outcome(check_guess(60, 50)) == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    assert _outcome(check_guess(40, 50)) == "Too Low"


def test_consistent_outcome_with_string_and_int_secret():
    """Regression test for mixed-type secret bug.

    Ensures the outcome is identical whether the secret is passed as an int
    or the same numeric value as a string (e.g. "50"). This targets the
    previous bug where string-vs-int comparisons produced different results.
    """
    cases = [
        (50, 50),  # win
        (60, 50),  # too high
        (40, 50),  # too low
    ]
    for guess, secret in cases:
        out_int = _outcome(check_guess(guess, secret))
        out_str = _outcome(check_guess(guess, str(secret)))
        assert out_int == out_str, f"Mismatched outcomes for guess={guess}: int_secret={out_int} vs str_secret={out_str}"
