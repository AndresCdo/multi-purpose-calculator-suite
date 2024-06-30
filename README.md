# Multi-Purpose Calculator Suite

This suite of Python scripts offers a variety of calculators, including salary expense distribution, egg classification, grade calculation, and product price calculation. Each script demonstrates input validation, error handling, and basic calculations tailored to its specific purpose.

## Getting Started

To run these scripts, you will need Python installed on your system. These scripts were developed and tested with Python 3.8, but they should work with most Python 3.x versions.

### Prerequisites

- Python 3.x

### Installation

Clone this repository to your local machine to get started:

```bash
git clone https://github.com/AndresCdo/multi-purpose-calculator-suite.git
cd multi-purpose-calculator-suite
```

Install the required Python packages:
  
  ```bash
  pip install -r requirements.txt
  ```

## Usage

Navigate to the cloned directory. To run a specific calculator, execute one of the following commands:

- Salary Expense Distribution Calculator:

  ```bash
  python salary_expense_distribution.py
  ```

- Egg Classification Calculator:

  ```bash
  python egg_classification.py
  ```

- Grade Calculator:

  ```bash
  python grade_calculator.py
  ```

- Product Price Calculator:

  ```bash
  python product_price_calculator.py
  ```

Follow the on-screen prompts to input the required information and view the calculated results.

## Features

- Multiple Calculators: Choose from various calculators based on your needs.
- Input Validation: Ensures that the user inputs are valid.
- Expense Calculation: Specifically for the salary expense calculator, it breaks down the salary into predefined expense categories.

## Docker Support

This suite includes a Dockerfile for building a Docker image that runs the calculators. To build and run the Docker container, use:

```bash
docker build -t calculator-suite .
docker run -it calculator-suite
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
