import json

expenses = []

#--------------------Load data---------------------
def load_data():
    global expenses
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

#--------------------Save data---------------------
def save_data():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)

#--------------------Add expense---------------------
def add_expense():
    #Data validation 
    while True:
        date = input("Enter the date (DD-MM-YYYY): ")
        if len(date) == 10 and date[2] == '-' and date[5] == '-':
            break
        else:
            print("Invalid date format. Please enter in DD-MM-YYYY format.")

    #Category validation
    while True:
        category = input("Enter the category: ").strip()
        if category:
            break
        else:
            print("Invalid category. Please enter a valid category name.")

    #Amount validation
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    expense = {
        'amount': amount,
        'category': category,
        'date': date
    }
    expenses.append(expense)
    save_data()

    print("Expense added successfully!\n")
          
#--------------------View expenses---------------------
def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\nAll Expenses:")
    print("-" * 40)

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Amount: {exp['amount']}, Category: {exp['category']}, Date: {exp['date']}")
        print()

#--------------------Category Analysis---------------------
def analyze_categories():
    if not expenses:
        print("No expenses found.\n")
        return

    category_totals = {}

    for exp in expenses:
        category = exp['category']
        amount = exp['amount']

        if category in category_totals:           
            category_totals[category] += amount
        else:
            category_totals[category] = (amount)

    print("\nCategory-wise spending:")
    print("-" * 30)        
    for category, total in category_totals.items():
        print(f"{category}: {total}")
    print()

#------------Monthly Analysis---------------------
def monthly_analysis():
    if not expenses:
        print("No expenses found.\n")
        return

    month = input("Enter the month (MM-YYYY): ")

    total = 0
    monthly_total = 0

    for exp in expenses:
        total += float(exp['amount'])

        # Extract month and year from the date
        exp_month = exp['date'][3:]  # from DD-MM-YYYY, we take MM-YYYY

        if exp_month == month:
            monthly_total += float(exp['amount'])

    print(f"\nTotal spending:", total)
    print(f"Monthly Spending ({month}):{monthly_total}\n")

#--------------------Clear all data---------------------
def clear_data():
    global expenses
    
    confirm = input("Are you sure you want to clear all data? (yes/no): ").lower()
    if confirm == 'yes':
        expenses = []
        save_data()
        print("All data cleared successfully!\n")
    else:
        print("Operation cancelled.\n")

#-------------------budget analysis---------------------
def budget_analysis():
    if not expenses:
        print("No expenses found.\n")
        return

    budget = float(input("Enter your monthly budget: "))
    
    total = 0

    for exp in expenses:
        total += float(exp['amount'])
    
    print(f"\nTotal spending: {total}")
    if total > budget:
        print("Warning: You have exceeded your budget.\n")
    else:
        print("You are within your budget.\n")

#--------------------Highest expense---------------------
def highest_expense():
    if not expenses:
        print("No expenses found.\n")
        return
    
    category_totals = {}

    for exp in expenses:
        category = exp['category']
        amount = exp['amount']

        if category in category_totals:           
            category_totals[category] += amount
        else:
            category_totals[category] = (amount)

    highest = max(category_totals, key=category_totals.get)
    print(f"\nHighest spending category: {highest} with amount {category_totals[highest]}\n")

#--------------------------sorting expenses---------------------
def sort_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    sorted_expenses = sorted(expenses, key=lambda x: x['amount'], reverse=True)

    print("\nExpenses sorted by amount (highest to lowest):")
    print("-" * 40)
    for i, exp in enumerate(sorted_expenses, start=1):
        print(f"{i}. Amount: {exp['amount']}| Category: {exp['category']}| Date: {exp['date']}")
        print()  

#--------------------export expenses---------------------
def export_expenses(): 
    if not expenses:
        print("No expenses found.\n")
        return

    file = open('exported_expenses.txt', 'w')

    total = 0
    file.write("======Expenses report======\n\n")
    for exp in expenses:
        line = f"Amount: {exp['amount']}| Category: {exp['category']}| Date: {exp['date']}\n"
        file.write(line)
        total += float(exp['amount'])

    file.write("\n-----------------------------\n")
    file.write(f"\nTotal spending: {total}\n")
    file.close()
    print("Expenses exported successfully to 'exported_expenses.txt'\n")

#--------------------Main menu---------------------
def main_menu():
    while True:
        print("======Expense Tracker======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Categories")
        print("4. Monthly Analysis")
        print("5. Clear Data")
        print("6. Highest Expense")
        print("7. Budget Analysis")
        print("8. Sort Expenses")
        print("9. Export Expenses") 
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            analyze_categories()
        elif choice == '4':
            monthly_analysis()
        elif choice == '5':
            clear_data()
        elif choice == '6':
            highest_expense()
        elif choice == '7':
            budget_analysis()
        elif choice == '8':
            sort_expenses()
        elif choice == '9':
            export_expenses()
        elif choice == '10':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice.\n")
            
#--------------------Run the program---------------------
load_data()
main_menu()