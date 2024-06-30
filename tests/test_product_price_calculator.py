import pytest
from unittest.mock import patch
from product_price_calculator import calculate_total_price

def test_calculate_total_price():
    products = [
        {
            'price': 10.0,
            'discount': 20.0,
            'expiration_date': '2022-12-31'
        },
        {
            'price': 15.0,
            'discount': 10.0,
            'expiration_date': 'today'
        },
        {
            'price': 5.0,
            'discount': 0.0,
            'expiration_date': '2023-01-01'
        }
    ]
    assert calculate_total_price(products) == 23.8