<h1 align="center">Student Expense Tracker</h1>

<p align="center">
  A Python and MySQL based expense management application
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Python">
  <img src="https://img.shields.io/badge/MySQL-Database-orange" alt="MySQL">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status">
</p>

---

## About the Project

Student Expense Tracker is a command-line application developed using Python and MySQL to help students record and manage their daily expenses.

The application stores expense records in a MySQL database and provides options to add, view, search, update, and delete expenses. It also includes summary features to help understand spending by total amount, category, and month.

This project was built to practice Python programming, SQL, database connectivity, and CRUD operations in a practical application.

---

## Key Features

- Add new expense records
- View all saved expenses
- Search expenses by category
- Update existing expenses
- Delete expenses
- Calculate total spending
- Calculate average expense
- View category-wise spending
- View monthly expense summary
- Store data using MySQL
- Menu-driven command-line interface

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Application logic and user interaction |
| MySQL | Persistent storage for expense records |
| MySQL Connector/Python | Connects the Python application to MySQL |
| SQL | Data management and expense analysis |
| python-dotenv | Loads database configuration from environment variables |
| VS Code | Development environment |

---

## Project Structure

```text
StudentExpenseTracker/
│
├── screenshots/
│   ├── main-menu.png
│   ├── view-expenses.png
│   ├── expense-summary.png
│   ├── category-summary.png
│   └── monthly-summary.png
│
├── main.py
├── database.py
├── database.sql
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

**`main.py`**  
Contains the main application logic and menu-driven interface.

**`database.py`**  
Handles the connection between the Python application and MySQL.

**`database.sql`**  
Contains the SQL commands required to create the database and `expenses` table.

**`requirements.txt`**  
Lists the Python packages required to run the application.

**`.gitignore`**  
Prevents sensitive and unnecessary files such as `.env`, Python cache files, and system files from being committed to Git.

**`screenshots/`**  
Contains screenshots showing the application running and its main features.

---

## Database Schema

The application uses MySQL to store expense records.

### Database

```text
student_expense_tracker
```

### Table: `expenses`

| Column | Data Type | Description |
|---|---|---|
| `id` | INT | Unique identifier for each expense |
| `expense_date` | DATE | Date on which the expense occurred |
| `category` | VARCHAR(100) | Category of the expense |
| `description` | VARCHAR(255) | Description of the expense |
| `amount` | DECIMAL(10,2) | Amount spent |

### Database Structure

```text
student_expense_tracker
        │
        └── expenses
              ├── id
              ├── expense_date
              ├── category
              ├── description
              └── amount
```

### SQL Schema

The database structure is included in `database.sql`.

```sql
CREATE DATABASE IF NOT EXISTS student_expense_tracker;

USE student_expense_tracker;

CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    category VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    amount DECIMAL(10, 2) NOT NULL
);
```

---

## CRUD Operations

The application implements the four basic database operations:

| Operation | Application Feature |
|---|---|
| Create | Add Expense |
| Read | View All Expenses / Search by Category |
| Update | Update Expense |
| Delete | Delete Expense |

In addition to CRUD operations, SQL aggregation is used for expense analysis:

- `SUM()` for total spending
- `AVG()` for average spending
- `COUNT()` for the number of expenses
- `GROUP BY` for category-wise summaries
- Date-based filtering for monthly analysis

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/aryanmor976-cmd/StudentExpenseTracker.git
```

Move into the project directory:

```bash
cd StudentExpenseTracker
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip3 install -r requirements.txt
```

### 3. Configure the Database

Make sure MySQL is installed and running.

Create a `.env` file in the project directory:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_MYSQL_PASSWORD
DB_NAME=student_expense_tracker
```

Replace `YOUR_MYSQL_PASSWORD` with your local MySQL password.

> The `.env` file should never be committed to GitHub because it contains private database credentials.

### 4. Create the Database

The required database and table can be created using the included `database.sql` file.

Alternatively, run:

```sql
CREATE DATABASE IF NOT EXISTS student_expense_tracker;

USE student_expense_tracker;

CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    category VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    amount DECIMAL(10, 2) NOT NULL
);
```

### 5. Start the Application

Run:

```bash
python3 main.py
```

---

## Application Menu

When the application starts, the following menu is displayed:

```text
==============================
      STUDENT EXPENSE TRACKER
==============================

1. Add Expense
2. View All Expenses
3. Search by Category
4. Update Expense
5. Delete Expense
6. Expense Summary
7. Category-wise Summary
8. Monthly Summary
9. Exit
```

---

## How It Works

### Add Expense

The user enters:

- Date
- Category
- Description
- Amount

The information is inserted into the MySQL `expenses` table.

Example:

```text
Enter date (YYYY-MM-DD): 2026-09-01
Enter category: Food
Enter description: Lunch
Enter amount: 120
```

### View Expenses

Displays all expense records stored in the database.

### Search by Category

Allows the user to search for expenses belonging to a particular category.

### Update Expense

The user enters an expense ID and can modify its date, category, description, and amount.

### Delete Expense

The user enters an expense ID to remove the corresponding record from the database.

### Expense Summary

Calculates:

- Total number of expenses
- Total amount spent
- Average expense

### Category-wise Summary

Groups expenses by category and calculates the total amount spent in each category.

### Monthly Summary

Calculates expense information based on the selected month.

---

## Application Screenshots

### Main Menu

![Main Menu](screenshots/main-menu.png)

### View All Expenses

![View All Expenses](screenshots/view-expenses.png)

### Expense Summary

![Expense Summary](screenshots/expense-summary.png)

### Category-wise Summary

![Category-wise Summary](screenshots/category-summary.png)

### Monthly Summary

![Monthly Summary](screenshots/monthly-summary.png)

---

## What I Learned

This project helped me gain practical experience with:

- Python functions and program structure
- Conditional statements and loops
- User input handling
- SQL queries
- MySQL database design
- Python-MySQL connectivity
- CRUD operations
- Data retrieval and filtering
- SQL aggregation functions
- Grouping data using SQL
- Environment-based configuration
- Building a menu-driven application

---

## Future Improvements

Some possible improvements for future versions include:

- Graphical user interface
- User authentication
- Personal student profiles
- Budget limits and alerts
- Expense charts and visualizations
- CSV/Excel export
- Web-based version
- Mobile application

---

## Author

**Aryan Mor**

B.Tech Computer Science & Engineering  
Specialization: Machine Learning

---

## License

This project was created for educational and portfolio purposes.