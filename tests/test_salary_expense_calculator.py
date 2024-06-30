from unittest.mock import patch

import pytest

from salary_expense_calculator import display_results


def test_display_results(capsys):
    salary = 50000.0
    expenses = {
        "Food": 5000.0,
        "Transportation": 7500.0,
        "Cinema tickets": 2500.0,
        "Books": 5000.0,
    }
    rent = 30000.0

    display_results(salary, expenses, rent)

    captured = capsys.readouterr()
    assert "Your salary is 50,000.00 Colombian pesos." in captured.out
    assert "- Food: 5,000.00 pesos" in captured.out
    assert "- Transportation: 7,500.00 pesos" in captured.out
    assert "- Cinema tickets: 2,500.00 pesos" in captured.out
    assert "- Books: 5,000.00 pesos" in captured.out
    assert "- Rent: 30,000.00 pesos" in captured.out
