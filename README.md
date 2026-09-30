# Expense Tracker

## Project Overview

Expense Tracker is a simple Python program that allows the user to add expenses, view all expenses, and view the total spending.

The program stores the expenses in a list. Each expense contains the date, category, discription, and amount.

## Features

- Add Expense
- View All Expenses
- View Total Spend
- Exit

## How the Program Works

### 1. Add Expense

The user can add a new expense by entering:

- Date
- Category
- Discription
- Amount

The entered details are stored in a dictionary. The dictionary is then added to the expenses list.

### 2. View All Expenses

The user can view all the expenses that have been added.

If there are no expenses in the list, the program displays:

No Expenses Added

Otherwise, the program displays the date, category, discription, and amount of each expense.

### 3. View Total Spending

The program calculates the total spending by going through all the expenses and adding their amounts.

The total spending is then displayed to the user.

### 4. Exit

The user can select option 4 to exit the program.

The program displays:

Thankyou for using our system

## Data Used in the Program

The program uses an expenses list to store expenses.

Each expense is stored as a dictionary with four details:

- date
- category
- discription
- amount

The structure used in the program is:

    expense = {
        "date": date,
        "category": category,
        "discription": discription,
        "amount": amount
    }

## Python Concepts Used

### List

The expenses list is used to store the expenses.

### Dictionary

A dictionary is used to store the details of each expense.

### While Loop

The while True loop is used to keep the menu running until the user selects the exit option.

### If-Elif-Else

if, elif, and else statements are used to handle the different menu choices and invalid choices.

### For Loop

The for loop is used to go through the expenses when displaying them and calculating the total spending.

### Input and Output

input() is used to take information from the user and print() is used to display information.

## Menu

The program provides the following menu:

    ====Menu====
    1. Add Expense
    2. View All Expenses
    3. view Total Spend
    4. Exit

## How to Run

1. Open the project in VS Code.
2. Open the terminal.
3. Run the Python file using:

    python main.py

4. Select an option from the menu.
5. Enter the required information.

## Limitations

- The expenses are stored in the list while the program is running.
- The program does not permanently save the expenses.
- The program is operated through the console.

## Conclusion

The Expense Tracker program is a simple Python project that uses lists, dictionaries, loops, conditional statements, and input/output to record expenses and calculate total spending.