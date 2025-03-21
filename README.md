# Leumi Budget Manager

A simple command-line budget management application that helps you track your income, expenses, and overall balance.

## Features

- Add income transactions
- Add expense transactions
- View current balance
- Display transaction history
- User-friendly menu interface

## Data Structure

The program uses a dictionary-based data structure to store budget information:

```python
budget_data = {
    "balance": 500,
    "transactions": [
        {"type": "income", "amount": "1000", "description": "Salary"},
        {"type": "expense", "amount": "500", "description": "Grocery"}
    ]
}
```

- `balance`: Represents the current available money
- `transactions`: A list of transaction records, where each transaction is a dictionary containing:
  - `type`: Either "income" or "expense"
  - `amount`: Transaction amount (stored as a string)
  - `description`: Brief description of the transaction

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/DevOOPS-Technion/Budget-Manager.git
   ```

2. Navigate to the project directory:
   ```
   cd Budget-Manager
   ```

3. Run the program:
   ```
   python budget_manager.py
   ```
   
## Code Structure

The program consists of several modules:

- `main.py`: Contains the main program loop and menu interface
- `budget_module.py`: Contains the core data structure and transaction functions

The main functionality is organized into separate functions:
- `displayMenu()`: Shows the user interface options
- `addIncome()`: Adds income transactions to the budget
- `addExpense()`: Adds expense transactions to the budget
- `showBalance()`: Displays the current balance
- `showTransactionHistory()`: Lists all past transactions
- `exitMenu()`: Handles program termination

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

Feel free to contact me about this via email: `alex.ivanov@campus.technion.ac.il`