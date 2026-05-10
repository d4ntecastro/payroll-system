from fpdf import FPDF
import os


def generate_payslip(name, date, gross, tax, net):
    pdf = FPDF()
    pdf.add_page()

    # Header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="OFFICIAL PAYSLIP", ln=True, align='C')
    pdf.ln(10)

    # Body
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Employee Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Pay Date: {date}", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt=f"Gross Salary: ${gross:,.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Tax Deducted: -${tax:,.2f}", ln=True)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"Net Pay: ${net:,.2f}", ln=True)

    # Create folder if it doesn't exist
    if not os.path.exists('payslips'):
        os.makedirs('payslips')

    filename = f"payslips/{name}_{date}.pdf"
    pdf.output(filename)
    return filename
