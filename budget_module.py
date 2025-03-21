## Adding income function
def addIncome(budget_data):
    """Adds a new income to the db"""
    while True:
        try:
            print("\n=== ADD NEW INCOME ===\n")
            inputIncomeAmount = float(input("Enter Income Amount (₪):\n> "))
            if inputIncomeAmount < 0:
                print("\n"+"="*80)
                print("❌ Error: Income Amount cannot be less than 0")
                print("="*80+"\n\n")
                continue

            inputIncomeDescription = input("Enter Income Description:\n> ")
            if not inputIncomeDescription.strip():
                print("\n"+"="*80)
                print("❌ Error: Income Description cannot be empty")
                print("="*80+"\n\n")
                continue    

            # Add transaction
            budget_data["transactions"].append({"type": "income","amount": inputIncomeAmount,"description": inputIncomeDescription
            })
            budget_data["balance"] += inputIncomeAmount

            # Success message
            print("\n"+"="*80)
            print(f"✅ SUCCESS: You added ₪ {inputIncomeAmount} to your INCOME with the description of '{inputIncomeDescription}'")
            print("="*80+"\n\n")
            
            # Add menu options after operation
            print("\n(1) - ADD another Income")
            print("(2) - Go Back")
            print("(3) - Quit")
            
            action = int(input("> "))
            if action == 1:
                continue  # Back to add another income
            elif action == 2:
                return budget_data  # Back to main menu
            elif action == 3:
                print("Exiting program. Goodbye!")
                exit()  # Exit program
            else:
                print("Invalid choice. Returning to main menu")
                return budget_data
                
        except ValueError:
            print("\n"+"="*80)
            print("❌ Error: Please enter valid values.")
            print("="*80+"\n\n")
            # Add menu options after error
            try:
                print("\n(1) - Try Again")
                print("(2) - Go Back")
                print("(3) - Quit")
                action = int(input("> "))
                if action == 1:
                    continue  # Try again
                elif action == 2:
                    return budget_data  # Back to main menu
                elif action == 3:
                    print("Exiting program. Goodbye!")
                    exit()  # Exit program
                else:
                    print("Invalid choice. Returning to main menu")
                    return budget_data
            except ValueError:
                print("Invalid input. Returning to main menu.")
                return budget_data
    
    return budget_data


## Adding expense function
def addExpense(budget_data):
    """Adds a new expense to the db"""
    while True:
        try:
            print("\n=== ADD NEW EXPENSE ===\n")
            inputExpenseAmount = float(input("Enter Expense Amount (₪):\n> "))
            if inputExpenseAmount < 0:
                print("\n"+"="*80)
                print("❌ Error: Expense Amount cannot be less than 0")
                print("="*80+"\n\n")
                continue

            inputExpenseDescription = input("Enter Expense Description:\n> ")
            if not inputExpenseDescription.strip():
                print("\n"+"="*80)
                print("❌ Error: Expense Description cannot be empty")
                print("="*80+"\n\n")
                continue    

            # Subtract the expense amount from the balance
            budget_data["balance"] -= inputExpenseAmount

            # Add the expense transaction to the list
            budget_data["transactions"].append({
                "type": "expense",
                "amount": str(inputExpenseAmount),
                "description": inputExpenseDescription
            })

            # Success message
            print("\n"+"="*80)
            print(f"✅ SUCCESS: You added ₪ {inputExpenseAmount} to your EXPENSE with the description of '{inputExpenseDescription}'")
            print("="*80+"\n\n")
            
            # Add menu options after operation
            print("\n(1) - ADD another Expense")
            print("(2) - Go Back")
            print("(3) - Quit")
            
            action = int(input("> "))
            if action == 1:
                continue  # Back to add another expense
            elif action == 2:
                return budget_data  # Back to main menu
            elif action == 3:
                print("Exiting program. Goodbye!")
                exit()  # Exit program
            else:
                print("Invalid choice. Returning to main menu")
                return budget_data
                
        except ValueError:
            print("\n"+"="*80)
            print("❌ Error: Please enter valid values.")
            print("="*80+"\n\n")
            # Add menu options after error
            try:
                print("\n(1) - Try Again")
                print("(2) - Go Back")
                print("(3) - Quit")
                action = int(input("> "))
                if action == 1:
                    continue  # Try again
                elif action == 2:
                    return budget_data  # Back to main menu
                elif action == 3:
                    print("Exiting program. Goodbye!")
                    exit()  # Exit program
                else:
                    print("Invalid choice. Returning to main menu")
                    return budget_data
            except ValueError:
                print("Invalid input. Returning to main menu.")
                return budget_data
    
    return budget_data


## Show balance function
def showBalance(budget_data):
    """Shows balance"""
    if not budget_data.keys():  # Check if the database is empty
        print("No info in the database.")
    else:
        balance = budget_data["balance"]
        print("\n"+"="*40)
        print(f"| Your BALANCE is: ₪ {balance}")
        print("="*40+"\n\n")
    
    # Return to main menu or exit
    while True:
        try:
            print("\n(2) - Go Back")
            print("(3) - Quit")
            action = int(input("> "))
            if action == 3:
                print("Exiting program. Goodbye!")
                return False  # Signal to exit the program
            elif action == 2:
                return budget_data  # Continue program
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Show show_balance function by Daniel Berliant
def show_balance(budget_data: dict) -> dict:
    return budget_data["balance"]


def printTransactionHistory(budget_data):
    # Calculate minimum padding for columns
    maxTypePad = max(max(len(transaction["type"]) for transaction in budget_data["transactions"]), 7) if budget_data["transactions"] else 7
    maxAmountPad = max(max(len(str(transaction["amount"])) for transaction in budget_data["transactions"]), 6) if budget_data["transactions"] else 6
    maxDescriptionPad = max(max(len(transaction["description"]) for transaction in budget_data["transactions"]), 10) if budget_data["transactions"] else 10

    typePad = maxTypePad + 4
    amountPad = maxAmountPad + 4
    descriptionPad = maxDescriptionPad + 4
    
    # Print the header
    print(f"\nType{' '*(typePad-4)} | Amount{' '*(amountPad-6)} | Description{' '*(descriptionPad-10)}|")
    print("-" * (typePad + amountPad + descriptionPad + 11))

    # Print the transactions
    for transaction in budget_data["transactions"]:
        print(f"{transaction['type']:<{typePad}} | {transaction['amount']:<{amountPad}} | {transaction['description']:<{descriptionPad}} |")


## Show transaction history function
def showTransactionHistory(budget_data):
    """Display all transaction in the database"""
    if not budget_data.keys():  # Check if the database is empty
        print("No info in the database.")
    else:
        printTransactionHistory(budget_data)
    
    # Return to main menu or exit
    while True:
        try:
            print("\n(2) - Go Back")
            print("(3) - Quit")
            action = int(input("> "))
            if action == 3:
                print("Exiting program. Goodbye!")
                return False  # Signal to exit the program
            elif action == 2:
                return budget_data  # Continue program
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

