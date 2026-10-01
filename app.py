# Author: 
# Date: 2026-10-01
# Name: app.py
# Description: Main Flask application entry point serving the payroll system interface.

from flask import Flask, render_template
from payroll.payroll import build_payroll_data

app = Flask(__name__)


@app.route("/")
@app.route("/payroll")
def payroll_view():
    """Renders the payroll summary template with serialized object data and totals."""
    data = build_payroll_data()
    return render_template("payroll.html", **data)


if __name__ == "__main__":
    app.run(debug=True)
