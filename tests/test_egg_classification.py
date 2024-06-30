from unittest.mock import patch

import pytest

from egg_classification import calculate_trays


def test_calculate_trays_with_A():
    classification = [{"egg_type": "A", "number_of_eggs": 90}]
    calculate_trays(classification)
    assert classification[0]["number_of_trays"] == 3


def test_calculate_trays_with_AA():
    classification = [{"egg_type": "AA", "number_of_eggs": 72}]
    calculate_trays(classification)
    assert classification[0]["number_of_trays"] == 3


def test_calculate_trays_with_AAA():
    classification = [{"egg_type": "AAA", "number_of_eggs": 36}]
    calculate_trays(classification)
    assert classification[0]["number_of_trays"] == 3


def test_calculate_trays_with_BC():
    classification = [{"egg_type": "BC", "number_of_eggs": 90}]
    calculate_trays(classification)
    assert classification[0]["number_of_trays"] == 3


def test_calculate_trays_with_multiple_types():
    classification = [
        {"egg_type": "A", "number_of_eggs": 90},
        {"egg_type": "AA", "number_of_eggs": 72},
        {"egg_type": "AAA", "number_of_eggs": 36},
        {"egg_type": "BC", "number_of_eggs": 90},
    ]
    calculate_trays(classification)
    assert classification[0]["number_of_trays"] == 3
    assert classification[1]["number_of_trays"] == 3
    assert classification[2]["number_of_trays"] == 3
    assert classification[3]["number_of_trays"] == 3
