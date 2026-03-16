# **PROJECT: DATA ANALYSER**


## Description:

**Data Analyzer** is a tool built to perform statistics calculation on datasets provided by users. Either by reading csv files, or by manual input. It can read single-column csv files, as well as multi-column, with the option to choose which columns to analyse, or simply using the *all keyword to analyze all columns.
This program was built using Python 3.14, it uses a class to handle all the data related work, as well as multiple function for the mathematic calculations.

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


## How to use:

There are two ways to use this program:
- By inputting a csv filepath in the command-line arguments, followed by any optional column headers the user wants to analyse.
- If no command-line arguments are provided, the program will prompt the user to enter manual data.


### Command-line arguments:

- The first command-line argument should be the csv filepath the users want to analyse.

``python project.py grades.csv``

- Then the users can input any number of column headers they want analysed. If they want to input all columns, they can use the command  `*all` instead.

``python project.py grades.csv Class_A Class_B``

``python project.py grades.csv *all``

- If only the csv is provided, the program will simply combine all numerical data contained within it, and add to a single list to analyse.


### Manual input:

- If no command-line argument is provided, after starting the program the user will be prompted to add numerical data by hand.
- After entering all the desired data, the user should enter "q" or "quit". The program will then start doing the calculations and print results.

## How to run tests:
-Input ``pytest test_project.py`` in your terminal. it iwll show if all the functions are working properly.


## Included Files:
- project.py -> The main program
- test_project.py -> The file for testing if each function works correctly
- grades.csv, simple.csv -> A sample student grades tables to try the program with


## Dependencies:
- Python 3.14
- Tabulate library (``pip install tabulate`` in terminal)



