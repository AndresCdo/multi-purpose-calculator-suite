# app.py
import sys
from egg_classification import classify_egg
from grade_calculator import calculate_grade
from product_price_calculator import calculate_total_price
from salary_expense_calculator import main as salary_expense_calculator


def main():
    # Simple CLI to interact with the different modules
    print("Welcome to the Utility App. Please choose an option:")
    print("1. Egg Classification")
    print("2. Grade Calculator")
    print("3. Product Price Calculator")
    print("4. Salary Expense Calculator")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        size = input("Enter egg size for classification: ")
        print(f"The egg is classified as: {classify_egg(size)}")
    elif choice == "2":
        score = input("Enter score for grade calculation: ")
        print(f"The calculated grade is: {calculate_grade(score)}")
    elif choice == "3":
        print("Enter list of products (price, discount, expiration_date): ")
        products = input()
        total_price = calculate_total_price(products)
    elif choice == "4":
        salary_expense_calculator()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()