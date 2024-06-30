"""
Product Price Calculator
"""
import json


def calculate_total_price(products):
    """
    Calculates the total price of a list of products.

    Args:
        products (list): A list of dictionaries representing products. Each dictionary should have the following keys:
            - 'price' (float): The price of the product.
            - 'discount' (float): The discount percentage for the product.
            - 'expiration_date' (str): The expiration date of the product. If it is 'today', a special discount is applied.

    Returns:
        float: The total price of all the products, rounded to 2 decimal places.
    """
    result = 0.0
    for product in products:
        price = product["price"]
        discount = product["discount"]
        if product["expiration_date"] == "today":
            result += (price * (1 - discount / 100)) * 0.8
        else:
            result += price * (1 - discount / 100)
    return round(result, 2)


if __name__ == "__main__":
    products = []
    while len(products) == 0:
        try:
            products = json.loads(input())
            if len(products) > 0:
                total_price = calculate_total_price(products)
                print(total_price)
        except json.JSONDecodeError:  # Catching specific exception
            print("An error has occurred.\nPlease enter a valid input.")
        except Exception as e:  # Optionally catch other exceptions explicitly
            print(f"An unexpected error has occurred: {e}\nPlease enter a valid input.")
