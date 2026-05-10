def calculate_tax(gross_salary):
    """
    Calculates tax based on simple progressive brackets:
    - Up to 50,000: 5%
    - 50,001 to 100,000: 10%
    - Over 100,000: 15%
    """
    if gross_salary <= 50000:
        tax = gross_salary * 0.05
    elif gross_salary <= 100000:
        tax = (50000 * 0.05) + ((gross_salary - 50000) * 0.10)
    else:
        tax = (50000 * 0.05) + (50000 * 0.10) + \
            ((gross_salary - 100000) * 0.15)

    return round(tax, 2)


def calculate_net_salary(gross_salary):
    tax = calculate_tax(gross_salary)
    return gross_salary - tax
