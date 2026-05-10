from main import run_monthly_payroll
from database import add_employee_to_db
import tkinter as tk
from tkinter import messagebox
# We'll tweak these imports
from database import add_employee_to_db, run_monthly_payroll


class PayrollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Pro v1.0")
        self.root.geometry("400x300")

        # Title Label
        self.label = tk.Label(
            root, text="Payroll Management System", font=("Arial", 16, "bold"))
        self.label.pack(pady=20)

        # Add Employee Button
        self.btn_add = tk.Button(
            root, text="Add New Employee", width=25, command=self.open_add_window)
        self.btn_add.pack(pady=10)

        # Run Payroll Button
        self.btn_run = tk.Button(
            root, text="Run Monthly Payroll", width=25, command=self.process_payroll)
        self.btn_run.pack(pady=10)

    def open_add_window(self):
        # A simple popup could go here, but for now, let's just show a message
        messagebox.showinfo(
            "Feature", "This would open a form to enter Name and Salary!")

    def process_payroll(self):
        # Trigger the logic we wrote earlier
        try:
            # We will call your existing logic here
            messagebox.showinfo(
                "Success", "Monthly Payroll processed and PDFs generated!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollApp(root)
    root.mainloop()
