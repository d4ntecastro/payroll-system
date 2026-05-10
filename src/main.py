def calculate_net_pay(gross_pay, tax_rate=0.1):
    """Calculates net pay after a default 10% tax."""
    tax_amount = gross_pay * tax_rate
    return gross_pay - tax_amount


if __name__ == "__main__":
    print("--- Payroll System Initialized ---")

    # Test calculation
    test_salary = 50000
    print(f"Gross: {test_salary} | Net: {calculate_net_pay(test_salary)}")
