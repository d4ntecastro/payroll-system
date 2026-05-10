import sqlite3


def create_tables():
    # Connect to (or create) the database file inside the 'data' folder
    conn = sqlite3.connect('data/payroll.db')
    cursor = conn.cursor()

    # Create Employee Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT,
            base_salary REAL NOT NULL
        )
    ''')

    # Create Payroll History Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payroll_records (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            pay_date TEXT,
            gross_pay REAL,
            net_pay REAL,
            FOREIGN KEY (employee_id) REFERENCES employees (id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database & Tables created successfully!")


if __name__ == "__main__":
    create_tables()


def add_employee_to_db(name, position, salary):
    conn = sqlite3.connect('data/payroll.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO employees (name, position, base_salary)
            VALUES (?, ?, ?)
        ''', (name, position, salary))
        conn.commit()
        print(f"\n✅ Successfully added {name} to the system.")
    except sqlite3.Error as e:
        print(f"❌ Error adding employee: {e}")
    finally:
        conn.close()
