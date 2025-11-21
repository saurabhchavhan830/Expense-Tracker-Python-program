# 💰 Expense Tracker Project

expenseslist = []  # list to store expense records in dictionary format

print("✨ Welcome to the Expense Tracker! ✨")

while True:
    print("\n==============================")
    print("📌  MENU")
    print("==============================")
    print("1️⃣  Add Expense")
    print("2️⃣  View All Expenses")
    print("3️⃣  View Total Expenses")
    print("4️⃣  Exit 🚪")
    
    choice = input("👉 Please choose an option (1-4): ")

    # Add Expense
    if choice == '1':
        print("\n📝 Add New Expense")
        date = input("📅 Enter the date (YYYY-MM-DD): ")
        category = input("📂 Enter the category (Food, Transport, etc.): ")
        description = input("💬 Enter the description: ")
        amount = float(input("💵 Enter the amount: "))
        
        expense_record = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }
        
        expenseslist.append(expense_record)
        print("✅ Expense added successfully!")    
    
    # View All Expenses
    elif choice == '2':
        print("\n📋 Viewing All Expenses:")
        
        if len(expenseslist) == 0:
            print("⚠️ No expenses recorded yet!")
        else:
            count = 1
            for expense in expenseslist:
                print(f"🔸 Expense {count}: {expense['date']} | {expense['category']} | {expense['description']} | ₹{expense['amount']}")
                count += 1
    
    # View Total Expenses
    elif choice == '3': 
        print("\n🔢 Calculating Total Expenses...")
        total = 0
        for expense in expenseslist:
            total += expense['amount']
        
        print(f"💳 Total Expenses = ₹{total}")
    
    # Exit
    elif choice == '4': 
        print("\n👋 Exiting Expense Tracker. Goodbye!")
        break
    
    else:
        print("❌ Invalid choice! Please select a valid option.")
