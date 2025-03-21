from budget_module import *

#-----------------------------
# Product List
#-----------------------------
budget_data = {
    "balance": 500,
    "transactions":[
        {"type": "income", "amount": "1000", "description": "Salary"},
        {"type": "expense", "amount": "500", "description": "Grocery"}
    ]
}

version = "1.0" # Version of the program


#-----------------------------
# Exit Menu
#-----------------------------
def exitMenu():
    """Exit the program"""
    print("Exiting program. Goodbye!")
    return False # Signal to exit the program


#-----------------------------
# Display Menu
#-----------------------------
def displayMenu():
    """Display the main menu options"""
    print("\n"+"="*40)
    print(f"||     Leumi Budget Manager (v{version})    ||")
    print("="*40+"\n")
    print("| 1 | Add Income")
    print("| 2 | Add Expense")
    print("| 3 | Show Balance")
    print("| 4 | Show Transaction History")
    print("| 5 | Exit")

#-----------------------------
# Main program loop
#-----------------------------
def mainMenuHandler():
    """Main program function that runs the Budget Manager"""
    while True:
        displayMenu()
        
        # Get user choice
        try:
            choice = int(input("\n> "))
        except ValueError:
            print("❌ Error: Invalid input.")
            continue
        
        # Process user choice
        continue_program = True
        match choice:
            case 1:  
                continue_program = addIncome(budget_data)
            case 2: 
                continue_program = addExpense(budget_data)
            case 3: 
                continue_program = showBalance(budget_data)
            case 4:  
                continue_program = showTransactionHistory(budget_data)
            case 5:
                print("\nExiting program. Goodbye!")
                break
            case _:  # Default case for invalid choices
                print("❌ Error: Invalid input.\nPlease enter a number between 1 and 5.")
        # Check if we should exit the program
        if not continue_program:
            break


#-----------------------------
# Run the main program
#-----------------------------
if __name__ == "__main__":
    mainMenuHandler()
