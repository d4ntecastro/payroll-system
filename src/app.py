import os
from flask import Flask, render_template
from database import get_all_employees

# 1. FIND THE ROOT FOLDER (C:\Users\User\OneDrive\Desktop\payroll-system)
# __file__ is 'src/app.py'. dirname(__file__) is 'src'.
# We go one level up to get to the main project folder.
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(base_path, 'templates')

print("-" * 50)
print(f"DIAGNOSTIC: Project Root is: {base_path}")
print(f"DIAGNOSTIC: Looking for index.html in: {template_path}")
print("-" * 50)

# 2. INITIALIZE FLASK WITH EXPLICIT PATHS
app = Flask(__name__,
            template_folder=template_path)


@app.route('/')
def index():
    try:
        # Check if index.html actually exists right now
        check_file = os.path.join(template_path, 'index.html')
        if not os.path.exists(check_file):
            return f"<h1>CRITICAL ERROR</h1><p>I cannot find index.html at {check_file}</p>"

        employees = get_all_employees()
        return render_template('index.html', count=len(employees))
    except Exception as e:
        return f"<h1>Python Error</h1><p>{str(e)}</p>"


if __name__ == '__main__':
    # Using port 5002 to completely bypass any old browser cache
    # We turn off debug/reloader to stop the Windows socket error
    app.run(host='127.0.0.1', port=5002, debug=False, use_reloader=False)
