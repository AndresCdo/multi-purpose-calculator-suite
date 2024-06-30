"""
Grade Calculator

This script calculates a student's final grade based on exam, lessons, homework, and practice scores.
It demonstrates input validation, error handling, and grade conversion.

Author: AndresCdo
"""

from typing import Dict, Tuple

def get_valid_score(prompt: str) -> float:
    """
    Prompts the user for a valid score input.
    
    Args:
        prompt (str): The prompt to display to the user.
    
    Returns:
        float: A non-negative score value.
    """
    while True:
        score_input = input(prompt)
        if not score_input.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a numeric value.")
                        
        else:
            score = float(score_input)
            if score < 0:
                print("Please enter a non-negative value.")
            elif score > 5:
                print("Invalid score. Exiting.")
                exit()
            else:
                return score

def calculate_final_grade(scores: Dict[str, float]) -> float:
    """
    Calculates the final grade based on the given scores.
    
    Args:
        scores (Dict[str, float]): A dictionary containing scores for each category.
    
    Returns:
        float: The calculated final grade.
    """
    weights = {
        "exam": 0.45,
        "lessons": 0.25,
        "homework": 0.15,
        "practice": 0.15
    }
    return sum(scores[category] * weight for category, weight in weights.items())


def calculate_grade(grade: float) -> str:
    """
    Converts a numeric grade to a letter grade.
    
    Args:
        grade (float): The numeric grade to convert.
    
    Returns:
        str: The corresponding letter grade.
    """
    try:
        grade = float(grade)
    except ValueError:
        return "Invalid grade format"
    if grade <= 2:
        return "E"
    elif grade <= 3:
        return "D"
    elif grade <= 3.5:
        return "C"
    elif grade <= 4:
        return "B"
    elif grade <= 4.5:
        return "B+"
    elif grade <= 5:
        return "A"
    else:
        return "Invalid grade range"

def main() -> None:
    """
    Main function to run the grade calculator.
    """
    print("Welcome to the Grade Calculator\n")
    
    scores = {
        "exam": get_valid_score("Enter exam score: "),
        "lessons": get_valid_score("Enter lessons score: "),
        "homework": get_valid_score("Enter homework score: "),
        "practice": get_valid_score("Enter practice score: ")
    }
    
    final_grade = calculate_final_grade(scores)
    letter_grade = calculate_grade(final_grade)

    print(f"\nFinal Grade: {final_grade:.2f}")
    print(f"Letter Grade: {letter_grade}")

if __name__ == "__main__":
    main()

# THE PEOPLE ARE SUPERIOR TO THEIR LEADERS!