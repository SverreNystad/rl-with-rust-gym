import pytest
import rl_with_rust_gym


def test_sum_as_string():
    assert rl_with_rust_gym.sum_as_string(1, 1) == "2"
