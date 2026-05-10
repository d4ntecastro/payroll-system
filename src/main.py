from datetime import datetime
from calculations import calculate_net_salary
from database import create_tables, add_employee_to_db, get_all_employees, save_payroll_record
from database import create_tables, add_employee_to_db
from database import create_tables


def calculate_net_pay(gross_pay, tax_rate=0.1):
    """Calculates net pay after a default 10% tax."""
    tax_amount = gross_pay * tax_rate
    return gross_pay - tax_amount


if __name__ == "__main__":
    print("--- Payroll System Initialized ---")

    # Test calculation
    test_salary = 50000
    print(f"Gross: {test_salary} | Net: {calculate_net_pay(test_salary)}")


def main():
    print("--- 💼 Payroll System Pro ---")
    create_tables()
    # Soon we will add functions to Add Employees and Calculate Pay here


if __name__ == "__main__":
    main()


def menu():
    while True:
        print("\n--- 💼 Payroll System Pro ---")
        print("1. Add New Employee")
        print("2. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter Employee Name: ")
            pos = input("Enter Position: ")
            try:
                salary = float(input("Enter Base Monthly Salary: "))
                add_employee_to_db(name, pos, salary)
            except ValueError:
                print("⚠️ Invalid salary amount. Please enter a number.")

        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    create_tables()  # Ensures DB exists on startup
    menu()


def run_monthly_payroll():
    employees = get_all_employees()
    if not employees:
        print("No employees found. Add some first!")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    print(f"\n--- Running Payroll for {today} ---")

    for emp in employees:
        emp_id, name, gross = emp
        net = calculate_net_salary(gross)
        save_payroll_record(emp_id, today, gross, net)
        print(f"💰 Processed {name}: Gross ${gross} | Net ${net}")

    print("\n✅ All payroll records saved to database.")

# Update your menu() function to include:
# print("2. Run Monthly Payroll")
# print("3. Exit")
