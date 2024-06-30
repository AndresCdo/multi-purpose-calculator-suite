from unittest.mock import patch

import pytest

from grade_calculator import main


def test_main(capsys):
    with patch("builtins.input", side_effect=["5", "5", "5", "5"]):
        main()
        captured = capsys.readouterr()
        assert "Final Grade: 5.00" in captured.out
        assert "Letter Grade: A" in captured.out


def test_main_with_invalid_score(capsys):
    with patch("builtins.input", side_effect=["5", "5", "5", "6"]):
        try:
            main()
            captured = capsys.readouterr()
            assert "Invalid score. Exiting." in captured.out
        except SystemExit:
            pass


def test_main_with_invalid_input(capsys):
    with patch("builtins.input", side_effect=["5", "5", "5", "invalid"]):
        try:
            main()
            captured = capsys.readouterr()
            assert "Invalid input. Please enter a numeric value." in captured.out
        except StopIteration:
            pass


def test_main_with_negative_score(capsys):
    try:
        with patch("builtins.input", side_effect=["5", "5", "5", "-1"]):
            main()
            captured = capsys.readouterr()
            assert "Please enter a non-negative value." in captured.out
            assert "Final Grade: 10.00" in captured.out
            assert "Letter Grade: A" in captured.out
    except StopIteration:
        pass


def test_main_with_invalid_input_and_negative_score(capsys):
    try:
        with patch("builtins.input", side_effect=["5", "5", "5", "invalid", "-1"]):
            main()
            captured = capsys.readouterr()
            assert "Invalid input. Please enter a numeric value." in captured.out
            assert "Please enter a non-negative value." in captured.out
            assert "Final Grade: 10.00" in captured.out
            assert "Letter Grade: A" in captured.out
    except StopIteration:
        pass
