"""
Salary Expense Calculator

This script calculates the distribution of expenses based on a user's salary input.
It demonstrates input validation, error handling, and basic financial calculations.

Author: AndresCdo
"""

import sys
from typing import Dict, Tuple

def get_valid_salary() -> float:
    """
    Prompts the user for a valid salary input.
    
    Returns:
        float: A positive, non-zero salary value.
    """
    while True:
        try:
            salary = float(input("Enter your salary in Colombian pesos: "))
            if salary <= 0:
                print("Please enter a positive, non-zero value.")
            else:
                return salary
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_expenses(salary: float) -> Dict[str, float]:
    """
    Calculates expense distribution based on the given salary.
    
    Args:
        salary (float): The total salary amount.
    
    Returns:
        Dict[str, float]: A dictionary containing expense categories and their amounts.
    """
    return {
        "Food": 0.1 * salary,
        "Transportation": 0.15 * salary,
        "Cinema tickets": 0.05 * salary,
        "Books": 0.1 * salary,
    }

def calculate_rent(salary: float, expenses: Dict[str, float]) -> float:
    """
    Calculates the remaining amount for rent after other expenses.
    
    Args:
        salary (float): The total salary amount.
        expenses (Dict[str, float]): Dictionary of other expenses.
    
    Returns:
        float: The amount left for rent.
    """
    return salary - sum(expenses.values())

def format_currency(amount: float) -> str:
    """
    Formats a float value as a currency string.
    
    Args:
        amount (float): The amount to format.
    
    Returns:
        str: Formatted currency string.
    """
    return f"{amount:,.2f}"

def display_results(salary: float, expenses: Dict[str, float], rent: float) -> None:
    """
    Displays the calculated expenses and rent.
    
    Args:
        salary (float): The total salary amount.
        expenses (Dict[str, float]): Dictionary of calculated expenses.
        rent (float): The calculated rent amount.
    """
    print(f"\nYour salary is {format_currency(salary)} Colombian pesos.")
    print("\nExpense distribution:")
    for category, amount in expenses.items():
        print(f"- {category}: {format_currency(amount)} pesos")
    print(f"- Rent: {format_currency(rent)} pesos")

def main() -> None:
    """
    Main function to run the salary expense calculator.
    """
    print("Welcome to the Salary Expense Calculator\n")
    
    salary = get_valid_salary()
    expenses = calculate_expenses(salary)
    rent = calculate_rent(salary, expenses)
    
    display_results(salary, expenses, rent)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)

# THE PEOPLE ARE SUPERIOR TO THEIR LEADERS!