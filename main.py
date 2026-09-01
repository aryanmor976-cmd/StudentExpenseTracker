from database import create_connection


def add_expense():
    connection = create_connection()
    cursor = connection.cursor()

    expense_date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    query = """
        INSERT INTO expenses
        (expense_date, category, description, amount)
        VALUES (%s, %s, %s, %s)
    """

    values = (expense_date, category, description, amount)

    cursor.execute(query, values)
    connection.commit()

    print("\nExpense added successfully!")

    cursor.close()
    connection.close()


def view_expenses():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM expenses ORDER BY expense_date DESC"

    cursor.execute(query)
    expenses = cursor.fetchall()

    if not expenses:
        print("\nNo expenses found.")
    else:
        print("\n========== ALL EXPENSES ==========")
        print("ID | Date       | Category    | Description       | Amount")
        print("-" * 65)

        for expense in expenses:
            print(
                f"{expense[0]} | "
                f"{expense[1]} | "
                f"{expense[2]:<11} | "
                f"{expense[3]:<17} | "
                f"₹{expense[4]}"
            )

    cursor.close()
    connection.close()


def search_by_category():
    connection = create_connection()
    cursor = connection.cursor()

    category = input("Enter category to search: ")

    query = """
        SELECT * FROM expenses
        WHERE category = %s
        ORDER BY expense_date DESC
    """

    cursor.execute(query, (category,))
    expenses = cursor.fetchall()

    if not expenses:
        print("\nNo expenses found for this category.")
    else:
        print(f"\n========== {category.upper()} EXPENSES ==========")

        for expense in expenses:
            print(
                f"ID: {expense[0]} | "
                f"Date: {expense[1]} | "
                f"Category: {expense[2]} | "
                f"Description: {expense[3]} | "
                f"Amount: ₹{expense[4]}"
            )

    cursor.close()
    connection.close()


def delete_expense():
    connection = create_connection()
    cursor = connection.cursor()

    expense_id = int(input("Enter expense ID to delete: "))

    query = "DELETE FROM expenses WHERE id = %s"

    cursor.execute(query, (expense_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("\nExpense deleted successfully!")
    else:
        print("\nExpense ID not found.")

    cursor.close()
    connection.close()


def update_expense():
    connection = create_connection()
    cursor = connection.cursor()

    expense_id = int(input("Enter expense ID to update: "))

    new_date = input("Enter new date (YYYY-MM-DD): ")
    new_category = input("Enter new category: ")
    new_description = input("Enter new description: ")
    new_amount = float(input("Enter new amount: "))

    query = """
        UPDATE expenses
        SET expense_date = %s,
            category = %s,
            description = %s,
            amount = %s
        WHERE id = %s
    """

    values = (
        new_date,
        new_category,
        new_description,
        new_amount,
        expense_id
    )

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("\nExpense updated successfully!")
    else:
        print("\nExpense ID not found.")

    cursor.close()
    connection.close()
def expense_summary():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT COUNT(*), COALESCE(SUM(amount), 0), COALESCE(AVG(amount), 0)
        FROM expenses
    """

    cursor.execute(query)
    result = cursor.fetchone()

    total_count = result[0]
    total_amount = result[1]
    average_amount = result[2]

    print("\n========== EXPENSE SUMMARY ==========")
    print(f"Total number of expenses : {total_count}")
    print(f"Total amount spent       : ₹{total_amount:.2f}")
    print(f"Average expense          : ₹{average_amount:.2f}")

    cursor.close()
    connection.close()
def category_summary():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """

    cursor.execute(query)
    results = cursor.fetchall()

    if not results:
        print("\nNo expenses found.")
    else:
        print("\n========== CATEGORY SUMMARY ==========")

        for category, total in results:
            print(f"{category:<15} ₹{total:.2f}")

    cursor.close()
    connection.close()
def monthly_summary():
    connection = create_connection()
    cursor = connection.cursor()

    month = input("Enter month (YYYY-MM): ")

    query = """
        SELECT COUNT(*), COALESCE(SUM(amount), 0), COALESCE(AVG(amount), 0)
        FROM expenses
        WHERE DATE_FORMAT(expense_date, '%Y-%m') = %s
    """

    cursor.execute(query, (month,))
    result = cursor.fetchone()

    total_count = result[0]
    total_amount = result[1]
    average_amount = result[2]

    print("\n========== MONTHLY SUMMARY ==========")
    print(f"Month                    : {month}")
    print(f"Number of expenses       : {total_count}")
    print(f"Total amount spent       : ₹{total_amount:.2f}")
    print(f"Average expense          : ₹{average_amount:.2f}")

    cursor.close()
    connection.close()

# ==============================
# MAIN MENU
# ==============================

while True:

    print("\n================================")
    print("     STUDENT EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search by Category")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Expense Summary")
    print("7. Category-wise Summary")
    print("8. Monthly Summary")
    print("9. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_by_category()

    elif choice == "4":
        update_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        expense_summary()

    elif choice == "7":
        category_summary()

    elif choice == "8":
        monthly_summary()

    elif choice == "9":
        confirm = input("Are you sure you want to exit? (yes/no): ")

    if confirm.lower() == "yes":
        print("\nThank you for using Student Expense Tracker!")
        break

    else:
        print("\nInvalid choice. Please try again.")