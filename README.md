# **STATISTICS ANALYSER**

**Statistics Analyzer** is a tool built to perform statistics calculation on datasets provided by users. Either by reading csv files, or by manual input. It can read single-column csv files, as well as multi-column, with the option to choose which columns to analyse, or simply using the *all keyword to analyze all columns.
This program was built using Python 3.14, it uses a class to handle all the data related work, as well as multiple function for the mathematic calculations.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to use](#how-to-use)
- [How to run tests](#how-to-run-tests)
- [Project Structure](#project-structure)

---

## Features:

This program will calculate all the following data:
- Mean
- Median
- Range
- First & third quartiles
- Interquartile range
- Mode
- Variance(with option for samples)
- Standard deviation(with option for samples)
- Outliers removal(1.5 IQR method)
- Mean absolute deviation
- Z-score

---

## Requirements:
- Python 3.14 or higher
- Tabulate library (``pip install tabulate`` in terminal)
- (optional) `pytest` for running tests

---

## Installation: 

Use git to install the repository on your computer:

```bash
git clone https://github.com/GFou-dev/stats-analyser
```

## How to use:

There are two ways to use this program:
- The user can input a csv filepath in the command-line arguments, followed by any optional column headers the user wants to analyse.
- If no command-line arguments are provided, the program will prompt the user to enter manual data.

---

### Command-line arguments:

- The first command-line argument should be the csv filepath the users want to analyse.

``python analyser.py grades.csv``

- Then the users can input any number of column headers they want analysed. If they want to input all columns, they can use the command  `*all` instead.

``python analyser.py grades.csv Class_A Class_B``

``python analyser.py grades.csv *all``

- If only the csv is provided, the program will simply combine all numerical data contained within it, and add to a single list to analyse.

---

### Manual input:

- If no command-line argument is provided, after starting the program the user will be prompted to add numerical data by hand.
- After entering all the desired data, the user should enter "q" or "quit". The program will then start doing the calculations and print results.

---

## How to run tests:

The test suite covers all the mathematical calculations.

```bash
pytest test_analyser.py -v
```

---

## Project Structure

```
analyser/
├── analyser.py       # Main program
├── test_analyser.py  # Pytest test suite
├── grades.csv        # A sample csv file with student grades
├── requirements.txt  #The required libraries to run this program
└── README.md
```

---

## License

This project is released under the MIT License.

## Authors

This project was developed collaboratively with another student.
